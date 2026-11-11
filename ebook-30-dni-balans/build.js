// usage: node render.js <book_dir> <out_pdf> [png_dir] [pages e.g. 1,5,7]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [bookDir, outPdf, pngDir, only] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(bookDir, 'index.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => {
    const pages = [...document.querySelectorAll('.page')];
    const idx = {}; pages.forEach((p, i) => { if (p.id) idx[p.id] = i + 1; });
    document.querySelectorAll('[data-ref]').forEach(el => { el.textContent = idx[el.dataset.ref] ?? '??'; });
    const mm = 96 / 25.4; const out = [];
    pages.forEach((p, i) => {
      const pr = p.getBoundingClientRect();
      const limit = pr.top + (297 - 19) * mm; // content must end above footer line
      let maxB = 0, worst = null;
      p.querySelectorAll('*').forEach(el => {
        if (el.closest('.foot') || el.closest('.cover') || el.closest('.opener') || el.closest('.back')) return;
        const r = el.getBoundingClientRect();
        if (r.height === 0) return;
        if (r.bottom > maxB) { maxB = r.bottom; worst = el; }
      });
      // horizontal overflow
      let hov = false;
      p.querySelectorAll('*').forEach(el => { const r = el.getBoundingClientRect(); if (r.right > pr.right - 10 * mm + 1 && !el.closest('.cover,.opener,.back,.foot') && el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow !== 'visible') hov = true; });
      const free = ((limit - maxB) / mm).toFixed(1);
      out.push(`${i + 1} ${p.id || ''} free=${free}mm${maxB > limit ? '  <<< OVERFLOW (' + (worst.className || worst.tagName) + ')' : ''}${hov ? ' HOV' : ''}`);
    });
    return out.join('\n');
  });
  console.log(report);
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: outPdf, preferCSSPageSize: true, printBackground: true });
  if (pngDir) {
    const sel = only ? only.split(',').map(Number) : null;
    const els = await page.$$('.page');
    await page.emulateMedia({ media: 'screen' });
    for (let i = 0; i < els.length; i++) {
      if (sel && !sel.includes(i + 1)) continue;
      await els[i].screenshot({ path: path.join(pngDir, `p${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await browser.close();
})();
