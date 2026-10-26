// Twilio Programmable Messaging: SMS only (Twilio has no Viber channel).
const API = 'https://api.twilio.com/2010-04-01/Accounts';
// Problems with the number itself: retrying won't help. Account-wide problems
// (auth, Bulgaria not enabled in Geo permissions, no balance) are retried after you fix them.
const PERMANENT = new Set([21211, 21612, 21614, 21610]);

export function buildTwilioRequest({ phone, smsText }, cfg) {
  const params = new URLSearchParams({ To: '+' + phone, Body: smsText });
  if (/^MG[0-9a-f]{32}$/i.test(cfg.twilioFrom)) params.set('MessagingServiceSid', cfg.twilioFrom);
  else params.set('From', cfg.twilioFrom);
  return {
    url: `${API}/${encodeURIComponent(cfg.twilioAccountSid)}/Messages.json`,
    init: {
      method: 'POST',
      headers: {
        Authorization: 'Basic ' + Buffer.from(`${cfg.twilioAccountSid}:${cfg.twilioAuthToken}`).toString('base64'),
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params.toString(),
    },
  };
}

/** @returns {{ok: true, channel: string} | {ok: false, permanent: boolean, reason: string}} */
export async function sendTwilio(msg, cfg, fetchImpl = fetch) {
  const { url, init } = buildTwilioRequest(msg, cfg);
  let res;
  try {
    res = await fetchImpl(url, { ...init, signal: AbortSignal.timeout(30000) });
  } catch (e) {
    return { ok: false, permanent: false, reason: `мрежова грешка: ${e.message}` };
  }
  const json = await res.json().catch(() => null);
  if (res.ok && json?.sid && json.status !== 'failed') return { ok: true, channel: 'sms' };
  const code = json?.code ?? json?.error_code;
  return {
    ok: false,
    permanent: PERMANENT.has(Number(code)),
    reason: code ? `twilio_${code}: ${json?.message || json?.error_message || 'грешка'}` : `http_${res.status}`,
  };
}
