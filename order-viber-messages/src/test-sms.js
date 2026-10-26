// Sends one sample thank-you SMS to check the provider setup: node --env-file=.env src/test-sms.js 0888123456
import { pathToFileURL } from 'node:url';
import { loadConfig } from './config.js';
import { normalizePhone } from './order.js';
import { render, smsSegments } from './messages.js';
import { sendMessage } from './bulkgate.js';
import { sendTwilio } from './twilio.js';

const SAMPLE = {
  firstName: '',
  courier: 'speedy',
  isOffice: true,
  office: { text: 'София, бул. Витоша 1', city: 'София' },
  amount: 25.38,
  currency: 'EUR',
  fulfillment: null,
};

export async function sendTestSms(rawPhone, cfg, send = cfg.smsProvider === 'twilio' ? sendTwilio : sendMessage) {
  const phone = normalizePhone(rawPhone);
  if (!phone) throw new Error('Невалиден български телефон. Пример: 0888123456');
  const { sms } = render('thanks', SAMPLE, cfg);
  const result = await send({ phone, smsText: sms, viberText: sms, tag: 'test' }, { ...cfg, viberSender: '' });
  return { sms, result };
}

if (import.meta.url === pathToFileURL(process.argv[1] || '').href) {
  const cfg = loadConfig();
  const missing = cfg.smsProvider === 'twilio' ? !cfg.twilioAccountSid || !cfg.twilioAuthToken : !cfg.bulkgateAppId || !cfg.bulkgateToken;
  if (missing) {
    console.error('Липсват ключовете: TWILIO_ACCOUNT_SID и TWILIO_AUTH_TOKEN (или BULKGATE_APP_ID и BULKGATE_TOKEN).');
    process.exit(1);
  }
  sendTestSms(process.argv[2], cfg)
    .then(({ sms, result }) => {
      console.log(`Доставчик: ${cfg.smsProvider}\nТекст (${sms.length} знака, ${smsSegments(sms)} SMS): ${sms}`);
      console.log(result.ok ? 'Приет за изпращане.' : `НЕ е изпратен: ${result.reason}`);
      process.exit(result.ok ? 0 : 1);
    })
    .catch((e) => {
      console.error(e.message);
      process.exit(1);
    });
}
