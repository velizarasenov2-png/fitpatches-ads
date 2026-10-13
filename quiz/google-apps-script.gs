/**
 * FitPatches Quiz → Google Sheet „FitPatches Quiz – отговори“
 * ----------------------------------------------------------------------------
 * Приема отговорите от quiz-а и ги записва в лист „Responses“ (по един ред на
 * човек). Claude чете листа през Google Drive връзката и прави анализа на ICP.
 * Не е нужно да отваряш таблицата.
 *
 * Инсталация (3 мин) — виж quiz/README.md, стъпка 2:
 *   1. В таблицата: Extensions → Apps Script → постави този код → Save.
 *   2. Deploy → New deployment → Web app → Execute as: Me, Who has access: Anyone → Deploy.
 *   3. Прати Web app URL-а на Claude (или го постави в CONFIG.SHEET_URL в quiz/index.html).
 */

var SHEET_RESPONSES = 'Responses';
var SHEET_SUMMARY = 'ICP Summary';

// Редът на въпросите — трябва да съвпада с STEPS в quiz/index.html.
var QUESTIONS = [
  ['gender', 'Пол'], ['age', 'Възраст'], ['goal', 'Цел'], ['kg', 'Колко кг'],
  ['history', 'Как се появиха килограмите'], ['triggers', 'Кога яде без глад'], ['sweets', 'Желание за сладко'],
  ['tried', 'Пробвали досега'], ['outcome', 'Как завърши опитът'], ['health', 'Здраве'],
  ['pain', 'Кое тормози най-много'], ['o_struggle', 'С нейни думи: най-трудното'], ['impact', 'Как влияе на живота'],
  ['o_body', 'С нейни думи: как се чувства в тялото си'], ['want', 'Какво решение търси'], ['o_future', 'С нейни думи: какво ще е различно след 3 месеца'],
  ['p_hunger', 'Гладна час-два след хранене'], ['p_sleep', 'Спи под 7 часа'], ['p_event', 'Има повод']
];

var META_COLS = [
  'qid', 'first_seen', 'last_seen', 'status', 'max_step', 'steps_total', 'last_step_id', 'seconds',
  'angle', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid',
  'device', 'referrer', 'profile'
];
var TAIL_COLS = ['cta_clicked', 'order', 'order_pack', 'order_total', 'version'];
var COLUMNS = META_COLS.concat(QUESTIONS.map(function (q) { return q[0]; })).concat(TAIL_COLS);

var STATUS_RANK = { view: 0, started: 1, completed: 2, clicked: 3, ordered: 4 };

function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_RESPONSES) || ss.insertSheet(SHEET_RESPONSES);
  sh.getRange(1, 1, 1, COLUMNS.length).setValues([COLUMNS]).setFontWeight('bold').setBackground('#fbe9f1');
  sh.setFrozenRows(1);
  var def = ss.getSheetByName('Sheet1') || ss.getSheetByName('Лист1');
  if (def && def.getLastRow() === 0 && ss.getSheets().length > 1) ss.deleteSheet(def);
}

function onOpen() {
  SpreadsheetApp.getUi().createMenu('FitPatches Quiz')
    .addItem('Обнови ICP отчета', 'buildSummary')
    .addItem('Автоматично обновяване всеки ден', 'installDailyTrigger')
    .addToUi();
}

function doGet() {
  return json_({ ok: true, service: 'fitpatches-quiz' });
}

function doPost(e) {
  var d;
  try { d = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false, error: 'bad json' }); }
  if (!d || !/^[a-z0-9]{8,40}$/i.test(String(d.qid || ''))) return json_({ ok: false, error: 'bad qid' });

  var lock = LockService.getScriptLock();
  if (!lock.tryLock(15000)) return json_({ ok: false, error: 'busy' });
  try {
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_RESPONSES);
    if (!sh) { setup(); sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_RESPONSES); }
    var header = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
    var col = {}; header.forEach(function (h, i) { col[h] = i; });

    var found = sh.getRange(2, 1, Math.max(1, sh.getLastRow() - 1), 1)
      .createTextFinder(d.qid).matchEntireCell(true).findNext();
    // Поръчка от Shopify Flow (по желание, виж README): само със секретния ключ и само за съществуващ ред.
    if (d.event === 'order') {
      var secret = PropertiesService.getScriptProperties().getProperty('ORDER_SECRET');
      if (!secret || d.secret !== secret) return json_({ ok: false, error: 'forbidden' });
      if (!found) return json_({ ok: false, error: 'unknown qid' });
    }
    var rowIdx = found ? found.getRow() : sh.getLastRow() + 1;
    var row = found ? sh.getRange(rowIdx, 1, 1, header.length).getValues()[0] : header.map(function () { return ''; });
    var now = new Date();

    function set(k, v) { if (col[k] !== undefined && v !== undefined && v !== null && v !== '') row[col[k]] = clean_(v); }

    set('qid', d.qid);
    if (!found) set('first_seen', now);
    set('last_seen', now);
    if (d.event !== 'order') ['steps_total', 'seconds', 'angle', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term',
     'fbclid', 'device', 'referrer', 'profile', 'version'].forEach(function (k) { set(k, d[k]); });
    if (d.step_id && d.event !== 'order') set('last_step_id', d.step_id);
    if (Number(d.max_step) > Number(row[col.max_step] || 0)) set('max_step', Number(d.max_step));

    var answers = d.answers || {};
    QUESTIONS.forEach(function (q) { set(q[0], answers[q[0]]); });

    if (d.event === 'order') { set('order', d.order); set('order_pack', d.order_pack); set('order_total', d.order_total); }

    var newStatus = d.event === 'order' ? 'ordered' : d.event === 'cta' ? 'clicked' : d.event === 'complete' ? 'completed'
      : Number(d.max_step) > 0 ? 'started' : 'view';
    var curStatus = row[col.status] || 'view';
    if ((STATUS_RANK[newStatus] || 0) >= (STATUS_RANK[curStatus] || 0)) set('status', newStatus);
    if (d.event === 'cta') set('cta_clicked', 'yes');

    sh.getRange(rowIdx, 1, 1, header.length).setValues([row.map(clean_)]);
    return json_({ ok: true });
  } finally {
    lock.releaseLock();
  }
}

/* ---------------------------------------------------------------------------
 * ICP отчет: за всеки въпрос — колко души избират всеки отговор и какъв %
 * от тях кликват към магазина / купуват. Тук се вижда кой е реалният ICP.
 * ------------------------------------------------------------------------- */
function buildSummary() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var src = ss.getSheetByName(SHEET_RESPONSES);
  var out = ss.getSheetByName(SHEET_SUMMARY) || ss.insertSheet(SHEET_SUMMARY);
  out.clear();
  var data = src.getDataRange().getValues();
  var header = data.shift();
  var c = {}; header.forEach(function (h, i) { c[h] = i; });
  var rows = data.filter(function (r) { return r[c.qid]; });

  var isDone = function (r) { return (STATUS_RANK[r[c.status]] || 0) >= 2; };
  var isClick = function (r) { return r[c.cta_clicked] === 'yes'; };
  var isOrder = function (r) { return String(r[c.order] || '') !== ''; };
  var pct = function (a, b) { return b ? a / b : ''; };

  var blocks = [];
  // 1) Фуния
  var views = rows.length, started = rows.filter(function (r) { return Number(r[c.max_step]) > 0; }).length;
  var done = rows.filter(isDone).length, clicks = rows.filter(isClick).length, orders = rows.filter(isOrder).length;
  var funnel = [['ФУНИЯ', 'Брой', '% от отворили'],
    ['Отворили quiz-а', views, 1], ['Започнали (1-ви отговор)', started, pct(started, views)]];
  var total = Number((rows[0] || [])[c.steps_total]) || QUESTIONS.length;
  for (var s = 2; s <= total; s++) {
    var n = rows.filter(function (r) { return Number(r[c.max_step]) >= s; }).length;
    funnel.push(['Отговорили на въпрос ' + s + ' (' + (QUESTIONS[s - 1] ? QUESTIONS[s - 1][1] : '') + ')', n, pct(n, views)]);
  }
  funnel.push(['Видели резултата', done, pct(done, views)], ['Кликнали към магазина', clicks, pct(clicks, views)], ['Поръчали', orders, pct(orders, views)]);
  blocks.push(funnel);

  // 2) По въпрос / отговор
  QUESTIONS.forEach(function (q) {
    if (/^o_/.test(q[0])) return; // свободен текст — Claude го анализира отделно
    var stats = {};
    rows.filter(isDone).forEach(function (r) {
      String(r[c[q[0]]] || '—').split(' | ').forEach(function (v) {
        v = v || '—';
        stats[v] = stats[v] || { n: 0, cl: 0, or: 0 };
        stats[v].n++; if (isClick(r)) stats[v].cl++; if (isOrder(r)) stats[v].or++;
      });
    });
    var b = [[q[1].toUpperCase(), 'Брой', '% от завършили', 'Кликнали', '% клик', 'Поръчали', '% поръчка']];
    Object.keys(stats).sort(function (a, z) { return stats[z].n - stats[a].n; }).forEach(function (v) {
      var x = stats[v]; b.push([v, x.n, pct(x.n, done), x.cl, pct(x.cl, x.n), x.or, pct(x.or, x.n)]);
    });
    blocks.push(b);
  });

  // 3) По рекламен ъгъл и по реклама (utm_content)
  ['angle', 'utm_campaign', 'utm_content'].forEach(function (k) {
    var g = {};
    rows.forEach(function (r) {
      var v = r[c[k]] || '—'; g[v] = g[v] || { v: 0, s: 0, d: 0, cl: 0, or: 0 };
      g[v].v++; if (Number(r[c.max_step]) > 0) g[v].s++; if (isDone(r)) g[v].d++; if (isClick(r)) g[v].cl++; if (isOrder(r)) g[v].or++;
    });
    var b = [['ПО ' + k.toUpperCase(), 'Отворили', '% започнали', '% завършили', '% кликнали', 'Поръчали']];
    Object.keys(g).sort(function (a, z) { return g[z].v - g[a].v; }).forEach(function (v) {
      var x = g[v]; b.push([v, x.v, pct(x.s, x.v), pct(x.d, x.v), pct(x.cl, x.v), x.or]);
    });
    blocks.push(b);
  });

  var r0 = 1;
  out.getRange(r0, 1).setValue('ICP отчет — обновен ' + Utilities.formatDate(new Date(), 'Europe/Sofia', 'dd.MM.yyyy HH:mm')).setFontWeight('bold').setFontSize(13);
  r0 += 2;
  blocks.forEach(function (b) {
    var w = b[0].length;
    b = b.map(function (row) { while (row.length < w) row.push(''); return row; });
    out.getRange(r0, 1, b.length, w).setValues(b.map(function (row) { return row.map(clean_); }));
    out.getRange(r0, 1, 1, w).setFontWeight('bold').setBackground('#fbe9f1');
    for (var j = 0; j < w; j++) {
      if (String(b[0][j]).indexOf('%') === 0) out.getRange(r0 + 1, j + 1, Math.max(1, b.length - 1), 1).setNumberFormat('0.0%');
    }
    r0 += b.length + 2;
  });
  out.autoResizeColumns(1, 7);
}

function installDailyTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'buildSummary') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('buildSummary').timeBased().everyDays(1).atHour(7).create();
}

function clean_(v) {
  if (v instanceof Date || typeof v === 'number' || v === '') return v;
  v = String(v).slice(0, 300);
  // Апостроф = записва се като текст: пази от формули (=, +, -, @) и от това
  // Sheets да превърне отговори като „5-10“ в дата.
  return /^[=+\-@0-9]/.test(v) ? "'" + v : v;
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
