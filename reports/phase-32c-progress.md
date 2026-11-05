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

## Exact next step

Rerun and save the complete 24-case matrix for `75f355f` with the universal WebGL signal, then run the same matrix at `796879d`, literal first post-baseline commit `d0b7726`, first source-behavior commit `2722901`, reference-scene defer commit `d4b376e`, and current `f9c96ca` as needed. Compare the four nodes' computed foregrounds, screenshot-sampled effective backdrops and ratios across history before assigning classifications or changing styles.
