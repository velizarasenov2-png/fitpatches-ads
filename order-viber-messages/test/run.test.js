import { test } from 'node:test';
import assert from 'node:assert/strict';
import { runOnce } from '../src/run.js';
import { buildRequest, sendMessage } from '../src/bulkgate.js';
import { parseTracking } from '../src/bigarena.js';
import { baseCfg, orderNode, fulfillment, trackingHtml } from './helpers.js';

function fakeShopify(orders) {
  const saved = [];
  return {
    saved,
    async recentOrders() {
      return orders;
    },
    async saveSent(id, key, sent) {
      saved.push({ id, key, sent });
    },
  };
}

const NOW = new Date('2026-10-26T09:00:00Z'); // 11:00 in Sofia
const waitingSince23 = parseTracking(trackingHtml([['2026-10-23 08:00:09', 'Айдемир', 'Айдемир']]));

function scenario() {
  return [
    // new order 30 minutes ago -> thank-you
    orderNode({ id: 'o1', name: '#3001', createdAt: '2026-10-26T08:30:00Z' }),
    // upsell replaced the original -> nothing
    orderNode({ id: 'o2', name: '#3002', createdAt: '2026-10-26T08:30:00Z', tags: ['fp-upsell-replaced'], displayFinancialStatus: 'VOIDED', cancelledAt: '2026-10-26T08:30:10Z' }),
    // waiting in Econt office since 23.10 -> reminder (arrival message skipped)
    orderNode({ id: 'o3', name: '#3003', createdAt: '2026-10-21T08:00:00Z', fulfillments: [fulfillment('1055000000003')], msgs: { value: JSON.stringify({ thanks: '2026-10-21T08:10:00Z' }) } }),
    // already paid (picked up) -> nothing, and no tracking lookup
    orderNode({ id: 'o4', name: '#3004', createdAt: '2026-10-20T08:00:00Z', displayFinancialStatus: 'PAID', fulfillments: [fulfillment('1055000000004')], msgs: { value: '{"thanks":"x"}' } }),
  ];
}

test('live run sends due messages and remembers them on the order', async () => {
  const shopify = fakeShopify(scenario());
  const lookups = [];
  const sends = [];
  const logs = [];
  const summary = await runOnce({
    cfg: baseCfg,
    shopify,
    now: NOW,
    fetchTrackingImpl: async (n) => {
      lookups.push(n);
      return waitingSince23;
    },
    send: async (msg) => {
      sends.push(msg);
      return { ok: true, channel: 'viber' };
    },
    log: (l) => logs.push(l),
  });
  assert.deepEqual(lookups, ['1055000000003']);
  assert.equal(summary.sent, 2);
  assert.deepEqual(sends.map((s) => s.tag), ['#3001 thanks', '#3003 office_r1']);
  assert.equal(sends[0].phone, '359888000111');
  assert.deepEqual(shopify.saved.map((s) => [s.id, s.key, Object.keys(s.sent).sort()]), [
    ['o1', 'msgs', ['thanks']],
    ['o3', 'msgs', ['office', 'office_r1', 'thanks']],
  ]);
  assert.equal(shopify.saved[1].sent.office, 'skipped');
  // logs never contain phones or names
  assert.ok(!logs.join('\n').match(/359888|Мария/));
});

test('dry run sends nothing and writes nothing', async () => {
  const shopify = fakeShopify(scenario());
  let sends = 0;
  const summary = await runOnce({
    cfg: { ...baseCfg, live: false },
    shopify,
    now: NOW,
    fetchTrackingImpl: async () => waitingSince23,
    send: async () => {
      sends++;
      return { ok: true };
    },
    log: () => {},
  });
  assert.equal(sends, 0);
  assert.equal(shopify.saved.length, 0);
  assert.equal(summary.planned, 2);
});

test('outside sending hours nothing happens', async () => {
  const shopify = fakeShopify(scenario());
  const summary = await runOnce({ cfg: baseCfg, shopify, now: new Date('2026-10-26T20:30:00Z'), log: () => {} });
  assert.equal(summary.orders, 0);
});

test('test phone receives everything and state is kept separately', async () => {
  const shopify = fakeShopify(scenario());
  const sends = [];
  await runOnce({
    cfg: { ...baseCfg, testPhone: '0887459494' },
    shopify,
    now: NOW,
    fetchTrackingImpl: async () => waitingSince23,
    send: async (msg) => {
      sends.push(msg.phone);
      return { ok: true };
    },
    log: () => {},
  });
  assert.deepEqual(sends, ['359887459494', '359887459494']);
  assert.ok(shopify.saved.every((s) => s.key === 'msgs_test'));
});

test('temporary send errors are retried next run, bad numbers are not', async () => {
  const shopify = fakeShopify([orderNode({ id: 'o1', name: '#3001', createdAt: '2026-10-26T08:30:00Z' })]);
  await runOnce({ cfg: baseCfg, shopify, now: NOW, send: async () => ({ ok: false, permanent: false, reason: 'http_500' }), log: () => {} });
  assert.equal(shopify.saved.length, 0);
  await runOnce({ cfg: baseCfg, shopify, now: NOW, send: async () => ({ ok: false, permanent: true, reason: 'invalid_number' }), log: () => {} });
  assert.equal(shopify.saved[0].sent.thanks, 'failed:invalid_number');
});

test('BulkGate request: Viber first with SMS fallback, or SMS only', () => {
  const msg = { phone: '359888000111', viberText: 'V', smsText: 'S', tag: '#1 thanks' };
  const both = buildRequest(msg, baseCfg);
  assert.deepEqual(Object.keys(both.channel), ['viber', 'sms']);
  assert.deepEqual(both.channel.viber, { sender: 'FitPatches', expiration: 3600, text: 'V' });
  assert.equal(both.channel.sms.text, 'S');
  assert.equal(both.channel.sms.unicode, false);
  assert.equal(both.country, 'bg');
  const smsOnly = buildRequest(msg, { ...baseCfg, viberSender: '' });
  assert.deepEqual(Object.keys(smsOnly.channel), ['sms']);
});

test('BulkGate responses: success, bad number, and backup host on network error', async () => {
  const ok = await sendMessage({ phone: '1', viberText: 'v', smsText: 's' }, baseCfg, async () => ({
    ok: true,
    json: async () => ({ data: { response: [{ status: 'accepted', channel: 'viber' }] } }),
  }));
  assert.deepEqual(ok, { ok: true, channel: 'viber' });

  const bad = await sendMessage({ phone: '1', viberText: 'v', smsText: 's' }, baseCfg, async () => ({
    ok: true,
    json: async () => ({ data: { response: [{ status: 'invalid_number' }] } }),
  }));
  assert.deepEqual(bad, { ok: false, permanent: true, reason: 'invalid_number' });

  const hosts = [];
  const viaBackup = await sendMessage({ phone: '1', viberText: 'v', smsText: 's' }, baseCfg, async (url) => {
    hosts.push(new URL(url).host);
    if (hosts.length === 1) throw new Error('ECONNRESET');
    return { ok: true, json: async () => ({ data: { response: [{ status: 'sent', channel: 'sms' }] } }) };
  });
  assert.deepEqual(hosts, ['portal.bulkgate.com', 'backup1.bulkgate.com']);
  assert.equal(viaBackup.ok, true);
});
