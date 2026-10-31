# Phase32 frozen-A 11-route Lighthouse A/B, run 02

## Protocol and limits

- Complete local-only Lighthouse mobile simulated Slow4G and 4x CPU run. Chromium 143.0.7499.0, Playwright 1.58.2 and Lighthouse 12.8.2. Seven alternating rounds per route, fresh Chromium process per sample, serial execution, no retries or resume. All 154 samples completed (77 A, 77 B) with zero Lighthouse warnings.
- A is the immutable pre-Phase32 render from `796879d7b3d5ca0fa1e398562e937e9f364a5f62`; candidate B application source is `4e709ed0cc6ec4e2b2a60d7d914765ae170634a0`. Frozen fixture SHA-256: `25708bdf3b527dc36ec50f08aaf568168419c10a5ac5c91ff5136064a966f8d5`. The committed per-route hashes and method are in `reports/phase-32-11-route-ab-fixtures.json`.
- Raw result: `reports/phase-32-11-route-ab-run-02-results.json`, SHA-256 `d886e44e6b94c7cdee639b172941dff7d72492c0a78eb2df4165608ff3ba5db9`. The run is local-only and uses exact local resource mirrors, not live CDN or field data. The runner preserves `performance_release_certified=false`.
- Medians and IQRs use the runner percentile method across seven samples per arm. The ratio is B median LCP divided by A median LCP. Transfer is Lighthouse total-byte-weight, not deployed compressed transfer.

## 11-route before/after medians and IQRs

| Route | LCP ms A median / IQR -> B median / IQR | B/A | CLS A median / IQR -> B median / IQR | TBT ms A median / IQR -> B median / IQR | Transfer bytes A -> B (delta) | Requests A -> B | Gate |
|---|---:|---:|---:|---:|---:|---:|---|
| `/` | 1831.2 / 6985.7 -> 2956.3 / 0.6 | 1.6144 | 0.000759 / 0.000010 -> 0.000000 / 0.000728 | 1097.5 / 263.0 -> 0.0 / 0.0 | 1,068,477 -> 352,203 (-716,274) | 15 -> 11 | FAIL (lcp) |
| `/services` | 9244.2 / 3782.1 -> 2477.6 / 478.7 | 0.2680 | 0.000000 / 0.001840 -> 0.000000 / 0.000614 | 1649.0 / 247.0 -> 0.0 / 0.0 | 1,093,036 -> 376,606 (-716,430) | 15 -> 11 | PASS |
| `/about` | 8729.3 / 101.9 -> 2730.6 / 402.5 | 0.3128 | 0.006588 / 0.004747 -> 0.000000 / 0.000000 | 1328.0 / 107.0 -> 0.0 / 0.0 | 1,047,238 -> 330,923 (-716,315) | 15 -> 11 | PASS |
| `/contact` | 10930.5 / 5460.5 -> 2730.9 / 201.9 | 0.2498 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 3552.0 / 1527.5 -> 0.0 / 0.0 | 1,049,773 -> 333,499 (-716,274) | 15 -> 11 | PASS |
| `/study-in-germany` | 1426.9 / 502.1 -> 1159.9 / 30.9 | 0.8129 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 1.5 / 23.5 | 225,134 -> 212,871 (-12,263) | 5 -> 5 | PASS |
| `/study-in-italy` | 1427.5 / 0.5 -> 1116.8 / 36.5 | 0.7824 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 11.0 / 12.5 -> 45.0 / 87.5 | 223,100 -> 210,838 (-12,262) | 5 -> 5 | PASS |
| `/study-abroad-counselling-mysuru` | 1876.5 / 75.2 -> 1727.2 / 352.2 | 0.9205 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 0.0 / 0.0 | 258,731 -> 246,577 (-12,154) | 7 -> 7 | PASS |
| `/study-abroad-counselling-bengaluru` | 2430.7 / 591.4 -> 2355.7 / 629.2 | 0.9692 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 4.4 / 51.8 | 258,829 -> 246,675 (-12,154) | 7 -> 7 | PASS |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1802.1 / 352.0 -> 1726.7 / 314.9 | 0.9582 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 0.0 / 0.2 | 266,647 -> 254,493 (-12,154) | 7 -> 7 | PASS |
| `/blog/cost-of-studying-abroad-for-indian-students` | 1801.8 / 75.3 -> 2430.5 / 628.9 | 1.3490 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 0.0 / 0.0 | 281,188 -> 269,034 (-12,154) | 8 -> 8 | FAIL (lcp) |
| `/blog/` | 1877.4 / 628.8 -> 2281.0 / 0.3 | 1.2150 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 0.0 / 0.0 | 258,042 -> 235,974 (-22,068) | 7 -> 6 | FAIL (lcp) |

## Budget findings

- **8 of 11 route gates passed.** Home, `/blog/cost-of-studying-abroad-for-indian-students`, and `/blog/` fail the LCP ratio limit. All 11 routes pass the added-transfer, TBT-delta, CLS no-worse-than-A, CLS-under-0.1, and no-new-render-blocking checks. `performance_release_certified` remains false.
- Home B median LCP is 2,956.3ms versus A 1,831.2ms (ratio 1.6144). It is under the absolute 4,000ms reference ceiling but fails the 110% baseline ratio. A has a very broad LCP IQR of 6,985.7ms, so its samples are strongly multimodal; preserve the median and IQR and do not dismiss the failed gate.
- The cost article B median is 2,430.5ms versus A 1,801.8ms (ratio 1.3490). The blog index B median is 2,281.0ms versus A 1,877.4ms (ratio 1.2150). For both, the A LCP element was the hero section; B correctly keeps text as LCP (`.seo-opening` for the article and `.sub` for the index) under the explicit Phase32 requirement. The changed LCP candidate does not waive the measured ratio failures.
- The earlier run01 Blog-index mobile TBT miss is not reproduced in run02: B median TBT is 0ms versus A 0ms, with no worse CLS. This is mobile simulation only. Required desktop Blog TBT remains open.
- All four reference B medians are below 4,000ms: Home 2,956.3ms, Services 2,477.6ms, About 2,730.6ms, Contact 2,730.9ms. Reference B median TBT is 0ms on all four and CLS medians are 0, 0, 0, 0 respectively. Those are mobile results and do not prove the desktop-scene TBT budget.
- All transfer deltas are negative; the largest reduction is 716,430 bytes on Services. There are no new render-blocking URLs on any route. B requested one 640px WebP in every sample for six template routes (42 requests total, 9,738 resource bytes / 9,914 transfer bytes each, HTTP 200); the Blog-index mobile palette guard made zero still requests. A requested the prior 720px WebP on those six routes. No reference route requests a new still.
- The separate eight-case local reference audit measured pre-scene uncompressed body bytes: Home 350,534 mobile / 364,566 desktop; Services 374,937 / 388,969; About 329,255 / 329,255; Contact 317,799 / 331,831. All are below 400,000, with Services desktop only 11,031 bytes of headroom. These are not compressed production transfer values.
- CLS B medians are no worse than A on every route. Reference Home B CLS is 0 versus A 0.000759; Services 0 versus 0; About 0 versus 0.006588; Contact 0 versus 0. The CLS gate passes in this mobile experiment. B TBT also passes the unchanged +50ms delta on all routes.
- No unchanged controls were selected: the four reference pages are Phase32 treatments. `control_reliability_applicable=false` is intentional. This does not turn any route result into a performance pass.

## Route-by-route outcome

- PASS: Services, About, Contact, Germany, Italy, Mysuru, Bengaluru, the how-to-choose article.
- FAIL: Home, the cost article, Blog index, all due to the LCP B/A ratio only.
- **Overall: complete raw 154-sample run, 8/11 local route gates passed, 3 LCP-ratio failures, not release certified.** Do not report this as an all-budget performance pass. Desktop Blog TBT, Contact `#miniHero` tails, visual safeguards, and the final current-HEAD ZIP verification remain open.
