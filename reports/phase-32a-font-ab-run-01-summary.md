# Phase32a fresh font candidate A/B summary

## Protocol

- Raw capture was committed and pushed before analysis: [`phase-32a-font-ab-run-01-raw.json`](phase-32a-font-ab-run-01-raw.json), SHA-256 `23c8b48d8eb06051fd98b08c3910cc66787d4f2af68fce4826582e1048bb9769`.
- Frozen candidate fixture SHA-256 `734b060d00486d788f4e50bc5eaa82187f18edc7aa1850a820fad649f5737231`; A is current post-fallback font policy from `4746142eaea674b66549d20d4352f720018adee7`. B changes only seven `font-display:block` declarations to `swap` and removes the single body-visibility gate rule.
- 28 passing samples, seven per arm per route, alternating order, fresh Chromium per sample. Chromium 143.0.7499.0, Playwright 1.58.2, Lighthouse 12.8.2.
- Local simulated mobile Lighthouse only. Not field data.
- Warnings: 0.

## Results

Cells show `median / IQR`, with IQR based on linear interpolation at `(n - 1) * p`. Paired LCP deltas/ratios use the seven interleaved rounds.

| Route | LCP A ms med/IQR | LCP B ms med/IQR | B/A ratio of medians | Paired LCP B/A med/IQR | Paired LCP delta ms med/IQR | CLS A med/IQR | CLS B med/IQR | Paired CLS delta med/IQR | TBT A ms med/IQR | TBT B ms med/IQR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `/study-abroad-counselling-mysuru` | 1652.92 / 703.49 | 1652.88 / 629.00 | 1.0000 | 1.0001 / 0.0479 | 0.21 / 75.62 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.00 / 0.00 | 0.00 / 0.00 |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 1652.98 / 628.83 | 1654.64 / 628.35 | 1.0010 | 0.9999 / 0.0013 | -0.23 / 2.13 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.000000 / 0.000000 | 0.00 / 18.50 | 0.00 / 5.00 |

| Route | Transfer A bytes med/IQR | Transfer B bytes med/IQR | Transfer B/A ratio | Requests A med/IQR | Requests B med/IQR | Fonts requested A/B per sample | Candidate LCP lower | CLS median no worse | Decision |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| `/study-abroad-counselling-mysuru` | 233892 / 0 | 233839 / 0 | 0.9998 | 6 / 0 | 6 / 0 | [4, 4, 4, 4, 4, 4, 4]/[4, 4, 4, 4, 4, 4, 4] | yes | yes | route criteria met |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 241808 / 0 | 241755 / 0 | 0.9998 | 6 / 0 | 6 / 0 | [4, 4, 4, 4, 4, 4, 4]/[4, 4, 4, 4, 4, 4, 4] | no | yes | route criteria fail |

The route-level column is diagnostic only. Adoption requires both routes to pass.

## Decision

**Keep the current font policy; candidate does not qualify on both routes.** The rule requires lower candidate median LCP on both Mysuru and the article, with candidate median CLS no worse on either. Mysuru candidate median LCP is lower by 0.03 ms; the article candidate median LCP is higher by 1.66 ms. LCP IQRs are 628-703 ms, so the small Mysuru difference is not a coherent gain. CLS medians are unchanged at zero on both routes. `performance_release_certified=false` remains unchanged.

No changes are made to font families, files, weights, preloads, `font-display` or the font gate. All values are local simulated results, not live or field performance.
