// Which message (if any) an order should get right now. One message per order per run.
import { DAY, HOUR, sofiaDate } from './time.js';

function officeSteps(reminderDays) {
  return [['office', 0], ...reminderDays.map((d, i) => [`office_r${i + 1}`, d * DAY])];
}

function lastSentAt(sent, keys) {
  const times = keys.map((k) => Date.parse(sent[k])).filter((t) => !Number.isNaN(t));
  return times.length ? Math.max(...times) : null;
}

// Parcel waiting in a courier office: arrival message, then reminders after cfg.reminderDays.
// Address deliveries the courier moved to an office after a failed attempt get only the reminders
// (the "failed delivery" message already told the customer).
function officeMessage(info, ship, sent, now, cfg) {
  if (ship.state !== 'at_office' || !ship.since) return null;
  const age = now - ship.since;
  if (age < 0 || age > 12 * DAY) return null;
  const steps = officeSteps(cfg.reminderDays);
  let idx = -1;
  steps.forEach(([, after], i) => {
    if (age >= after) idx = i;
  });
  if (!info.isOffice && idx === 0) return null;
  if (idx < 0 || steps.slice(idx).some(([k]) => sent[k])) return null;
  const prev = lastSentAt(sent, [...steps.map(([k]) => k), ...Object.keys(sent).filter((k) => k.startsWith('failed_'))]);
  if (prev && now - prev < 20 * HOUR) return null;
  const type = idx === 0 ? 'office' : idx === steps.length - 1 ? 'office_last' : 'office_reminder';
  const skip = steps.slice(0, idx).map(([k]) => k).filter((k) => !sent[k] && (info.isOffice || k !== 'office'));
  return { key: steps[idx][0], type, skip };
}

/**
 * @param info  orderInfo(...)
 * @param ship  shipmentStatus(...) or null when the order has no shipment yet
 * @param sent  { [key]: ISO time | 'skipped' | 'failed:...' } stored on the order
 * @returns {{key: string, type: string, skip?: string[]} | null}
 */
export function decide(info, ship, sent, now, cfg) {
  if (info.cancelled || info.upsellReplaced) return null;
  const finished = ship && ['delivered', 'returned', 'cancelled'].includes(ship.state);

  if (!sent.thanks && !finished) {
    const start = cfg.startAt ?? (cfg.live ? null : new Date(0));
    const age = now - info.createdAt;
    if (start && info.createdAt >= start && age >= cfg.thanksDelayMinutes * 60000 && age <= 2 * DAY) {
      return { key: 'thanks', type: 'thanks' };
    }
  }
  if (!ship || !info.fulfillment || finished) return null;
  if (info.isOffice) return officeMessage(info, ship, sent, now, cfg);

  const count = (prefix) => Object.keys(sent).filter((k) => k.startsWith(prefix)).length;
  if (ship.failedAt && now - ship.failedAt < DAY && (!ship.outAt || ship.failedAt >= ship.outAt)) {
    const key = 'failed_' + sofiaDate(ship.failedAt);
    if (!sent[key] && count('failed_') < 2) return { key, type: 'address_failed' };
  }
  if (ship.state === 'out_for_delivery' && ship.outAt && sofiaDate(ship.outAt) === sofiaDate(now)) {
    const key = 'out_' + sofiaDate(ship.outAt);
    if (!sent[key] && count('out_') < 2) return { key, type: 'address_out' };
  }
  return officeMessage(info, ship, sent, now, cfg);
}
