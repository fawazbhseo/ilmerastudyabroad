# Phase32a six-route local A/B summary

## Protocol and scope

- Raw capture: [`phase-32a-6-route-ab-run-01-raw.json`](phase-32a-6-route-ab-run-01-raw.json), SHA-256 `73884a1e3b306dfb9ae5323c23eee22173cc466c32af396eae05ac4e89099875`. Raw was committed and pushed before this analysis.
- A: frozen Task4 source `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`. B rendered source: `b0dc2652c281720027e3d44ae0da6471a1b2c8fb`. Frozen fixture SHA-256 `31acc1582b723779b65a9c9f388f7fc4b864e197b3e2b5de21609842553a0aea`.
- 84 completed samples, seven per arm on each of six routes, alternating order, one fresh Chromium process per sample. Chromium `143.0.7499.0`, Playwright `1.58.2`, Lighthouse `12.8.2`.
- Local simulated mobile Lighthouse only, using the pinned local fixture and resource mirrors. This is not live-site or field data.
- Lighthouse warnings: 0.

## Median and IQR results

IQR is Q3 minus Q1, with quartiles linearly interpolated at `(n - 1) * p`. Arm cells show `median / IQR`. The paired LCP ratio uses seven within-round B/A pairs. The budget LCP ratio is B median divided by A median.
Paired ratios with a zero A denominator are omitted; those cells are descriptive only and not used by the fixed budget gates. The LCP budget uses ratio of arm medians.

| Route | LCP A ms med/IQR | LCP B ms med/IQR | LCP B/A medians | Paired LCP B/A med/IQR | TBT A ms med/IQR | TBT B ms med/IQR | TBT delta ms | CLS A med/IQR | CLS B med/IQR | CLS delta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `/study-in-germany` | 1198.67 / 55.65 | 1209.70 / 630.63 | 1.0092 | 1.0001 / 0.0634 | 0.00 / 5.00 | 46.00 / 76.00 | 46.00 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 |
| `/study-abroad-counselling-mysuru` | 1652.33 / 0.45 | 1728.17 / 314.39 | 1.0459 | 1.0456 / 0.1905 | 0.00 / 0.00 | 66.24 / 121.96 | 66.24 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1654.08 / 628.03 | 2355.84 / 628.15 | 1.4243 | 1.0451 / 0.2020 | 0.00 / 15.91 | 59.00 / 59.27 | 59.00 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 |
| `/blog/` | 2280.94 / 627.92 | 2281.15 / 314.78 | 1.0001 | 1.0002 / 0.5178 | 0.00 / 0.00 | 0.00 / 33.00 | 0.00 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 |
| `/services` | 8406.54 / 7382.41 | 2956.10 / 238.88 | 0.3516 | 0.3516 / 1.0615 | 2400.00 / 913.50 | 0.00 / 0.00 | -2400.00 | 0.000000 / 0.000000 | 0.000491 / 0.000747 | 0.000491 |
| `/contact` | 11358.83 / 5569.31 | 2730.69 / 401.92 | 0.2404 | 0.2404 / 0.5356 | 5166.00 / 1058.50 | 0.00 / 0.00 | -5166.00 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 |

Paired per-round changes are included because local timings are variable. Each cell below is the median / IQR of seven round-level B minus A differences.

| Route | LCP delta ms med/IQR | TBT delta ms med/IQR | CLS delta med/IQR | Transfer delta bytes med/IQR | Transfer paired B/A med/IQR | TBT paired B/A med/IQR | CLS paired B/A med/IQR |
|---|---:|---:|---:|---:|---:|---:|---:|
| `/study-in-germany` | 0.32 / 74.96 | 33.50 / 76.00 | 0.000000 / 0.000000 | 13278 / 0 | 1.0665 / 0.0000 | 27.6900 / 24.0100 | n/a |
| `/study-abroad-counselling-mysuru` | 75.34 / 314.71 | 66.24 / 111.46 | 0.000000 / 0.000000 | 13387 / 0 | 1.0574 / 0.0000 | 5.6716 / 0.0000 | n/a |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 74.85 / 314.10 | 33.34 / 38.85 | 0.000000 / 0.000000 | 13387 / 0 | 1.0555 / 0.0000 | 2.1861 / 20.3350 | n/a |
| `/blog/` | 0.50 / 942.79 | 0.00 / 9.00 | 0.000000 / 0.000000 | 3473 / 0 | 1.0149 / 0.0000 | 0.8691 / 0.0000 | n/a |
| `/services` | -5450.68 / 7366.22 | -2400.00 / 913.50 | 0.000491 / 0.000747 | -564546 / 0 | 0.4002 / 0.0000 | 0.0000 / 0.0000 | n/a |
| `/contact` | -8628.13 / 5471.79 | -5166.00 / 1058.50 | 0.000000 / 0.000000 | -574182 / 0 | 0.3674 / 0.0000 | 0.0000 / 0.0000 | n/a |

| Route | Transfer A bytes med/IQR | Transfer B bytes med/IQR | Added median bytes | Transfer B/A medians | Requests A med/IQR | Requests B med/IQR | Still requests A/B | New render-blocking URLs | Budget/fallback decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `/study-in-germany` | 199593 / 0 | 212871 / 0 | 13278 | 1.0665 | 4 / 0 | 5 / 0 | 0/7 | none | PASS |
| `/study-abroad-counselling-mysuru` | 233190 / 0 | 246577 / 0 | 13387 | 1.0574 | 6 / 0 | 7 / 0 | 0/7 | none | FAIL; fallback to palette required |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 241106 / 0 | 254493 / 0 | 13387 | 1.0555 | 6 / 0 | 7 / 0 | 0/7 | none | FAIL; fallback to palette required |
| `/blog/` | 232501 / 0 | 235974 / 0 | 3473 | 1.0149 | 6 / 0 | 6 / 0 | 0/0 | none | PASS |
| `/services` | 941152 / 0 | 376606 / 0 | -564546 | 0.4002 | 7 / 0 | 11 / 0 | 0/0 | none | CONTROL ONLY |
| `/contact` | 907681 / 0 | 333499 / 0 | -574182 | 0.3674 | 7 / 0 | 11 / 0 | 0/0 | none | CONTROL ONLY |

## Budget outcome

- Treatment targets meeting all unchanged budgets: **2/4**.
- Target fallback routes: `/study-abroad-counselling-mysuru`, `/blog/how-to-choose-study-abroad-consultant-karnataka`.
- Services and Contact symmetric median-LCP control gate: **FAIL**. They are measurement controls with pre-existing shared Phase32 presentation differences and cannot be changed in this phase.
- `performance_release_certified=false` remains unchanged.
- Fixed budgets: added transfer strictly below 150,000 bytes; median LCP B/A at most 1.10; median TBT increase at most 50 ms; median CLS no worse than A and below 0.1; no new render-blocking URL. No budget was relaxed.

| Control route | B/A median LCP | Symmetric ratio | Control gate |
|---|---:|---:|---|
| `/services` | 0.3516 | 2.8438 | FAIL |
| `/contact` | 0.2404 | 4.1597 | FAIL |

### `/study-in-germany`: PASS
- No median-based budget failure.
- Median deltas: transfer 13278 bytes; TBT 46.00 ms; CLS 0.000000; median LCP ratio 1.0092.
- Required palette fallback: no
### `/study-abroad-counselling-mysuru`: FAIL
- median TBT delta 66.24 ms exceeds 50 ms
- Median deltas: transfer 13387 bytes; TBT 66.24 ms; CLS 0.000000; median LCP ratio 1.0459.
- Required palette fallback: yes
### `/blog/how-to-choose-study-abroad-consultant-karnataka`: FAIL
- median LCP B/A 1.4243 exceeds 1.10
- median TBT delta 59.00 ms exceeds 50 ms
- Median deltas: transfer 13387 bytes; TBT 59.00 ms; CLS 0.000000; median LCP ratio 1.4243.
- Required palette fallback: yes
### `/blog/`: PASS
- No median-based budget failure.
- Median deltas: transfer 3473 bytes; TBT 0.00 ms; CLS 0.000000; median LCP ratio 1.0001.
- Required palette fallback: no
### `/services`: CONTROL ONLY
- control-only observation: CLS failed
- Median deltas: transfer -564546 bytes; TBT -2400.00 ms; CLS 0.000491; median LCP ratio 0.3516.
### `/contact`: CONTROL ONLY
- No median-based budget failure.
- Median deltas: transfer -574182 bytes; TBT -5166.00 ms; CLS 0.000000; median LCP ratio 0.2404.

## Interpretation limits

Single-session local simulated mobile Lighthouse data only. B/A compares pushed B renders with frozen Task4 A and includes prior shared Phase32 presentation differences. Services and Contact are controls, not byte-identical no-op controls. Do not describe these results as field performance.
The Blog index mobile guard intentionally skips the hero still at viewport widths at or below 768px; the mobile B samples therefore made no still request on /blog/.

Font request, still request, render-blocking URL and warning details are preserved in the raw JSON and the companion summary JSON. No font change has been made based on this report.
