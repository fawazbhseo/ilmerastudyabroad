# Phase32c progress

- **Date:** 2026-11-06
- **Branch:** `arena/48320ee5-ilmerastudyabroad`
- **Scope:** contrast reproduction and classification, reference scene safeguard checks, conservative place/article hero-still A/B, one final full suite, deploy payload verification and documentation. No merge or deployment.
- **Remote match:** fetched `origin/arena/48320ee5-ilmerastudyabroad` and fast-forwarded the existing local branch from `c2c57b5` to the remote tip `f9c96caf3f1ff1ed7fe031b87d899cd8da78c0c2`. The working tree was clean before this progress file. No branch switch or new branch.

## Read-in and prior state

- Read `reports/phase-32a-release-check.md`, `reports/phase-32a-progress.md`, `reports/phase-32-progress.md` and recent history. Phase32a's final aggregate is 23/24 PASS and 1 FAIL, with four new baseline-relative Home/About contrast findings retained and the full suite not rerun after its original run.
- Prior measurements and runtime results are historical local-simulation evidence. Phase32's reference scene changes and fallbacks are already pushed. Current full-suite, reference-state, three-arm hero A/B and deploy ZIP checks are not yet run in this Phase32c task.
- The owner's final decisions dated 2026-10-31 are the active design and budget gates. Existing protected wording, layout, content, schema, metadata and desktop design remain fixed. Where evidence is inconclusive, preserve the plain palette hero and record the uncertainty.

## Completed this checkpoint

- Matched the session branch to the fetched remote `f9c96ca` tip and read the required reports and history.
- No browser audit, source edit, measurement, full-suite run, payload build or ZIP build has occurred yet in Phase32c.

## 2026-11-05 checkpoint: source history and runtime availability checked

- Confirmed the literal first commit after Phase31 baseline `796879d` is `d0b7726` (a Phase32 preflight note with no source edits). The first Phase32 source/runtime change is `2722901` (responsive hero still and shared presentation changes); `8f055bd` before it only adds the smaller mobile still asset. The reference scene loader/defer change is later commit `d4b376e`. These distinct points will be retained in the bisect report so a documentation checkpoint is not mistaken for a source change.
- Current findings map to unchanged markup/styles in `index.php:544` and `about.php:376-378,606,635,678`. The current visual layer can alter their rendered backdrop through the deferred reference scene path in `includes/visual-system.php`; no classification is assigned before screenshot reproduction.
- The external pinned runtime directories `/home/user/phase32-runtime` and `/home/user/phase32a-runtime` are absent. The repository contains the Phase31 accessibility/render/target baselines and prior Phase32 scene smoke records. No new browser run has occurred.
- No public source edit has been made.

## 2026-11-05 checkpoint: pinned runtime restored

- Restored the pinned PHP-WASM 8.5.8 CLI and PHP-WASM adapter packages, Playwright 1.58.2, Chromium 143.0.7499.0, Lighthouse 12.8.2, axe-core 4.11.0, local Three.js/GSAP mirrors, PNG tooling and image tooling under `/home/user/phase32c-runtime`, outside the repository. The external `php` shim successfully required `includes/proof.php`.
- Started the current PHP-WASM adapter on port 8094. PHP lint passed for `includes/visual-system.php`, `includes/visual-config.php`, `index.php` and `about.php`; current Home and About rendered HTTP 200. An About 1280px browser smoke with the local scene mirrors waited 3.2 seconds and reported no page or console errors.
- One preliminary browser smoke that reused a browser across contexts hit a browser-closed error after Home. A fresh independent process then rendered About successfully. The actual audit will use a new Chromium process for each requested case and record any crash/retry.
- Exported source trees outside Git for `75f355f`, `796879d`, the literal first commit after baseline `d0b7726`, first Phase32 public-runtime source commit `2722901`, reference scene defer commit `d4b376e`, and pre-Phase32c HEAD `f9c96ca`.
- No public source edit or screenshot evidence has been made yet.

## 2026-11-05 checkpoint: contrast harness validated

- Added `tools/phase32c/contrast-repro.cjs` with a fresh Chromium process per case, route-pinned resources, real mouse-wheel scrolling plus End, a three-second full-page settle, computed foreground and ancestry capture, adjacent screenshot-pixel backdrop sampling, contrast calculation and per-finding crops. The harness supports route/width/state filters for focused smoke tests; the full matrix remains 24 cases.
- Validated the JavaScript-off Home 360px case after replacing page-side scrolling: it completed with zero scene calls, `#888888` text, and a preliminary 3.545:1 sampled contrast. Validated About at 1280px with the reference scene eligible: one scene initialization and preliminary sampled ratios 1.097:1 (`#faq-h2`), 1.948:1 (team label) and 1.935:1 (Kodagu label). The FAQ crop visibly shows very dark text against the dark animated scene. These are smoke-test observations only, not classifications.
- The earlier current-source 360px partial crops in `reports/screenshots/phase-32c/f9c96ca/` are retained and will be overwritten by the completed 24-case capture. Focused smoke outputs remain outside Git under `/home/user/phase32c-runtime`.
- No public source edit or contrast fix has been made.

## 2026-11-05 checkpoint: screenshot timeout recovered

- The first full current-source matrix completed cases 1-19, then stopped on About 768px JavaScript-off because Playwright's screenshot call hit its 30-second timeout. The harness did not save a JSON report in that initial run; those logged ratios are exploratory, not complete evidence.
- Increased the screenshot timeout, disabled active CSS animations during crop capture, added atomic per-case JSON checkpoints, and added a resume mode so later failures do not discard completed measurements. A focused fresh-process rerun of About 768px JavaScript-off passed with zero scene calls and sampled ratios 1.098:1, 1.935:1, and 1.935:1.
- No public source edit or contrast classification has been made.

## 2026-11-05 checkpoint: current-source contrast matrix complete

- Completed and saved all 24 current public-runtime cases for Home and About at 360, 768 and 1280px in touch/coarse, eligible desktop, reduced-motion and JavaScript-off states. The JSON is `reports/phase-32c-contrast-f9c96ca.json`; it contains all 24 unique cases, 48 per-finding PNG crops, complete computed colors/backdrop samples/ratios, and no browser or console errors. Every referenced crop exists.
- The Home note remained `rgb(136, 136, 136)` on sampled `#FFFFFF` at 3.545:1 in all states. About `#faq-h2` remained `rgb(10, 22, 40)` over sampled dark pixels `#060811` to `#070911`, at 1.097:1 to 1.098:1. Both About section labels remained `rgb(201, 168, 76)` over `#E8ECF8`, at 1.935:1. These all-state results make the apparent defects reproducible, but no REAL/TRANSIENT/MEASUREMENT ARTEFACT classification is assigned before historical comparisons.
- Scene initialization occurred exactly once only for the eligible 1280px fine-pointer case on Home and About; all 22 other cases, including JavaScript-off and reduced-motion, recorded zero scene calls.
- No public source edit or contrast fix has been made.

## 2026-11-05 checkpoint: historical scene-start signal corrected

- Started a separate PHP-WASM adapter for the `75f355f` source export on port 8095. A focused About 1280px no-scene smoke reproduced 1.089:1 for the FAQ heading and 1.935:1 for both labels. The first historical matrix reached 8 cases, then exposed a harness assumption: those pre-Phase32 pages initialize WebGL directly instead of calling the Phase32 deferred `__ILMERA_SCENE_INIT` wrapper.
- Added a version-independent scene-start signal by instrumenting `HTMLCanvasElement.getContext` for WebGL. The 75f355f desktop smoke now records one `webgl2` context, visible scene layers, and the same preliminary contrast ratios. These are historical smoke observations only. A full historical matrix is not complete, and expected blocked remote-font console messages are being kept distinct from application errors in analysis.
- No public source edit or classification has been made.

## 2026-11-05 checkpoint: 75f355f historical matrix complete

- Completed all 24 cases and 48 crops for `75f355f` in `reports/phase-32c-contrast-75f355f.json` and `reports/screenshots/phase-32c/75f355f/`. The four computed foregrounds match current: Home note `rgb(136, 136, 136)`, About FAQ heading `rgb(10, 22, 40)`, and both labels `rgb(201, 168, 76)`. Home remained 3.545:1 on `#FFFFFF`; FAQ measured 1.012:1 to 1.097:1 against animated dark pixels; the labels measured 1.935:1 to 1.967:1 against `#E8ECF8`/`#E9EDF8`.
- The original pre-Phase32 source created a WebGL context in all 18 JavaScript-enabled cases, including touch/coarse and reduced-motion inputs; the six JavaScript-off cases created none. Therefore the requested no-scene phone/reduced-motion state was not actually achieved by this historical build. The capture records actual behavior rather than claiming those cases were scene-free.
- Each case has one expected `ERR_BLOCKED_BY_CLIENT` console event because the isolated browser intentionally blocks remote Google Fonts. No page exceptions occurred; computed colors and backdrops are recorded. No contrast classification or public edit has been made.

## 2026-11-05 checkpoint: Phase31b reference matrix complete

- Completed the 24-case, 48-crop matrix at the Phase31b reference `796879d`. All crops exist; the only console event per case is the expected blocked remote-font notice, with no page exceptions. Foregrounds match `75f355f` and current. Home is 3.545:1; About FAQ is 1.018:1 to 1.102:1; the two section labels are 1.935:1 to 1.953:1.
- Like `75f355f`, `796879d` creates WebGL in all 18 JavaScript-enabled cases, including touch/coarse and reduced-motion inputs; its six JavaScript-off cases create no WebGL context. The requested no-scene phone/reduced states are therefore not real states in these earlier builds. The color/backdrop defects predate the Phase32 source changes sampled so far; animated FAQ pixels account for the small range, not a passing 4.5:1 result.
- Confirmed `796879d..d0b7726` changes only `reports/phase-32-progress.md`; no runtime-affecting PHP, CSS, assets or content changed at the literal first post-baseline commit.
- No classification or public source edit has been made.

## 2026-11-05 checkpoint: first Phase32 source matrix complete

- Completed all 24 cases and 48 crops at `2722901`, the first Phase32 public-runtime source behavior change. The report is `reports/phase-32c-contrast-2722901.json`; all crops exist. Home is still 3.545:1, About FAQ remains 1.018:1 to 1.102:1, and both labels remain about 1.935:1. Computed foregrounds match the two Phase31 checkpoints and current.
- WebGL contexts were created in all 18 JavaScript-enabled cases and none of the six JavaScript-off cases. Thus the first Phase32 hero-still change did not yet safeguard Home/About scenes for touch/coarse or reduced-motion, and it did not change these four color/background relationships. The 24 remote-font console notices are the expected isolated-runner blocks; no other console or page errors occurred.
- `d0b7726` remains verified runtime-identical to `796879d`; no duplicate matrix is needed. No classification or public color edit has been made.

## 2026-11-05 checkpoint: reference-scene defer matrix complete

- Completed all 24 cases and 48 crops at `d4b376e`. WebGL context creation and the deferred init wrapper occurred only for Home and About at 1280px in the fine-pointer eligible state. The other 22 cases, including phone/touch, reduced-motion and JavaScript-off, made no WebGL context.
- The four text foregrounds and low-contrast color/background pairs remain materially the same as the earlier checkpoints and current `f9c96ca`: Home note 3.545:1; About FAQ 1.089:1 to 1.097:1; About labels 1.935:1. The defer change corrected scene-state behavior but did not introduce or fix any of these contrast relationships. All crops exist; only the known blocked-font console event occurred per case.
- Across the completed historical points, the four visual defects predate Phase32, while scene behavior changed at `d4b376e`. No classification or public source edit has been made.

## 2026-11-05 checkpoint: historical contrast classification

- All five completed matrices (`75f355f`, `796879d`, `2722901`, `d4b376e`, `f9c96ca`) contain 24 cases and 48 existing crops each. `d0b7726` is runtime-identical to `796879d`, confirmed by an empty runtime-path diff. The relevant Home/About color declarations are unchanged from `75f355f` to `f9c96ca`; the only edits to those PHP files in that interval are team min-height rules. The Phase31 accessibility baseline does not list these exact revealed nodes, which is not evidence that their fully scrolled visual relationships passed.
- **Classification: REAL, pre-existing** for all four. They are visibly rendered in the full-scroll crops and every matching screenshot measurement is below 4.5:1. Home `em`: `rgb(136,136,136)` on `#FFFFFF`, 3.545:1. About `#faq-h2`: `rgb(10,22,40)` on dark sampled pixels, 1.089:1 to 1.098:1 on the current/deferred build. About team and Kodagu labels: `rgb(201,168,76)` on `#E8ECF8`, 1.935:1. Historical animated-scene samples add small backdrop variation but never pass; this does not make the findings transient or measurement artefacts.
- The requested historical set has no last-passing commit for these exact pairs. The smallest authorized repairs will reuse already-present passing palette relationships without changing wording, layout, surfaces or imagery: remove only the Home note's explicit `#888` so it inherits the existing `--grey-dark` (`#4A5568`, 7.526:1 on white); change only `#faq-h2` from the existing dark-heading variant to the existing light-heading variant on the dark FAQ surface (white, approximately 19.9:1); set only the team label and Kodagu label to the existing `--navy` (`#1A2E5A`, 11.239:1 on `#E8ECF8`). Each finding will be fixed in its own commit. The scene safeguards are a separate behavior change: older builds create WebGL in 18 JavaScript-enabled cases, while `d4b376e` and current create it only for the two eligible 1280px desktop cases.
- No contrast source fixes have been applied yet.

## 2026-11-05 checkpoint: Home contrast finding fixed

- Removed only the inline `color:#888` from the Home programme-conditions note. It now inherits the existing `--grey-dark` text color; wording, size, background, layout and imagery are unchanged.
- Fresh-process no-scene screenshot captures at 360px and 1280px both measured 7.526:1 on white. Both reported zero scene calls. The original CRLF line endings remain intact.
- This is the first of four separately committed contrast fixes.

## 2026-11-05 checkpoint: About FAQ heading contrast fixed

- Changed only `#faq-h2` from the existing `dk` heading variant to the existing `lt` variant. Text, font, size, spacing, section surface and layout are unchanged.
- Fresh no-scene About screenshot checks at 360px and 1280px measured 19.883:1 for the FAQ heading, with zero scene calls. The team and Kodagu labels remain at 1.935:1 and are the next findings. Existing mixed CRLF/LF line endings in `about.php` are preserved.
- This is the second of four separately committed contrast fixes.

## 2026-11-05 checkpoint: About team label contrast fixed

- Added one narrowly scoped rule for `#team > .container > .team-hdr > .sec-label`, reusing the existing `--navy` token. Only the color of the affected label changes; its text, font, spacing, surface and section layout remain unchanged.
- Fresh no-scene About screenshot checks at 360px and 1280px measured 11.239:1 for the team label. The FAQ heading remained at 19.883:1; the Kodagu label remains at 1.935:1. No scene calls occurred.
- This is the third of four separately committed contrast fixes.

## 2026-11-05 checkpoint: About Kodagu label contrast fixed

- Added one selector scoped to `#kodagu > .container > .sec-label`, reusing the existing `--navy` token. Only the affected label color changes; text, font, spacing, background, image content and layout are unchanged.
- Fresh no-scene About screenshot checks at 360px and 1280px measured 11.239:1 for both the team and Kodagu labels and 19.883:1 for the FAQ heading. All three affected About nodes pass 4.5:1 in both viewports, with zero scene calls.
- All four separately scoped contrast corrections now have fast-check evidence. The Home note measures 7.526:1 at both requested widths. Existing line endings remain intact.

## 2026-11-05 checkpoint: contrast task complete

- Fixed each REAL contrast finding in its own pushed commit: Home note `bde0ddd`, About FAQ heading `6c9fea4`, About team label `f6a91c8`, and About Kodagu label `3324432`. All changes reuse existing palette values and leave wording, font sizing, layout, surfaces and imagery unchanged.
- Added `tools/phase32c/contrast-regression.cjs`. Its fresh-browser screenshot gate checked Home and About at 360px and 1280px with the scene not started, verified all four nodes and eight crops, and enforced 4.5:1. It passed; the minimum measured contrast was 7.526:1. Evidence is in `reports/phase-32c-contrast-regression-3324432.json` and `reports/screenshots/phase-32c/contrast-regression-3324432/`.
- The complete historical evidence remains committed for `75f355f`, `796879d`, `2722901`, `d4b376e` and pre-fix current `f9c96ca`. No full suite has been run.

## 2026-11-05 checkpoint: Task 2 comparison harness smoke-validated

- Recreated the pinned PHP-WASM, Chromium and Playwright runtime outside Git after the external cache was absent in this continuation environment. Started the current adapter on port 8096, the Phase31b `796879d` adapter on 8097, and isolated `ILMERA_SCENES_ENABLED=false` source adapters on 8098 and 8099. No site dependency or source tree was modified for the disabled-switch test; those adapters use external test copies.
- Added `tools/phase32c/reference-safeguards.cjs`. It compares every visible DOM element outside the scene layers at a 0.1 CSS-pixel tolerance, checks text, headings, links, images, picture sources, canonicals and JSON-LD, uses pinned local font and scene mirrors, and records header, footer and team-card boxes. Each source/state pair gets a fresh Chromium process, full scroll, three-second settle and deterministic phase-zero pause for infinite CSS animations. The cursor-following overlay is excluded from geometry because its position depends on the physical pointer.
- Focused smoke checks passed: About 360px still fallback had exact content parity and zero element geometry delta; Home 1280px scene had both baseline/current WebGL starts and zero geometry delta; Home 1280px disabled-switch mode had no WebGL, both off styles present and zero geometry delta. The About smoke recorded only the expected contrast color differences and current reveal-animation class additions. No reference hero-still elements or still requests appeared.
- These are harness smoke checks only. An initial partial matrix attempt was discarded after exposed test-harness issues: infinite marquee phase noise, sticky descendants measured in document coordinates, and a JavaScript-off animation-frame wait. The comparison now pauses infinite CSS animation at a deterministic phase, measures fixed/sticky descendants in viewport coordinates, and uses a bounded settle wait. Follow-up Home 360px JavaScript-off and disabled-switch smokes pass with zero geometry delta. No partial matrix report is retained.
- The requested 60-case visual comparison has not yet completed, and no final suite has run.

## 2026-11-05 checkpoint: Task 2 incremental matrix complete

- Completed the corrected 60-case matrix in `reports/phase-32c-reference-safeguards.json`: Home 15/15 PASS, Services 15/15 PASS, About 15/15 PASS, Contact 4/15 literal geometry PASS. The remaining 11 Contact cases retain raw differences over the 0.1px threshold. All 11 are classified MEASUREMENT ARTEFACT based on same-source A/A controls; the 0.1px threshold is not waived and no source change was made. Summary and interpretation: `reports/phase-32c-reference-safeguards.md`.
- All 120 baseline/current renders reached the page end, all tracked current reveal targets settled, and there were zero runtime errors or content differences. Visible text, headings, links, images, picture sources, JSON-LD and canonicals matched in 60/60. Header and About team geometry matched in 60/60; team-card text/boxes matched in 60/60. The 11 Contact footer positions follow the 4px native-select height variation.
- Contact's two selects measured 46px in the Phase31b render and 48px in current in each of the 11 raw-difference cases. Each is 2px taller and the downstream page/footer shift totals 4px; maximum absolute element delta is 4px. The same-source A/A report is `reports/phase-32c-reference-safeguards-aa.json`: 8 controls, 6 exact, 2 Contact geometry differences; the direction reverses in same-source Contact 360px and 1280px disabled-switch pairs. Contact 768px disabled-switch and JavaScript-off A/A at all three widths are exact. About and Services 360px A/A are exact with 14 and 41 reveal targets active.
- The current source starts WebGL only for the four eligible 1280px normal-scene cases; the Phase31b source starts in 24/60 states, including phone-width and reduced-motion cases. The current local-font style is present in every reference render. There were no hero-still nodes or requests on these four reference pages in any state. The earlier Phase32 hero-still scope remains limited to destination/place/article/blog-index pages; no reference logo or Contact `#miniHero` change was applied. Current Phase32c Task 3 has not started.
- The earlier large-wheel matrix and separate-page trial remain invalid diagnostics because About and Services reveals were not aligned. The accepted Task 2 evidence is the incremental-scroll matrix and the attached A/A controls. No final full suite has run.
- This checkpoint changes only test tooling and reports. No public runtime/content source was edited for Task 2.

## 2026-11-06 checkpoint: Task 3 fixtures frozen and smoke checked

- Rendered only the two selected routes with PHP-WASM 8.5.8: exact A source `7d1bb9ec0522bcbc7953262920fafb50bf04ab72` and current B source `ac2d9b06dc85578e4b4c31ad236b228f67d44333`. B-still and B-plain were made from the same B source, with one external test-only `ILMERA_VISUAL_PLAIN_HERO_TEMPLATES` toggle. The source-tree diff between B arms is exactly `includes/visual-config.php`.
- `reports/phase-32c-hero-ab-fixtures.json` records the route renders, hashes and test-arm guards. External fixture JSON is 373,542 bytes with SHA-256 `9a037671a583590250d9002860bb7cbd2563a0bec1ac9288dee2b3cc89dfcf82`. Both routes passed HTTP 200 for all three arms. Text, title, headings, metadata, robots, canonicals, links, images, picture sources and JSON-LD match between A, B-still and B-plain.
- Six fresh-browser fixture smoke checks passed at 360px, one per route and arm. B-still loaded its hero image on both routes; A and B-plain had no still canvas. These were page/asset integration checks only, not Lighthouse performance samples.
- Provenance issue found and preserved: the committed Phase31 Task4 fixture archive declares A as `7d1bb9e`, but its stored A HTML does not match a direct PHP-WASM render of that commit for the selected routes. Mysuru differs in text, title, headings, metadata, robots, links and JSON-LD; the article differs in text, headings and links. The old artifact remains unchanged. Task 3 uses the direct exact-commit A render so page content is not mixed between arms; details are in the fixture manifest.
- Restored pinned PHP-WASM 8.5.8, Playwright 1.58.2, Chromium 143.0.7499.0 and Lighthouse 12.8.2 outside Git. PHP smoke, Chromium/CDP preflight, fixture content guards, and the six route/arm smoke checks passed. No Task 3 performance sample has run and no source or still decision has been changed.

## 2026-11-06 checkpoint: Task 3 raw sample collection committed before analysis

- Completed the planned 63 fresh-browser Lighthouse samples: nine each for A, B-still and B-plain on both routes, plus nine additional A-repeat samples paired on Mysuru. All 63 samples recorded PASS, with no retry or resume. The raw file retains per-sample metrics, transfer records, render-blocking URLs, font/still requests, warnings and effective Lighthouse settings.
- Raw data is committed as `reports/phase-32c-hero-ab-raw.json`, 585,625 bytes, SHA-256 `039eb45d973b00844df525665d1ce6d6ebfb7a592c2db93dc0758aadd4e8351b`. Its metadata confirms all planned arm counts and `analysis_status: NOT_STARTED`.
- No medians, IQRs, paired ratios, noise-floor values or budget outcomes were computed before committing the raw file. The still/plain decision remains open. These are local simulated Lighthouse results only; PageSpeed Insights owner confirmation is still required.

## 2026-11-06 checkpoint: analysis method fixed before calculation

- Added `tools/phase32c/analyze-hero-ab.py` after the raw data commit. It verifies the committed raw hash, sample order/counts, browser and Lighthouse model, and fixture-manifest identity before calculating anything. It emits a separate machine-readable analysis and Markdown report.
- The analysis reports median/IQR per route and arm, all paired-round B/A LCP ratios and TBT deltas, the nine Mysuru A/A LCP/TBT/CLS/transfer differences, render-blocking URL sets, still requests and strict point-estimate gates. The conservative rule allows B-still only if all five hard budgets pass on both routes and transfer, LCP, TBT and CLS remain inside the maximum observed Mysuru A/A noise margin. Any failed or unresolved gate retains B-plain. The added noise check can only make owner limits stricter.
- At the time this method checkpoint was pushed, the analyzer had not yet run. The completed analysis and decision are recorded in the following checkpoint.

## 2026-11-06 checkpoint: Task 3 analysis complete

- `tools/phase32c/analyze-hero-ab.py` validated the committed raw SHA, sample schedule/counts, exact source commits, pinned Chromium version and Lighthouse mobile simulation settings, then generated `reports/phase-32c-hero-ab-analysis.json` and `.md`. The raw file was already pushed as `9ad242e` before any metrics were summarized.
- All five point-estimate gates passed for both B arms on both routes. B-still median added transfer was 13,420 bytes, with LCP ratios 1.0449 and 1.0452, median TBT increase 0ms, CLS 0.000 and no new render-blocking URLs. B-plain added 702 bytes, with LCP ratios 1.0003 and 0.9998, median TBT increase 0ms, CLS 0.000 and no new render-blocking URLs. Both arms stay strictly below 150,000 added bytes.
- The Mysuru A/A LCP noise floor is broad: median absolute difference 75.331ms, IQR 627.202ms, maximum 703.968ms; maximum absolute paired-ratio deviation from 1 is 0.4464. TBT and CLS A/A absolute differences are zero. One A/A pair also had a 98,454-byte transfer difference from an extra 200-status logo network entry. B-still fetched the 640px still in 9/9 samples per route at a 9,947-byte transfer each.
- Decision: retain B-plain for the selected Mysuru and article routes. This is an inconclusive, noise-based conservative choice, not a point-budget failure and not evidence that B-plain is a proven faster arm. All point gates pass, but B-still's noise-adjusted LCP upper ratios are 1.4913 and 1.4916, above 1.10. The decision does not change production source; destination and blog-index behavior was not measured by this two-route run.
- All 63 Lighthouse run warnings were zero. The browser request-failure listener recorded two events per sample: internal `chrome://terms/` `ERR_INVALID_URL` and a logo `ERR_ABORTED`; the logo is also present as a 200-status network-audit entry. These are retained diagnostics; no console or page-error assertion is made because those events were not collected.
- All numbers are local simulated Lighthouse data. PageSpeed Insights owner confirmation remains required. The Phase31 fixture A provenance mismatch is documented without changing the old fixture. No final full suite has run.

## 2026-11-06 checkpoint: final-suite runtime restored

- Restored the pinned Phase32c runtime outside the repository, including PHP-WASM CLI 3.1.50, Playwright 1.58.2, Chromium 143.0.7499.0, Lighthouse 12.8.2, axe-core 4.11.0 and sharp 0.34.5. Verified a single-file PHP-WASM lint, module imports, and a Chromium launch.
- This was setup only. No current 43-route render, browser matrix, axe scan, palette check or blank-space scan has run for the final suite. Task 4 remains pending, and no production source was changed.

## 2026-11-06 checkpoint: Task 4 final-suite harness ready

- Added `tools/phase32c/run-final-suite.py` with a one-run lock and serial PASS/FAIL groups, plus the Phase31b 43-route render comparator, one-Chromium-process-per-route axe runner for Home/Services/About/Contact, literal 44px rectangle audit, and Phase31 blank-space summarizer. The Phase31 scanner now records Contact `#miniHero` tail and scroll-cue measurements for every scanned state. These are test-only changes.
- Python and Node syntax checks, CLI help checks, and local browser/axe/sharp module preflights passed. No final-suite route render, browser case, axe scan, palette check, or blank-space scan has run.
- The stored Phase31 target map contains 5,670 measured main-content rectangles, of which 1,552 are below 44px by literal element bounds. The final audit will report those findings and any delta without inferring extra hit area or changing layout; baseline parity will not be called a full 44px pass.

## 2026-11-06 checkpoint: Contact-tail metric smoke validated

- Started the current PHP-WASM adapter on port 8094. Its single render capture contains all 43 routes at source head `749f138`; no final-suite checks have run yet.
- A one-case Contact 1280px scan smoke exposed that the first added flow-tail metric counted absolute HUD overlay text. That partial smoke is invalid and will not be used. The metric now excludes absolute/fixed descendants; a fresh one-case smoke measured a 792px hero, a 192px rounded flow tail (the focused inspector reports 192.34px), a 30px cue-to-hero-bottom gap, and a completed three-second settle with return to the top.
- The suite runner and comparator now permit only test-tool/report commits after this render capture and explicitly fail if any production runtime path changes. No PHP, assets, includes, content, or styling changed after the capture. The complete 516-case blank-space scan has not run.

## 2026-11-06 checkpoint: Task 4 final suite complete

- The one permitted final-suite run completed once at suite HEAD `62af0b2`, using the 43-route capture at `749f138`. It recorded all 16 groups and exited 1 after 4,467.1 seconds; 9 groups are marked FAIL. No suite group was repeated.
- PASS groups: PHP-WASM lint (100/100 files), sitemap exactness (38 URLs), static discovery/wording fixtures (10 commands), technical SEO/structured data, Phase20 inventory, fresh-process axe A/AA (zero new node identities on the four requested routes), and Git whitespace/CRLF checks.
- The route index lacks a per-route `sha256` field. The render-integrity group is marked FAIL, although all 43 adapter bodies match saved render bytes and statuses match Phase31b. The comparator reports exact parity for text, title, headings, links, images, picture sources and JSON-LD on all 43 routes; its runner status also failed on the same index-hash assumption.
- Rendered discovery and publication review failed because the existing scripts require native `php` for a local proof-data lookup. Palette checking passed its first case, then Chromium closed before case two. All 306 browser cases completed (258 normal and 48 reduced-motion), with no overflow or hidden-text assertion failure recorded. The final target-baseline size comparison failed after emitting 20 examples; its total was not recorded, and no matrix JSON was written. The separate 44px audit did not run. No current below-44px count is claimed.
- The 516-case blank-space scan completed with 1,147 pixel candidates, down 24 from 1,171; zero hidden reveal-text findings; and 16 intentional scroll-indicator dismissals. Four Contact `#miniHero` tails per width remain as previously documented. Four additional Home `#team` 1280px cases report a 202px tail candidate; it is unclassified, not confirmed removable space. No source or layout change was made.
- Results and group-level interpretations are recorded in `reports/phase-32c-final-suite-run-01.json` and `reports/phase-32c-final-suite-run-01.md`. The original suite report and raw case evidence remain in the external run directory. The adapter has been stopped.

## 2026-11-06 checkpoint: Task 4 PR update posted

- Pushed the one-shot suite report and progress update in commit `70710a4`.
- Posted the Task 4 checkpoint to existing PR #1: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1#issuecomment-6678504007. No merge or deployment was performed.

## 2026-11-06 checkpoint: Task 5 payload scope audited

- The current 131-entry manifest is pinned to Phase30 source `f54e4cc` and predates Phase32c runtime files. The current rendered reference pages add four Cormorant faces; the destination and blog-index templates use the 640px and 1440px still fallbacks. Place and article remain on the plain-palette path. The legacy 720px image path is not referenced by current PHP output and stays excluded. The eight deny-only `.htaccess` policies and temporary self-check remain in scope.
- Updated the temporary self-check's fixed hash table for the planned 137-file allowlist, preserving its existing critical-versus-existence-only checks. PHP-WASM parsed it and verified the missing-key 404, noindex and no-store behavior. No live request or deployment occurred.
- The source snapshot and ZIP have not yet been regenerated. The upload-relevant changed-file list since `796879d` will include the changed PHP/CSS/config/font/still files and the updated temporary checker; internal reports, tools and release artifacts remain excluded.

## 2026-11-06 checkpoint: Task 5 manifest regenerated

- Regenerated `reports/phase-27-payload-manifest.json` for source commit `065934a1ef2b0962308ce440ada959619e8824f2`. The exact allowlist has 137 files: the prior 131 entries plus four referenced Cormorant font faces and the 640px/1440px hero-still fallbacks used by the current destination and blog-index templates. Place and article remain on the plain-palette path. The legacy 720px image path remains excluded.
- The source snapshot has 6,217 tracked files; 6,080 are excluded from the 137-entry payload. All eight deny-only policies remain included. `reports/phase-32c-upload-scope.json` records the counts, six required additions, explicit exclusions and the 11 upload-relevant changed paths since `796879d`, including the refreshed temporary checker.
- Every allowlist row's size and SHA-256 was verified against its Git blob. The export folder and ZIP have not yet been created.

## 2026-11-06 checkpoint: clean payload, ZIP and route/asset parity verified

- Restored the pinned PHP-WASM adapter packages outside the repository and started isolated repository and clean-payload render adapters. Compared all 43 route responses: HTTP 200 in both, byte-identical bodies, zero mismatches. Compared 31 requested/local static asset URLs, including every local `/assets/` reference found in the 43 rendered bodies: zero mismatches. Sitemap, robots and both LLM endpoints were identical.
- Rechecked all 137 manifest entries against their source Git blobs, current checkout, clean extracted copy and ZIP; exact file sets, sizes and SHA-256 values match. ZIP CRC passed; no duplicates or unsafe paths. Payload runtime files are unchanged since source `065934a`.
- ZIP: `releases/ilmera-deploy-065934a.zip`, 137 files, 833,237 bytes, SHA-256 `3c56cdf481f639f98c689a26af517454576fae6d9ec9237c9e145eb38dfa8b57`. Raw branch URL: `https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-065934a.zip`.
- Payload folder counts are recorded in `reports/phase-32c-payload-parity.json`: root 46; CSS 1; fonts 16; images 9; blog 9; data 8; destinations 10; includes 18; places 18; reports 1; tools 1. Eight payload `.htaccess` policies are included; `releases/.htaccess` is excluded. No live site, native Apache, host headers or deployment was checked.
- The complete machine-readable evidence, including route and asset aggregate hashes and verification limits, is `reports/phase-32c-payload-parity.json`. The ZIP is not yet committed or pushed.

## 2026-11-06 checkpoint: Task 5 owner checklist and PDF updated

- Updated `reports/post-deploy-checklist.md` for the 137-file ZIP and source `065934a`. It now contains blank before/after PSI fields for LCP, TBT, CLS, score, transfer and render-blocking resources; the unchanged owner pass lines; explicit post-upload route and visual checks; exact folder/file counts; rollback steps; and the 11 changed upload paths since `796879d`.
- The checklist includes the current ZIP raw link, 833,237-byte size and SHA-256; records all 13 WOFF2 URLs; states that the Mysuru place and selected article remain on the plain-palette hero; and keeps owner/native-host acceptance open. No PSI values were invented.
- Regenerated the PDF once more after adding the 43-route inventory reference to the Markdown; extracted-text verification confirms both files now include the same route-list reference and package checksum.
- Regenerated `reports/post-deploy-checklist.pdf` offline from the Markdown with no external requests. Parsed the PDF: three A4 pages, valid EOF, and extracted text contains the PSI gates, ZIP checksum, counts, rollback and changed-path list. `tools/phase27/README.md` now describes the current three-page output instead of the stale page-count instruction. LF line endings are preserved.
- Task 5 is complete. The local package and browser checks do not certify Hostinger or live speed. No upload, merge or deployment occurred.
- Posted the Task 5 checkpoint to PR #1: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1#issuecomment-6684617953.

## 2026-11-06 checkpoint: Task 6 documentation completed

- Added the Phase32c disposition to `CHANGELOG.md`, including the four separate contrast fixes, reference safeguards, conservative local A/B choice, one-shot suite status and verified ZIP. Earlier changelog history is retained.
- Appended section 34 to `flagged-items-for-verification.md`. It points to the final report, records owner actions and keeps all prior verification items and blockers unchanged.
- Created `reports/phase-32c-release-report.md` with the historical contrast classifications, scene evidence, all arm medians/IQRs and paired LCP ratios, fixed budgets/noise floor, all 16 suite group statuses, exact remaining failures, payload/ZIP proof and owner follow-ups.
- Fast documentation checks: `git diff --check` passes; source files remain LF; new Task6 text contains no em dash or prohibited terminology; flagged-item diff is append-only. No suite or suite group was run again.

## Exact next step

Commit and push the Task6 documentation checkpoint, then post its summary to existing PR #1. Record the PR comment URL in this progress file and push that final progress checkpoint. Automated Phase32c work is then complete. Remaining work is owner-side PSI and native-host/contact checks only if the owner later chooses to proceed. Do not merge or deploy.
