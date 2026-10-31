#!/usr/bin/env node
// Measure rendered hero text contrast over the loaded still by comparing hidden-text pixels.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const { launchBrowser, routePinnedResources } = require('../phase31/browser.cjs');
const ROOT = path.resolve(__dirname, '../..');
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
const PAGES = [
  ['/study-in-germany', 'destination'],
  ['/study-abroad-counselling-mysuru', 'place'],
  ['/blog/how-to-choose-study-abroad-consultant-karnataka', 'article'],
  ['/blog/', 'blog']
];
function rgb(value) {
  const m = String(value).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/i);
  return m ? m.slice(1, 4).map(Number) : [255, 255, 255];
}
function lum(c) {
  const v = c.map(x => x / 255).map(x => x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4);
  return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
}
function ratio(a, b) {
  const x = lum(a), y = lum(b);
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
}
(async () => {
  const browser = await launchBrowser();
  const context = await browser.newContext({ viewport: { width: 360, height: 900 }, deviceScaleFactor: 1 });
  const cases = [];
  try {
    for (const [route, template] of PAGES) {
      for (const width of [360, 768, 1280]) {
        const page = await context.newPage();
        await page.setViewportSize({ width, height: 900 });
        await routePinnedResources(page);
        await page.goto(BASE + route, { waitUntil: 'load', timeout: 60000 });
        await page.waitForFunction(() => document.querySelector('.p32-hero-still')?.classList.contains('is-loaded'), null, { timeout: 8000 });
        await page.waitForFunction(() => Number(getComputedStyle(document.querySelector('.p32-hero-still')).opacity) > 0.419, null, { timeout: 2000 });
        await page.evaluate(() => document.fonts.ready);
        const requestedOpacity = Number(process.env.PHASE32_HERO_OPACITY || 0.42);
        await page.evaluate(value => { document.querySelector('.p32-hero-still').style.opacity = String(value); }, requestedOpacity);
        await page.addStyleTag({ content: '*,*::before,*::after{animation:none!important;transition:none!important}' });
        const rows = await page.evaluate(() => {
          const hero = document.querySelector('.article-hero,.blog-hero');
          return [...hero.querySelectorAll('*')].filter(el => [...el.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.nodeValue.trim())).filter(el => {
            const r = el.getBoundingClientRect(), s = getComputedStyle(el);
            return r.width > 0 && r.height > 0 && s.display !== 'none' && s.visibility !== 'hidden' && s.color !== 'transparent';
          }).map((el, i) => {
            const r = el.getBoundingClientRect();
            return { i, tag: el.tagName, text: (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 100), color: getComputedStyle(el).color, box: { x: Math.max(0, r.x), y: Math.max(0, r.y), width: Math.min(r.width, innerWidth - Math.max(0, r.x)), height: Math.min(r.height, innerHeight - Math.max(0, r.y)) } };
          });
        });
        const shown = await page.screenshot({ animations: 'disabled' });
        await page.evaluate(() => {
          const hero = document.querySelector('.article-hero,.blog-hero');
          for (const el of hero.querySelectorAll('*')) if ([...el.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.nodeValue.trim())) {
            el.style.setProperty('color', 'transparent', 'important');
            el.style.setProperty('-webkit-text-fill-color', 'transparent', 'important');
            el.style.setProperty('text-shadow', 'none', 'important');
          }
        });
        const hidden = await page.screenshot({ animations: 'disabled' });
        const hiddenImage = await sharp(hidden).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
        const shownImage = await sharp(shown).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
        const pix = (image, x, y) => {
          const i = (Math.floor(y) * image.info.width + Math.floor(x)) * image.info.channels;
          return [image.data[i], image.data[i + 1], image.data[i + 2]];
        };
        const results = [];
        for (const row of rows) {
          const fg = rgb(row.color);
          const left = Math.max(0, Math.floor(row.box.x)), top = Math.max(0, Math.floor(row.box.y));
          const right = Math.min(shownImage.info.width, Math.ceil(row.box.x + row.box.width));
          const bottom = Math.min(shownImage.info.height, Math.ceil(row.box.y + row.box.height));
          let min = Infinity, pixels = 0;
          for (let y = top; y < bottom; y += 1) for (let x = left; x < right; x += 1) {
            const a = pix(shownImage, x, y), b = pix(hiddenImage, x, y);
            if (Math.max(Math.abs(a[0] - b[0]), Math.abs(a[1] - b[1]), Math.abs(a[2] - b[2])) < 18) continue;
            min = Math.min(min, ratio(fg, b)); pixels++;
          }
          results.push({ tag: row.tag, text: row.text, color: row.color, glyph_pixels: pixels, min_contrast: Number.isFinite(min) ? Number(min.toFixed(3)) : null });
        }
        const measured = results.filter(x => x.glyph_pixels > 0 && x.min_contrast !== null);
        const minimum = measured.length ? Math.min(...measured.map(x => x.min_contrast)) : null;
        if (minimum === null || minimum < 4.5) throw new Error(`Contrast gate failed ${route} ${width}: ${JSON.stringify({ minimum, results })}`);
        cases.push({ route, template, width, still_opacity: requestedOpacity, minimum_text_contrast: minimum, text_runs: measured.length, results, method: 'Pixel glyph mask from shown versus transparent-text viewport screenshot; foreground color from computed style; contrast against rendered still/gradient pixels.' });
        await page.close();
        console.log('PASS contrast', route, width, minimum);
      }
    }
  } finally {
    await context.close().catch(() => {});
    await browser.close();
  }
  const report = { phase: 32, status: 'PASS', threshold: 4.5, cases, interpretation: 'Rendered browser-pixel measurement in the hero text glyphs at 360px, 768px and 1280px. Local-only visual evidence.' };
  fs.writeFileSync(path.join(ROOT, 'reports/phase-32-hero-contrast.json'), JSON.stringify(report, null, 2) + '\n');
})().catch(error => { console.error(error.stack || error); process.exit(1); });
