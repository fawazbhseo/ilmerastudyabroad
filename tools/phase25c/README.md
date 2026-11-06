# Phase25c verification harness

Local-only evidence, not native Apache/LiteSpeed, real CDN, field performance, contact delivery or deployment proof. Tools/reports/Git/runtime caches are not deployment payloads. Never run a completed benchmark again without new owner authorization. Phase25c has exhausted its three performance reliability sessions.

## Runtime

Use the existing external runtime via `. tools/phase25/env.sh`. Recorded versions: Lighthouse12.8.2, Playwright1.58.2, PHP WASM node adapter3.1.58/PHP8.5, fontsource Outfit/Cormorant Garamond5.2.8. Python image/math dependencies are pinned in requirements.txt and installed outside Git at /home/user/phase25-runtime/pylibs. No native-server assertion follows from this adapter.

## Immutable references and structural gate

Archive Stage1 commit3f0e141 into /home/user/phase25c-evidence/stage1 using git archive, without changing the session branch. render.cjs independently renders that tree into stage1-references.json. current-references.json is separately fetched from the local PHP adapter on8080, as `{routes:{path:{html:string}}}` for `/`, `/services`, `/about`, `/contact`. Both files live outside Git. Recorded source/HTML SHA values and compressed full structures live under reports.

reference.cjs makes six independent baseline captures (three predefined pairs) plus current per page/width. Capture-only seeded clock/random, frozen first scene frame, settled finite animations and forced reveal visibility are applied identically to both arms, never to production sources. All visible DOM elements, direct text/order, rounded0.1px boxes and requested computed styles/pseudo paint are compared. Raw raster files stay outside Git. pixels.py computes full-resolution RGB7x7 SSIM in strips with halo; it does not downsample. Approved card rectangles/windows are excluded from raster backstops, not from the stronger exact structure comparison. Each case retains its own three-pair noise floor. No source edits or structural exception were needed.

## Performance

fixtures.py freezes A/B first: immutable Stage1 HTML for references, immutable committed Phase24b captures elsewhere, independently fetched current B. fixture-server.cjs serves both arms at exactly the same document origin/path and static delivery; existing resources.cjs supplies the exact npm mirrors equally. selected.json chooses the arm, not a public app feature. Do not run any other capture/browser/QA benchmark during ab.cjs. Seven samples/arm, fresh isolated Chromium process for every sample, serial alternating round order. Real animations remain active. Passive observers send LCP/font/paint-gate diagnostics before Lighthouse closes its target. The oversized post-trace report screenshot is disabled in reruns; no metric trace or throttling is disabled.

Every session is retained. A known failed reference can end an unreliable session early; the last allowed session still measures all14 routes. Both directions of reference median LCP ratios must remain<=1.10. No route budget is relaxed. ab_report.py adds an independent external stylesheet/classic blocking-script proof, median/IQR table and conservative certification decision. Failed/partial rows are never promoted to complete seven-sample medians. An initial target-closed setup probe log remains outside Git, with no recorded pair used for acceptance.

## Other checks

- tiers.py records whole-template uniformity and actual five-probe LCP diagnostics. No speculative font-gate/source edit is justified by unreliable controls.
- chrome.cjs compares every visible chrome node rect/text/order plus canonical computed styles. Only geometry strictly below0.1px is tolerated. Disable test-DOM active-link transitions before clearing active state, otherwise the old active colour is sampled.404 abbreviated footer is the accepted exception; header still tested.
- overflow.cjs observes five original JS-on reference cases, including invisible transform contributors, without applying CSS changes. a11y_report.py preserves all24 original contrast groups/387 node instances with colours/ratios and a nearest passing existing-palette single-foreground suggestion. Suggestions are not applied. Hidden offscreen reveal transforms explain numerical scrollWidth excess; no horizontal-wheel pan was observed, not a blanket promise for every animation frame.
- run.py/check.py/browser.cjs/accessibility.cjs/contrast.py/regions.cjs are isolated-output copies of established checks. Historical source/content/metadata guards are not weakened. The first full final cycle executes all lints, units,43 renders,258 browser cases, strict discovery/schema/wording/overlap/palette, accessibility and117 region/14 font-failure-condition cases. At most two final cycles are permitted. No fourth performance session is authorized by a final QA cycle.

The release report must say NOT READY when controls are unreliable or any required budget/proof is missing, even when individual numerical rows pass. Preserve prior source/business/native-host/proof/backup/restore blockers and do not deploy, merge or push main.
