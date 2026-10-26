import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildTwilioRequest, sendTwilio } from '../src/twilio.js';
import { loadConfig, validateConfig } from '../src/config.js';

const cfg = { twilioAccountSid: 'AC123', twilioAuthToken: 'secret', twilioFrom: 'FitPatches' };
const msg = { phone: '359888000111', viberText: 'V', smsText: 'FitPatches: test', tag: '#1 thanks' };
const reply = (status, json) => async () => ({ ok: status < 400, status, json: async () => json });

test('Twilio request: E.164 number, sender, Basic auth', () => {
  const { url, init } = buildTwilioRequest(msg, cfg);
  assert.equal(url, 'https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json');
  assert.equal(init.headers.Authorization, 'Basic ' + Buffer.from('AC123:secret').toString('base64'));
  const body = new URLSearchParams(init.body);
  assert.equal(body.get('To'), '+359888000111');
  assert.equal(body.get('From'), 'FitPatches');
  assert.equal(body.get('Body'), 'FitPatches: test');

  const viaService = new URLSearchParams(buildTwilioRequest(msg, { ...cfg, twilioFrom: 'MG0123456789abcdef0123456789abcdef' }).init.body);
  assert.equal(viaService.get('MessagingServiceSid'), 'MG0123456789abcdef0123456789abcdef');
  assert.equal(new URLSearchParams(buildTwilioRequest(msg, { ...cfg, twilioFrom: 'MGshop' }).init.body).get('From'), 'MGshop');
  assert.equal(viaService.get('From'), null);
});

test('Twilio responses: accepted, bad number, account problem, network error', async () => {
  assert.deepEqual(await sendTwilio(msg, cfg, reply(201, { sid: 'SM1', status: 'queued' })), { ok: true, channel: 'sms' });

  const bad = await sendTwilio(msg, cfg, reply(400, { code: 21211, message: "Invalid 'To' Phone Number" }));
  assert.equal(bad.ok, false);
  assert.equal(bad.permanent, true);
  assert.match(bad.reason, /^twilio_21211/);

  const geo = await sendTwilio(msg, cfg, reply(400, { code: 21408, message: 'Permission to send an SMS has not been enabled' }));
  assert.equal(geo.permanent, false);

  const down = await sendTwilio(msg, cfg, async () => {
    throw new Error('ECONNRESET');
  });
  assert.deepEqual(down, { ok: false, permanent: false, reason: 'мрежова грешка: ECONNRESET' });
});

test('provider is picked from the keys that are set', () => {
  const shop = { SHOPIFY_CLIENT_ID: 'x', SHOPIFY_CLIENT_SECRET: 'y' };
  assert.equal(loadConfig({ ...shop, TWILIO_ACCOUNT_SID: 'AC1' }).smsProvider, 'twilio');
  assert.equal(loadConfig({ ...shop, BULKGATE_APP_ID: '1' }).smsProvider, 'bulkgate');
  assert.equal(loadConfig({ ...shop, TWILIO_ACCOUNT_SID: 'AC1', SMS_PROVIDER: 'BulkGate' }).smsProvider, 'bulkgate');

  const live = { ...shop, LIVE: 'true', START_AT: '2026-10-27T08:00:00+02:00' };
  assert.deepEqual(validateConfig(loadConfig({ ...live, TWILIO_ACCOUNT_SID: 'AC1', TWILIO_AUTH_TOKEN: 't' })), []);
  assert.match(validateConfig(loadConfig({ ...live, TWILIO_ACCOUNT_SID: 'AC1' })).join(), /TWILIO_AUTH_TOKEN/);
  assert.match(validateConfig(loadConfig({ ...live, TWILIO_ACCOUNT_SID: 'AC1', TWILIO_AUTH_TOKEN: 't', VIBER_SENDER: 'FitPatches' })).join(), /Viber/);
});
