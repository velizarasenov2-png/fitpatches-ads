/**
 * FitPatches — бързи поръчки (име + телефон) → Google таблица.
 *
 * Как се пуска (еднократно, ~3 минути, от компютър):
 *  1. Отвори таблицата „FitPatches — Бързи поръчки“ в Google Drive.
 *  2. Меню Разширения → Apps Script. Изтрий примерния код и постави целия този файл. Запази (Ctrl+S).
 *  3. Горе вдясно: Внедряване → Ново внедряване → иконка зъбно колело → „Уеб приложение“.
 *       Изпълнява се като: Аз
 *       Кой има достъп: Всеки
 *     Натисни „Внедряване“ и разреши достъпа с профила си.
 *  4. Копирай „URL адреса на уеб приложението“ (завършва на /exec) и го изпрати —
 *     той се слага в темата (snippets/fp-offer-v2.liquid → endpoint).
 *
 * Всяка заявка от сайта става нов ред със статус „Нова“. Колоната „Статус“ е падащо меню.
 * Ако същият телефон е изпратил заявка през последните 24 часа, редът се маркира като „Дубликат“.
 */
var SHEET_NAME = 'Поръчки';
var HEADERS = ['Дата и час', 'Номер на заявка', 'Име', 'Телефон', 'Пакет', 'Брой пакети', 'Сума (€)',
  'Статус', 'Бележка', 'Дубликат', 'Страница', 'Реферер',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'Устройство'];
var STATUSES = ['Нова', 'Потвърдена', 'Изпратена', 'Доставена', 'Отказана', 'Без отговор', 'Дубликат'];
var PHONE_COL = 4;

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var p = (e && e.parameter) || {};
    var sheet = getSheet_();
    var phone = clean_(p.phone);
    var digits = phone.replace(/\D/g, '');
    var duplicate = digits && isDuplicate_(sheet, digits) ? 'Да' : '';
    sheet.appendRow([
      new Date(), clean_(p.lead_id), clean_(p.name), "'" + phone, clean_(p.package),
      Number(p.packs) || '', Number(p.total) || '', 'Нова', '', duplicate,
      clean_(p.page), clean_(p.referrer), clean_(p.utm_source), clean_(p.utm_medium),
      clean_(p.utm_campaign), clean_(p.utm_content), clean_(p.utm_term), clean_(p.fbclid), clean_(p.user_agent)
    ]);
    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput('FitPatches: формата за бързи поръчки работи.');
}

// Пусни веднъж от редактора (бутон „Изпълни“ с избрана функция setup), за да оформи таблицата и обобщението.
function setup() {
  getSheet_();
}

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
  if (sheet.getName() !== SHEET_NAME) sheet.setName(SHEET_NAME);
  if (sheet.getLastRow() === 0) sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
  var props = PropertiesService.getScriptProperties();
  if (props.getProperty('formatted') !== '1') {
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#fbe9f1');
    sheet.setFrozenRows(1);
    sheet.getRange('A:A').setNumberFormat('dd.mm.yyyy hh:mm');
    sheet.getRange('D:D').setNumberFormat('@');
    var rule = SpreadsheetApp.newDataValidation().requireValueInList(STATUSES, true).setAllowInvalid(true).build();
    sheet.getRange(2, 8, sheet.getMaxRows() - 1, 1).setDataValidation(rule);
    ensureSummary_(ss);
    props.setProperty('formatted', '1');
  }
  return sheet;
}

// Таб „Обобщение“ — броячи с формули, които се обновяват сами с всяка нова заявка.
function ensureSummary_(ss) {
  var sum = ss.getSheetByName('Обобщение') || ss.insertSheet('Обобщение');
  var src = "'" + SHEET_NAME + "'!";
  var rows = [
    ['Показател', 'Стойност'],
    ['Общо заявки', '=COUNTA(' + src + 'B2:B)'],
    ['Заявки днес', '=COUNTIFS(' + src + 'A2:A,">="&TODAY())'],
    ['Заявки последните 7 дни', '=COUNTIFS(' + src + 'A2:A,">="&TODAY()-6)']
  ];
  STATUSES.forEach(function (s) {
    rows.push(['Статус: ' + s, '=COUNTIF(' + src + 'H2:H,"' + s + '")']);
  });
  rows.push(['Маркирани като дубликат', '=COUNTIF(' + src + 'J2:J,"Да")']);
  rows.push(['Сума на доставените (€)', '=SUMIF(' + src + 'H2:H,"Доставена",' + src + 'G2:G)']);
  rows.push(['Средна сума на заявка (€)', '=IFERROR(AVERAGE(' + src + 'G2:G),0)']);
  sum.getRange(1, 1, rows.length, 2).setValues(rows);
  sum.getRange(1, 1, 1, 2).setFontWeight('bold').setBackground('#fbe9f1');
  sum.setColumnWidth(1, 240);
}

function isDuplicate_(sheet, digits) {
  var last = sheet.getLastRow();
  if (last < 2) return false;
  var from = Math.max(2, last - 300);
  var rows = sheet.getRange(from, 1, last - from + 1, PHONE_COL).getValues();
  var dayAgo = Date.now() - 24 * 60 * 60 * 1000;
  return rows.some(function (r) {
    var when = r[0] instanceof Date ? r[0].getTime() : 0;
    return when > dayAgo && String(r[PHONE_COL - 1]).replace(/\D/g, '') === digits;
  });
}

// Пази таблицата от формули, подадени през формата (=, +, -, @ в началото).
function clean_(v) {
  return String(v == null ? '' : v).replace(/^[=+\-@\s]+/, '').slice(0, 300);
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
