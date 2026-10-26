// Turns a Shopify order into the fields the messages need, and works out where the parcel is.
import { classify, cityKey } from './bigarena.js';

export function normalizePhone(raw) {
  let p = String(raw ?? '').replace(/[^\d+]/g, '');
  if (p.startsWith('+')) p = p.slice(1);
  else if (p.startsWith('00')) p = p.slice(2);
  else if (p.startsWith('0')) p = '359' + p.slice(1);
  else if (/^[89]\d{8}$/.test(p)) p = '359' + p;
  return /^359\d{8,9}$/.test(p) ? p : null;
}

function titleCase(s) {
  return s.toLowerCase().replace(/(^|[\s-])(\p{L})/gu, (_, sep, ch) => sep + ch.toUpperCase());
}

export function cleanName(raw) {
  const first = String(raw ?? '').trim().split(/[\s.,_@]+/)[0] || '';
  const name = first.replace(/[^\p{L}'-]/gu, '').slice(0, 20);
  if (!name) return '';
  return name === name.toLowerCase() || name === name.toUpperCase() ? titleCase(name) : name;
}

// "До офис econt[7538]: Айдемир -  Айдемир кв. Деленките ул. София №7"
// "До офис speedy[299]: СОФИЯ - ОВЧА КУПЕЛ - СТАРАТА ЧАСТ 2 ул. Народно хоро No 11"
export function parseOffice(address1, fallbackCity) {
  const a = String(address1 ?? '').replace(/\s+/g, ' ').trim();
  const m = a.match(/^до офис[^:]*\]:\s*(.+)$/iu);
  if (!m) {
    const city = String(fallbackCity ?? '').trim();
    return { city, text: a || city };
  }
  const rest = m[1];
  const i = rest.indexOf(' - ');
  const rawCity = i > 0 ? rest.slice(0, i).trim() : String(fallbackCity ?? '').trim();
  const place = i > 0 ? rest.slice(i + 3).trim() : rest;
  const city = rawCity === rawCity.toUpperCase() ? titleCase(rawCity) : rawCity;
  const text = cityKey(place).startsWith(cityKey(city)) ? place : `${city}, ${place}`;
  return { city, text };
}

function courierOf(title, company) {
  const s = `${title ?? ''} ${company ?? ''}`;
  if (/econt|еконт/iu.test(s)) return 'econt';
  if (/speedy|спиди/iu.test(s)) return 'speedy';
  return null;
}

export function orderInfo(order) {
  const addr = order.shippingAddress || {};
  const title = order.shippingLine?.title || '';
  const address1 = String(addr.address1 ?? '').trim();
  const isOffice = /офис/iu.test(title) || /^до офис/iu.test(address1);

  const withTracking = (order.fulfillments || [])
    .filter((f) => f.trackingInfo?.[0]?.number)
    .sort((a, b) => new Date(b.createdAt || 0) - new Date(a.createdAt || 0));
  const f = withTracking[0];
  const courier = courierOf(title, f?.trackingInfo?.[0]?.company);
  const office = isOffice ? parseOffice(address1, addr.city) : null;
  const money = order.totalOutstandingSet?.presentmentMoney;

  return {
    id: order.id,
    name: order.name,
    createdAt: new Date(order.createdAt),
    cancelled: Boolean(order.cancelledAt) || ['VOIDED', 'REFUNDED'].includes(order.displayFinancialStatus),
    upsellReplaced: (order.tags || []).includes('fp-upsell-replaced'),
    paid: order.displayFinancialStatus === 'PAID',
    firstName: cleanName(addr.firstName || order.customer?.firstName),
    phone: normalizePhone(order.phone || addr.phone),
    isOffice,
    courier,
    office,
    destCity: office?.city || String(addr.city ?? '').trim(),
    amount: Number(money?.amount || 0),
    currency: money?.currencyCode || 'EUR',
    fulfillment: f
      ? {
          tracking: String(f.trackingInfo[0].number),
          url: f.trackingInfo[0].url || '',
          displayStatus: f.displayStatus || '',
          events: (f.events?.nodes || [])
            .map((e) => ({ status: e.status, at: new Date(e.happenedAt) }))
            .sort((a, b) => a.at - b.at),
        }
      : null,
  };
}

// Status from Shopify's own fulfillment events (filled in by Middleware.bg). Used as a cross-check
// and as a fallback when BigArena has no data.
export function shopifyShipment(info) {
  const f = info.fulfillment;
  if (!f) return { state: 'unknown', since: null, outAt: null, failedAt: null };
  const has = (s) => f.events.some((e) => e.status === s);
  if (f.displayStatus === 'DELIVERED' || has('DELIVERED')) return { state: 'delivered', since: null, outAt: null, failedAt: null };
  if (f.displayStatus === 'NOT_DELIVERED' || has('FAILURE')) return { state: 'returned', since: null, outAt: null, failedAt: null };

  let state = 'unknown';
  let since = null;
  let outAt = null;
  let failedAt = null;
  for (const e of f.events) {
    let next = null;
    if (e.status === 'IN_TRANSIT') next = 'in_transit';
    else if (e.status === 'READY_FOR_PICKUP') next = 'at_office';
    else if (e.status === 'OUT_FOR_DELIVERY') next = info.isOffice ? 'at_office' : 'out_for_delivery';
    else if (e.status === 'ATTEMPTED_DELIVERY') next = 'failed_attempt';
    if (next === 'out_for_delivery') outAt = e.at;
    if (next === 'failed_attempt') failedAt = e.at;
    if (!next || next === state) continue;
    state = next;
    since = e.at;
  }
  return { state, since, outAt, failedAt };
}

const TERMINAL = new Set(['delivered', 'returned', 'cancelled']);
export const isTerminal = (ship) => TERMINAL.has(ship?.state);

// Shopify decides "cancelled / paid / delivered / returned"; BigArena gives the live courier status.
export function shipmentStatus(info, tracking) {
  if (info.cancelled) return { state: 'cancelled', since: null, outAt: null, failedAt: null, source: 'shopify' };
  if (info.paid) return { state: 'delivered', since: null, outAt: null, failedAt: null, source: 'shopify' };
  const shop = shopifyShipment(info);
  if (isTerminal(shop)) return { ...shop, source: 'shopify' };
  if (tracking && !tracking.noData) {
    return { ...classify(tracking.events, { courier: info.courier, destCity: info.destCity }), source: 'bigarena' };
  }
  return { ...shop, source: 'shopify' };
}

export function needsTracking(info) {
  return Boolean(info.fulfillment) && !info.cancelled && !info.paid && !isTerminal(shopifyShipment(info));
}
