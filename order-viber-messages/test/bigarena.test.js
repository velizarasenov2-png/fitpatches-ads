import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseTracking, classify, normalize, trackingUrl } from '../src/bigarena.js';
import { fromSofiaLocal, withinHours } from '../src/time.js';
import { trackingHtml } from './helpers.js';

test('Sofia local time converts correctly in summer and winter', () => {
  assert.equal(fromSofiaLocal('2026-10-22 08:46:03').toISOString(), '2026-10-22T05:46:03.000Z');
  assert.equal(fromSofiaLocal('2026-10-26 07:53:57').toISOString(), '2026-10-26T05:53:57.000Z');
  assert.equal(withinHours(new Date('2026-10-26T06:00:00Z'), '08:00-21:00'), true); // 08:00 Sofia
  assert.equal(withinHours(new Date('2026-10-26T05:59:00Z'), '08:00-21:00'), false);
  assert.equal(withinHours(new Date('2026-10-26T19:00:00Z'), '08:00-21:00'), false); // 21:00 Sofia
});

test('tracking URL is the base64 of the tracking number', () => {
  assert.equal(trackingUrl('63000000001'), 'https://my.bigarena.net/tracking/order/NjMwMDAwMDAwMDE=');
});

test('parses events with and without city, and the "no data" page', () => {
  const html = trackingHtml([
    ['2026-10-16 08:25:07', 'Провадия', 'Провадия'],
    ['2026-10-15 15:32:39', 'Пловдив', 'Пловдив ЛЛЦ Цар Борис III &amp; Ко'],
    ['2026-10-17 09:00:00', '', 'Връщане на пратката'],
  ]);
  const t = parseTracking(html);
  assert.equal(t.noData, false);
  assert.deepEqual(t.events.map((e) => e.city), ['Пловдив', 'Провадия', '']); // sorted by time
  assert.equal(t.events[0].text, 'Пловдив ЛЛЦ Цар Борис III & Ко');
  assert.equal(parseTracking(trackingHtml([])).noData, true);
});

test('normalize fixes Latin look-alike letters inside Cyrillic words only', () => {
  assert.equal(normalize('Неуспешнa доставка'), 'неуспешна доставка');
  assert.equal(normalize('Oтказване от получател'), 'отказване от получател');
  assert.equal(normalize('Tatiana Slavova'), 'tatiana slavova');
});

const speedy = (rows) => classify(parseTracking(trackingHtml(rows)).events, { courier: 'speedy' });

test('Speedy: parcel waiting in the office', () => {
  const s = speedy([
    ['2026-10-21 09:44:19', '', 'Получена информация за пратка'],
    ['2026-10-21 21:39:11', '', 'Изпращане от офис'],
    ['2026-10-22 08:44:48', '', 'Подготовка за предаване на клиент в офис'],
    ['2026-10-22 08:49:35', '', 'Изпратено известие за пратка в офис/автомат'],
    ['2026-10-23 10:00:00', '', 'Уточняване на доставка'],
  ]);
  assert.equal(s.state, 'at_office');
  assert.equal(s.since.toISOString(), '2026-10-22T05:44:48.000Z');
});

test('Speedy: refused at the office counts as returned and stays returned', () => {
  const s = speedy([
    ['2026-10-22 08:37:42', '', 'Подготовка за предаване на клиент в офис'],
    ['2026-10-22 08:46:03', '', 'Oтказване от получател'],
    ['2026-10-22 09:05:35', '', 'Връщане към подателя'],
    ['2026-10-23 09:24:39', '', 'Предаване обратно на подател'],
  ]);
  assert.equal(s.state, 'returned');
});

test('Speedy: picked up from the office', () => {
  const s = speedy([
    ['2026-10-21 08:35:56', '', 'Подготовка за предаване на клиент в офис'],
    ['2026-10-23 17:58:10', '', 'Отказ от преглед/тестване'],
    ['2026-10-23 17:58:12', '', 'Доставка на клиент'],
  ]);
  assert.equal(s.state, 'delivered');
});

test('Speedy: failed address delivery, then moved to an office', () => {
  const s = speedy([
    ['2026-10-21 08:20:59', '', 'Предаване на куриер за доставка'],
    ['2026-10-21 11:06:40', '', 'Неуспешнa доставка'],
    ['2026-10-21 11:21:36', '', 'Подготовка за предаване на клиент в офис'],
    ['2026-10-21 11:47:31', '', 'Връщане в офис'],
  ]);
  assert.equal(s.state, 'at_office');
  assert.equal(s.outAt.toISOString(), '2026-10-21T05:20:59.000Z');
  assert.equal(s.failedAt.toISOString(), '2026-10-21T08:06:40.000Z');
});

const econt = (rows, destCity) => classify(parseTracking(trackingHtml(rows, { courier: 'Еконт експрес' })).events, { courier: 'econt', destCity });

test('Econt: last scan in the destination office means waiting there', () => {
  const s = econt(
    [
      ['2026-10-21 15:12:45', 'Пловдив', 'Пловдив ЛЛЦ Цар Борис III'],
      ['2026-10-21 22:17:57', 'Пловдив', 'Пловдив - София - Пловдив'],
      ['2026-10-22 01:20:24', 'София', 'София НЛЦ Орион'],
      ['2026-10-22 05:34:57', 'София', 'София - Кюстендил'],
      ['2026-10-22 08:00:09', 'Кюстендил', 'Кюстендил Мориц Леви'],
    ],
    'Кюстендил',
  );
  assert.equal(s.state, 'at_office');
  assert.equal(s.since.toISOString(), '2026-10-22T05:00:09.000Z');
});

test('Econt: receiver name as last location means delivered', () => {
  const s = econt(
    [
      ['2026-10-22 08:47:49', 'Ямбол', 'Ямбол'],
      ['2026-10-22 17:26:51', 'Ямбол', 'Иван Иванов'],
    ],
    'Ямбол',
  );
  assert.equal(s.state, 'delivered');
});

test('Econt: "Връщане на пратката" means returned, later scans do not matter', () => {
  const s = econt(
    [
      ['2026-10-21 08:06:47', 'София', 'София Челопечене'],
      ['2026-10-23 11:17:35', '', 'Връщане на пратката'],
      ['2026-10-26 11:34:41', 'Пловдив', 'Подател ЕООД'],
    ],
    'София',
  );
  assert.equal(s.state, 'returned');
});

test('Econt: an office in another city is still in transit', () => {
  const s = econt([['2026-10-21 08:06:47', 'Пловдив', 'Пловдив Тракия']], 'Варна');
  assert.equal(s.state, 'in_transit');
});
