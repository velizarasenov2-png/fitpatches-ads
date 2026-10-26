import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizePhone, parseOffice, cleanName, orderInfo, shipmentStatus, needsTracking } from '../src/order.js';
import { decide } from '../src/decide.js';
import { render, toLatin } from '../src/messages.js';
import { parseTracking } from '../src/bigarena.js';
import { baseCfg, orderNode, fulfillment, trackingHtml } from './helpers.js';

const H = 3600 * 1000;
const D = 24 * H;

test('phone numbers are normalised to 359...', () => {
  assert.equal(normalizePhone('+359 888 000 111'), '359888000111');
  assert.equal(normalizePhone('0888000111'), '359888000111');
  assert.equal(normalizePhone('00359888000111'), '359888000111');
  assert.equal(normalizePhone('888000111'), '359888000111');
  assert.equal(normalizePhone('12345'), null);
  assert.equal(normalizePhone(''), null);
});

test('office text is read from address1 (Econt and Speedy formats)', () => {
  assert.deepEqual(parseOffice('До офис econt[7538]: Айдемир -  Айдемир кв. Деленките ул. София №7', 'Айдемир'), {
    city: 'Айдемир',
    text: 'Айдемир кв. Деленките ул. София №7',
  });
  assert.deepEqual(parseOffice('До офис speedy[299]: СОФИЯ - ОВЧА КУПЕЛ - СТАРАТА ЧАСТ 2 ул. Народно хоро No 11', 'София'), {
    city: 'София',
    text: 'София, ОВЧА КУПЕЛ - СТАРАТА ЧАСТ 2 ул. Народно хоро No 11',
  });
  assert.deepEqual(parseOffice('ул. Някоя 5', 'Варна'), { city: 'Варна', text: 'ул. Някоя 5' });
});

test('names are cleaned and capitalised', () => {
  assert.equal(cleanName('мария петрова'), 'Мария');
  assert.equal(cleanName('ЙОАНА'), 'Йоана');
  assert.equal(cleanName('  '), '');
});

test('orderInfo reads courier, office, amount, phone and tracking', () => {
  const info = orderInfo(orderNode({ fulfillments: [fulfillment('1055000000001')] }));
  assert.equal(info.courier, 'econt');
  assert.equal(info.isOffice, true);
  assert.equal(info.destCity, 'Айдемир');
  assert.equal(info.amount, 25.38);
  assert.equal(info.phone, '359888000111');
  assert.equal(info.fulfillment.tracking, '1055000000001');
});

test('Shopify cancel / paid / FAILURE override BigArena; no BigArena data falls back to Shopify', () => {
  const waiting = parseTracking(trackingHtml([['2026-10-22 08:00:09', 'Айдемир', 'Айдемир']]));
  const cancelled = orderInfo(orderNode({ cancelledAt: '2026-10-23T00:00:00Z', fulfillments: [fulfillment('1')] }));
  assert.equal(shipmentStatus(cancelled, waiting).state, 'cancelled');
  assert.equal(needsTracking(cancelled), false);

  const paid = orderInfo(orderNode({ displayFinancialStatus: 'PAID', fulfillments: [fulfillment('1')] }));
  assert.equal(shipmentStatus(paid, waiting).state, 'delivered');

  const failed = orderInfo(orderNode({ fulfillments: [fulfillment('1', [['IN_TRANSIT', '2026-10-21T10:00:00Z'], ['FAILURE', '2026-10-23T10:00:00Z']])] }));
  assert.equal(shipmentStatus(failed, waiting).state, 'returned');

  const live = orderInfo(orderNode({ fulfillments: [fulfillment('1', [['IN_TRANSIT', '2026-10-21T10:00:00Z']])] }));
  assert.equal(shipmentStatus(live, waiting).state, 'at_office');
  assert.equal(shipmentStatus(live, waiting).source, 'bigarena');
  const fallback = shipmentStatus(live, parseTracking(trackingHtml([])));
  assert.equal(fallback.state, 'in_transit');
  assert.equal(fallback.source, 'shopify');
});

test('thank-you: after the delay, only for orders after START_AT, never for upsell-replaced or cancelled', () => {
  const info = orderInfo(orderNode({ createdAt: '2026-10-26T08:00:00Z' }));
  const t = (min) => new Date(Date.parse('2026-10-26T08:00:00Z') + min * 60000);
  assert.equal(decide(info, null, {}, t(2), baseCfg), null);
  assert.deepEqual(decide(info, null, {}, t(6), baseCfg), { key: 'thanks', type: 'thanks' });
  assert.equal(decide(info, null, { thanks: 'x' }, t(6), baseCfg), null);
  assert.equal(decide(info, null, {}, t(6), { ...baseCfg, startAt: new Date('2026-10-27T00:00:00Z') }), null);
  assert.equal(decide(info, null, {}, t(3 * 24 * 60), baseCfg), null);
  const replaced = orderInfo(orderNode({ tags: ['fp-upsell-replaced'] }));
  assert.equal(decide(replaced, null, {}, t(6), baseCfg), null);
  const cancelled = orderInfo(orderNode({ cancelledAt: '2026-10-26T08:01:00Z', displayFinancialStatus: 'VOIDED' }));
  assert.equal(decide(cancelled, null, {}, t(6), baseCfg), null);
});

test('office: arrival message, reminder after 2 days, last reminder after 4 days', () => {
  const info = orderInfo(orderNode({ createdAt: '2026-10-20T08:00:00Z', fulfillments: [fulfillment('1055000000001')] }));
  const since = new Date('2026-10-22T06:00:00Z');
  const ship = { state: 'at_office', since, outAt: null, failedAt: null };
  const at = (ms) => new Date(since.getTime() + ms);
  const sent = { thanks: 'x' };

  assert.equal(decide(info, ship, sent, at(H), baseCfg).type, 'office');
  const s1 = { ...sent, office: at(H).toISOString() };
  assert.equal(decide(info, ship, s1, at(D), baseCfg), null);
  assert.equal(decide(info, ship, s1, at(2 * D + H), baseCfg).type, 'office_reminder');
  const s2 = { ...s1, office_r1: at(2 * D + H).toISOString() };
  assert.equal(decide(info, ship, s2, at(3 * D), baseCfg), null);
  assert.equal(decide(info, ship, s2, at(4 * D + 2 * H), baseCfg).type, 'office_last');
  const s3 = { ...s2, office_r2: at(4 * D + 2 * H).toISOString() };
  assert.equal(decide(info, ship, s3, at(6 * D), baseCfg), null);
});

test('office backlog: a parcel already waiting 5 days gets only the last reminder', () => {
  const info = orderInfo(orderNode({ createdAt: '2026-09-20T08:00:00Z', fulfillments: [fulfillment('1')] }));
  const since = new Date('2026-10-21T06:00:00Z');
  const due = decide(info, { state: 'at_office', since }, {}, new Date(since.getTime() + 5 * D), baseCfg);
  assert.deepEqual(due, { key: 'office_r2', type: 'office_last', skip: ['office', 'office_r1'] });
});

test('nothing is sent for delivered or returned parcels', () => {
  const info = orderInfo(orderNode({ createdAt: '2026-10-20T08:00:00Z', fulfillments: [fulfillment('1')] }));
  const now = new Date('2026-10-26T10:00:00Z');
  for (const state of ['delivered', 'returned', 'cancelled']) {
    assert.equal(decide(info, { state, since: null }, {}, now, baseCfg), null);
  }
});

test('address: courier out today, failed attempt, then reminders if moved to an office', () => {
  const info = orderInfo(
    orderNode({
      createdAt: '2026-10-19T08:00:00Z',
      shippingLine: { title: 'До адрес speedy' },
      shippingAddress: { firstName: 'Ива', phone: '+359888000222', address1: 'ул. Примерна 1', city: 'Бургас' },
      fulfillments: [fulfillment('63000000001', [], 'FULFILLED', 'Спиди')],
    }),
  );
  const out = new Date('2026-10-21T05:20:00Z');
  const sent = { thanks: 'x' };
  assert.equal(decide(info, { state: 'out_for_delivery', since: out, outAt: out }, sent, new Date('2026-10-21T06:00:00Z'), baseCfg).key, 'out_2026-10-21');
  assert.equal(decide(info, { state: 'out_for_delivery', since: out, outAt: out }, sent, new Date('2026-10-22T06:00:00Z'), baseCfg), null);

  const failedAt = new Date('2026-10-21T08:06:00Z');
  const moved = { state: 'at_office', since: new Date('2026-10-21T08:21:00Z'), outAt: out, failedAt };
  const s1 = { ...sent, 'out_2026-10-21': 'x' };
  assert.equal(decide(info, moved, s1, new Date('2026-10-21T09:00:00Z'), baseCfg).type, 'address_failed');
  const s2 = { ...s1, 'failed_2026-10-21': '2026-10-21T09:00:00Z' };
  assert.equal(decide(info, moved, s2, new Date('2026-10-22T09:00:00Z'), baseCfg), null);
  const r = decide(info, moved, s2, new Date('2026-10-23T09:00:00Z'), baseCfg);
  assert.deepEqual(r, { key: 'office_r1', type: 'office_reminder', skip: [] });
  assert.match(render(r.type, info, baseCfg).viber, /още Ви чакат в офис на Спиди\./);
});

test('texts: product line, tracking number, phone; no order number; SMS fits one GSM-7 message', () => {
  const info = orderInfo(
    orderNode({
      name: '#2001',
      shippingAddress: {
        firstName: 'Александра-Мариела',
        phone: '+359888000111',
        address1: 'До офис speedy[46]: ГОРНА ОРЯХОВИЦА - СВ.КНЯЗ БОРИС I (УЛ.) ул. Св. княз Борис I No 24 много дълъг адрес на офиса',
        city: 'Горна Оряховица',
      },
      shippingLine: { title: 'До офис speedy' },
      fulfillments: [fulfillment('63000000002', [], 'FULFILLED', 'Спиди')],
    }),
  );
  for (const type of ['thanks', 'office', 'office_reminder', 'office_last', 'address_out', 'address_failed']) {
    const { viber, sms } = render(type, info, baseCfg);
    assert.match(viber, /розов(ите|и) лепенки FitPatches за намаляване на апетита/i, type);
    assert.doesNotMatch(viber, /#2001/, type);
    assert.doesNotMatch(sms, /#2001/, type);
    assert.ok(sms.length <= 160, `${type} SMS is ${sms.length} chars`);
    assert.match(sms, /^[A-Za-z0-9 .,:;!?'"()\-\/+&%#*@]+$/, type);
    if (type !== 'thanks') assert.match(viber, /Товарителница: 63000000002/, type);
  }
  assert.match(render('thanks', info, baseCfg).viber, /За въпроси: 0887459494/);
  assert.match(render('office', info, baseCfg).viber, /💶 Сума за плащане: 25\.38 €/);
});

test('texts: zero amount and missing name are handled', () => {
  const info = orderInfo(orderNode({ totalOutstandingSet: { presentmentMoney: { amount: '0.0', currencyCode: 'EUR' } }, shippingAddress: { firstName: '', address1: '', city: 'Варна' }, customer: null, fulfillments: [fulfillment('1')] }));
  const { viber, sms } = render('office', info, baseCfg);
  assert.match(viber, /^Здравейте! 📦/);
  assert.doesNotMatch(viber, /Сума/);
  assert.doesNotMatch(sms, /suma/);
});

test('transliteration', () => {
  assert.equal(toLatin('София, ул. Гео Милев №10'), 'Sofia, ul. Geo Milev No10');
  assert.equal(toLatin('Щастлива Юлия'), 'Shtastliva Yulia');
});
