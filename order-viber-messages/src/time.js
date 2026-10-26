// Europe/Sofia helpers without external libraries.
const TZ = 'Europe/Sofia';
const fmt = new Intl.DateTimeFormat('en-GB', {
  timeZone: TZ,
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hourCycle: 'h23',
});

function parts(date) {
  return Object.fromEntries(fmt.formatToParts(date).map((p) => [p.type, p.value]));
}

function offsetMs(date) {
  const p = parts(date);
  const asUtc = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second);
  return asUtc - Math.floor(date.getTime() / 1000) * 1000;
}

export function sofiaDate(date) {
  const p = parts(date);
  return `${p.year}-${p.month}-${p.day}`;
}

export function sofiaMinutes(date) {
  const p = parts(date);
  return Number(p.hour) * 60 + Number(p.minute);
}

// "2026-10-22 08:46:03" in Sofia local time -> Date
export function fromSofiaLocal(str) {
  const m = String(str).trim().match(/^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2})(?::(\d{2}))?$/);
  if (!m) return null;
  const naive = Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4], +m[5], +(m[6] || 0));
  let guess = naive - offsetMs(new Date(naive));
  guess = naive - offsetMs(new Date(guess));
  return new Date(guess);
}

export function withinHours(date, range) {
  const [from, to] = range.split('-').map((t) => {
    const [h, m] = t.split(':').map(Number);
    return h * 60 + (m || 0);
  });
  const x = sofiaMinutes(date);
  return x >= from && x < to;
}

export const HOUR = 3600 * 1000;
export const DAY = 24 * HOUR;
