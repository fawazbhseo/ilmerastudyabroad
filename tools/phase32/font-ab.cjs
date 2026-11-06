#!/usr/bin/env node
// Isolated local font-display/gate A/B for place, article and blog templates. No retries.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const packed = require('@sparticuz/chromium');
const { resources } = require('../phase25/resources.cjs');
const ROOT = path.resolve(__dirname, '../..');
const RUNTIME = process.env.PHASE31_RUNTIME || '/home/user/phase32-runtime/node_modules';
const { inflate } = require(path.join(RUNTIME, '@sparticuz/chromium/build/cjs/lambdafs.cjs'));
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
const PORT = Number(process.env.PHASE32_FONT_AB_PORT || 9222);
const OUTPUT = path.join(ROOT, 'reports/phase-32-font-ab-results.json');
const ROUTES = ['/study-abroad-counselling-mysuru', '/blog/how-to-choose-study-abroad-consultant-karnataka', '/blog/'];
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const quantile = (values, q) => { const sorted = [...values].sort((a, b) => a - b), p = (sorted.length - 1) * q, i = Math.floor(p); return sorted[i] + (sorted[Math.ceil(p)] - sorted[i]) * (p - i); };
const summarize = samples => Object.fromEntries(['lcp_ms', 'cls', 'tbt_ms', 'transfer_bytes', 'requests'].map(key => {
  const values = samples.map(sample => sample[key]);
  const median = quantile(values, .5), q1 = quantile(values, .25), q3 = quantile(values, .75);
  return [key, { median, q1, q3, iqr: q3 - q1 }];
}));
function chromeArgs() { return [...packed.args.filter(arg => !['--single-process', '--in-process-gpu'].includes(arg)), `--remote-debugging-port=${PORT}`]; }
async function chromiumRuntime() {
  const extracted = await inflate(path.join(RUNTIME, '@sparticuz/chromium/bin/al2023.tar.br'));
  process.env.LD_LIBRARY_PATH = path.join(extracted, 'lib') + ':' + (process.env.LD_LIBRARY_PATH || '');
}
function makeFontVariant(html) {
  const displayCount = (html.match(/font-display:block/g) || []).length;
  const gateCount = (html.match(/\.p25-font-pending body\.p25\{visibility:hidden;\}/g) || []).length;
  if (displayCount !== 7 || gateCount !== 1) throw new Error(`Unexpected font candidate source: display=${displayCount}, gate=${gateCount}`);
  const transformed = html.replace(/font-display:block/g, 'font-display:swap').replace('.p25-font-pending body.p25{visibility:hidden;}', '');
  return { html: transformed, replacements: { font_display_block_to_swap: displayCount, font_visibility_gate_removed: gateCount }, before_sha256: sha(html), after_sha256: sha(transformed), changed_bytes: Buffer.byteLength(transformed) - Buffer.byteLength(html) };
}
function compute(row) {
  row.summary = { A: summarize(row.A), B: summarize(row.B) };
  const a = row.summary.A, b = row.summary.B;
  row.lcp_ratio_b_over_a = b.lcp_ms.median / a.lcp_ms.median;
  row.cls_delta = b.cls.median - a.cls.median;
  row.decision = b.lcp_ms.median < a.lcp_ms.median && b.cls.median <= a.cls.median ? 'ADOPT_CANDIDATE' : 'KEEP_BASELINE';
}
async function main() {
  if (fs.existsSync(OUTPUT)) throw new Error(`Refusing to overwrite prior evidence: ${OUTPUT}`);
  await chromiumRuntime();
  if (process.argv.includes('--preflight-only')) {
    const url = BASE + ROUTES[0];
    const response = await fetch(url);
    if (!response.ok) throw new Error(`Preflight route returned HTTP ${response.status}`);
    const transformed = makeFontVariant(await response.text());
    console.log('PASS font A/B preflight, no Lighthouse sample or browser navigation', JSON.stringify({ route: ROUTES[0], status: response.status, replacements: transformed.replacements, before_sha256: transformed.before_sha256, after_sha256: transformed.after_sha256 }));
    return;
  }
  const { default: lighthouse } = await import(pathToFileURL(require.resolve('lighthouse/core/index.js')));
  const report = {
    phase: 32,
    task: 'font diagnostic experiment',
    status: 'RUNNING',
    source: 'Current Phase32 source at test time; each B document differs only by font-display:block to swap and removal of the p25 font-pending visibility gate.',
    environment: { local_only: true, base: BASE, browser: 'Chromium 143 via @sparticuz/chromium', playwright: require('playwright/package.json').version, lighthouse: require('lighthouse/package.json').version, model: 'Lighthouse mobile simulated Slow4G and 4x CPU' },
    protocol: { routes: ROUTES, samples_per_arm_per_route: 7, fresh_browser_process_per_sample: true, serial: true, order: 'round 0 A then B, round 1 B then A, alternating through round 6', retries: 0, storage_reset: true, metrics: ['LCP', 'CLS', 'TBT', 'total transfer bytes', 'request count', 'LCP element', 'font requests', 'font readiness/gate events'] },
    candidate_transform: null,
    rows: []
  };
  let firstTransform = null;
  try {
    for (const route of ROUTES) {
      const row = { route, A: [], B: [] };
      report.rows.push(row);
      for (let round = 0; round < 7; round++) for (const arm of round % 2 ? ['B', 'A'] : ['A', 'B']) {
        const sample = { round, arm, order: round % 2 ? 'B/A' : 'A/B', status: 'STARTED', started_at: new Date().toISOString() };
        row[arm].push(sample);
        let browser, cdp;
        try {
          browser = await chromium.launch({ executablePath: await packed.executablePath(), args: chromeArgs(), headless: true });
          if (!browser.version().startsWith('143.')) throw new Error(`Expected Chromium 143, got ${browser.version()}`);
          cdp = await chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
          const context = cdp.contexts()[0];
          const observed = [];
          await context.exposeBinding('__p32FontEmit', (_, event) => observed.push(event));
          await context.addInitScript(() => {
            const emit = event => window.__p32FontEmit(event).catch(() => {});
            try { new PerformanceObserver(list => list.getEntries().forEach(entry => emit({ kind: 'lcp', time: entry.startTime, tag: entry.element?.tagName || null, className: typeof entry.element?.className === 'string' ? entry.element.className : null }))).observe({ type: 'largest-contentful-paint', buffered: true }); } catch (_) {}
            try { new PerformanceObserver(list => list.getEntries().forEach(entry => emit({ kind: 'layout-shift', time: entry.startTime, value: entry.value, recentInput: entry.hadRecentInput }))).observe({ type: 'layout-shift', buffered: true }); } catch (_) {}
            try { document.fonts?.addEventListener('loadingdone', event => emit({ kind: 'fonts-loaded', time: performance.now(), faces: event.fontfaces.map(face => ({ family: face.family, weight: face.weight, status: face.status })) })); } catch (_) {}
            try { new MutationObserver(() => emit({ kind: 'font-gate', time: performance.now(), pending: document.documentElement.classList.contains('p25-font-pending') })).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] }); } catch (_) {}
          });
          await context.route('**/*', async routeHandler => {
            const request = routeHandler.request(), url = new URL(request.url());
            const isDocument = request.isNavigationRequest() && url.origin === new URL(BASE).origin && url.pathname === route;
            if (arm === 'B' && isDocument) {
              const response = await routeHandler.fetch();
              const original = await response.body();
              const transformed = makeFontVariant(original.toString('utf8'));
              if (!firstTransform) firstTransform = { ...transformed, html: undefined };
              return routeHandler.fulfill({ response, body: transformed.html });
            }
            return resources(routeHandler);
          });
          const { lhr } = await lighthouse(BASE + route, { port: PORT, output: 'json', logLevel: 'error', onlyCategories: ['performance'], disableFullPageScreenshot: true, maxWaitForLoad: 15000, disableStorageReset: false });
          if (lhr.runtimeError) throw new Error(JSON.stringify(lhr.runtimeError));
          const audits = lhr.audits, network = audits['network-requests']?.details?.items || [];
          Object.assign(sample, {
            status: 'PASS', completed_at: new Date().toISOString(),
            lcp_ms: audits['largest-contentful-paint']?.numericValue,
            cls: audits['cumulative-layout-shift']?.numericValue,
            tbt_ms: audits['total-blocking-time']?.numericValue,
            transfer_bytes: audits['total-byte-weight']?.numericValue,
            requests: network.length,
            lcp_element: audits['largest-contentful-paint-element']?.details?.items?.[0]?.items?.[0]?.node?.snippet || null,
            font_network: network.filter(item => item.resourceType === 'Font').map(item => ({ url: new URL(item.url).pathname, bytes: item.transferSize, start: item.startTime, end: item.endTime })),
            render_blocking: (audits['render-blocking-resources']?.details?.items || []).map(item => item.url),
            observed_events: observed,
            warnings: lhr.runWarnings || []
          });
          for (const key of ['lcp_ms', 'cls', 'tbt_ms', 'transfer_bytes', 'requests']) if (!Number.isFinite(sample[key])) throw new Error(`Missing metric ${key}`);
          console.log(`SAMPLE ${route} round${round} ${arm} LCP=${sample.lcp_ms} CLS=${sample.cls} TBT=${sample.tbt_ms} bytes=${sample.transfer_bytes}`);
        } catch (error) {
          sample.status = 'FAIL'; sample.completed_at = new Date().toISOString(); sample.error = String(error.stack || error);
          report.status = 'INCOMPLETE'; report.failed_sample = { route, round, arm, error: String(error.message || error) };
          fs.writeFileSync(OUTPUT, JSON.stringify(report, null, 2) + '\n'); throw error;
        } finally {
          if (cdp) await cdp.close().catch(() => {});
          if (browser) await browser.close().catch(() => {});
        }
        fs.writeFileSync(OUTPUT, JSON.stringify(report, null, 2) + '\n');
      }
      if (row.A.length !== 7 || row.B.length !== 7) throw new Error(`Incomplete arms ${route}`);
      compute(row);
      fs.writeFileSync(OUTPUT, JSON.stringify(report, null, 2) + '\n');
    }
  } catch (error) {
    console.error(error.stack || error);
    process.exitCode = 1;
    return;
  }
  report.candidate_transform = firstTransform;
  report.status = 'COMPLETE';
  report.finished_at = new Date().toISOString();
  report.conclusion = report.rows.every(row => row.decision === 'ADOPT_CANDIDATE') ? 'Candidate improves median LCP without a worse median CLS in all three routes; manual implementation decision still required.' : 'Candidate did not improve median LCP without a worse median CLS in every route. Keep the existing font-display, preloads, gate and CSS unchanged.';
  report.totals = { samples: report.rows.reduce((sum, row) => sum + row.A.length + row.B.length, 0), routes: report.rows.length, candidate_adoption_eligible_all_routes: report.rows.every(row => row.decision === 'ADOPT_CANDIDATE') };
  fs.writeFileSync(OUTPUT, JSON.stringify(report, null, 2) + '\n');
  for (const row of report.rows) console.log('SUMMARY', row.route, 'A_LCP', row.summary.A.lcp_ms.median, 'B_LCP', row.summary.B.lcp_ms.median, 'A_CLS', row.summary.A.cls.median, 'B_CLS', row.summary.B.cls.median, 'decision', row.decision);
  console.log('COMPLETE', report.totals);
}
main().catch(error => { console.error(error.stack || error); process.exit(1); });
