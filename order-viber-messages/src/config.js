const bool = (v, d) => (v == null || v === '' ? d : /^(1|true|yes|on|да)$/i.test(String(v).trim()));
const num = (v, d) => (v == null || v === '' ? d : Number(v));

export function loadConfig(env = process.env) {
  const cfg = {
    shopifyShop: env.SHOPIFY_SHOP || '99adx5-f2.myshopify.com',
    shopifyAccessToken: env.SHOPIFY_ACCESS_TOKEN || '',
    shopifyClientId: env.SHOPIFY_CLIENT_ID || '',
    shopifyClientSecret: env.SHOPIFY_CLIENT_SECRET || '',
    shopifyApiVersion: env.SHOPIFY_API_VERSION || '2026-04',

    // twilio = SMS only through Twilio; bulkgate = SMS (and Viber later). Picked automatically from the keys that are set.
    smsProvider: (env.SMS_PROVIDER || (env.TWILIO_ACCOUNT_SID ? 'twilio' : 'bulkgate')).trim().toLowerCase(),
    twilioAccountSid: env.TWILIO_ACCOUNT_SID || '',
    twilioAuthToken: env.TWILIO_AUTH_TOKEN || '',
    // Alphanumeric sender (max 11 characters), a Twilio number (+...), or a Messaging Service SID (MG...).
    twilioFrom: env.TWILIO_FROM || 'FitPatches',

    bulkgateAppId: env.BULKGATE_APP_ID || '',
    bulkgateToken: env.BULKGATE_TOKEN || '',
    // Registered Viber sender name. Empty = SMS only (e.g. while Viber registration is pending).
    viberSender: env.VIBER_SENDER || '',
    // Seconds Viber has to deliver before BulkGate falls back to SMS.
    viberExpiration: num(env.VIBER_EXPIRATION, 3600),
    // Viber requires approved templates for transactional messages (see `npm run templates`).
    // false = plain text (billed as promotional).
    viberTemplates: bool(env.VIBER_TEMPLATES, true),
    viberTemplateLanguage: env.VIBER_TEMPLATE_LANGUAGE || 'bg',
    smsSenderId: env.SMS_SENDER_ID || 'gSystem',
    smsSenderValue: env.SMS_SENDER_VALUE || '',

    // cyrillic: 2–3 SMS per message; latin: 1 SMS per message (cheaper).
    smsAlphabet: (env.SMS_ALPHABET || 'cyrillic').trim().toLowerCase(),
    supportPhone: env.SUPPORT_PHONE || '0887459494',

    // LIVE=false (default) only prints what would be sent: nothing is sent and nothing is written to Shopify.
    live: bool(env.LIVE, false),
    // When set, every message goes to this phone instead of the customer (state is kept separately).
    testPhone: env.TEST_PHONE || '',
    // Orders created before this moment never get the thank-you message.
    startAt: env.START_AT ? new Date(env.START_AT) : null,
    sendHours: env.SEND_HOURS || '08:00-21:00',
    lookbackDays: num(env.LOOKBACK_DAYS, 14),
    thanksDelayMinutes: num(env.THANKS_DELAY_MINUTES, 5),
    reminderDays: (env.REMINDER_DAYS || '2,4').split(',').map((s) => Number(s.trim())).filter((n) => n > 0),
    maxSendsPerRun: num(env.MAX_SENDS_PER_RUN, 40),
    // Prints full message texts. Keep off in GitHub Actions: logs of a public repo are public.
    printTexts: bool(env.PRINT_TEXTS, false),
  };
  return cfg;
}

export function validateConfig(cfg) {
  const errors = [];
  if (!cfg.shopifyAccessToken && !(cfg.shopifyClientId && cfg.shopifyClientSecret)) {
    errors.push('Липсва достъп до Shopify: задайте SHOPIFY_CLIENT_ID и SHOPIFY_CLIENT_SECRET (или SHOPIFY_ACCESS_TOKEN).');
  }
  if (cfg.startAt && Number.isNaN(cfg.startAt.getTime())) errors.push('START_AT не е валидна дата (пример: 2026-10-27T08:00:00+02:00).');
  if (cfg.live) {
    if (cfg.smsProvider === 'twilio') {
      if (!cfg.twilioAccountSid || !cfg.twilioAuthToken) errors.push('LIVE=true, но липсват TWILIO_ACCOUNT_SID и TWILIO_AUTH_TOKEN.');
    } else if (!cfg.bulkgateAppId || !cfg.bulkgateToken) {
      errors.push('LIVE=true, но липсват BULKGATE_APP_ID и BULKGATE_TOKEN.');
    }
    if (!cfg.startAt) errors.push('LIVE=true изисква START_AT, за да не се пишат благодарности за стари поръчки.');
  }
  if (!['twilio', 'bulkgate'].includes(cfg.smsProvider)) errors.push('SMS_PROVIDER трябва да е twilio или bulkgate.');
  if (!['cyrillic', 'latin'].includes(cfg.smsAlphabet)) errors.push('SMS_ALPHABET трябва да е cyrillic или latin.');
  if (cfg.smsProvider === 'twilio' && cfg.viberSender) errors.push('Twilio не праща Viber: махнете VIBER_SENDER или ползвайте BulkGate.');
  if (!/^\d{2}:\d{2}-\d{2}:\d{2}$/.test(cfg.sendHours)) errors.push('SEND_HOURS трябва да е във формат 08:00-21:00.');
  return errors;
}
