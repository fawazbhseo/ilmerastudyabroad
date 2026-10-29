#!/usr/bin/env node
// Check delayed still requests, responsive selection, reduced motion and Save-Data policy.
const fs = require('node:fs');
const path = require('node:path');
const { launchBrowser, routePinnedResources } = require('../phase31/browser.cjs');
const ROOT = path.resolve(__dirname, '../..');
const EVIDENCE = process.env.PHASE32_SMOKE_DIR || '/home/user/phase32-runtime/hero-previews';
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
const PAGES = [
  ['/study-in-germany', 'destination'],
  ['/study-abroad-counselling-mysuru', 'place'],
  ['/blog/how-to-choose-study-abroad-consultant-karnataka', 'article'],
  ['/blog/', 'blog']
];
const sha = value => require('node:crypto').createHash('sha256').update(value).digest('hex');
(async () => {
  fs.mkdirSync(EVIDENCE, { recursive: true });
  const browser = await launchBrowser();
  const context = await browser.newContext({ viewport: { width: 360, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'no-preference' });
  const cases = [];
  try {
    for (const [route, template] of PAGES) {
      for (const width of [360, 768, 1280]) {
        const page = await context.newPage();
        await page.setViewportSize({ width, height: 900 });
        await routePinnedResources(page);
        await page.addInitScript(() => {
          window.__p32Lcp = [];
          new PerformanceObserver(list => {
            for (const entry of list.getEntries()) window.__p32Lcp.push({ startTime: entry.startTime, tag: entry.element?.tagName || null, id: entry.element?.id || null, className: typeof entry.element?.className === 'string' ? entry.element.className : '' });
          }).observe({ type: 'largest-contentful-paint', buffered: true });
        });
        const requests = [];
        page.on('request', request => {
          if (request.url().includes('/assets/images/hero-still-')) requests.push({ url: new URL(request.url()).pathname, wallTime: Date.now() });
        });
        const response = await page.goto(BASE + route, { waitUntil: 'load', timeout: 60000 });
        if (!response || response.status() !== 200) throw new Error(`HTTP failure ${route}`);
        await page.waitForFunction(() => document.querySelector('.p32-hero-still')?.classList.contains('is-loaded'), null, { timeout: 8000 });
        await page.waitForFunction(() => Number(getComputedStyle(document.querySelector('.p32-hero-still')).opacity) > 0.419, null, { timeout: 2000 });
        await page.waitForTimeout(60);
        const state = await page.evaluate(() => {
          const canvas = document.querySelector('.p32-hero-still');
          const nav = performance.getEntriesByType('navigation')[0];
          const entries = performance.getEntriesByType('resource').filter(e => /hero-still-(?:640|1440)\.webp/.test(e.name));
          const lcp = window.__p32Lcp || [];
          return {
            loaded: canvas.classList.contains('is-loaded'),
            canvas: { width: canvas.width, height: canvas.height, cssWidth: canvas.getBoundingClientRect().width, cssHeight: canvas.getBoundingClientRect().height, transitionDuration: getComputedStyle(canvas).transitionDuration, opacity: getComputedStyle(canvas).opacity },
            resources: entries.map(e => ({ name: new URL(e.name).pathname, startTime: e.startTime, transferSize: e.transferSize, initiatorType: e.initiatorType })),
            loadEventEnd: nav.loadEventEnd,
            lcp,
            heroBox: (() => { const r = canvas.parentElement.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; })()
          };
        });
        const expected = width <= 768 ? '/assets/images/hero-still-640.webp' : '/assets/images/hero-still-1440.webp';
        if (state.resources.length !== 1 || state.resources[0].name !== expected || state.resources[0].startTime < state.loadEventEnd) {
          throw new Error(`Still selection or load timing failed ${route} ${width}: ${JSON.stringify(state)}`);
        }
        if (!state.lcp.length || state.lcp.some(entry => !/^H[1-6]$|^(P|SPAN)$/.test(entry.tag || ''))) {
          throw new Error(`Hero still must not become an image/canvas LCP candidate: ${JSON.stringify({ route, width, lcp: state.lcp })}`);
        }
        const screenshot = path.join(EVIDENCE, `${template}-${width}.png`);
        await page.screenshot({ path: screenshot, fullPage: false, animations: 'disabled' });
        const shot = fs.readFileSync(screenshot);
        cases.push({ route, template, width, expected, status: 'PASS', request_count: requests.length, state, screenshot: path.basename(screenshot), screenshot_sha256: sha(shot) });
        await page.close();
        console.log('PASS', route, width, expected, state.resources[0].transferSize);
      }
    }
    const savePage = await context.newPage();
    await savePage.setViewportSize({ width: 360, height: 900 });
    await savePage.addInitScript(() => Object.defineProperty(navigator, 'connection', { configurable: true, value: { saveData: true, effectiveType: '4g', downlink: 10 } }));
    await routePinnedResources(savePage);
    let saveRequests = 0;
    savePage.on('request', request => { if (request.url().includes('/assets/images/hero-still-')) saveRequests++; });
    await savePage.goto(BASE + '/study-in-germany', { waitUntil: 'load' });
    await savePage.waitForTimeout(2200);
    const saveState = await savePage.evaluate(() => ({ loaded: document.querySelector('.p32-hero-still')?.classList.contains('is-loaded') || false, background: getComputedStyle(document.querySelector('.article-hero')).backgroundImage }));
    if (saveRequests !== 0 || saveState.loaded) throw new Error(`Save-Data must skip hero still: ${JSON.stringify({ saveRequests, saveState })}`);
    cases.push({ route: '/study-in-germany', width: 360, mode: 'Save-Data', requests: saveRequests, state: saveState, status: 'PASS' });
    await savePage.close();

    const slowPage = await context.newPage();
    await slowPage.setViewportSize({ width: 360, height: 900 });
    await slowPage.addInitScript(() => Object.defineProperty(navigator, 'connection', { configurable: true, value: { saveData: false, effectiveType: '2g', downlink: 0.4 } }));
    await routePinnedResources(slowPage);
    let slowRequests = 0;
    slowPage.on('request', request => { if (request.url().includes('/assets/images/hero-still-')) slowRequests++; });
    await slowPage.goto(BASE + '/study-in-germany', { waitUntil: 'load' });
    await slowPage.waitForTimeout(2200);
    const slowState = await slowPage.evaluate(() => ({ loaded: document.querySelector('.p32-hero-still')?.classList.contains('is-loaded') || false, background: getComputedStyle(document.querySelector('.article-hero')).backgroundImage }));
    if (slowRequests !== 0 || slowState.loaded) throw new Error(`Slow connection must skip hero still: ${JSON.stringify({ slowRequests, slowState })}`);
    cases.push({ route: '/study-in-germany', width: 360, mode: 'slow-connection', requests: slowRequests, state: slowState, status: 'PASS' });
    await slowPage.close();

    const reducedPage = await context.newPage();
    await reducedPage.setViewportSize({ width: 360, height: 900 });
    await reducedPage.emulateMedia({ reducedMotion: 'reduce' });
    await routePinnedResources(reducedPage);
    await reducedPage.goto(BASE + '/study-in-germany', { waitUntil: 'load' });
    await reducedPage.waitForFunction(() => document.querySelector('.p32-hero-still')?.classList.contains('is-loaded'), null, { timeout: 8000 });
    const reduced = await reducedPage.locator('.p32-hero-still').evaluate(canvas => ({ opacity: getComputedStyle(canvas).opacity, transitionDuration: getComputedStyle(canvas).transitionDuration }));
    if (reduced.transitionDuration !== '0s') throw new Error(`Reduced-motion still must not fade: ${JSON.stringify(reduced)}`);
    cases.push({ route: '/study-in-germany', width: 360, mode: 'reduced-motion', state: reduced, status: 'PASS' });
    await reducedPage.close();
  } finally {
    await context.close().catch(() => {});
    await browser.close();
  }
  const report = { phase: 32, status: 'PASS', browser: 'Chromium 143 via @sparticuz/chromium', base: 'local PHP-WASM adapter', cases, interpretation: 'Local browser smoke evidence only. Stills are requested after window load and idle, not initial navigation. Canvas does not create a DOM image LCP candidate. Save-Data and slow-connection hints skip the template still; reduced motion removes the fade. Resource Timing transferSize is zero in this intercepted local setup, so it is not used as byte-size evidence.' };
  const output = path.join(ROOT, 'reports/phase-32-hero-smoke.json');
  fs.writeFileSync(output, JSON.stringify(report, null, 2) + '\n');
  console.log(`WROTE ${output}`);
})().catch(error => { console.error(error.stack || error); process.exit(1); });
