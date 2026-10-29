# Phase32 frozen-A 11-route Lighthouse A/B, run 01

## Protocol and limits

- Complete local-only Lighthouse mobile simulated Slow4G and 4x CPU run. Chromium 143.0.7499.0, Playwright 1.58.2 and Lighthouse 12.8.2. Seven alternating rounds per route, fresh Chromium process per arm sample, serial execution, no retries or resume. All 154 samples completed: 77 A and 77 B, with zero Lighthouse warnings.
- A is the immutable pre-Phase32 render from `796879d7b3d5ca0fa1e398562e937e9f364a5f62`; B is the render captured from application source `e193be3036dff6a4f95923460a2525226faaae35`. The paired fixture SHA-256 is `1edc4a65117c748ffdf42d9417398f4e87e7b46be97ade30ef941df7d98fa5a7`. Fixture details and per-route HTML hashes are in `reports/phase-32-11-route-ab-fixtures.json`.
- Raw sample data: `reports/phase-32-11-route-ab-run-01-results.json`, SHA-256 `83e29ce1aaf2086ed39068b51a7b83ad83e908cecec97b6302bac0f99f475d25`. Local resource mirrors were used. No live CDN, native-hosting or field data is represented.
- Medians and IQRs use the runner percentile method across seven samples per arm. Transfer is Lighthouse total-byte-weight, not a deployment transfer measurement. Ratios are B median LCP / A median LCP.

## 11-route before/after medians and IQRs

| Route | LCP ms A -> B, median / IQR | CLS A -> B, median / IQR | TBT ms A -> B, median / IQR | Transfer bytes A -> B (delta) | Requests A -> B | LCP B/A | Route gate |
|---|---:|---:|---:|---:|---:|---:|---|
| `/` | 9371.2 / 7921.7 -> 3662.2 / 494.9 | 0.000749 / 0.000020 -> 0.055063 / 0.000927 | 2263.5 / 639.5 -> 0.0 / 0.0 | 1,068,477 -> 352,654 (-715,823) | 15 -> 12 | 0.3908 | FAIL: cls |
| `/services` | 10052.4 / 173.4 -> 3811.4 / 690.0 | 0.000000 / 0.000000 -> 0.026096 / 0.027742 | 2509.0 / 168.2 -> 0.0 / 0.0 | 1,093,036 -> 377,213 (-715,823) | 15 -> 12 | 0.3792 | FAIL: cls |
| `/about` | 9275.1 / 268.2 -> 3511.8 / 187.6 | 0.008559 / 0.006608 -> 0.020411 / 0.010698 | 1900.0 / 251.5 -> 0.0 / 0.0 | 1,047,238 -> 331,374 (-715,864) | 15 -> 12 | 0.3786 | FAIL: cls |
| `/contact` | 10851.3 / 5542.6 -> 3106.4 / 675.0 | 0.000000 / 0.000000 -> 0.000000 / 0.000717 | 3757.0 / 1047.7 -> 0.0 / 0.0 | 1,049,773 -> 333,950 (-715,823) | 15 -> 12 | 0.2863 | PASS |
| `/study-in-germany` | 1427.5 / 502.2 -> 1176.2 / 24.1 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 46.0 -> 46.5 / 42.0 | 225,134 -> 212,777 (-12,357) | 5 -> 5 | 0.8240 | PASS |
| `/study-in-italy` | 1427.5 / 0.7 -> 1169.2 / 38.2 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 3.0 / 7.5 -> 3.5 / 48.2 | 223,100 -> 210,744 (-12,356) | 5 -> 5 | 0.8191 | PASS |
| `/study-abroad-counselling-mysuru` | 1802.5 / 74.7 -> 1727.2 / 352.0 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 15.0 / 49.2 | 258,731 -> 246,483 (-12,248) | 7 -> 7 | 0.9582 | PASS |
| `/study-abroad-counselling-bengaluru` | 2430.9 / 591.0 -> 1727.2 / 314.5 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 2.0 -> 0.0 / 53.8 | 258,829 -> 246,581 (-12,248) | 7 -> 7 | 0.7105 | PASS |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1802.1 / 0.8 -> 1727.6 / 628.7 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 4.0 -> 0.0 / 72.5 | 266,647 -> 254,399 (-12,248) | 7 -> 7 | 0.9586 | PASS |
| `/blog/cost-of-studying-abroad-for-indian-students` | 1952.5 / 75.7 -> 1802.2 / 0.9 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 0.0 -> 0.0 / 33.3 | 281,188 -> 268,940 (-12,248) | 8 -> 8 | 0.9230 | PASS |
| `/blog/` | 1877.0 / 554.1 -> 1727.1 / 314.8 | 0.000000 / 0.000000 -> 0.000000 / 0.000000 | 0.0 / 4.0 -> 59.3 / 25.8 | 258,042 -> 245,794 (-12,248) | 7 -> 7 | 0.9201 | FAIL: tbt |

## Budget findings

- **7 of 11 route gates passed.** The four failures are Home (CLS), Services (CLS), About (CLS) and the blog index (TBT delta). Every route passes the LCP ratio limit, added-transfer limit and no-new-render-blocking check. B total-byte-weight medians are lower than A on all 11 routes.
- Blog index B median TBT is 59.3ms versus A 0ms, exceeding the unchanged +50ms limit by 9.3ms. This is a real measured budget miss. Keep the raw failure visible; do not round it into a pass.
- Three reference routes have worse B CLS medians than A: Home 0.055063 vs 0.000749, Services 0.026096 vs 0, About 0.020411 vs 0.008559. Each B CLS is below 0.1, but the no-worse-than-baseline gate fails. Contact passes with both medians 0. Reference pages therefore do **not** pass all owner budgets.
- Reference B median LCPs are Home 3,662.2ms, Services 3,811.4ms, About 3,511.8ms and Contact 3,106.4ms, all at or below 4,000ms. However, individual B samples exceed 4,000ms on Home (3/7, max 4,157.3ms) and Services (2/7, max 4,232.5ms). Reference B median TBT is 0ms for all four routes and below 600ms in this mobile simulation. These mobile results exclude the deferred desktop scene path and do not certify desktop TBT.
- The separate post-change resource audit measured local uncompressed pre-scene response bodies of 351,606 bytes Home, 376,165 Services, 330,327 About and 318,871 Contact at 360px. All are below 400,000 bytes in that local audit, not verified compressed network transfer.
- The 7 target pages requested the 640px WebP still once in every B sample: 9,738 resource bytes and 9,914 transfer bytes, HTTP 200. The A arm requested the prior 720px WebP at 24,574 resource bytes and 24,751 transfer bytes. B therefore uses a smaller mobile still and makes no additional request relative to A. The mobile still is below 14KB.
- The raw runner reports `control_reliable=false`. The inherited Phase31 field treated the four reference pages as unchanged controls, but those pages are intentionally changed Phase32 treatments. This false value is not an unchanged-control stability test and must not be described as a failed sample or as a valid Phase32 control gate. It also must not be re-labeled as a pass. All samples completed; the report remains uncertified.
- The one-sample desktop browser probes separately observed long tasks of 1,827ms About and 3,682ms Contact during scene startup. Those are not Lighthouse TBT. The desktop scene path remains flagged pending a direct desktop budget check.

## Route-by-route outcome

- PASS: Contact, Germany, Italy, Mysuru, Bengaluru, the how-to-choose article and the cost article.
- FAIL: Home, Services and About due to CLS worse than A; blog index due to B TBT median 59.3ms vs A 0ms.
- Overall session: complete raw data, 7/11 route gates, `performance_release_certified=false`. No release, deployment or field-speed claim is supported.
