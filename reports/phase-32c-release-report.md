# Phase32c release report

- **Date:** 2026-11-06
- **Branch:** `arena/48320ee5-ilmerastudyabroad`
- **PR:** [#1](https://github.com/fawazbhseo/ilmerastudyabroad/pull/1)
- **Disposition:** No merge, upload or deployment. This report records local evidence and owner actions still required.
- **Progress log:** `reports/phase-32c-progress.md`

## Executive result

Task 1 contrast findings were classified as real and pre-existing, then corrected with four separate color-only commits and a screenshot regression gate. Task 2 reference-page safeguards passed on Home, Services and About; 11 Contact geometry differences remain recorded as same-source measurement artefacts, not waived. Task 3 retained the plain-palette hero for Mysuru and the selected article because the A/A noise margin made the still decision inconclusive. Task 4, the one permitted full-suite run, remains **FAIL** with 9 of 16 groups marked FAIL. Task 5's clean 137-file payload and ZIP passed exact-set, byte/hash, route and asset checks. Task 6 documentation is completed in this checkpoint.

All browser, PHP-WASM and Lighthouse evidence described below is local. No native Apache/Hostinger, live-site, PageSpeed Insights or contact-inbox result is claimed. The one-shot suite was not repeated and no suite group was rerun.

## Task 1: contrast findings

### Historical comparison and classification

All four findings were **REAL, pre-existing** in each completed screenshot matrix. None is classified TRANSIENT or MEASUREMENT ARTEFACT. The requested snapshots include `75f355f`, `796879d`, the literal first post-baseline commit `d0b7726`, first Phase32 source change `2722901`, scene-defer change `d4b376e`, and pre-fix current `f9c96ca`. `d0b7726` changed documentation only and is runtime-identical to `796879d`. The affected color declarations predate Phase32; the scene-defer change alters scene startup but did not create these color pairs. No last-passing instance of these exact pairs was found in the requested snapshots, so the repairs reused existing passing palette relationships.

The older `75f355f` and `796879d` pages start WebGL in every JavaScript-enabled historical case, including phone-width and reduced-motion inputs. The harness recorded actual browser behavior rather than claiming those builds had no WebGL startup. In the deferred-scene/current matrices, only eligible 1280px normal-scene cases start WebGL. Computed colors, sampled visible backdrops, ratios and full-scroll screenshot crops are recorded per case in the five contrast JSON reports and `reports/screenshots/phase-32c/`.

| Finding | Pre-fix foreground and backdrop | Pre-fix contrast | Smallest restoration and commit | Fresh regression result |
|---|---|---:|---|---:|
| Home programme-conditions `em` | `rgb(136, 136, 136)` on white | 3.545:1 | Removed only the inline `#888` color; inherits existing `--grey-dark`. `bde0ddd` | 7.526:1 |
| About FAQ heading `#faq-h2` | `rgb(10, 22, 40)` over sampled dark scene pixels | 1.089:1 to 1.098:1 on the deferred/current matrix; earlier animated samples ranged lower | Changed only to the existing light heading variant. `6c9fea4` | 19.883:1 |
| About team section label | `rgb(201, 168, 76)` on `#E8ECF8` | 1.935:1 | Scoped color-only rule reusing `--navy`. `f6a91c8` | 11.239:1 |
| About Kodagu section label | `rgb(201, 168, 76)` on `#E8ECF8` | 1.935:1 | Scoped color-only rule reusing `--navy`. `3324432` | 11.239:1 |

The screenshot-based regression check is `tools/phase32c/contrast-regression.cjs`. It used fresh browser processes with the scene not started, tested Home and About at 360px and 1280px, saved eight affected-node crops, and enforced 4.5:1. All checks passed; the minimum was 7.526:1. Evidence: `reports/phase-32c-contrast-regression-3324432.json` and `reports/screenshots/phase-32c/contrast-regression-3324432/`. The fixes do not change wording, font size, spacing, layout, surfaces or imagery.

## Task 2: reference-page scene safeguards

Compared Phase31b `796879d` with current reference-page source `091442f` at 360, 768 and 1280 CSS px in scene, still, reduced-motion, disabled-scene-switch and JavaScript-off states. The incremental-scroll harness reached page end, settled for three seconds and checked visible DOM geometry outside scene layers at the unchanged 0.1px tolerance. Full matrix and same-source A/A evidence: `reports/phase-32c-reference-safeguards.json`, `reports/phase-32c-reference-safeguards-aa.json` and `reports/phase-32c-reference-safeguards.md`.

| Route | Literal 0.1px geometry result | Disposition |
|---|---:|---|
| Home | 15/15 PASS | Exact |
| Services | 15/15 PASS | Exact |
| About | 15/15 PASS | Exact |
| Contact | 4/15 PASS, 11 raw differences | MEASUREMENT ARTEFACT by same-source A/A; raw differences remain FAILs, not waived |

Across all 60 cases, rendered text, headings, links, images, picture sources, JSON-LD and canonicals matched 60/60. Header and About team landmark geometry matched 60/60; team-card boxes and text matched 60/60. Footer geometry matched 49/60. In each of the 11 Contact differences, both native select controls measured 46px in the reference and 48px in current; the downstream footer shift totals 4px, with a maximum element delta of 4px. Same-source A/A controls reproduce and reverse the select-height direction. No select CSS change was made.

The Phase32 shared local-font style/preloads reached all four reference pages in all 60 current renders. The deferred scene policy reduced WebGL starts from 24/60 in Phase31b to four eligible 1280px normal-scene cases in current. The four contrast restorations are also present. There were no hero-still nodes or requests on Home, Services, About or Contact. The still was not applied to those reference pages; the reference logo was not optimized; Contact `#miniHero` was not changed. The older Phase32 hero-still scope remains destination, place, article and blog-index templates. Task 3's evidence only supports the plain-palette decision for Mysuru/place and the selected article; destination and blog-index decisions were not tested in that two-route experiment.

## Task 3: three-arm hero-still A/B

This was local simulated Lighthouse data, not field results or PageSpeed Insights. Raw evidence was committed before analysis as `reports/phase-32c-hero-ab-raw.json` in `9ad242e`; SHA-256 `039eb45d973b00844df525665d1ce6d6ebfb7a592c2db93dc0758aadd4e8351b`. The experiment collected 63 fresh-browser samples: nine each for A, B-still and B-plain on each route, plus nine adjacent A/A repeats on Mysuru. Order alternated by round; no retry or resume occurred. A was frozen at `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`; current B was `ac2d9b06dc85578e4b4c31ad236b228f67d44333`. All three arms matched protected rendered content for both routes. The prior fixture archive's stored A HTML did not match exact-commit content; the experiment used fresh PHP-WASM renders of the exact A commit and left that archive unchanged.

### Median and IQR summary

LCP, TBT and transfer are medians with IQRs. All CLS medians/IQRs and transfer IQRs are zero. Request-count IQRs are zero.

| Route | Arm | n | LCP ms median (IQR) | TBT ms median (IQR) | CLS median (IQR) | Transfer bytes median | Requests median |
|---|---|---:|---:|---:|---:|---:|---:|
| Mysuru | A | 9 | 1652.655 (629.025) | 0 (0) | 0 (0) | 224,797 | 6 |
| Mysuru | B-still | 9 | 1726.861 (554.690) | 0 (0) | 0 (0) | 238,217 | 7 |
| Mysuru | B-plain | 9 | 1653.130 (629.052) | 0 (0) | 0 (0) | 225,499 | 6 |
| Selected article | A | 9 | 1652.193 (0.362) | 0 (0) | 0 (0) | 238,734 | 6 |
| Selected article | B-still | 9 | 1726.814 (629.088) | 0 (9.184) | 0 (0) | 252,154 | 7 |
| Selected article | B-plain | 9 | 1651.803 (74.536) | 0 (0) | 0 (0) | 239,436 | 6 |

### Paired-round LCP ratios

Values are B/A in round order. The full per-round TBT, CLS and transfer deltas are in `reports/phase-32c-hero-ab-analysis.md`.

| Route and arm | Rounds 1 through 9, LCP B/A |
|---|---|
| Mysuru B-still | 0.7239, 0.7570, 1.0951, 1.0454, 0.7571, 1.4262, 0.9995, 1.3801, 1.4938 |
| Mysuru B-plain | 0.9993, 1.0001, 1.0475, 0.9996, 0.7241, 1.3810, 1.0003, 1.0005, 1.0479 |
| Selected article B-still | 0.9996, 1.4262, 1.0327, 0.9999, 1.0456, 1.4259, 0.7572, 1.0450, 1.0451 |
| Selected article B-plain | 0.9996, 1.0000, 0.7240, 0.9998, 1.0004, 0.9547, 0.7242, 0.9540, 0.9543 |

### Fixed budget outcomes and noise floor

| Route | Arm | Added transfer | New render blocker | Median LCP B/A | Median TBT increase | CLS | Point budgets | Noise-adjusted LCP upper bound |
|---|---|---:|---|---:|---:|---:|---|---:|
| Mysuru | B-still | 13,420 B | None | 1.0449 | 0 ms | 0.000 | All PASS | 1.4913, inconclusive |
| Mysuru | B-plain | 702 B | None | 1.0003 | 0 ms | 0.000 | All PASS | Inconclusive margin; retained as fallback |
| Selected article | B-still | 13,420 B | None | 1.0452 | 0 ms | 0.000 | All PASS | 1.4916, inconclusive |
| Selected article | B-plain | 702 B | None | 0.9998 | 0 ms | 0.000 | All PASS | Inconclusive margin; retained as fallback |

For both routes and both B arms, point estimates pass the strict transfer `<150,000 B`, no-new-render-blocker, LCP `<=1.10`, TBT increase `<=50 ms`, and CLS no-worse-than-A and `<0.1` budgets. The Mysuru A/A noise proxy has median absolute LCP difference 75.331ms, IQR 627.202ms, maximum 703.968ms; median A-repeat/A ratio 1.0002, IQR 0.0910, maximum absolute deviation from 1 of 0.4464. A/A maximum absolute TBT and CLS differences were zero. Maximum A/A transfer difference was 98,454 bytes due to one extra logo network-audit entry. B-still fetched the 640px image in 9/9 samples per route at 9,947 bytes each.

**Decision: retain B-plain for Mysuru and the selected article.** This is a conservative choice under an inconclusive noise-adjusted result, not evidence that B-plain is faster and not a point-budget failure. Still upper LCP ratios of 1.4913 and 1.4916 exceed 1.10 after the observed noise margin. Destination and blog-index still behavior was not measured by this two-route run. Owner confirmation using PageSpeed Insights remains required.

## Task 4: one permitted final full-suite run

The final suite ran once, after Tasks 1-3, at suite head `62af0b29e36f5cc6a0456d0537d75f2050029bd2`. It recorded all 16 groups in 4,467.1 seconds and exited 1: **7 PASS, 9 FAIL**. The complete report is `reports/phase-32c-final-suite-run-01.md` and `reports/phase-32c-final-suite-run-01.json`. No group was repeated or resumed.

| Group | Status | Result or exact limitation |
|---|---|---|
| 43 current route renders and adapter integrity | FAIL | 43 adapter bodies matched saved bytes and statuses matched Phase31b. The route index lacks the validator's expected per-route `sha256` field. |
| PHP-WASM lint, all tracked PHP | PASS | 100 PHP files linted. |
| 43-route text, link, image and picture-source parity to Phase31b | FAIL in runner | Semantic comparison itself matched text, title, headings, links, images and picture sources on 43/43 routes; status failed on the same route-index hash assumption. |
| 43-route JSON-LD parity to Phase31b | FAIL in runner | JSON-LD itself matched on 43/43 routes; status failed on the same route-index hash assumption. |
| Sitemap exactness and 38 unique URLs | PASS | Byte-identical to Phase31b; 38 unique URLs. |
| Static discovery and wording policy fixtures | PASS | All 10 static commands passed. |
| Rendered discovery, robots and inbound-link checks | FAIL | Existing helper required a native `php` executable, which was absent. |
| Rendered publication wording and protected-copy review | FAIL | Stopped at the same unavailable native `php` executable. |
| Technical SEO and structured data | PASS | 38 published pages; heading order, visible/schema parity, images, canonicals and route depth passed. |
| Phase20 published-route inventory | PASS | 38 pages, 17 document fragments and 50 prompts checked. |
| Palette and measured fallback scope | FAIL | First `/study-in-germany` 360px case passed; Chromium closed before case two. |
| 258-case browser matrix, overflow and target-baseline shrink checks | FAIL | 306/306 cases logged: 258 normal plus 48 reduced-motion. No overflow or hidden-text assertion failed. Target comparison then emitted 20 shrink examples and stopped before writing matrix JSON; total shrinks are unavailable. |
| 44px target rectangle audit | FAIL, not run | Required matrix JSON was absent. Phase31 baseline has 1,552 of 5,670 rectangles below 44px; this is not a current count. |
| Fresh-process axe A/AA on Home, Services, About and Contact | PASS | Zero node identities outside the Phase31 baseline. Baseline node counts were 8, 21, 5 and 2 respectively. |
| Phase31 full blank-space scan and Contact tails | FAIL as screening result | 516/516 cases; 1,147 quiet-band candidates, 24 fewer than 1,171 baseline; zero hidden reveal-text findings; 16 intentional cue dismissals; eight min-height-tail candidates. |
| Git whitespace and CRLF-aware diff check | PASS | Passed. |

The semantic comparison inside the final run reports exact text, title, headings, links, images, picture sources and JSON-LD on all 43 routes, with zero status mismatches. This does not make the three runner groups above PASS. The browser matrix contains 20 emitted Home 360px target-shrink examples, including Mysuru at 58.47x19px baseline and 50.86x20px current; the total is unavailable. The separate 44px audit did not execute, so no current 44px compliance result is claimed.

The blank-space scan retains four documented Contact `#miniHero` tails, one at each state per width. Current inspector values are 184.53px at 360px, 244.94px at 768px and 192.34px at 1280px; hero/min-height is 792px and the cue ends 30px above the hero bottom. Prior after-scan values at 360px and 768px were 138px and 233px; 1280px was not reported as comparable. Four additional Home `#team` 1280px states show an unclassified 202px tail candidate after 110px bottom padding. It has no saved crop, contains visible content and was not changed. The suite failure remains recorded; this candidate is not confirmed removable space.

The nine suite failures are therefore: the route-index hash assertion; two semantic comparator statuses affected by that same assertion; rendered discovery; rendered publication review; incomplete palette run; target-baseline shrink comparison; 44px audit not run; and unclassified Home `#team` tail candidate. These are named separately in the machine-readable suite result. No full suite group was rerun.

## Task 5: package, clean-copy and ZIP verification

The manifest is pinned to source commit `065934a1ef2b0962308ce440ada959619e8824f2`, the latest upload-relevant runtime source. Later commits through the Task 5 documentation checkpoint did not change any manifest runtime path. The manifest contains 137 files from 6,217 tracked source files; 6,080 tracked files are excluded. It includes eight payload `.htaccess` policies. The ninth tracked policy, `releases/.htaccess`, is excluded. The 720px still and unused legacy helper are excluded; the current 640px and 1440px still fallbacks, four newly required Cormorant reference faces and temporary checker are included.

| Folder | Files |
|---|---:|
| Root | 46 |
| `assets/css` | 1 |
| `assets/fonts` | 16 |
| `assets/images` | 9 |
| `blog` | 9 |
| `data` | 8 |
| `destinations` | 10 |
| `includes` | 18 |
| `places` | 18 |
| `reports` | 1 |
| `tools` | 1 |
| **Total** | **137** |

`tools/phase27/export.py` created `releases/ilmera-deploy-065934a.zip`. It contains exactly 137 unique safe paths, has a passing CRC, and is 833,237 bytes. Every allowlist file's size and SHA-256 matches its source Git blob, current repository, clean extracted temporary copy and ZIP bytes. ZIP SHA-256: `3c56cdf481f639f98c689a26af517454576fae6d9ec9237c9e145eb38dfa8b57`.

[Download the raw ZIP from this branch](https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/arena/48320ee5-ilmerastudyabroad/releases/ilmera-deploy-065934a.zip).

The isolated PHP-WASM repository and clean-payload adapters returned HTTP 200 and byte-identical bodies for 43/43 routes. Thirty-one static asset URLs matched byte-for-byte; every local `/assets/` URL extracted from the 43 returned HTML bodies exists in the manifest and clean payload. Sitemap, robots and both LLM endpoints matched. Route aggregate SHA-256: `61a682d18e11a837bbc8bc56b55769d104ed03e733289697b9ca492e68129ee5`. Asset aggregate SHA-256: `4552cb293dd3a1f970fd496eb344a2d43ad3c191e12bdf09c7025b176c9dadcd`. Details: `reports/phase-32c-payload-parity.json` and `reports/phase-32c-upload-scope.json`.

The owner checklist and PDF are updated at `reports/post-deploy-checklist.md` and `.pdf`. The checklist has blank before/after PSI fields and strict budgets, lists post-upload routes, folder counts, rollback directions and the 11 changed upload paths since `796879d`. The PDF is three A4 pages, regenerated offline without external requests. This package verification does not test native Apache, Hostinger headers, production access control or live performance.

### Upload-relevant changed paths since `796879d`

- `about.php`
- `assets/css/visual-system.css`
- `assets/fonts/cormorant-garamond-reference-300-italic.woff2`
- `assets/fonts/cormorant-garamond-reference-300.woff2`
- `assets/fonts/cormorant-garamond-reference-400-italic.woff2`
- `assets/fonts/cormorant-garamond-reference-600.woff2`
- `assets/images/hero-still-640.webp`
- `deploy-check.php`
- `includes/visual-config.php`
- `includes/visual-system.php`
- `index.php`

The 1440px still remains in the allowlist because current templates use it, but it was not a changed path since `796879d`.

## Task 6: documentation and owner actions

`CHANGELOG.md` records the Phase32c disposition and links to this report. `flagged-items-for-verification.md` receives an appended Phase32c owner-verification section; all earlier items and blockers remain unchanged. The detailed progress and exact next-step history remains in `reports/phase-32c-progress.md`.

Owner actions remain open: compare the same five mobile URLs before and after any owner-approved upload in PageSpeed Insights; confirm the strict gates in the checklist; verify live MIME/cache/CSP and `.htaccess` behavior on the native host; test the real contact submission and inbox; remove the temporary checker after its one permitted use; and confirm the old-site backup can be restored. No values or hosting results have been invented. No merge or deployment was performed.
