#!/usr/bin/env node
// Resource, long-task, image, coverage and paint audit for four reference pages.
const fs = require('node:fs');
const path = require('node:path');
const { launchBrowser } = require('../phase31/browser.cjs');
const { resources } = require('../phase25/resources.cjs');
const ROOT = path.resolve(__dirname, '../..');
const BASE = process.env.PHASE32_BASE_URL || 'http://127.0.0.1:8080';
const ROUTES = ['/', '/services', '/about', '/contact'];
const SCENE_DEPENDENCY = /three\.min\.js|gsap\.min\.js|ScrollTrigger\.min\.js/;
function usedBytes(source, ranges) {
  const spans = ranges.filter(range => Number.isFinite(range.start) && Number.isFinite(range.end) && range.end > range.start).map(range => [range.start, range.end]).sort((a, b) => a[0] - b[0]);
  const merged = [];
  for (const span of spans) {
    const last = merged[merged.length - 1];
    if (last && span[0] <= last[1]) last[1] = Math.max(last[1], span[1]);
    else merged.push([...span]);
  }
  return merged.reduce((sum, [start, end]) => sum + Buffer.byteLength(source.slice(start, end), 'utf8'), 0);
}
function jsUsedBytes(source, functions) {
  const profiles = functions.map(fn => {
    const ranges = fn.ranges || [];
    if (!ranges.length) return null;
    return { fn, start: Math.min(...ranges.map(r => r.startOffset)), end: Math.max(...ranges.map(r => r.endOffset)), ranges };
  }).filter(Boolean);
  const used = [];
  for (const profile of profiles) {
    const boundaries = [...new Set(profile.ranges.flatMap(range => [range.startOffset, range.endOffset]))].sort((a, b) => a - b);
    const own = [];
    for (let i = 0; i < boundaries.length - 1; i++) {
      const start = boundaries[i], end = boundaries[i + 1];
      if (end <= start) continue;
      const covering = profile.ranges.filter(range => range.startOffset <= start && range.endOffset >= end).sort((a, b) => (a.endOffset - a.startOffset) - (b.endOffset - b.startOffset));
      if (covering.length && covering[0].count > 0) own.push([start, end]);
    }
    const nested = profiles.filter(other => other !== profile && other.start >= profile.start && other.end <= profile.end && (other.start > profile.start || other.end < profile.end));
    for (const [start, end] of own) {
      let pieces = [[start, end]];
      for (const child of nested) {
        const next = [];
        for (const [left, right] of pieces) {
          if (child.end <= left || child.start >= right) next.push([left, right]);
          else {
            if (child.start > left) next.push([left, child.start]);
            if (child.end < right) next.push([child.end, right]);
          }
        }
        pieces = next;
      }
      used.push(...pieces);
    }
  }
  return usedBytes(source, used.map(([start, end]) => ({ start, end })));
}
(async () => {
  const browser = await launchBrowser();
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  await context.route('**/*', resources);
  const cases = [];
  try {
    for (const route of ROUTES) for (const width of [360, 1280]) {
      const page = await context.newPage();
      await page.setViewportSize({ width, height: 900 });
      await page.addInitScript(() => {
        window.__p32audit = { lcp: [], cls: [], longTasks: [] };
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32audit.lcp.push({ startTime: e.startTime, size: e.size, tag: e.element?.tagName || null, id: e.element?.id || null, className: typeof e.element?.className === 'string' ? e.element.className : null, text: e.element?.textContent?.trim().slice(0, 100) || null }))).observe({ type: 'largest-contentful-paint', buffered: true }); } catch (_) {}
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32audit.cls.push({ value: e.value, startTime: e.startTime, recentInput: e.hadRecentInput }))).observe({ type: 'layout-shift', buffered: true }); } catch (_) {}
        try { new PerformanceObserver(list => list.getEntries().forEach(e => window.__p32audit.longTasks.push({ startTime: e.startTime, duration: e.duration }))).observe({ type: 'longtask', buffered: true }); } catch (_) {}
      });
      await page.coverage.startJSCoverage({ resetOnNavigation: false, reportAnonymousScripts: true });
      await page.coverage.startCSSCoverage({ resetOnNavigation: false });
      const bodyPromises = [];
      const failures = [];
      page.on('response', response => {
        const request = response.request();
        bodyPromises.push((async () => {
          const body = await response.body().catch(() => Buffer.alloc(0));
          return { url: response.url(), type: request.resourceType(), status: response.status(), bytes: body.length, headers: await response.allHeaders().catch(() => ({})) };
        })());
      });
      page.on('requestfailed', request => failures.push({ url: request.url(), type: request.resourceType(), error: request.failure()?.errorText || null }));
      const response = await page.goto(BASE + route, { waitUntil: 'load', timeout: 60000 });
      if (!response || response.status() !== 200) throw new Error(`Reference route returned non-200: ${route}`);
      await page.waitForTimeout(3200);
      const [jsCoverage, cssCoverage, state, bodies] = await Promise.all([
        page.coverage.stopJSCoverage(), page.coverage.stopCSSCoverage(),
        page.evaluate(() => {
          const nav = performance.getEntriesByType('navigation')[0];
          const resources = performance.getEntriesByType('resource').map(e => ({ name: e.name, path: (() => { try { return new URL(e.name).pathname; } catch (_) { return e.name; } })(), type: e.initiatorType, startTime: Number(e.startTime.toFixed(2)), responseEnd: Number((e.startTime + e.duration).toFixed(2)), duration: Number(e.duration.toFixed(2)), transferSize: e.transferSize, decodedBodySize: e.decodedBodySize }));
          const images = [...document.images].map(img => ({ src: img.currentSrc || img.src, alt: img.alt, complete: img.complete, naturalWidth: img.naturalWidth, naturalHeight: img.naturalHeight, renderedWidth: Number(img.getBoundingClientRect().width.toFixed(1)), renderedHeight: Number(img.getBoundingClientRect().height.toFixed(1)), loading: img.loading || 'eager', decoding: img.decoding || 'auto' }));
          return { loadEventEnd: nav.loadEventEnd, domContentLoadedEventEnd: nav.domContentLoadedEventEnd, lcp: window.__p32audit.lcp, clsEvents: window.__p32audit.cls, longTasks: window.__p32audit.longTasks, resources, images, externalStylesheets: [...document.querySelectorAll('link[rel="stylesheet"]')].map(x => x.href), externalScripts: [...document.scripts].filter(x => x.src).map(x => x.src) };
        }),
        Promise.all(bodyPromises)
      ]);
      const cssRows = cssCoverage.map(entry => { const text = entry.text || ''; const ranges = entry.ranges || []; return { url: entry.url, bytes: Buffer.byteLength(text, 'utf8'), used_bytes: usedBytes(text, ranges), inline: !entry.url }; });
      const jsRows = jsCoverage.map(entry => { const source = entry.source || ''; return { url: entry.url || '(inline)', bytes: Buffer.byteLength(source, 'utf8'), used_bytes: jsUsedBytes(source, entry.functions || []), inline: !entry.url }; });
      const cssTotal = cssRows.reduce((sum, row) => sum + row.bytes, 0), cssUsed = cssRows.reduce((sum, row) => sum + row.used_bytes, 0);
      const jsTotal = jsRows.reduce((sum, row) => sum + row.bytes, 0), jsUsed = jsRows.reduce((sum, row) => sum + row.used_bytes, 0);
      const resourceRows = bodies.map(body => {
        const entry = state.resources.find(item => item.name === body.url || item.path === new URL(body.url).pathname);
        return { ...body, startTime: entry?.startTime ?? null, responseEnd: entry?.responseEnd ?? null, initiatorType: entry?.type ?? null, transferSize: entry?.transferSize ?? 0 };
      });
      const sceneResources = resourceRows.filter(resource => SCENE_DEPENDENCY.test(resource.url));
      const preScene = resourceRows.filter(resource => !SCENE_DEPENDENCY.test(resource.url));
      const preSceneBytes = preScene.reduce((sum, resource) => sum + resource.bytes, 0);
      const sceneDependencyBytes = sceneResources.reduce((sum, resource) => sum + resource.bytes, 0);
      const imageResponses = resourceRows.filter(resource => resource.type === 'image');
      const longTaskTbt = state.longTasks.reduce((sum, task) => sum + Math.max(0, task.duration - 50), 0);
      cases.push({ route, width, status: 'PASS', document_bytes: resourceRows.find(r => r.type === 'document')?.bytes ?? null, response_bytes: resourceRows.reduce((sum, row) => sum + row.bytes, 0), pre_scene_bytes: preSceneBytes, pre_scene_resource_count: preScene.length, pre_scene_limit_bytes: 400000, pre_scene_budget_pass: preSceneBytes < 400000, scene_dependency_bytes: sceneDependencyBytes, scene_dependencies: sceneResources.map(r => ({ url: r.url, bytes: r.bytes, startTime: r.startTime, status: r.status })), image_response_bytes: imageResponses.reduce((sum, row) => sum + row.bytes, 0), image_responses: imageResponses.map(r => ({ url: r.url, bytes: r.bytes, status: r.status })), js_coverage: { total_bytes: jsTotal, used_bytes: jsUsed, unused_bytes: jsTotal - jsUsed, unit: 'uncompressed UTF-8 source bytes using nested V8 function/block coverage intervals', top_unused: [...jsRows].sort((a, b) => (b.bytes - b.used_bytes) - (a.bytes - a.used_bytes)).slice(0, 12).map(row => ({ url: row.url, bytes: row.bytes, unused_bytes: row.bytes - row.used_bytes })) }, css_coverage: { total_bytes: cssTotal, used_bytes: cssUsed, unused_bytes: cssTotal - cssUsed, top_unused: [...cssRows].sort((a, b) => (b.bytes - b.used_bytes) - (a.bytes - a.used_bytes)).slice(0, 12).map(row => ({ url: row.url, bytes: row.bytes, unused_bytes: row.bytes - row.used_bytes })) }, observed_long_task_tbt_ms: Number(longTaskTbt.toFixed(2)), failures, state, resources: resourceRows });
      await page.close();
      console.log('PASS ref audit', route, width, 'bytes', resourceRows.reduce((sum, row) => sum + row.bytes, 0), 'pre-scene', preSceneBytes, 'LCP', state.lcp.at(-1)?.startTime ?? null, 'long tasks', state.longTasks.length, 'unused JS', jsTotal - jsUsed);
    }
  } finally {
    await context.close().catch(() => {});
    await browser.close();
  }
  const report = { phase: 32, status: 'PASS', scope: 'Pre-change local reference audit before scene deferral; route responses use the local PHP-WASM adapter and resource mirrors, not live CDN. Pre-scene bytes are all successful response-body bytes except Three.js, GSAP and ScrollTrigger. Coverage measures executed/unused bytes for this one browser path and do not equal Lighthouse audit values.', budgets: { lcp_ms_lte: 4000, tbt_ms_lte: 600, cls_lt: 0.1, pre_scene_transfer_bytes_lt: 400000 }, cases };
  fs.writeFileSync(path.join(ROOT, 'reports/phase-32-reference-audit-before.json'), JSON.stringify(report, null, 2) + '\n');
})().catch(error => { console.error(error.stack || error); process.exit(1); });
