# Phase32 progress log

## 2026-10-29 checkpoint 1: Phase31 prerequisite gate blocks Phase32

- Fetched `origin/arena/48320ee5-ilmerastudyabroad`. The workspace was clean and its local branch was behind the remote; it now matches the remote at `dd7950885a80992fbae5d6bc7d83710902136515`. No branch was created or switched.
- Read `reports/phase-31-task4-ab-summary.md`, `reports/phase-31-progress.md`, the Task2 and Task3 check reports, the Phase31-related reports, and the recent git history. The Phase31 progress log ends at checkpoint 15 and says Tasks5-7 remain active. No `reports/phase-31-release-report.*` or Phase31 payload/ZIP verification report was found.
- The blank-space fixes are complete: Task2 source commit `7d1bb9e`; the required after-scan and verification are recorded in the Phase31 progress log and Task2 reports.
- The authorized hero stills are complete: Task3 source commit `806769a`; scope, visual, resource and verification evidence are recorded in the Task3 reports.
- Task4's single local A/B session is complete and documented. It has 112 samples; only 2 of 8 routes pass all local budgets, and the report explicitly does not certify release performance.
- The ZIP prerequisite is not complete for the current Phase31 branch. The only existing ZIPs are `releases/ilmera-deploy-850d0af.zip` and `releases/ilmera-deploy-f54e4cc.zip`. Their source commits date to 2026-10-24 and 2026-10-26; the latest ZIP build commit is `7d59c62`, identified in git history as a Phase30 export. Neither package reflects current Phase31 HEAD `dd79508`, and no Phase31 payload completeness or per-file hash evidence is present.
- **Gate result: BLOCKED. Phase32 implementation has not started.** In accordance with the request, no Phase32 speed edits, audits, benchmarks, image/font changes, deployment package, documentation changes outside this checkpoint, or release actions were attempted. No files were deployed or merged.
- Resume Phase32 only after the remaining Phase31 release/payload work is complete and a current-HEAD ZIP plus its completeness and hash verification are committed on this same session branch. Then fetch and match the branch again before beginning Phase32 work.

## 2026-10-29 checkpoint 2: preflight stop due unresolved Task4 route-budget failures

- Fetched `origin/arena/48320ee5-ilmerastudyabroad` and fast-forwarded the existing session branch from the stale local checkout to remote commit `796879d7b3d5ca0fa1e398562e937e9f364a5f62`. The branch now matches the remote; no branch was created or switched.
- Read `reports/phase-31-task4-ab-summary.md`, `reports/phase-31-release-check.md` and the recent git log. The Phase31 release-check report exists and its Task5 verification passed (31/31 groups), but it also explicitly reports `Task4 per-route local A/B budget: FAIL, carried to Phase32`, only 2/8 routes within all local budgets, and `performance_release_certified=false`.
- The current resume note says to stop if the Phase31 release-check report shows an unresolved failure. The six local route-budget failures are still unresolved, so this stop condition is met. The separate Phase31 verification pass does not clear that failed route-budget gate.
- The newer instruction that Phase31 intentionally skipped the ZIP supersedes checkpoint 1's older ZIP prerequisite. No ZIP was attempted. No Phase32 source edit, scene/font/image change, benchmark, audit, contact sheet, payload build or release action was attempted after the preflight gate triggered. No public source changed.
- **Gate result: STOPPED before Phase32 implementation**, as required by the resume note. No Task4 samples were rerun. This checkpoint records the gate only; prior blockers and evidence remain unchanged.


## 2026-10-29 checkpoint 3: corrected resume gate passed

- Fetched `origin/arena/48320ee5-ilmerastudyabroad`; the working tree was clean and the existing session branch matched remote at `d0b7726061abf77855465021ac4745e729eebfac`. No branch was created or switched.
- Read `reports/phase-31-task4-ab-summary.md`, `reports/phase-31-release-check.md`, this progress log and the recent git history. The release-check exists and reports Task5 PASS (31/31 groups). Its Task4 result remains the known failure Phase32 is intended to fix (2/8 local routes pass, `performance_release_certified=false`); the corrected resume note explicitly authorizes proceeding despite that result.
- Verified the session branch contains the Phase31 public source changes relative to `75f355f`: `about.php`, `index.php` and `includes/visual-system.php` are modified. Phase31's final source check and all Task5 groups passed in the release report. The stop conditions in the corrected gate are not met.
- **Gate result: CLEARED.** Continue Phase32 on this branch. The prior checkpoints document historical gate decisions; this checkpoint supersedes their stop disposition. No Phase32 implementation or benchmark was repeated during this preflight.


## 2026-10-29 checkpoint 4: local test runtime prepared

- Installed the pinned browser, Lighthouse, PHP-WASM, image, font and test packages under `/home/user/phase32-runtime`, outside the repository. No production dependency or runtime package was added to the site.
- Runtime is Node `v22.22.3` / npm `10.9.8`; PHP-WASM packages printed engine-range warnings requesting Node 24 and npm 11, as in earlier phase evidence. Execution compatibility has not yet been validated in this runtime.
- This setup checkpoint changes no site behavior and does not replace or repeat Phase31 measurements.


## 2026-10-29 checkpoint 5: pre-Phase32 route baseline frozen

- Verified the public runtime files at the working tree still match Phase31 final commit `796879d`; the intervening commits change only progress documentation.
- Captured all 43 rendered routes at HTTP 200 and the exact 38-entry sitemap from the isolated PHP-WASM adapter before Phase32 source edits. Stored the compressed render baseline, route hashes/index and sitemap in `reports/phase-32-before-renders.json.gz`, `reports/phase-32-before-render-index.json` and `reports/phase-32-before-sitemap.xml`.
- The render archive is 894,404 bytes. It is an immutable local pre-Phase32 comparison baseline, not live-host evidence.


## 2026-10-29 checkpoint 6: smaller mobile still encoded

- Re-encoded the approved mobile still as 640x800 WebP at quality 64. The result is 9,738 bytes, below the 14,000-byte limit. The existing desktop WebP is 1440x900 and 37,226 bytes, below the 40,000-byte limit; it is reused unchanged.
- Committed the reproducible encoder, mobile asset and hash/size record.

## 2026-10-29 checkpoint 7: delayed hero still rendering and fallback QA passed

- Replaced the eager still background on destination, place, article and blog-index heroes with a reserved canvas. The still is requested only after window load plus idle, with the 1,500ms fallback. It uses responsive 640/1440 WebP, cover-crop drawing, and skips for Save-Data, slow connection hints or `ILMERA_SCENES_ENABLED=false`. Reduced motion retains the still without a fade. The plain palette remains the fallback on an image failure or disabled switch.
- The revised 12-case Chromium smoke passed all four templates at 360px, 768px and 1280px. Every request began after `loadEventEnd`, the expected asset was selected, and the recorded LCP candidate was text (`P`, `H1` or `H2`), not a still image or canvas. Save-Data and slow-connection each produced zero still requests; reduced motion had zero transition duration.
- JavaScript-off fallback passed at 360px and 1280px. A PHP-WASM policy test passed all four template groups with `ILMERA_SCENES_ENABLED=false`: the animated scene script, still canvas, still asset URLs and loader are absent while headings remain.
- Visually reviewed the post-crop screenshots for the four templates at all three widths. A browser-pixel text mask measured 57 runs. The initial 0.56 canvas opacity failed at 3.654:1 on an article breadcrumb at 1280px; opacity was lowered to 0.42 without wording changes. The updated pass minimum is 5.339:1. See `reports/phase-32-hero-smoke.json`, `reports/phase-32-noscript-smoke.json`, `reports/phase-32-scene-switch-smoke.json`, `reports/phase-32-hero-contrast.json` and `reports/phase-32-hero-assets.json`.
- The local browser interceptor exposes `ResourceTiming.transferSize=0`; it is not used as byte evidence. The asset hashes/sizes meet their existing limits, but this local smoke does not establish compressed transfer on the target host or prove the LCP/CLS/TBT budgets.
- Next: complete the reference-page/resource and font-chain investigations, then perform the frozen-A seven-sample interleaved lab only after test harness and serving policy are validated. Continue to preserve the immutable 43-route/38-URL baseline and do not repeat Phase31 Task4.

## 2026-10-29 checkpoint 8: font chain diagnosed, candidate rejected

- Audited place, article and blog at 360px and 1280px. Each uses seven self-hosted webfont faces with `font-display:block`, two local metric fallbacks, two head preloads (Outfit 300 and Cormorant Garamond 700), and a body-visibility gate until fonts are ready or the 3,000ms fail-open timer. No external visual-system stylesheet is requested. Actual local font response bodies were 72,784 bytes at 360px (four faces) and 86,816 bytes at 1280px (five faces).
- Ran one isolated, serial 42-sample font A/B: seven samples per arm on each of the three templates, fresh Chromium per sample, alternating A/B order. B changed only `font-display:block` to `swap` and removed the font-pending visibility rule. CLS medians remained zero, but B did not improve LCP consistently. Place and blog medians were higher; article improved by only 0.45ms. Broad IQRs on two B routes limit interpretation. No source font change was adopted.
- Results and transform proof are in `reports/phase-32-font-audit.json`, `reports/phase-32-font-ab-results.json` and `reports/phase-32-font-ab-summary.md`; the conservative decision is recorded in `flagged-items-for-verification.md`.
- Next: audit reference resources and implement a guarded scene loader for Home, Services, About and Contact, keeping static content and fallback intact. Preserve Contact `#miniHero` and its previously documented 138px mobile and 233px tablet tails. Then run the full frozen-A eleven-route lab after source changes are complete.

## 2026-10-29 checkpoint 9: reference resource audit identifies deferred bundle

- Audited Home, Services, About and Contact at 360px and 1280px with local response-body sizes, browser resource timing, LCP/CLS/long-task observers, image dimensions, and V8 JavaScript/CSS coverage.
- The three eagerly requested scene libraries total 717,632 bytes per reference page: Three.js 603,445, GSAP 71,520 and ScrollTrigger 42,667. Full response bodies were 1,034,492 to 1,105,818 bytes. Excluding those three dependencies, the ordinary page payload was 316,860 to 388,186 bytes, numerically below the 400,000-byte reference limit in all eight cases; Services at 1280px has only 11,814 bytes of local headroom. These are uncompressed local response bodies, not Hostinger transfer figures.
- The only image response was the existing logo PNG at 98,340 bytes, displayed around 38px; it is left unchanged to preserve the image. V8 block-coverage estimates show 458,022 to 469,027 unused JavaScript source bytes and 8,017 to 12,179 unused CSS source bytes for a single path. These are diagnostic coverage estimates, not Lighthouse wasted-transfer bytes.
- Raw unthrottled local browser LCP was 36ms to 468ms, with one or two long tasks per case and a longest task of 662ms. These numbers are not comparable to Lighthouse simulated budgets. The complete resource and coverage evidence is in `reports/phase-32-reference-audit-before.json` and its readable summary in `reports/phase-32-reference-audit-before.md`.
- Contact `#miniHero` remains unchanged. Preserve its existing 138px 360px and 233px 768px bottom scroll-cue tails. The reference-page code change will defer only the existing scene libraries on approved desktop conditions and will keep static fallback layers and reserved canvas geometry for excluded users. No new image will be added to these pages because Services has little headroom under the pre-scene cap.

## 2026-10-29 checkpoint 10: guarded reference scene deferral implemented and measured

- Added output-buffer deferral for Home, Services, About and Contact only. The original Three.js scene is initialized once after eligible desktop scripts load. The original scripts are no longer in the eager markup. Scene libraries are added sequentially after `window.load` plus `requestIdleCallback`, with the 1,500ms timeout fallback. The loader excludes widths below 900px, coarse pointers, reduced motion, Save-Data, 2G and downlink below 1.1 Mbps. Excluded users retain the full-viewport canvas geometry and static CSS background layers; no image was added to the reference pages.
- Preserved page-scope W/H dimensions required by the About and Contact HUD loops. `ILMERA_SCENES_ENABLED=false` removes all three heavy reference dependencies and keeps the plain palette; on the other template groups, the prior flag behavior is retained so GSAP reveal scripts remain available. PHP-WASM output-policy fixtures pass all eight routes.
- The 36-case Chromium smoke passes for all four reference pages: 28 excluded-device cases made no scene-library requests; the four idle-callback desktop runs and four forced 1,500ms fallback runs each initialized the existing scene once without page errors. First idle-start request was 3ms to 476ms after load. With `requestIdleCallback` disabled, the first request began at 1,501ms on every route. Evidence: `reports/phase-32-reference-scene-smoke.json`, `reports/phase-32-reference-scene-policy-smoke.json` and `reports/phase-32-scene-switch-smoke.json`.
- Post-change local response-body totals are 318,871 to 376,165 bytes at 360px and 1,047,959 to 1,107,829 bytes at 1280px after eligible desktop scenes load. The non-scene body sums are 318,871 to 390,197 bytes, all numerically under 400,000; Services at 1280px has 9,803 bytes of headroom. These are uncompressed local response bodies. The injected HTML added 1,970 to 2,011 bytes, with no new external resource. Full post-change resource details are in `reports/phase-32-reference-audit-after.json` and `reports/phase-32-reference-audit-after.md`.
- The audit's raw unthrottled LCP values are not Lighthouse LCP. Observer CLS sums are under 0.1 in these eight cases, but do not establish the unchanged no-worse-than-baseline gate. The coverage-enabled long-task TBT proxy is 866ms on Services desktop, 2,963ms on About desktop and 3,902ms on Contact desktop. Separate one-sample, no-coverage diagnostics observed about 1,827ms on About and 3,682ms on Contact during scene startup. These are red flags, not Lighthouse TBT. **Do not claim reference TBT or the owner budgets pass.** The full frozen-A, seven-sample, interleaved 11-route Lighthouse lab remains required and may require another conservative scene policy change.
- Contact `#miniHero` remains untouched at the retained 138px mobile and 233px tablet tails. The audit's only image remains the 98,340-byte logo; no image optimization or wording change was made.

## 2026-10-29 checkpoint 11: frozen 11-route lab protocol prepared

- Selected 11 unique routes for the final frozen-A comparison: the four reference controls, Germany and Italy destination pages, Mysuru and Bengaluru place pages, the how-to-choose and cost articles, and the blog index. The Mysuru, how-to-choose and blog-index routes are the pages used in the font-chain diagnosis.
- The candidate A arm is the immutable `796879d7b3d5ca0fa1e398562e937e9f364a5f62` render archive, verified against its SHA-256 index and 43-route inventory. B will be captured from the current committed HEAD after this harness checkpoint. The fixture tool checks each selected HTML byte count and SHA-256 before creating the paired fixture.
- Added a serial seven-round runner: A/B then B/A alternating by round, seven fresh Chromium processes per arm per route, no retries or resume, Lighthouse mobile simulated Slow4G and 4x CPU. It records per-sample LCP, CLS, TBT, transfer, request count, render-blocking URLs, fonts, still requests, warnings and control reliability. Budgets are unchanged; release certification remains false.
- The actual B render capture and Lighthouse experiment have not run yet at this checkpoint. The raw lab remains pending and no outcome is claimed. The local fixture host binds to loopback and serves only the paired fixture plus tracked assets.
