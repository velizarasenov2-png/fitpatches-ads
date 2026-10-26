// BulkGate Advanced transactional API v2: Viber first, SMS if Viber can't deliver.
const HOSTS = ['https://portal.bulkgate.com', 'https://backup1.bulkgate.com'];
const PATH = '/api/2.0/advanced/transactional';
const OK = new Set(['accepted', 'sent', 'scheduled']);
// Problems with the number itself: retrying won't help.
const PERMANENT = new Set(['invalid_number', 'blacklisted', 'invalid_phone_number']);

export function buildRequest({ phone, viberText, smsText, tag, template }, cfg) {
  const channel = {};
  if (cfg.viberSender && cfg.viberTemplates && template) {
    channel.viber = {
      sender: cfg.viberSender,
      expiration: cfg.viberExpiration,
      template_id: '@' + template.key,
      template_language: cfg.viberTemplateLanguage,
      template_parameters: template.params,
    };
  } else if (cfg.viberSender) {
    channel.viber = { sender: cfg.viberSender, expiration: cfg.viberExpiration, text: viberText };
  }
  channel.sms = {
    sender_id: cfg.smsSenderId,
    ...(cfg.smsSenderValue ? { sender_id_value: cfg.smsSenderValue } : {}),
    unicode: false,
    text: smsText,
  };
  return {
    application_id: cfg.bulkgateAppId,
    application_token: cfg.bulkgateToken,
    number: [phone],
    text: smsText,
    country: 'bg',
    duplicates_check: 'on',
    tag,
    channel,
  };
}

/** @returns {{ok: true, channel: string} | {ok: false, permanent: boolean, reason: string}} */
export async function sendMessage(msg, cfg, fetchImpl = fetch) {
  const body = JSON.stringify(buildRequest(msg, cfg));
  let lastError = null;
  for (const host of HOSTS) {
    let res;
    try {
      res = await fetchImpl(host + PATH, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body,
        signal: AbortSignal.timeout(30000),
      });
    } catch (e) {
      lastError = `мрежова грешка: ${e.message}`;
      continue; // request never arrived: try the backup host
    }
    const json = await res.json().catch(() => null);
    if (!res.ok || !json?.data) {
      const type = json?.type || `http_${res.status}`;
      return { ok: false, permanent: PERMANENT.has(type), reason: `${type}: ${json?.error || 'грешка'}` };
    }
    const r = json.data.response?.[0];
    if (r && OK.has(r.status)) return { ok: true, channel: r.channel || '' };
    const status = r?.status || 'unknown';
    return { ok: false, permanent: PERMANENT.has(status), reason: status };
  }
  return { ok: false, permanent: false, reason: lastError || 'няма връзка с BulkGate' };
}
