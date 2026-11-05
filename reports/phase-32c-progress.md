# Phase32c progress

- **Date:** 2026-11-05
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
- These are harness smoke checks only. The requested 60-case visual comparison has not yet run, and no final suite has run.

## Exact next step

Run the complete Task 2 matrix: Home, Services, About and Contact at 360, 768 and 1280px in scene, still, reduced-motion, disabled-scene-switch and JavaScript-off states. Review all 60 cases, identify and report every 0.1px geometry or content difference, summarize header/footer/team cards/text/links/schema parity, identify which Phase32 changes reached the reference pages and state which Task 3 items were not applied. Then commit, push and post the Task 2 checkpoint. Do not run the final full suite until Tasks 1-3 are complete.
