# Phase32c final suite run 01

- **Result:** FAIL, exit code 1
- **Execution:** one complete run, 16 of 16 groups recorded, 9 groups marked FAIL
- **Duration:** 4,467.1 seconds
- **Suite source:** `62af0b29e36f5cc6a0456d0537d75f2050029bd2`
- **43-route render capture:** `749f138542948786d97ea513334d1cd881b45be4`
- **Reference:** Phase31b `796879d7b3d5ca0fa1e398562e937e9f364a5f62`
- **Later commit during run:** `969e154` changed progress documentation only. No production runtime path changed after the render capture.
- No suite group was repeated. The detailed machine-readable result is `reports/phase-32c-final-suite-run-01.json`.

## Group results

| Group | Result | Finding |
| --- | --- | --- |
| 43 current route renders and adapter integrity | FAIL | All 43 adapter bodies matched saved render bytes and all route statuses matched Phase31b. The validator expected a per-route `sha256` field that the server route index does not emit. |
| PHP-WASM lint, all tracked PHP | PASS | 100 files linted. |
| 43-route text, links, images and picture sources | FAIL in runner | Semantic comparison found identical text, title, headings, links, images, picture sources and JSON-LD on all 43 routes. The runner status followed the same route-index hash assumption. |
| 43-route JSON-LD parity | FAIL in runner | JSON-LD matched on all 43 routes. The runner status followed the same route-index hash assumption. |
| Sitemap exactness and 38 unique URLs | PASS | Byte-identical to Phase31b, with 38 unique URLs. |
| Static discovery and wording policy fixtures | PASS | All 10 static commands passed. |
| Rendered discovery, robots and inbound-link checks | FAIL | The existing check invoked native `php` for a local proof-data lookup. This environment had PHP-WASM, but no native `php` executable. |
| Rendered publication wording and protected-copy review | FAIL | Stopped at the same unavailable native `php` executable. |
| Technical SEO and structured-data validation | PASS | 38 published pages checked; heading order, visible/schema parity, image checks, canonical targets and route-depth checks passed. |
| Phase20 published-route inventory | PASS | 38 published pages, 17 document fragments and 50 prompts checked. |
| Palette and measured fallback scope | FAIL | The first `/study-in-germany` 360px case passed. Chromium closed before the second case could start. |
| 258-case browser matrix, overflow and target-baseline shrink checks | FAIL | All 306 logged cases completed: 258 normal and 48 reduced-motion. No overflow or hidden-text assertion failure was recorded. The final target-baseline comparison failed; only the first 20 shrink examples were emitted and the matrix JSON was not written. The total shrink count is unavailable. |
| 44px target rectangle audit | FAIL, not run | The required matrix JSON was absent after the preceding target-baseline failure. The Phase31 baseline has 1,552 of 5,670 measured rectangles below 44px; this is not a current count. |
| Fresh-process axe A/AA on Home, Services, About and Contact | PASS | Zero node identities outside the Phase31 baseline. Preserved baseline node counts: Home 8, Services 21, About 5, Contact 2. |
| Phase31 full blank-space scan and Contact tails | FAIL | All 516 cases completed. The scan retained an unclassified Home `#team` tail candidate described below. |
| Git whitespace and CRLF-aware diff check | PASS | No whitespace or line-ending failure. |

## Render and content comparison

- The adapter returned all 43 routes with HTTP 200, matched all 43 saved render bodies byte-for-byte, and had zero Phase31b status mismatches.
- The current route index records route, file, status, byte count and evidence, but has no `sha256` field. The render-integrity group therefore failed its index assertion. Its captured index digest is recorded in the JSON report.
- Independently produced content comparison data reports no mismatches in any of these seven categories on 43 of 43 routes: text, title, headings, links, images, picture sources and JSON-LD. The content comparison artifact hash is included in the machine-readable report. The original comparator status remains FAIL because it also used the missing index field.

## Browser matrix and target findings

- The log has all 306 completion lines and each reports `hidden=0`. No overflow assertion failure was emitted before the target-size comparison stopped the group.
- The runner emitted 20 target-shrink examples, all from the Home 360px normal, JavaScript-on case. Width deltas range from -4.72px to -35.38px; the measured heights are 1px larger than baseline. Examples include Mysuru at 58.47 x 19px baseline and 50.86 x 20px current, and the route-specific checklist link at 298.11 x 46.19px baseline and 262.73 x 47.19px current. Nineteen of the 20 emitted examples have current heights below 44px. These are examples only, not the total number of changed rectangles.
- No current below-44px total was produced. The separate 44px audit did not execute, so no current compliance claim is made.

## Axe result

Fresh Chromium process per route, axe-core 4.11.0, rulesets WCAG 2.0 A/AA and WCAG 2.1 A/AA:

| Route | Existing baseline nodes | New identities |
| --- | ---: | ---: |
| Home | 8 | 0 |
| Services | 21 | 0 |
| About | 5 | 0 |
| Contact | 2 | 0 |

This is a baseline-relative result. It does not claim zero existing violations or certify other routes.

## Blank-space scan and Contact tails

- Completed 516 of 516 cases with HTTP 200. The scan recorded 1,147 pixel quiet-band candidates versus 1,171 after Phase31, a change of -24; zero hidden reveal-text findings; and 16 intentional scroll-indicator dismissals, unchanged from Phase31.
- There were eight `unused-min-height-tail` DOM screening candidates. Four are the already documented Contact `#miniHero` tails, four states at each width. The remaining four are Home `#team` cases at 1280px across JavaScript and motion states.
- Contact `#miniHero` measurements were stable across all four states per width. The section and min-height were 792px, with a 30px cue-to-hero-bottom gap. The prior Contact tail disposition remains unchanged.

| Width | Current scan tail | Focused inspector | Phase31 after-scan value | Change |
| ---: | ---: | ---: | ---: | ---: |
| 360px | 185px | 184.53px | 138px | +47px |
| 768px | 245px | 244.94px | 233px | +12px |
| 1280px | 192px | 192.34px | Not reported | Not comparable |

- The Home `#team` candidate has a 202px measured tail after 110px bottom padding, a section height of 962.188px, 490 visible text characters, seven visible media elements and no hidden text. It has no saved crop. It remains unclassified, not confirmed removable space. No source or layout change was made.

## Remaining failures and interpretation

The suite result remains **FAIL**. The nine marked failures are: (1) missing route-index hash field in render integrity, (2) text/link/image/picture-source comparator status affected by that same check, (3) JSON-LD comparator status affected by that same check, (4) rendered discovery check blocked by missing native `php`, (5) rendered publication review blocked by missing native `php`, (6) incomplete palette run after Chromium closed, (7) target-baseline rectangle shrink comparison, (8) 44px audit not run because its input JSON was not written, and (9) the unclassified Home `#team` blank-space candidate. The semantic route content comparison itself matched all 43 routes.

The one-shot run is preserved as observed. No group was rerun, no source or layout change was made in response to the screening candidate, and these local results are not a live-site certification.
