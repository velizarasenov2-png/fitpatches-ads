// One pass: read recent orders, check BigArena tracking, send the messages that are due.
// Logs contain only order numbers and message types (GitHub Actions logs of a public repo are public).
import { pathToFileURL } from 'node:url';
import { loadConfig, validateConfig } from './config.js';
import { createShopify } from './shopify.js';
import { fetchTracking } from './bigarena.js';
import { orderInfo, shipmentStatus, needsTracking, normalizePhone } from './order.js';
import { decide } from './decide.js';
import { render } from './messages.js';
import { sendMessage } from './bulkgate.js';
import { DAY, withinHours } from './time.js';

const LABEL = {
  thanks: 'благодарност',
  office: 'пристигна в офиса',
  office_reminder: 'напомняне',
  office_last: 'последно напомняне',
  address_out: 'днес до адрес',
  address_failed: 'неуспешна доставка',
};

async function mapLimit(items, limit, fn) {
  const out = new Array(items.length);
  let i = 0;
  await Promise.all(
    Array.from({ length: Math.min(limit, items.length) }, async () => {
      while (i < items.length) {
        const idx = i++;
        out[idx] = await fn(items[idx]);
      }
    }),
  );
  return out;
}

export async function runOnce({ cfg, shopify, now = new Date(), fetchTrackingImpl = fetchTracking, send = sendMessage, log = console.log }) {
  const stateKey = cfg.testPhone ? 'msgs_test' : 'msgs';
  const summary = { orders: 0, tracked: 0, sent: 0, failed: 0, planned: 0 };

  if (cfg.live && !withinHours(now, cfg.sendHours)) {
    log(`Извън часовете за изпращане (${cfg.sendHours}). Нищо не се праща.`);
    return summary;
  }

  const orders = await shopify.recentOrders(new Date(now - cfg.lookbackDays * DAY));
  summary.orders = orders.length;

  const items = await mapLimit(orders, 4, async (order) => {
    const info = orderInfo(order);
    const raw = order[stateKey === 'msgs' ? 'msgs' : 'msgsTest']?.value;
    let sent = {};
    try {
      sent = raw ? JSON.parse(raw) : {};
    } catch {
      sent = {};
    }
    let tracking = null;
    if (needsTracking(info)) {
      try {
        tracking = await fetchTrackingImpl(info.fulfillment.tracking, info.fulfillment.url);
        summary.tracked++;
      } catch (e) {
        log(`${info.name}: bigarena не отговори (${e.message}), ползвам статуса от Shopify`);
      }
    }
    const ship = info.fulfillment ? shipmentStatus(info, tracking) : null;
    return { info, sent, ship, due: decide(info, ship, sent, now, cfg) };
  });

  for (const { info, sent, ship, due } of items) {
    if (!due) continue;
    const where = ship ? ` [${ship.state}, ${ship.source}]` : '';
    if (!info.phone) {
      log(`${info.name}: ${LABEL[due.type]} – пропуснато, няма валиден телефон`);
      continue;
    }
    const text = render(due.type, info, cfg);
    if (!cfg.live) {
      summary.planned++;
      log(`ПРОБА ${info.name}: щеше да се изпрати „${LABEL[due.type]}“${where}`);
      if (cfg.printTexts) log(`--- Viber ---\n${text.viber}\n--- SMS ---\n${text.sms}\n`);
      continue;
    }
    if (summary.sent + summary.failed >= cfg.maxSendsPerRun) {
      log(`Достигнат лимит от ${cfg.maxSendsPerRun} съобщения за едно пускане. Останалите – следващия път.`);
      break;
    }
    const result = await send(
      { phone: cfg.testPhone ? normalizePhone(cfg.testPhone) : info.phone, viberText: text.viber, smsText: text.sms, tag: `${info.name} ${due.key}` },
      cfg,
    );
    const stamp = now.toISOString();
    const next = { ...sent };
    for (const k of due.skip || []) next[k] = 'skipped';
    if (result.ok) {
      next[due.key] = stamp;
      summary.sent++;
      log(`${info.name}: изпратено „${LABEL[due.type]}“${where} (${result.channel || 'ok'})`);
    } else {
      summary.failed++;
      log(`${info.name}: НЕ е изпратено „${LABEL[due.type]}“ – ${result.reason}`);
      if (!result.permanent) continue; // try again next run
      next[due.key] = `failed:${result.reason}`;
    }
    try {
      await shopify.saveSent(info.id, stateKey, next);
    } catch (e) {
      log(`${info.name}: не можах да запиша в Shopify (${e.message})`);
    }
  }

  log(
    `Поръчки: ${summary.orders}, проверени пратки: ${summary.tracked}, ` +
      (cfg.live ? `изпратени: ${summary.sent}, неуспешни: ${summary.failed}` : `за изпращане (проба): ${summary.planned}`),
  );
  return summary;
}

async function main() {
  const cfg = loadConfig();
  const errors = validateConfig(cfg);
  if (errors.length) {
    for (const e of errors) console.error(e);
    process.exit(1);
  }
  console.log(
    cfg.live
      ? `РЕЖИМ: на живо${cfg.testPhone ? ' (всичко отива на тестовия телефон)' : ''}, канал: ${cfg.viberSender ? 'Viber + SMS' : 'само SMS'}`
      : 'РЕЖИМ: проба (LIVE=false) – нищо не се праща и не се записва',
  );
  const shopify = await createShopify(cfg);
  await runOnce({ cfg, shopify });
}

if (import.meta.url === pathToFileURL(process.argv[1] || '').href) {
  main().catch((e) => {
    console.error(`Грешка: ${e.message}`);
    process.exit(1);
  });
}
