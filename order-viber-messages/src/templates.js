// Prints the Viber templates to register in BulkGate: SMS & Viber messaging → Viber templates → New template.
import { loadConfig } from './config.js';
import { viberTemplates, TEMPLATE_KEYS } from './messages.js';

const EXAMPLES = {
  name: 'Мария',
  courier: 'Еконт',
  office: 'Айдемир кв. Деленките ул. София №7',
  place: 'офиса на Еконт – Айдемир кв. Деленките ул. София №7',
  tracking: '1055281553065',
  amount: '25.38 €',
  delivery: 'офис на Еконт – Айдемир кв. Деленките ул. София №7',
};

const cfg = loadConfig();
for (const [type, text] of Object.entries(viberTemplates(cfg))) {
  const vars = [...new Set([...text.matchAll(/\{\{(\w+)\}\}/g)].map((m) => m[1]))];
  console.log(`=== Ключ (key): ${TEMPLATE_KEYS[type]}   Език: ${cfg.viberTemplateLanguage}   Тип: transactional ===`);
  console.log(text);
  console.log('--- Примерни стойности ---');
  for (const v of vars) console.log(`${v}: ${EXAMPLES[v]}`);
  console.log('');
}
