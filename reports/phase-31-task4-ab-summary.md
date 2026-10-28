# Task4 local A/B result summary

## Scope and evidence

This is the single local-only comparison of the frozen Task2 source (A, `7d1bb9e`) against Task3 with the approved static still CSS (B, `806769a`). It uses the eight routes in the fixed protocol, with four byte-identical reference controls and four treatment routes. This is not a live-site, CDN, field Core Web Vitals, release, merge, or deployment result.

- Run: 2026-10-28T12:13:04.419Z to 2026-10-28T12:26:00.084Z.
- Samples: 112 total, 56 A and 56 B. All 112 samples completed with `PASS`; the capture contains zero Lighthouse warnings. No sample was retried or resumed.
- Runtime: Chromium 143.0.7499.0, Playwright 1.58.2, Lighthouse 12.8.2; Lighthouse mobile simulated Slow4G and 4x CPU.
- Fixture SHA-256: `806e5ab8df048c1bda227211a57a67fe8331b6121a045eccc43c8c5629d2f1d6`. Raw report: [`phase-31-task4-ab-results.json`](phase-31-task4-ab-results.json), SHA-256 `f4fed8a08a8f6d683af398ef44001cc48aca5b63f5f2cc537670cbc514d10cd0`.
- The pre-navigation Chromium startup diagnostic is preserved separately in `phase-31-task4-ab-preflight-failure.json`; it did not navigate a page or contribute a sample.

## Findings

- **Median-LCP control gate: PASS (4/4 controls).** The protocol compares the symmetric ratio `max(B/A, A/B)` with 1.10. This is a median-only gate, not proof that local variance is low. In particular, the measured LCP IQRs are broad on `/` A (4,137 ms), `/services` B (7,872 ms), and `/contact` A/B (4,980/8,906 ms).
- **Per-route local budget gate: 2/8 PASS.** Passing routes: `/contact`, `/study-abroad-counselling-mysuru`. Failing routes: `/`, `/services`, `/about`, `/study-in-germany`, `/blog/how-to-choose-study-abroad-consultant-karnataka`, `/blog/`. These are diagnostic, one-session local results only.
- **Treatment-route still requests:** each target has A/B counts `0/7` for Germany, `0/7` for Mysuru, `0/7` for the article, and `0/7` for the blog index. Every B sample requested one 720px still (24,574 resource bytes, HTTP 200); A requested none. B's median total transfer was 25,541 bytes higher per target route, below the fixed 150,000-byte cap, with one additional request. No new render-blocking URLs were observed on any route.
- B's median LCP was higher than A on all four targets in this local simulator. B/A ratios were `/study-in-germany` 1.2233, `/study-abroad-counselling-mysuru` 1.0657, `/blog/how-to-choose-study-abroad-consultant-karnataka` 1.1366, `/blog/` 1.1362. Germany, the article, and the blog index fail the 1.10 LCP ratio budget; Mysuru stays within it and passes the other route budgets.
- `control_reliable` is true by the prespecified median-LCP rule, while `performance_release_certified` is false. The prescribed route budgets are not all met. Do not interpret any median as a live speed gain or make deployment or release claims from this capture.

## Control reliability calculation

| Control route | B/A median LCP | Symmetric ratio | Median control gate |
|---|---:|---:|---|
| `/` | 0.9955 | 1.0046 | PASS |
| `/services` | 0.9748 | 1.0259 | PASS |
| `/about` | 0.9842 | 1.0161 | PASS |
| `/contact` | 0.9607 | 1.0409 | PASS |

## Per-route budget results

The fixed checks are: added transfer below 150,000 bytes; median LCP ratio B/A no greater than 1.10; median TBT no greater than A plus 50 ms; median CLS no greater than A and below 0.1; and no new render-blocking URL.

| Route | Added transfer (B) | B/A median LCP | Failed check(s) | Local route gate |
|---|---:|---:|---|---|
| `/` | 0 | 0.9955 | CLS (0.000779 > 0.000769) | FAIL |
| `/services` | 0 | 0.9748 | TBT (+115.00 ms > 50 ms); CLS (0.003891 > 0.000000) | FAIL |
| `/about` | 0 | 0.9842 | CLS (0.006346 > 0.004126) | FAIL |
| `/contact` | 0 | 0.9607 | None | PASS |
| `/study-in-germany` | 25541 | 1.2233 | LCP (1.2233 > 1.10) | FAIL |
| `/study-abroad-counselling-mysuru` | 25541 | 1.0657 | None | PASS |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 25541 | 1.1366 | LCP (1.1366 > 1.10) | FAIL |
| `/blog/` | 25541 | 1.1362 | LCP (1.1362 > 1.10) | FAIL |

## Medians and IQRs

Each cell is `median / IQR` over seven samples for that route and arm. Quartiles use linear interpolation at `(n - 1) * p` for p = 0.25 and 0.75, matching the runner. Transfer is in bytes, requests are counts, and CLS is unitless. Full samples, Q1/Q3, render-blocking URLs, still requests, font records, passive observations, and warnings remain in the raw JSON.

| Route | Arm | LCP ms median / IQR | CLS median / IQR | TBT ms median / IQR | Transfer bytes median / IQR | Requests median / IQR |
|---|---:|---:|---:|---:|---:|---:|
| `/` | A | 9414.44 / 4137.00 | 0.000769 / 0.000040 | 1909.00 / 350.25 | 1067769 / 0 | 15 / 0 |
| `/` | B | 9371.80 / 245.51 | 0.000779 / 0.000025 | 1911.00 / 271.00 | 1067769 / 0 | 15 / 0 |
| `/services` | A | 9882.53 / 478.60 | 0.000000 / 0.001843 | 2470.00 / 481.25 | 1093036 / 0 | 15 / 0 |
| `/services` | B | 9633.24 / 7872.27 | 0.003891 / 0.034855 | 2585.00 / 606.25 | 1093036 / 0 | 15 / 0 |
| `/about` | A | 9389.27 / 121.15 | 0.004126 / 0.002744 | 1928.00 / 208.75 | 1046673 / 0 | 15 / 0 |
| `/about` | B | 9240.71 / 106.60 | 0.006346 / 0.003829 | 1869.00 / 129.00 | 1046673 / 0 | 15 / 0 |
| `/contact` | A | 10994.48 / 4979.73 | 0.000000 / 0.005142 | 3617.00 / 631.50 | 1049773 / 0 | 15 / 0 |
| `/contact` | B | 10562.91 / 8905.96 | 0.000000 / 0.000000 | 3342.50 / 472.50 | 1049773 / 0 | 15 / 0 |
| `/study-in-germany` | A | 1166.90 / 55.56 | 0.000000 / 0.000000 | 15.50 / 45.50 | 199593 / 0 | 4 / 0 |
| `/study-in-germany` | B | 1427.50 / 0.91 | 0.000000 / 0.000000 | 2.00 / 43.23 | 225134 / 0 | 5 / 0 |
| `/study-abroad-counselling-mysuru` | A | 2280.90 / 313.95 | 0.000000 / 0.000000 | 0.00 / 0.00 | 233190 / 0 | 6 / 0 |
| `/study-abroad-counselling-mysuru` | B | 2430.80 / 628.70 | 0.000000 / 0.000000 | 0.00 / 7.50 | 258731 / 0 | 7 / 0 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | A | 1651.66 / 389.76 | 0.000000 / 0.000000 | 0.00 / 0.00 | 241106 / 0 | 6 / 0 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | B | 1877.25 / 352.18 | 0.000000 / 0.000000 | 0.00 / 0.00 | 266647 / 0 | 7 / 0 |
| `/blog/` | A | 1651.89 / 0.57 | 0.000000 / 0.000000 | 0.00 / 0.00 | 232501 / 0 | 6 / 0 |
| `/blog/` | B | 1876.89 / 628.61 | 0.000000 / 0.000000 | 0.00 / 0.00 | 258042 / 0 | 7 / 0 |

## Interpretation limits

All browser requests were routed through the local fixture and the checked-in resource handler or fulfilled from pinned local mirrors; unsupported external requests are aborted. URL strings retained in the report identify resources, not remote measurements. This single Lighthouse mobile simulation has substantial control-route spread and is not a field test. The result changes no site behavior, historical benchmark, release status, or merge/deployment decision.
