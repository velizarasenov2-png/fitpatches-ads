// Shipment tracking from the public BigArena tracking page (my.bigarena.net/tracking/order/<base64 tracking number>).
import { fromSofiaLocal } from './time.js';

const UA = 'Mozilla/5.0 (compatible; FitPatches-order-messages/1.0)';

export function trackingUrl(number, url) {
  if (url && /^https:\/\/my\.bigarena\.net\/tracking\/order\//.test(url)) return url;
  return 'https://my.bigarena.net/tracking/order/' + Buffer.from(String(number)).toString('base64');
}

export async function fetchTracking(number, url, fetchImpl = fetch) {
  const res = await fetchImpl(trackingUrl(number, url), {
    headers: { 'User-Agent': UA, Accept: 'text/html' },
    signal: AbortSignal.timeout(20000),
  });
  if (!res.ok) throw new Error(`bigarena HTTP ${res.status}`);
  return parseTracking(await res.text());
}

const ENTITIES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' };
function decode(s) {
  return s
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(+n))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)))
    .replace(/&([a-z]+);/gi, (m, n) => ENTITIES[n.toLowerCase()] ?? m);
}
const clean = (s) => decode(String(s ?? '').replace(/<[^>]*>/g, ' ')).replace(/\s+/g, ' ').trim();

export function parseTracking(html) {
  const events = [];
  const blocks = html.split('tracking-shipment-box-steps"').slice(1);
  for (const block of blocks) {
    const date = block.match(/steps-date">([\s\S]*?)<\/div>/);
    if (!date) continue;
    const dm = clean(date[1]).match(/^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(?:\s*-\s*(.*))?$/);
    if (!dm) continue;
    const msg = block.match(/steps-message">([\s\S]*?)<\/div>/);
    events.push({ at: fromSofiaLocal(dm[1]), city: dm[2] || '', text: msg ? clean(msg[1]) : '' });
  }
  events.sort((a, b) => a.at - b.at);
  return { events, noData: events.length === 0 };
}

// Speedy mixes Latin look-alike letters into Cyrillic words ("Неуспешнa", "Oтказване").
const LOOKALIKE = { A: 'А', B: 'В', E: 'Е', K: 'К', M: 'М', H: 'Н', O: 'О', P: 'Р', C: 'С', T: 'Т', X: 'Х', Y: 'У', a: 'а', e: 'е', o: 'о', p: 'р', c: 'с', x: 'х', y: 'у' };
export function normalize(s) {
  return String(s ?? '')
    .split(/(\s+)/)
    .map((w) => (/[а-яё]/i.test(w) ? w.replace(/[ABEKMHOPCTXYaeopcxy]/g, (ch) => LOOKALIKE[ch]) : w))
    .join('')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim();
}

export function cityKey(s) {
  return normalize(s)
    .replace(/^(гр\.?|град|с\.|село)\s*/, '')
    .replace(/[^a-zа-я0-9 ]/g, '')
    .trim();
}

function sameCity(a, b) {
  const x = cityKey(a);
  const y = cityKey(b);
  return Boolean(x && y && (x === y || x.startsWith(y + ' ') || y.startsWith(x + ' ')));
}

function speedyState(text) {
  const t = normalize(text);
  if (/доставка на клиент/.test(t)) return 'delivered';
  if (/отказване от получател|отказ от получател|връщане към подател|предаване обратно на подател/.test(t)) return 'returned';
  if (/неуспешна доставка/.test(t)) return 'failed_attempt';
  if (/предаване на куриер за доставка/.test(t)) return 'out_for_delivery';
  if (/подготовка за предаване на клиент в офис|изпратено известие за пратка в офис/.test(t)) return 'at_office';
  if (/уточняване на доставка|предикт|преглед|тестване|пристигане в офис|връщане в офис/.test(t)) return null; // no change
  return 'in_transit';
}

function econtState(event, destCity) {
  const t = normalize(event.text);
  if (/връщане на пратката/.test(t)) return 'returned';
  if (/(^|\s)(ллц|нлц|цлц)(\s|$)|склад|сортировъч/.test(t) || / - /.test(event.text)) return 'in_transit';
  const city = cityKey(event.city);
  if (city && cityKey(event.text).includes(city)) {
    return !destCity || sameCity(event.city, destCity) ? 'at_office' : 'in_transit';
  }
  // Econt shows the receiver's name as the last location once the parcel is handed over.
  return event.city ? 'delivered' : null;
}

/**
 * @returns {{state: string, since: Date|null, outAt: Date|null, failedAt: Date|null}}
 * state: unknown | in_transit | at_office | out_for_delivery | failed_attempt | delivered | returned
 * outAt / failedAt: latest "out for delivery" / "failed delivery" event, kept even when a later
 * event (e.g. Speedy moving the parcel back to an office) changes the state.
 */
export function classify(events, { courier, destCity } = {}) {
  let state = 'unknown';
  let since = null;
  let outAt = null;
  let failedAt = null;
  for (const ev of events) {
    if (state === 'delivered' || state === 'returned') break;
    const next = courier === 'econt' ? econtState(ev, destCity) : speedyState(ev.text);
    if (next === 'out_for_delivery') outAt = ev.at;
    if (next === 'failed_attempt') failedAt = ev.at;
    if (!next || next === state) continue;
    state = next;
    since = ev.at;
  }
  return { state, since, outAt, failedAt };
}
