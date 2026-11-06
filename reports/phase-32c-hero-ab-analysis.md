# Phase32c Task 3 hero-still A/B analysis

## Scope and raw evidence

This is a local simulated Lighthouse analysis, not PageSpeed Insights, field data, production/CDN timing or a live-site performance claim. The committed raw input is `reports/phase-32c-hero-ab-raw.json` (585,625 bytes, SHA-256 `039eb45d973b00844df525665d1ce6d6ebfb7a592c2db93dc0758aadd4e8351b`), committed as `9ad242e` before analysis. All 63 planned fresh-browser sample rows passed collection QA.

Routes: `/study-abroad-counselling-mysuru` and `/blog/how-to-choose-study-abroad-consultant-karnataka`. A source: `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`. Current B source: `ac2d9b06dc85578e4b4c31ad236b228f67d44333`. Each primary arm has nine samples per route; Mysuru includes nine additional adjacent A/A pairs.

## Median and IQR results

| Route | Arm | n | LCP median (ms) | LCP IQR | CLS median | CLS IQR | TBT median (ms) | TBT IQR | Transfer median (bytes) | Transfer IQR | Requests median | Requests IQR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `/study-abroad-counselling-mysuru` | A | 9 | 1652.655 | 629.025 | 0.000 | 0.000 | 0.000 | 0.000 | 224797.000 | 0.000 | 6.000 | 0.000 |
| `/study-abroad-counselling-mysuru` | B-still | 9 | 1726.861 | 554.690 | 0.000 | 0.000 | 0.000 | 0.000 | 238217.000 | 0.000 | 7.000 | 0.000 |
| `/study-abroad-counselling-mysuru` | B-plain | 9 | 1653.130 | 629.052 | 0.000 | 0.000 | 0.000 | 0.000 | 225499.000 | 0.000 | 6.000 | 0.000 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | A | 9 | 1652.193 | 0.362 | 0.000 | 0.000 | 0.000 | 0.000 | 238734.000 | 0.000 | 6.000 | 0.000 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-still | 9 | 1726.814 | 629.088 | 0.000 | 0.000 | 0.000 | 9.184 | 252154.000 | 0.000 | 7.000 | 0.000 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-plain | 9 | 1651.803 | 74.536 | 0.000 | 0.000 | 0.000 | 0.000 | 239436.000 | 0.000 | 6.000 | 0.000 |

## Paired-round ratios and deltas

LCP ratios are candidate/A for the same route and round. TBT, CLS and transfer fields are B minus A. Values are listed for all nine rounds.

### `/study-abroad-counselling-mysuru`

| Round | B-still/A LCP | B-still TBT delta (ms) | B-plain/A LCP | B-plain TBT delta (ms) |
|---:|---:|---:|---:|---:|
| 1 | 0.7239 | 0.000 | 0.9993 | 0.000 |
| 2 | 0.7570 | 2.470 | 1.0001 | 0.000 |
| 3 | 1.0951 | 0.000 | 1.0475 | 0.000 |
| 4 | 1.0454 | 0.000 | 0.9996 | 0.000 |
| 5 | 0.7571 | 0.000 | 0.7241 | 0.000 |
| 6 | 1.4262 | 0.000 | 1.3810 | 0.000 |
| 7 | 0.9995 | 0.000 | 1.0003 | 0.000 |
| 8 | 1.3801 | 0.000 | 1.0005 | 0.000 |
| 9 | 1.4938 | 11.110 | 1.0479 | 0.000 |
### `/blog/how-to-choose-study-abroad-consultant-karnataka`

| Round | B-still/A LCP | B-still TBT delta (ms) | B-plain/A LCP | B-plain TBT delta (ms) |
|---:|---:|---:|---:|---:|
| 1 | 0.9996 | 0.000 | 0.9996 | 0.000 |
| 2 | 1.4262 | 0.000 | 1.0000 | 0.000 |
| 3 | 1.0327 | 0.000 | 0.7240 | 0.000 |
| 4 | 0.9999 | 0.000 | 0.9998 | 0.000 |
| 5 | 1.0456 | 1.318 | 1.0004 | 0.000 |
| 6 | 1.4259 | 33.370 | 0.9547 | 0.000 |
| 7 | 0.7572 | 9.184 | 0.7242 | 0.000 |
| 8 | 1.0450 | 31.000 | 0.9540 | 0.000 |
| 9 | 1.0451 | 0.000 | 0.9543 | 0.000 |

## A/A noise floor

Nine paired fresh-browser repeats on Mysuru compare the primary A sample with its adjacent A-repeat sample. The maximum observed absolute differences are used only as a stricter decision margin, not as a confidence interval. The same-harness Mysuru noise proxy is applied to the article route because no separate article A/A block was collected.

| Metric | Median | IQR | Maximum observed |
|---|---:|---:|---:|
| Absolute LCP difference (ms) | 75.331 | 627.202 | 703.968 |
| A-repeat/A LCP ratio | 1.0002 | 0.0910 | max absolute deviation from 1 = 0.4464 |
| Absolute TBT difference (ms) | 0.000 | 0.000 | 0.000 |
| Absolute CLS difference | 0.000000 | 0.000000 | 0.000000 |
| Absolute transfer difference (bytes) | 0.000 | 0.000 | 98454.000 |

The maximum A/A transfer difference occurred in round 4: A had 1 logo network entry and A-repeat had 2 entries, each audited with status [200, 200]. The raw transfer difference was 98454 bytes.

## Fixed budget gates

| Route | Arm | Added transfer <150,000 B | No new render blocker | LCP ratio <=1.10 | TBT increase <=50 ms | CLS no worse and <0.1 | Point result | Transfer + A/A max | Noise-adjusted still margin |
|---|---|---|---|---|---|---|---|---|---|
| `/study-abroad-counselling-mysuru` | B-still | 13420.000 B, PASS | PASS | 1.0449, PASS | 0.000 ms, PASS | 0.000000, PASS | PASS | 111874.000 B, PASS | INCONCLUSIVE |
| `/study-abroad-counselling-mysuru` | B-plain | 702.000 B, PASS | PASS | 1.0003, PASS | 0.000 ms, PASS | 0.000000, PASS | PASS | 99156.000 B, PASS | INCONCLUSIVE |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-still | 13420.000 B, PASS | PASS | 1.0452, PASS | 0.000 ms, PASS | 0.000000, PASS | PASS | 111874.000 B, PASS | INCONCLUSIVE |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-plain | 702.000 B, PASS | PASS | 0.9998, PASS | 0.000 ms, PASS | 0.000000, PASS | PASS | 99156.000 B, PASS | INCONCLUSIVE |

New render-blocking URL sets are in `reports/phase-32c-hero-ab-analysis.json`. Hero-still network requests per arm are recorded there as well.

## Sample quality and still requests

All 63 Lighthouse runs emitted 0 Lighthouse run warnings. The raw browser request-failure listener recorded 126 events. Distinct URL/reason pairs: `chrome://terms/` `net::ERR_INVALID_URL` x63; `https://ilmerastudyabroad.com/assets/images/ilmera.logo.png` `net::ERR_ABORTED` x63.
The `ilmera.logo.png` network-audit status counts are `{'200': 64}`. The internal `chrome://terms/` failure and aborted logo event remain in raw diagnostics; no console or page-error assertion is made because those events were not collected.
The maximum A/A transfer difference was 98454 bytes in round 4, where the logo appeared 1 time in A and 2 times in A-repeat. Both A-repeat logo network-audit entries had status `[200, 200]`.

| Route | Arm | Samples with still request | Still requests | URLs | Median bytes per still request |
|---|---|---:|---:|---|---:|
| `/study-abroad-counselling-mysuru` | A | 0 | 0 | none | - |
| `/study-abroad-counselling-mysuru` | B-still | 9 | 9 | http://127.0.0.1:8091/assets/images/hero-still-640.webp | 9947 |
| `/study-abroad-counselling-mysuru` | B-plain | 0 | 0 | none | - |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | A | 0 | 0 | none | - |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-still | 9 | 9 | http://127.0.0.1:8091/assets/images/hero-still-640.webp | 9947 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B-plain | 0 | 0 | none | - |

## Conservative decision

Select B-still only if it passes all five point-estimate budgets on both routes and transfer, LCP, TBT and CLS remain inside those limits after adding the maximum observed Mysuru A/A absolute noise margin. Any failed point budget or unresolved noise-adjusted margin retains B-plain. The added noise margin is stricter than the owner limits and cannot relax them.

**Decision: retain `B-plain`.** All point-estimate budgets pass for both B arms on both routes. B-still median LCP ratios are 1.0449 and 1.0452, but the maximum Mysuru A/A ratio deviation is 0.4464; the noise-adjusted upper ratios are 1.4913 and 1.4916, above 1.10. This is inconclusive, not a point-budget failure. Retain B-plain as the conservative default, not as a proven faster arm.

Owner confirmation via PageSpeed Insights remains required. No PageSpeed Insights result was supplied or inferred.

## Fixture provenance note

The prior Phase31 Task4 fixture archive was retained unchanged, but its claimed A source commit does not match its stored A HTML on protected content for these two routes. This analysis uses a fresh PHP-WASM render of the exact A commit, with content parity validated across all three arms. See `reports/phase-32c-hero-ab-fixtures.json` for the specific differing fields.

## Reproducibility

Raw data hash: `039eb45d973b00844df525665d1ce6d6ebfb7a592c2db93dc0758aadd4e8351b`. Analysis script: `tools/phase32c/analyze-hero-ab.py`. Machine-readable results: `reports/phase-32c-hero-ab-analysis.json`. The run is simulated and local-only; it is not live-site verification.
