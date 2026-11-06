# Phase32 local reference-font candidate diagnostics

## Scope and method

Four single-sample B-arm Lighthouse diagnostics were run against the frozen run02 fixture, SHA-256 `25708bdf3b527dc36ec50f08aaf568168419c10a5ac5c91ff5136064a966f8d5`. Candidate source is `4e709ed0cc6ec4e2b2a60d7d914765ae170634a0`. Each diagnostic launched a fresh Chromium 143.0.7499.0 process with Playwright 1.58.2 and Lighthouse 12.8.2. Browser requests used the local fixture/assets and the pinned local resource mirrors. These diagnostics are excluded from the seven-sample A/B result and are not release metrics.

| Route | LCP (ms) | CLS | TBT (ms) | Raw artifact |
|---|---:|---:|---:|---|
| `/` | 2956.53 | 0 | 0 | `phase-32-local-font-diagnostic-home.json` |
| `/services` | 2956.47 | 0.000491 | 0 | `phase-32-local-font-diagnostic-services.json` |
| `/about` | 2730.93 | 0 | 0 | `phase-32-local-font-diagnostic-about.json` |
| `/blog/` | 2281.78 | 0 | 0 | `phase-32-local-font-diagnostic-blog-index.json` |

The Home, Services and About values are lower than their earlier one-sample candidate diagnostics from checkpoint 19, and their CLS values are much lower. The comparison is not a controlled paired experiment: it compares different candidate commits and single samples. It is a reason to retain this candidate for the planned full run02, not proof that the owner budgets pass.

## Attribution observations

- Home and About had zero observer layout shifts. Services had one recorded observer entry of 0.000491; its reported source rectangles were unchanged before and after. The Lighthouse CLS metric was 0.000491. No page-level shift approaching the earlier Home/Services values was observed.
- Local Outfit and Cormorant faces were reported loaded. Home's font-ready events completed at about 200ms and 1,139ms; the later event also includes the full face set. No Google Fonts CSS request is present in the candidate page.
- Blog index remained at CLS 0 and TBT 0 in this mobile diagnostic. It does not establish desktop Blog TBT or the required A/B delta.
- The observer also captured renderer-clock long tasks near 1,002ms on each route. These are not Lighthouse TBT and are not substituted for the LHR values.

## Decision and limits

Retain this candidate provisionally for the fresh frozen-A seven-round 11-route A/B. Do not call the local fonts a fix until that comparison reports medians, IQRs, absolute LCP, ratios, TBT deltas, CLS, transfer and render-blocking results. The four diagnostic samples do not establish desktop typography, native-host transfer, reference desktop scene TBT or production behavior. Contact `#miniHero` tails and Blog desktop TBT remain open.
