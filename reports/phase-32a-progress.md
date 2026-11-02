# Phase32a progress

- **Current branch:** `arena/48320ee5-ilmerastudyabroad`
- **Remote match:** fetched and matched the existing session branch on 2026-11-02, fast-forwarding the local branch to the remote tip before work. The initial scope/gate checkpoint is now pushed. No branch switch or new branch.
- **Scope:** Destination, place, article and Blog-index hero stills and font request-chain diagnosis. No ZIP. No new changes to Home, Services, About or Contact. Those four may be used only as the requested controls; the existing pushed Phase32 reference changes are not repeated or expanded here.

## Gate and prior evidence

- `reports/phase-31-release-check.md` exists and records Task5 verification PASS, 31/31 groups. The branch contains the Phase31 source baseline and later work. Gate passed.
- `reports/phase-31-task4-ab-summary.md` records frozen A `7d1bb9e`, B `806769a`, 112 samples, 2/8 routes passing the unchanged budgets. Known target LCP-ratio failures: Germany 1.2233, the chosen article 1.1366 and Blog index 1.1362. This is local simulated evidence and the reason for Phase32a, not a stop condition.
- Previously pushed Phase32 Task1 assets and safeguards already meet the requested file-size and contrast limits: mobile `assets/images/hero-still-640.webp`, 640x800, 9,738 bytes; desktop `assets/images/hero-still-1440.webp`, 1440x900, 37,226 bytes. Existing `phase-32-hero-assets.json`, `phase-32-hero-smoke.json` and `phase-32-hero-contrast.json` record 360/768/1280 review, post-load loading, text LCP, no-JS, Save-Data/slow-connection and scene-switch fallback checks, and minimum contrast 5.339:1. These pushed results will not be regenerated unchanged.
- The existing Phase32 font-chain audit and candidate experiment are already committed. The only tested font-display candidate did not produce a coherent LCP gain without worse CLS: Mysuru B/A 1.3639, article 0.9997 (0.45ms difference), Blog index 1.3640. Existing decision is no font change. Do not repeat that experiment unchanged.
- Frozen Phase32 run02 used a different A (`796879d`) and 11 routes; it is not a substitute for the newly requested six-route Task2 run against A `7d1bb9e`. Its three LCP misses remain in the existing report and are not erased.

## Completed this checkpoint

- Fetched the existing session branch and fast-forwarded the local branch to the exact remote tip `a4ca343`. No branch switch, new branch, PR, merge or deployment.
- Read the required Task4 summary, Phase31 release-check, Phase32 progress and branch history. Confirmed the gate above.
- Confirmed the previous pinned runtime directory `/home/user/phase32-runtime` is absent in this workspace, and native PHP is unavailable. The frozen Task4 fixture archive is present and hashes to `806e5ab8df048c1bda227211a57a67fe8331b6121a045eccc43c8c5629d2f1d6`.
- Restored a temporary audit runtime outside Git: Node 22.22.3, PHP-WASM 8.5.8 CLI, @php-wasm 3.1.50, Chromium 143.0.7499.0, Playwright 1.58.2 and Lighthouse 12.8.2.
- The current pushed B adapter rendered all 43 routes at HTTP 200. All six targeted routes also returned 200. PHP-WASM lint passed for the shared visual system/config and Germany, Mysuru, chosen article and Blog-index entry files. The B render index was captured at `b0dc265`; runtime files are unchanged from the previously pushed candidate at `4e709ed`.
- No runtime code changed in this checkpoint. No ZIP will be built.
- The initial Phase32a scope/gate checkpoint and appended blocker note were pushed as commit `6ff7535`.

## 2026-11-02 checkpoint: six-route fixture frozen

- Combined the frozen Task4 A HTML at `7d1bb9e` with current B renders captured at `b0dc265`; runtime files still match the current branch. The six-route fixture hash is `31acc1582b723779b65a9c9f388f7fc4b864e197b3e2b5de21609842553a0aea`, stored externally at `/home/user/phase32a-runtime/phase32a-ab-run01/fixtures.json`.
- Fast checks passed: PHP-WASM lint, all 43 current B route renders HTTP 200, six selected B routes HTTP 200, and six-route content comparison with zero failures for text/order, title, headings, meta, robots, canonical, link semantics/order, images/picture sources and JSON-LD. Text, anchor and image counts match A on all six.
- Services and Contact HTML differ from Task4 A due already-pushed shared Phase32 presentation work. They remain requested measurement controls, not byte-identical no-op controls. Phase32a has made no reference-page source change.
- Fixture manifest and human summary: `reports/phase-32a-six-route-fixtures.json` and `.md`. No Lighthouse sample has started yet.

## 2026-11-02 checkpoint: raw-only measurement runner prepared

- Added `tools/phase32a/ab-runner.cjs`; syntax and pinned Node package loads pass. It validates all twelve frozen A/B route bodies before launch and can run a no-sample Chromium preflight.
- The run records 84 raw Lighthouse samples only, serially, with fresh Chromium per sample, seven samples per arm per route, alternating order, no retry/resume. It retains absolute metrics, network/request, blocking, still/font timing details and warnings. It does not compute medians, IQRs, ratios or budget outcomes.
- Raw destination: `reports/phase-32a-6-route-ab-run-01-raw.json`. Analysis must not begin until that complete raw file is committed and pushed.

## 2026-11-02 checkpoint: fixture and Chromium preflight passed

- Started the isolated six-route fixture host on `127.0.0.1:8092` from the frozen external fixture.
- `ab-runner.cjs --preflight-only` passed: all 12 A/B route responses exactly match the frozen fixture bodies, and the pinned Chromium 143.0.7499.0 launches and connects. Zero Lighthouse samples were collected.

## 2026-11-02 checkpoint: six-route A/B raw run complete

- Completed exactly 84/84 Lighthouse samples: six routes, seven samples per arm per route, alternating A/B order, a fresh Chromium 143.0.7499.0 process per sample, serial, zero retries/resumes. All samples passed. This is a local simulated mobile lab run only, not field data.
- Raw JSON: `reports/phase-32a-6-route-ab-run-01-raw.json`, 352,597 bytes, SHA-256 `73884a1e3b306dfb9ae5323c23eee22173cc466c32af396eae05ac4e89099875`. Structural validation, six affected-file PHP-WASM lints, six route HTTP checks, and the six-route content invariants passed.
- No medians, IQRs, ratios or budget outcomes have been calculated. Raw data must be pushed first.

## 2026-11-02 checkpoint: raw A/B analysis complete

- Analysis is now recorded in `reports/phase-32a-6-route-ab-run-01-summary.md` and `.json`; the committed raw SHA-256 is unchanged. All values are local simulated mobile Lighthouse results, not field data.
- Germany passed all median-based budgets: LCP B/A 1.0092, TBT +46 ms, CLS unchanged, transfer +13,278 bytes, no new blocking URL. Blog index passed: LCP B/A 1.0001, TBT unchanged, CLS unchanged, transfer +3,473 bytes, no new blocking URL. Its existing mobile guard skipped the still at <=768px.
- Mysuru failed TBT (+66.24 ms, over +50 ms) and the choosing-consultant article failed LCP (B/A 1.4243) and TBT (+59 ms). Both require the approved plain-palette hero fallback. CLS and transfer budgets passed on all four targets.
- Services and Contact are not byte-identical controls and the symmetric median-LCP control gate failed; this is recorded as a limitation, not a request to change those pages. `performance_release_certified=false` stays unchanged.
- No font-chain decision or source change has been made yet.

## 2026-11-02 checkpoint: measured palette fallback applied

- Added `place` and `article` to `ILMERA_VISUAL_PLAIN_HERO_TEMPLATES` in `includes/visual-config.php`, using the existing palette fallback. `ILMERA_SCENES_ENABLED` remains the site-wide switch and stays enabled by default. Germany (`destination`) and Blog index (`blog`) still use the approved loader; no reference page changed.
- Fast lint passed for shared files, route entries and affected data files. PHP-WASM rendered Mysuru and the choosing-consultant article HTTP 200. Both now contain no hero still canvas, still URL, delayed `Image` loader or noscript still. Protected text/order, title, headings, metadata, canonical, links, images and JSON-LD remain invariant against frozen A. Details: `reports/phase-32a-palette-fallback-check.md`.

## 2026-11-02 checkpoint: font chain diagnosed

- Current font chain is unchanged by the fallback: one inline visual-system stylesheet, no external stylesheet response, no Google Fonts request, seven self-hosted `font-display:block` faces and two local metric fallbacks. The head preloads Outfit 300 and Cormorant Garamond 700; the font gate hides `body.p25` until `document.fonts.ready` or 3,000ms.
- Reused the matching-source six-case Resource Timing evidence in `reports/phase-32-font-audit.json` rather than repeating an unchanged check. New report: `reports/phase-32a-font-chain-diagnosis.md`. Fresh Task2 raw samples confirm four local face requests per arm/sample on Mysuru, article and Blog index, all HTTP 200.
- No font change has been made. The earlier candidate had no coherent gain and is not treated as the fresh experiment required here.

## Exact next step

Build the current post-fallback font candidate fixture for Mysuru and the choosing-consultant article. Candidate changes only `font-display:block` to `swap` and removes the body-visibility gate, preserving font families, files, weights, preloads, markup and content. Run a fresh interleaved local Lighthouse A/B with seven samples per arm per route, fresh Chromium per sample, alternating order, no retries. Save and push the 28 raw samples before analysis; adopt no font change unless LCP improves on both routes and CLS is no worse.

## Remaining sequence

1. Run the fresh Mysuru/article font candidate experiment and report the no-change/change decision against the required rule.
2. Complete the all-43-route rendered text/link/image/JSON-LD comparison against the pre-phase render.
3. Run the specified full suite exactly once at the end: lint, renders, 258 browser cases, discovery, strict wording, sitemap, palette, structured data, axe on one page per template and 360/768/1280 overflow.
4. Update `CHANGELOG.md`, append flags without rewriting old blockers, and create `reports/phase-32a-release-check.md` with each check, lab table, palette fallback and every changed file since `796879d`. Push the final checkpoint and PR #1 comment; do not merge or deploy.
