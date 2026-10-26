// Message texts. The Viber texts are also the Viber templates registered in BulkGate ({{variable}} = filled per order);
// the SMS fallback is short Latin text so it fits in one SMS.
const COURIER = { econt: 'Еконт', speedy: 'Спиди' };
const COURIER_LAT = { econt: 'Econt', speedy: 'Speedy' };

// BulkGate template keys (SMS & Viber messaging → Viber templates), sent as template_id "@<key>".
export const TEMPLATE_KEYS = {
  thanks: 'fp-thanks',
  office: 'fp-office',
  office_reminder: 'fp-office-reminder',
  office_last: 'fp-office-last',
  address_out: 'fp-address-out',
  address_failed: 'fp-address-failed',
};

// Viber rules for transactional templates: max 8 variables, max 875 characters,
// the text must not start or end with a variable.
export function viberTemplates(cfg) {
  const phone = cfg.supportPhone;
  return {
    thanks: [
      'Здравейте, {{name}}! 💗',
      'Благодарим Ви за поръчката във FitPatches!',
      '',
      '💗 Розовите лепенки FitPatches за намаляване на апетита',
      '💶 Сума при получаване: {{amount}}',
      '📍 Доставка: {{delivery}}',
      '',
      `Ще Ви пишем, когато пратката пристигне. За въпроси: ${phone}`,
    ].join('\n'),
    office: [
      'Здравейте, {{name}}! 📦',
      'Вашите розови лепенки FitPatches за намаляване на апетита вече Ви чакат в офиса на {{courier}}:',
      '📍 {{office}}',
      '🔢 Товарителница: {{tracking}}',
      '💶 Сума за плащане: {{amount}}',
      '',
      'Вземете я, когато Ви е удобно. Пратките се пазят в офиса само няколко дни.',
    ].join('\n'),
    office_reminder: [
      'Здравейте, {{name}}! 💗',
      'Напомняме, че розовите лепенки FitPatches за намаляване на апетита още Ви чакат в {{place}}.',
      '🔢 Товарителница: {{tracking}} · 💶 Сума: {{amount}}',
      `Ако не можете да я вземете, обадете ни се: ${phone}`,
    ].join('\n'),
    office_last: [
      'Здравейте, {{name}}! ⏰',
      'Последно напомняне: пратката Ви с розовите лепенки FitPatches за намаляване на апетита е в {{place}}.',
      '🔢 Товарителница: {{tracking}} · 💶 Сума: {{amount}}',
      'Ако не бъде взета в следващите дни, куриерът ще я върне.',
    ].join('\n'),
    address_out: [
      'Здравейте, {{name}}! 🚚',
      'Днес куриер на {{courier}} ще Ви донесе розовите лепенки FitPatches за намаляване на апетита.',
      '🔢 Товарителница: {{tracking}}',
      '💶 Пригответе {{amount}} за плащане.',
    ].join('\n'),
    address_failed: [
      'Здравейте, {{name}}! Куриерът на {{courier}} не успя да Ви открие днес с розовите лепенки FitPatches за намаляване на апетита.',
      '🔢 Товарителница: {{tracking}}',
      `Обадете ни се на ${phone}, за да уточним кога да Ви я донесат.`,
    ].join('\n'),
  };
}

const TRANSLIT = {
  а: 'a', б: 'b', в: 'v', г: 'g', д: 'd', е: 'e', ж: 'zh', з: 'z', и: 'i', й: 'y', к: 'k', л: 'l', м: 'm',
  н: 'n', о: 'o', п: 'p', р: 'r', с: 's', т: 't', у: 'u', ф: 'f', х: 'h', ц: 'ts', ч: 'ch', ш: 'sh',
  щ: 'sht', ъ: 'a', ь: 'y', ю: 'yu', я: 'ya', ё: 'yo', ы: 'i', э: 'e',
};

// Bulgarian streamlined transliteration, reduced to plain GSM-7 characters.
export function toLatin(s) {
  return String(s ?? '')
    .replace(/ия(?![а-яё])/g, 'ia')
    .replace(/ИЯ(?![А-ЯЁ])/g, 'IA')
    .replace(/[а-яё]/gi, (ch) => {
      const lat = TRANSLIT[ch.toLowerCase()];
      if (ch === ch.toLowerCase()) return lat;
      return lat.charAt(0).toUpperCase() + lat.slice(1);
    })
    .replace(/№/g, 'No')
    .replace(/[^A-Za-z0-9 .,:;!?'"()\-\/+&%#*@]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

const money = (n) => (Math.round(n * 100) / 100).toFixed(2);

function fit(parts, max = 160) {
  const text = parts.filter(Boolean).join(' ');
  return text.length <= max ? text : text.slice(0, max - 1).trimEnd() + '.';
}

export function fill(template, params) {
  return template.replace(/\{\{(\w+)\}\}/g, (_, k) => params[k] ?? '');
}

export function render(type, info, cfg) {
  const template = viberTemplates(cfg)[type];
  if (!template) throw new Error(`Непознат тип съобщение: ${type}`);

  const name = info.firstName;
  const courier = COURIER[info.courier] || 'куриера';
  const office = info.office?.text || '';
  const all = {
    name: name || 'клиент',
    courier,
    office,
    // Address orders that ended up in an office have no office address in the order.
    place: office ? `офиса на ${courier} – ${office}` : `офис на ${courier}`,
    tracking: info.fulfillment?.tracking || '',
    amount: `${money(info.amount)} ${info.currency === 'EUR' ? '€' : info.currency}`,
    delivery: info.isOffice ? `офис на ${courier} – ${office}` : `до адрес ${info.courier === 'speedy' ? 'със' : 'с'} ${courier}`,
  };
  // Only the variables this template uses (Viber rejects unknown ones).
  const params = Object.fromEntries([...template.matchAll(/\{\{(\w+)\}\}/g)].map(([, k]) => [k, String(all[k]).slice(0, 125)]));
  const viber = fill(name ? template : template.replace('Здравейте, {{name}}!', 'Здравейте!'), params);

  const helloLat = name ? `${toLatin(name)}, ` : '';
  const courierLat = COURIER_LAT[info.courier] || 'kuriera';
  const officeLat = info.office?.city ? ' ' + toLatin(info.office.city).slice(0, 25) : '';
  const tracking = all.tracking;
  const amountLat = info.amount > 0 ? `${money(info.amount)} ${info.currency}` : '';
  const phone = cfg.supportPhone;
  const sms = {
    thanks: [
      name ? `FitPatches: Blagodarim za porachkata, ${toLatin(name)}!` : 'FitPatches: Blagodarim za porachkata!',
      `Rozovite lepenki za namalyavane na apetita idvat ${info.courier === 'speedy' ? 'sas' : 's'} ${courierLat}.`,
      amountLat && `Suma ${amountLat}.`,
      `Tel. ${phone}`,
    ],
    office: [
      `FitPatches: ${helloLat}rozovite lepenki za namalyavane na apetita vi chakat v ofis ${courierLat}${officeLat}.`,
      `Tovaritelnitsa ${tracking}${amountLat && `, suma ${amountLat}`}.`,
    ],
    office_reminder: [
      `FitPatches: Napomnyane - lepenkite vi chakat v ofis ${courierLat}${officeLat}.`,
      `Tovaritelnitsa ${tracking}${amountLat && `, suma ${amountLat}`}.`,
      `Tel. ${phone}`,
    ],
    office_last: [
      `FitPatches: Posledno napomnyane - pratkata vi e v ofis ${courierLat}${officeLat} i skoro shte bade varnata.`,
      `Tovaritelnitsa ${tracking}${amountLat && `, suma ${amountLat}`}.`,
    ],
    address_out: [
      `FitPatches: ${helloLat}dnes kurier na ${courierLat} shte vi donese rozovite lepenki za namalyavane na apetita.`,
      `Tovaritelnitsa ${tracking}${amountLat && `, prigotvete ${amountLat}`}.`,
    ],
    address_failed: [
      `FitPatches: ${helloLat}kurierat na ${courierLat} ne uspya da vi otkrie dnes.`,
      `Tovaritelnitsa ${tracking}. Obadete ni se: ${phone}`,
    ],
  }[type];

  return { viber, sms: fit(sms), template: { key: TEMPLATE_KEYS[type], params } };
}
