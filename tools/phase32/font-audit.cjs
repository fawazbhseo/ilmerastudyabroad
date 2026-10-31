#!/usr/bin/env node
// Diagnose local font-face, preload, request and paint chains for Phase32 target templates.
const fs = require('node:fs');
const path = require('node:path');
const { launchBrowser, routePinnedResources } = require('../phase31/browser.cjs');
const ROOT = path.resolve(__dirname, '../..');
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
const PAGES = [
  ['/study-abroad-counselling-mysuru', 'place'],
  ['/blog/how-to-choose-study-abroad-consultant-karnataka', 'article'],
  ['/blog/', 'blog']
];
(async () => {
  const browser = await launchBrowser();
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  const cases = [];
  try {
    for (const [route, template] of PAGES) for (const width of [360, 1280]) {
      const page = await context.newPage();
      await page.setViewportSize({ width, height: 900 });
      await routePinnedResources(page);
      await page.addInitScript(() => {
        window.__p32lcp = [];
        window.__p32cls = [];
        window.__p32long = [];
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32lcp.push({ startTime: e.startTime, tag: e.element?.tagName || null, id: e.element?.id || null, className: typeof e.element?.className === 'string' ? e.element.className : null }))).observe({ type: 'largest-contentful-paint', buffered: true }); } catch (_) {}
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32cls.push({ value: e.value, startTime: e.startTime, hadRecentInput: e.hadRecentInput }))).observe({ type: 'layout-shift', buffered: true }); } catch (_) {}
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32long.push({ startTime: e.startTime, duration: e.duration }))).observe({ type: 'longtask', buffered: true }); } catch (_) {}
      });
      const responses = [];
      page.on('requestfinished', async request => {
        try {
          const response = await request.response();
          if (!response) return;
          const url = request.url();
          if (/\.(?:woff2?|css)(?:\?|$)/i.test(url) || url.includes('fonts.googleapis')) {
            const body = await response.body().catch(() => Buffer.alloc(0));
            responses.push({ url: new URL(url).pathname, type: request.resourceType(), status: response.status(), bytes: body.length, timing: request.timing() });
          }
        } catch (_) {}
      });
      const navigation = await page.goto(BASE + route, { waitUntil: 'load', timeout: 60000 });
      if (!navigation || navigation.status() !== 200) throw new Error(`HTTP failure ${route} ${width}`);
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(250);
      const state = await page.evaluate(() => {
        const nav = performance.getEntriesByType('navigation')[0];
        const fonts = [...document.fonts].map(face => ({ family: face.family.replaceAll('"', ''), weight: face.weight, style: face.style, display: face.display || null, status: face.status }));
        const css = [...document.styleSheets].map(sheet => ({ href: sheet.href || null, disabled: sheet.disabled, owner: sheet.ownerNode?.tagName || null, media: sheet.media?.mediaText || null }));
        const fontRules = [];
        for (const sheet of document.styleSheets) {
          let rules;
          try { rules = [...sheet.cssRules]; } catch (_) { continue; }
          for (const rule of rules) if (rule.type === CSSRule.FONT_FACE_RULE) fontRules.push({ family: rule.style.getPropertyValue('font-family').replaceAll('"', '').replaceAll("'", ''), weight: rule.style.getPropertyValue('font-weight'), style: rule.style.getPropertyValue('font-style'), display: rule.style.getPropertyValue('font-display'), src: rule.style.getPropertyValue('src') });
        }
        const entries = performance.getEntriesByType('resource').map(entry => ({ name: new URL(entry.name).pathname, type: entry.initiatorType, startTime: Number(entry.startTime.toFixed(2)), duration: Number(entry.duration.toFixed(2)), transferSize: entry.transferSize, decodedBodySize: entry.decodedBodySize })).filter(entry => /\.(?:woff2?|css)(?:\?|$)/i.test(entry.name) || /fonts\.googleapis/.test(entry.name));
        const preload = [...document.querySelectorAll('link[rel="preload"][as="font"]')].map(link => ({ href: new URL(link.href).pathname, type: link.type, crossorigin: link.crossOrigin || null }));
        return { readyState: document.readyState, loadEventEnd: nav.loadEventEnd, domContentLoadedEventEnd: nav.domContentLoadedEventEnd, fontPending: document.documentElement.classList.contains('p25-font-pending'), preload, css, fontRules, loadedFonts: fonts, resourceEntries: entries, lcp: window.__p32lcp, clsEvents: window.__p32cls, longTasks: window.__p32long };
      });
      const fontResponses = responses.filter(r => r.type === 'font' || /\.woff2?/.test(r.url));
      const cssResponses = responses.filter(r => r.type === 'stylesheet' || /\.css/.test(r.url));
      cases.push({ route, template, width, http_status: navigation.status(), font_response_count: fontResponses.length, font_response_bytes: fontResponses.reduce((sum, r) => sum + r.bytes, 0), font_responses: fontResponses, stylesheet_responses: cssResponses, state, status: 'PASS' });
      await page.close();
      console.log('PASS font audit', route, width, 'font bytes', fontResponses.reduce((sum, r) => sum + r.bytes, 0), 'faces', state.fontRules.length, 'preloads', state.preload.length);
    }
  } finally {
    await context.close().catch(() => {});
    await browser.close();
  }
  const report = { phase: 32, status: 'PASS', method: 'Local PHP-WASM routes and Playwright Chromium 143. Fonts are measured as local response body bytes, not ResourceTiming transferSize.', source_observation: 'Target templates use the inline visual-system stylesheet, self-hosted WOFF2 faces and two head preloads. Inspect the per-route rules and actual requests below; no font A/B was run by this diagnostic.', cases };
  fs.writeFileSync(path.join(ROOT, 'reports/phase-32-font-audit.json'), JSON.stringify(report, null, 2) + '\n');
})().catch(error => { console.error(error.stack || error); process.exit(1); });
