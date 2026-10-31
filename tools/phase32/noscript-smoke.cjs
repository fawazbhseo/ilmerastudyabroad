#!/usr/bin/env node
// Confirm the noscript CSS paints the responsive still without application JavaScript.
const fs = require('node:fs');
const path = require('node:path');
const { launchBrowser, routePinnedResources } = require('../phase31/browser.cjs');
const ROOT = path.resolve(__dirname, '../..');
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
(async () => {
  const browser = await launchBrowser();
  const cases = [];
  try {
    for (const width of [360, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, javaScriptEnabled: false });
      const page = await context.newPage();
      await routePinnedResources(page);
      const stillRequests = [];
      const sceneRequests = [];
      page.on('request', request => {
        const url = request.url();
        if (url.includes('/assets/images/hero-still-')) stillRequests.push(new URL(url).pathname);
        if (/three\.min\.js|scene-(home|services|about|contact)\.js/.test(url)) sceneRequests.push(url);
      });
      const response = await page.goto(BASE + '/study-in-germany', { waitUntil: 'load', timeout: 60000 });
      if (!response || response.status() !== 200) throw new Error(`No-JS route failed at ${width}px`);
      const state = await page.evaluate(() => ({
        scriptsEnabled: typeof window === 'undefined' ? null : false,
        noscriptStyles: document.querySelectorAll('noscript style').length,
        backgroundImage: getComputedStyle(document.querySelector('.article-hero')).backgroundImage,
        stillCanvasReserved: !!document.querySelector('.p32-hero-still'),
        headingText: document.querySelector('h1')?.textContent.trim() || null
      }));
      const expected = width <= 768 ? '/assets/images/hero-still-640.webp' : '/assets/images/hero-still-1440.webp';
      if (stillRequests.length !== 1 || stillRequests[0] !== expected || !state.backgroundImage.includes(expected) || state.noscriptStyles !== 1 || sceneRequests.length) {
        throw new Error(`No-JS still policy failed: ${JSON.stringify({ width, stillRequests, sceneRequests, state })}`);
      }
      cases.push({ width, expected, stillRequests, sceneRequests, state, status: 'PASS' });
      await page.close();
      console.log('PASS no-JS still', width, expected);
    }
  } finally {
    await browser.close();
  }
  const report = { phase: 32, status: 'PASS', method: 'Playwright with application JavaScript disabled; local PHP-WASM adapter', cases, native_hosting: false };
  fs.writeFileSync(path.join(ROOT, 'reports/phase-32-noscript-smoke.json'), JSON.stringify(report, null, 2) + '\n');
})().catch(error => { console.error(error.stack || error); process.exit(1); });
