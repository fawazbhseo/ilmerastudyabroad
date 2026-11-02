# Phase32a-2 release verification and speed result

- **Date:** 2026-11-02
- **Branch:** `arena/48320ee5-ilmerastudyabroad`
- **Pre-phase baseline:** `796879d7b3d5ca0fa1e398562e937e9f364a5f62`
- **Original full-suite source HEAD:** `2ee711c2cc52c30a0f8d8aff2ae86ad2e03f39e4`
- **Final recomputed result:** 23/24 PASS, 1 FAIL
- **Release status:** Not certified. `performance_release_certified=false` remains unchanged.

## Summary and scope

The original serial full suite ran once and recorded 20 PASS and 4 FAIL. The four failed groups were then rerun individually, without rerunning the full suite: rendered discovery PASS, rendered publication wording PASS, isolated palette PASS, and axe A/AA remains FAIL baseline-relative because four new contrast findings were observed on unchanged Home/About reference controls. The other 20 groups retain their original PASS results. The saved 24-group summary was recomputed without `KeyError`; final status is 23 PASS and 1 FAIL.

The public Phase32a change remains only the measured `place` and `article` plain-palette fallback in `includes/visual-config.php`. `ILMERA_SCENES_ENABLED` remains enabled and site-wide. No Phase32a wording, headings, links, FAQs, schema, canonicals, statuses, protected images, Home, Services, About or Contact page source was changed. No site source was changed to address the four new axe findings because their source nodes and styles are outside the Phase32a change.

The all-43-route rendered-content comparison against the frozen pre-phase render passed: 43/43 HTTP 200, zero protected invariant failures, and an exact byte-identical sitemap with 38 unique URLs. Details remain in `reports/phase-32a-43-route-content-comparison.md` and `.json`.

## Fixed budgets and speed-data provenance

The budgets remain unchanged:

| Budget | Gate |
|---|---|
| Added transfer | Strictly below 150,000 bytes |
| Median LCP | B/A no more than 1.10 |
| Median TBT | Increase no more than 50 ms |
| Median CLS | No worse than A and below 0.1 |
| Render-blocking resources | No new render-blocking URL |

The existing Phase32a six-route A/B contains 84 valid local simulated mobile Lighthouse samples: seven interleaved samples per arm for each of four treatment routes and two measurement controls, with fresh Chromium per sample, Lighthouse 12.8.2 / Playwright 1.58.2 and zero warnings. IQR is Q3 minus Q1 with linear interpolation at `(n - 1) * p`. Home and About were axe reference controls only, not performance routes; there are no raw Phase32a performance medians or IQRs for those two pages. The only performance controls in the six-route capture are Services and Contact.

**Important B-arm limit:** the frozen A source is `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`; the measured B render source is `b0dc2652c281720027e3d44ae0da6471a1b2c8fb`, before the later `place`/`article` plain-palette fallback. The raw data therefore describes the frozen pre-fallback candidate B, not a measured post-fallback B. No post-fallback A/B metrics or IQRs exist for Mysuru or the selected article; none are inferred here. The table is the complete available raw A/B evidence, not a speed claim for the post-fallback pages.

### Frozen A and measured B medians / IQRs

| Route / role | LCP A median (IQR) -> B median (IQR), ms | LCP B/A arm medians; paired median / IQR | TBT A median (IQR) -> B median (IQR), ms | CLS A median (IQR) -> B median (IQR) | Transfer A median (IQR) -> B median (IQR), bytes; B/A |
|---|---:|---:|---:|---:|---:|
| `/study-in-germany` (target) | 1198.67 (55.65) -> 1209.70 (630.63) | 1.0092 ; 1.0001 / 0.0634 | 0.00 (5.00) -> 46.00 (76.00) | 0.000000 (0.000000) -> 0.000000 (0.000000) | 199,593 (0) -> 212,871 (0) ; 1.0665 |
| `/study-abroad-counselling-mysuru` (target) | 1652.33 (0.45) -> 1728.17 (314.39) | 1.0459 ; 1.0456 / 0.1905 | 0.00 (0.00) -> 66.24 (121.96) | 0.000000 (0.000000) -> 0.000000 (0.000000) | 233,190 (0) -> 246,577 (0) ; 1.0574 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` (target) | 1654.08 (628.03) -> 2355.84 (628.15) | 1.4243 ; 1.0451 / 0.2020 | 0.00 (15.91) -> 59.00 (59.27) | 0.000000 (0.000000) -> 0.000000 (0.000000) | 241,106 (0) -> 254,493 (0) ; 1.0555 |
| `/blog/` (target) | 2280.94 (627.92) -> 2281.15 (314.78) | 1.0001 ; 1.0002 / 0.5178 | 0.00 (0.00) -> 0.00 (33.00) | 0.000000 (0.000000) -> 0.000000 (0.000000) | 232,501 (0) -> 235,974 (0) ; 1.0149 |
| `/services` (control) | 8406.54 (7382.41) -> 2956.10 (238.88) | 0.3516 ; 0.3516 / 1.0615 | 2400.00 (913.50) -> 0.00 (0.00) | 0.000000 (0.000000) -> 0.000491 (0.000747) | 941,152 (0) -> 376,606 (0) ; 0.4002 |
| `/contact` (control) | 11358.83 (5569.31) -> 2730.69 (401.92) | 0.2404 ; 0.2404 / 0.5356 | 5166.00 (1058.50) -> 0.00 (0.00) | 0.000000 (0.000000) -> 0.000000 (0.000000) | 907,681 (0) -> 333,499 (0) ; 0.3674 |

### B/A ratios, unchanged budget outcome and palette decisions

| Route | LCP B/A (arm medians; paired median / IQR) | TBT B/A medians | CLS B/A medians | Transfer B/A medians | Budget / control result | Configured hero |
|---|---:|---:|---:|---:|---|---|
| `/study-in-germany` | 1.0092; paired 1.0001 / 0.0634 | n/a (A median 0) | n/a (A median 0) | 1.0665 | all target budgets PASS | retained still |
| `/study-abroad-counselling-mysuru` | 1.0459; paired 1.0456 / 0.1905 | n/a (A median 0) | n/a (A median 0) | 1.0574 | TBT +66.24 ms > 50 ms | plain palette |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1.4243; paired 1.0451 / 0.2020 | n/a (A median 0) | n/a (A median 0) | 1.0555 | LCP 1.4243 > 1.10; TBT +59.00 ms > 50 ms | plain palette |
| `/blog/` | 1.0001; paired 1.0002 / 0.5178 | n/a (A median 0) | n/a (A median 0) | 1.0149 | all target budgets PASS | retained still |
| `/services` | 0.3516; paired 0.3516 / 1.0615 | 0.0000 | n/a (A median 0) | 0.4002 | CONTROL ONLY; symmetric LCP gate FAIL (ratio 2.8438); control CLS observation FAIL | control |
| `/contact` | 0.2404; paired 0.2404 / 0.5356 | 0.0000 | n/a (A median 0) | 0.3674 | CONTROL ONLY; symmetric LCP gate FAIL (ratio 4.1597) | control |

The LCP budget uses the ratio of the A and B arm medians; the paired median/IQR is the separate round-matched ratio distribution. They can differ substantially on noisy routes, as for the article, and do not replace the recorded arm-median budget result. TBT and CLS B/A are undefined where A's median is zero. The later fallback changes only place/article, so the other four routes in the speed table are unchanged by it.

Transfer additions on all four treatment routes passed the unchanged 150,000-byte gate, and the A/B summary recorded no new render-blocking URL on any of the six routes. Germany and Blog index passed all target budgets. Mysuru passed LCP, CLS, transfer and blocking but failed TBT by 16.24 ms. The article failed both LCP and TBT. The templates using the plain-palette fallback are **place** and **article**.

The interleaved control gate remains **FAIL as recorded**. Services has B/A median LCP 0.3516 and symmetric ratio 2.8438; Contact has 0.2404 and symmetric ratio 4.1597. They are not byte-identical controls because of earlier shared Phase32 presentation changes, so these control deltas are not a reliable no-op adjustment or release signal. Keep the controls unchanged and do not use them to relax or reinterpret any target budget.

### Final retained hero still sizes

| Asset | Dimensions | Size | Recorded limit |
|---|---:|---:|---:|
| Mobile `assets/images/hero-still-640.webp` | 640 x 800 | 9,738 bytes / 9.738 KB | 14,000 bytes |
| Desktop `assets/images/hero-still-1440.webp` | 1440 x 900 | 37,226 bytes / 37.226 KB | 40,000 bytes |

## Font finding

The place, article and Blog-index request chain has one inline visual-system style block, no external or Google Fonts stylesheet/request, seven declared self-hosted WOFF2 faces but four local font requests per A/B sample, and preloads only Outfit 300 and Cormorant Garamond 700; all faces use `font-display:block`, while `body.p25` stays hidden until `document.fonts.ready` or the 3-second fail-open, so the gate can delay visible text and contribute to slower starts. The fresh 28-sample `swap`/gate-removal A/B lowered Mysuru median LCP by 0.03 ms but raised the article median by 1.66 ms, with zero median CLS on both, so the two-route improvement rule failed and the font setup was left unchanged.

## Targeted reruns of the four original failures

### Rendered discovery and publication wording: PASS

The original checks failed because the helper invoked a native `php` executable that was not installed. The pinned PHP-WASM CLI 8.5.8 from `@php-wasm/cli` 3.1.50 was reinstalled outside the repository and exposed as an external `php` shim. The prior `tools/phase31/server.cjs` PHP-WASM adapter was restarted on port 8094 from the unchanged site runtime source. Both checks passed with one attempt each:

- Discovery: 43 routes, 38 indexable and 5 blocked; statuses, canonicals, robots, sitemap coverage, inbound links, internal targets, fragments and served LLM directory parity passed.
- Publication wording review: 42 editorial self-canonicals and all 43 route status/robots, JSON-LD, Service contact, punctuation, approved-source, LLM policy/served-parity and sitemap checks passed.

Full stdout logs are external at `/home/user/phase32a-runtime/phase32a-2/rendered-discovery-rerun.log` and `/home/user/phase32a-runtime/phase32a-2/rendered-publication-wording-rerun.log`.

### Palette: PASS, isolated

The former cascade was replaced by one fresh Chromium process and one page per route. Ten checks passed: destination, place, article, Blog index, Home, Services, About, Contact, a reduced-motion destination and the mobile Blog-index still guard. The place/article pages had no still canvas, loader, still request or still URL and retained the plain gradient. Destination and Blog-index retained the approved still behavior; the mobile Blog guard requested no still. Responsive still dimensions decoded as 640 x 800 and 1440 x 900. No page crashed and no retry was required.

### Axe A/AA: FAIL, baseline-relative

Axe-core 4.11.0 completed all eight route scans in separate fresh browser processes at the Phase31 baseline settings (1280px, JavaScript on, reduced motion, WCAG 2 A/AA and 2.1 A/AA tags). The Phase31 baseline contains 36 violation nodes on the four reference routes and zero on the four Phase32a target routes. Current scans found 40 nodes: the 36 baseline identities remain, **4 new identities** were added on Home/About, and 0 were resolved. Destination, place, article and Blog index each have zero findings. Services remains 21 baseline/current nodes and Contact 2 baseline/current nodes.

The four added findings are serious `color-contrast` failures. Each is on an unchanged reference-control source node, not on the Phase32a `place` or `article` fallback:

| Route | Rule / selector | Node source | Current finding |
|---|---|---|---|
| `/` Home | `color-contrast`, `em` | `index.php:544` | 3.54:1, below 4.5:1; inline `#888888` text on white |
| `/about` About | `color-contrast`, `#faq-h2` | `about.php:678`; `.sec-h2.dk` rule at `about.php:378` | 1.11:1, below 3:1 |
| `/about` About | `color-contrast`, `#team > .container > .team-hdr > .sec-label` | `about.php:635`; `.sec-label` rule at `about.php:376` | 1.95:1, below 4.5:1 |
| `/about` About | `color-contrast`, `.container > .sec-label` | `about.php:606`; `.sec-label` rule at `about.php:376` | 1.95:1, below 4.5:1 |

These are real baseline-relative findings on reference controls, but they are not defects introduced by Phase32a. The only public runtime file changed since the Phase32a start checkpoint `6ff7535` is `includes/visual-config.php`, which adds the `place` and `article` fallback; `index.php` and `about.php` were not changed in Phase32a. No public file was changed to fix findings outside the authorized scope. The axe group remains the one final FAIL and is retained in `flagged-items-for-verification.md`.

No route process crashed during these isolated palette or axe reruns, so there were no page retries. The original cascade failures are retained in the run record. Full route results, rules, selectors, baseline comparisons and attempt logs are in `reports/phase-32a-2-rerun-results.json` and `/home/user/phase32a-runtime/phase32a-2/`.

## Final status of all 24 groups

The original full suite ran once, serially, without skip or resume and recorded 20 PASS / 4 FAIL. The targeted reruns above updated only those four group outcomes. The full suite was not rerun. The recomputed final result is **23 PASS / 1 FAIL**:

| # | Group | Final result | Evidence / note |
|---:|---|---|---|
| 1 | 43-route current render and content inputs | PASS | 43/43 HTTP 200; protected comparison inputs valid. |
| 2 | PHP-WASM lint all tracked PHP | PASS | 100 PHP files, zero syntax failures. |
| 3 | Static discovery tests | PASS | 6 tests. |
| 4 | Strict wording tests | PASS | 7 tests. |
| 5 | Citations tests | PASS | 3 tests. |
| 6 | Italy claims tests | PASS | 4 tests. |
| 7 | LLM directory tests | PASS | 9 tests. |
| 8 | LLM policy tests | PASS | 12 tests. |
| 9 | Content presence tests | PASS | 9 tests. |
| 10 | Duplicate answer tests | PASS | 4 tests. |
| 11 | Team biography policy tests | PASS | 14 tests. |
| 12 | Public exposure tests | PASS | 5 tests. |
| 13 | Rendered discovery routes | PASS | Targeted rerun passed on PHP-WASM; original native-php attempt retained in `original_run`. |
| 14 | Rendered publication wording review | PASS | Targeted rerun passed on PHP-WASM; original native-php attempt retained in `original_run`. |
| 15 | Rendered Italy claim policy | PASS | 22 expected exact owner-sentence occurrences. |
| 16 | Rendered Phase19 policy | PASS | 38 published pages; metadata, H1 and destination-data checks passed. |
| 17 | Technical SEO and sitemap routes | PASS | 38 pages; local checks passed. Native redirects and live performance remain unverified. |
| 18 | Phase20 content inventory | PASS | 38 unique primaries; zero changed primaries. |
| 19 | Sitemap exactness and 38 unique URLs | PASS | Byte-identical, 38 unique URLs. |
| 20 | All-43-route structured data parity | PASS | 43 routes, zero JSON-LD mismatches. |
| 21 | Final palette and fallback scope | PASS | 10/10 isolated cases, including reduced motion and mobile Blog guard. |
| 22 | 258-case browser matrix and no-overflow | PASS | 258 normal + 48 reduced-motion cases; zero overflow and hidden text. |
| 23 | Axe representative pages, one per template | FAIL | Four new baseline-relative color-contrast nodes on Home/About reference controls; zero new findings on the four Phase32a target templates. |
| 24 | Git whitespace | PASS | Original full-suite `git diff --check` passed. |

## Summary aggregation and preserved history

`tools/phase32a/summarize_saved_results.py` read all 24 saved groups and the four targeted outcomes. It completed without `KeyError` and recomputed 23 PASS / 1 FAIL. `reports/phase-32a-full-suite-run-01.json` now contains the final per-group statuses, the successful aggregation record, and the original full-suite outcome under `original_run` (20 PASS / 4 FAIL, including the original post-check `KeyError`). The helper did not run the full suite or remeasure performance.

`performance_release_certified=false` remains unchanged. The local simulated results are not field data, live-host evidence or a deployment certification. No performance budget was changed or weakened. No ZIP was built, no reference page was changed, and nothing was merged or deployed.

## Every file changed since the pre-phase baseline

The list below is the complete changed-path inventory relative to `796879d7b3d5ca0fa1e398562e937e9f364a5f62` at final report preparation. External PHP-WASM runtime files, browser processes, temporary output and logs are outside Git and excluded.

```text
CHANGELOG.md
assets/css/visual-system.css
assets/fonts/cormorant-garamond-reference-300-italic.woff2
assets/fonts/cormorant-garamond-reference-300.woff2
assets/fonts/cormorant-garamond-reference-400-italic.woff2
assets/fonts/cormorant-garamond-reference-600.woff2
assets/images/hero-still-640.webp
flagged-items-for-verification.md
includes/visual-config.php
includes/visual-system.php
reports/phase-32-11-route-ab-fixtures.json
reports/phase-32-11-route-ab-run-01-results.json
reports/phase-32-11-route-ab-run-01-summary.md
reports/phase-32-11-route-ab-run-02-results.json
reports/phase-32-11-route-ab-run-02-summary.md
reports/phase-32-43-route-content-comparison.json
reports/phase-32-43-route-content-comparison.md
reports/phase-32-before-render-index.json
reports/phase-32-before-renders.json.gz
reports/phase-32-before-sitemap.xml
reports/phase-32-blog-desktop-ab-results.json
reports/phase-32-blog-desktop-ab-summary.md
reports/phase-32-blog-tbt-diagnostic.json
reports/phase-32-candidate-font-reflow-diagnostics.md
reports/phase-32-cls-about-candidate-diagnostic.json
reports/phase-32-cls-blog-index-candidate-diagnostic.json
reports/phase-32-cls-home-candidate-diagnostic.json
reports/phase-32-cls-home-diagnostic.json
reports/phase-32-cls-services-candidate-diagnostic.json
reports/phase-32-contact-minihero-audit.json
reports/phase-32-contact-minihero-postscroll-audit.json
reports/phase-32-contact-minihero-tail-summary.md
reports/phase-32-font-ab-results.json
reports/phase-32-font-ab-summary.md
reports/phase-32-font-audit.json
reports/phase-32-hero-assets.json
reports/phase-32-hero-contrast.json
reports/phase-32-hero-smoke.json
reports/phase-32-local-font-candidate-diagnostics.md
reports/phase-32-local-font-diagnostic-about.json
reports/phase-32-local-font-diagnostic-blog-index.json
reports/phase-32-local-font-diagnostic-home.json
reports/phase-32-local-font-diagnostic-services.json
reports/phase-32-noscript-smoke.json
reports/phase-32-post-run01-attribution.md
reports/phase-32-progress.md
reports/phase-32-reference-audit-after.json
reports/phase-32-reference-audit-after.md
reports/phase-32-reference-audit-before.json
reports/phase-32-reference-audit-before.md
reports/phase-32-reference-audit-candidate.json
reports/phase-32-reference-audit-local-font-candidate.json
reports/phase-32-reference-font-candidate.json
reports/phase-32-reference-scene-policy-smoke.json
reports/phase-32-reference-scene-smoke.json
reports/phase-32-scene-switch-smoke.json
reports/phase-32a-2-rerun-results.json
reports/phase-32a-43-route-content-comparison.json
reports/phase-32a-43-route-content-comparison.md
reports/phase-32a-6-route-ab-run-01-raw.json
reports/phase-32a-6-route-ab-run-01-summary.json
reports/phase-32a-6-route-ab-run-01-summary.md
reports/phase-32a-font-ab-run-01-fixtures.json
reports/phase-32a-font-ab-run-01-fixtures.md
reports/phase-32a-font-ab-run-01-raw.json
reports/phase-32a-font-ab-run-01-summary.json
reports/phase-32a-font-ab-run-01-summary.md
reports/phase-32a-font-chain-diagnosis.md
reports/phase-32a-full-suite-run-01.json
reports/phase-32a-palette-fallback-check.md
reports/phase-32a-progress.md
reports/phase-32a-release-check.md
reports/phase-32a-six-route-fixtures.json
reports/phase-32a-six-route-fixtures.md
tools/phase32/ab-fixture-server.cjs
tools/phase32/ab-fixtures.py
tools/phase32/ab-runner.cjs
tools/phase32/cls-attribution.cjs
tools/phase32/compare_43_route_content.py
tools/phase32/contact-minihero-audit.cjs
tools/phase32/contact-minihero-postscroll.cjs
tools/phase32/desktop-blog-ab.cjs
tools/phase32/encode_hero_stills.cjs
tools/phase32/font-ab.cjs
tools/phase32/font-audit.cjs
tools/phase32/freeze_baseline.py
tools/phase32/hero-contrast.cjs
tools/phase32/hero-smoke.cjs
tools/phase32/noscript-smoke.cjs
tools/phase32/reference-audit.cjs
tools/phase32/reference-scene-policy-smoke.php
tools/phase32/reference-scene-smoke.cjs
tools/phase32/scene-switch-smoke.php
tools/phase32a/ab-runner.cjs
tools/phase32a/axe_template_check.cjs
tools/phase32a/compare_43_routes.py
tools/phase32a/font_ab_runner.cjs
tools/phase32a/freeze_font_ab_fixtures.py
tools/phase32a/freeze_six_route_fixtures.py
tools/phase32a/palette_check.cjs
tools/phase32a/run_full_suite.py
tools/phase32a/summarize_ab.py
tools/phase32a/summarize_font_ab.py
tools/phase32a/summarize_saved_results.py
```
