# Phase32a release check

- **Date:** 2026-11-02
- **Branch:** `arena/48320ee5-ilmerastudyabroad`
- **Pre-phase baseline:** `796879d7b3d5ca0fa1e398562e937e9f364a5f62`
- **Full-suite source HEAD:** `2ee711c2cc52c30a0f8d8aff2ae86ad2e03f39e4`
- **Full-suite run:** one serial run, 2026-11-02 05:05:58 UTC, 1,818.13 seconds
- **Disposition:** Verification completed with failures. The suite recorded 24/24 checks: 20 PASS and 4 FAIL. This is not a release or performance certification. `performance_release_certified=false` remains unchanged.

## Executive summary

- The required six-route simulated A/B and the fresh two-route font A/B are complete. The approved `place` and `article` plain-palette fallback is configured; no font change was made.
- The all-43-route rendered-content comparison against the frozen pre-phase render passed: 43/43 HTTP 200, zero protected invariant failures, and a byte-identical sitemap with 38 unique URLs.
- The one final full suite completed all 24 named checks. The 306-case browser matrix passed with zero overflow and zero hidden main text. PHP-WASM syntax lint passed for all 100 tracked PHP files.
- Four checks failed: rendered discovery and rendered publication wording could not invoke a native `php` executable; the final palette check and axe check lost their Playwright browser/context after their first case. These checks are incomplete, not passes. No attempt was made to repeat or resume them.
- After saving check 24, the runner raised `KeyError: 'runner_error'` while constructing its aggregate summary. The checked-in JSON was finalized from the saved per-check records and records this error. The runner's missing-field guard was corrected after the run only. The full suite was not rerun.
- All performance values below are local simulated mobile Lighthouse results. They are not field data or live-site performance. The unchanged budgets were not relaxed.

## Scope and invariants

The measured fallback applies only to the `place` and `article` template groups. `ILMERA_SCENES_ENABLED` stays enabled and remains the site-wide switch. Destination and Blog-index scenes stay in scope as previously approved; Services and Contact are measurement controls only. No wording, headings, links, FAQs, schema, canonicals, statuses or protected images were changed by the fallback. No Phase32a page-specific Home, Services, About or Contact source change was made.

The rendered comparison in `reports/phase-32a-43-route-content-comparison.md` compared the frozen A render at `796879d` with B rendered from `ba5e97dc4038bae315ae5612ad9a5ef5061f9ea0`. All 43 routes returned HTTP 200. Text and order, title, headings, meta, robots, canonical, anchor semantics and order, image and picture-source attributes, and JSON-LD all matched. There were zero protected invariant failures. HTML bytes differ where visual markup differs, as expected. The sitemap is byte-identical, with 38 unique URLs and SHA-256 `de23394bfe3150db0a29d684f4f13187f644a4bba617beeabeaf0d19e769ddbb`.

## Unchanged performance budgets

| Budget | Gate retained |
|---|---|
| Added transfer | Strictly below 150,000 bytes |
| Median LCP | B/A no more than 1.10 |
| Median TBT | Increase no more than 50 ms |
| Median CLS | No worse than A and below 0.1 |
| Render-blocking resources | No new render-blocking URL |

The six-route run is one local simulated lab session, not field data. It recorded 84 valid samples, seven per arm on each of six routes, with interleaved order, fresh Chromium per sample, zero retries and zero Lighthouse warnings. Full quartiles and paired-round summaries are in `reports/phase-32a-6-route-ab-run-01-summary.md` and `.json`.

| Route | LCP A/B median ms | LCP B/A | TBT A to B, delta ms | CLS A to B | Transfer delta bytes | New blocking URL | Route disposition |
|---|---:|---:|---:|---:|---:|---|---|
| `/study-in-germany` | 1198.67 / 1209.70 | 1.0092 | 0.00 to 46.00, +46.00 | 0.000000 to 0.000000 | +13,278 | None | PASS |
| `/study-abroad-counselling-mysuru` | 1652.33 / 1728.17 | 1.0459 | 0.00 to 66.24, +66.24 | 0.000000 to 0.000000 | +13,387 | None | FAIL, plain-palette fallback required |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1654.08 / 2355.84 | 1.4243 | 0.00 to 59.00, +59.00 | 0.000000 to 0.000000 | +13,387 | None | FAIL, plain-palette fallback required |
| `/blog/` | 2280.94 / 2281.15 | 1.0001 | 0.00 to 0.00, 0.00 | 0.000000 to 0.000000 | +3,473 | None | PASS |
| `/services` | 8406.54 / 2956.10 | 0.3516 | 2400.00 to 0.00, -2400.00 | 0.000000 to 0.000491 | -564,546 | None | CONTROL ONLY; symmetric LCP control gate failed |
| `/contact` | 11358.83 / 2730.69 | 0.2404 | 5166.00 to 0.00, -5166.00 | 0.000000 to 0.000000 | -574,182 | None | CONTROL ONLY; symmetric LCP control gate failed |

Germany and Blog index passed their target median budgets. Mysuru met the LCP, CLS, transfer and render-blocking gates but failed TBT by 16.24 ms. The article failed LCP and TBT. These two template groups therefore use the existing plain-palette fallback. Services and Contact remain controls and were not changed. `performance_release_certified=false` remains unchanged.

## Fresh font candidate A/B

The fresh font experiment recorded 28 valid local simulated samples, seven per arm on Mysuru and the selected article, interleaved with fresh Chromium per sample and zero warnings. The candidate changed only seven `font-display:block` declarations to `swap` and removed the body-visibility gate in the frozen fixture. It did not qualify because adoption required a lower candidate median LCP on both routes and CLS no worse on either.

| Route | LCP A/B median ms | LCP B/A | Candidate LCP delta | CLS A/B medians | Font requests A/B per sample | Decision |
|---|---:|---:|---:|---:|---:|---|
| `/study-abroad-counselling-mysuru` | 1652.92 / 1652.88 | 1.0000 | -0.03 ms | 0.000000 / 0.000000 | 4 / 4 | Route-level criteria met, but insufficient for adoption |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1652.98 / 1654.64 | 1.0010 | +1.66 ms | 0.000000 / 0.000000 | 4 / 4 | Route-level criteria fail |

Decision: retain the current font policy. No font family, file, weight, preload, `font-display` value or font gate was changed. Full evidence is in `reports/phase-32a-font-ab-run-01-summary.md` and `.json`. These results are local simulated data, not field performance.

## Palette fallback and retained still scope

The implementation is `ILMERA_VISUAL_PLAIN_HERO_TEMPLATES = ['place','article']`; `ILMERA_SCENES_ENABLED` remains `true`. Existing approved still assets remain within their recorded size gates: 640 x 800 at 9,738 bytes (limit 14,000) and 1440 x 900 at 37,226 bytes (limit 40,000). The prior affected-template render check found no still canvas, still URL, loader or noscript still on Mysuru and the selected article, and the 43-route protected-content comparison passed.

| Template | Representative route | Final configured treatment | Evidence status |
|---|---|---|---|
| `destination` | `/study-in-germany` | Retain approved still/scene method | One final palette cell at 360px passed; prior still checks also passed |
| `place` | `/study-abroad-counselling-mysuru` | Plain-palette fallback, no still | Prior affected-template render and content comparison passed; final matrix did not reach this route |
| `article` | `/blog/how-to-choose-study-abroad-consultant-karnataka` | Plain-palette fallback, no still | Prior affected-template render and content comparison passed; final matrix did not reach this route |
| `blog-index` | `/blog/` | Retain approved still/scene method; existing mobile guard skips the still at widths <=768px | Prior approved checks remain; final matrix did not reach this route |

The final palette test itself is **FAIL / incomplete**, not a full palette verification: `/study-in-germany` at 360px logged PASS, then creation of the next browser context failed with `Target page, context or browser has been closed`. It did not complete the remaining route/viewport cells or the reduced-motion check. The prior fallback evidence remains valid, but this final harness failure is retained as a verification flag.

## All 24 final-suite check results

The single run used `tools/phase32a/run_full_suite.py`, did not skip or resume checks, and wrote `reports/phase-32a-full-suite-run-01.json`. Individual logs are under `/home/user/phase32a-runtime/phase32a-full-suite-run01/` and are intentionally external to Git.

| # | Check | Result | Result detail |
|---:|---|---|---|
| 1 | 43-route current render and content inputs | PASS | 43 HTTP 200 renders; current source and protected-content comparison inputs were unchanged and valid. |
| 2 | PHP-WASM lint all tracked PHP | PASS | 100 tracked PHP files; zero syntax failures. |
| 3 | Static discovery tests | PASS | 6 tests passed. |
| 4 | Strict wording tests | PASS | 7 tests passed. |
| 5 | Citations tests | PASS | 3 tests passed. |
| 6 | Italy claims tests | PASS | 4 tests passed. |
| 7 | LLM directory tests | PASS | 9 tests passed. |
| 8 | LLM policy tests | PASS | 12 tests passed. |
| 9 | Content presence tests | PASS | 9 tests passed. |
| 10 | Duplicate answer tests | PASS | 4 tests passed. |
| 11 | Team biography policy tests | PASS | 14 tests passed. |
| 12 | Public exposure tests | PASS | 5 tests passed. |
| 13 | Rendered discovery routes | FAIL | Stopped in `tools/build_llms_directory.py` because subprocess `php` was not found. This is an environment/tool execution failure; the check did not complete. |
| 14 | Rendered publication wording review | FAIL | Reached the same missing native `php` executable through the discovery check. The review did not complete. |
| 15 | Rendered Italy claim policy | PASS | Local rendered claim check passed, including 22 exact owner-sentence occurrences in the expected visible/schema/metadata surfaces. |
| 16 | Rendered Phase19 policy | PASS | 38 published pages, unique short metadata, one H1, primary in heading/opening and destination data byte-identical. |
| 17 | Technical SEO and sitemap routes | PASS | 38 pages, headings, breadcrumbs, images, click depth, orphan and canonical checks passed. Native redirects and live performance were not verified. |
| 18 | Phase20 content inventory | PASS | 38 published pages, 38 unique primaries, zero changed primaries; protected destination/location data unchanged. |
| 19 | Sitemap exactness and 38 unique URLs | PASS | Sitemap bytes matched; 38 URLs and 38 unique URLs. |
| 20 | All-43-route structured data parity | PASS | 43 routes, zero JSON-LD mismatches. |
| 21 | Final palette and fallback scope | FAIL | First case `/study-in-germany` at 360px passed; next `browserContext.newPage` failed because the browser/context was closed. Remaining cells and reduced-motion check were not completed. |
| 22 | 258-case browser matrix and no-overflow | PASS | 258 normal cases plus 48 reduced-motion representatives, 306 total; zero horizontal overflow, zero hidden main text, and the matrix's image-load checks passed. |
| 23 | Axe representative pages, one per template | FAIL | Destination `/study-in-germany` logged zero violation nodes; the next browser context failed with the same browser-closed error. No axe summary JSON was produced and the other representatives were not scanned. |
| 24 | Git whitespace | PASS | `git -c core.whitespace=cr-at-eol diff --check` returned zero. |

The four failed check logs are `rendered-discovery-routes.log`, `rendered-publication-wording-review.log`, `final-palette-and-fallback-scope.log` and `axe-representative-pages,-one-per-template.log` in `/home/user/phase32a-runtime/phase32a-full-suite-run01/`. The first two require a native `php` executable not present in PATH. The latter two stopped on browser/context closure. These results are recorded as failures; they are not relabeled as passes.

After check 24 had been saved, the runner raised `KeyError: 'runner_error'` in its final aggregation. The JSON report records the complete 24-check result, the four failed checks and the aggregation error. The runner's initialization/lookup guard was corrected after that run so future output will finalize cleanly. The suite was not rerun, resumed or altered after the failure.

## Release boundaries

- `performance_release_certified=false` remains unchanged. No performance budget was changed or weakened.
- Local simulated measurements are not field data, live-host evidence or deployment verification. No native-host or live speed check is claimed.
- No ZIP was built, no reference page was changed, and no merge or deployment occurred.
- No runtime source was modified during the full-suite run. The later runner change is limited to aggregate-report bookkeeping and does not change site runtime.

## Every file changed since the pre-phase baseline

The list below is the complete changed-path inventory relative to `796879d7b3d5ca0fa1e398562e937e9f364a5f62` at final report preparation. It includes the release report itself and the release/changelog/progress records. External runtime logs and temporary rendered HTML are excluded.

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
```
