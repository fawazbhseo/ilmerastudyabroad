# Phase32 candidate font/reflow diagnostics

## Scope and method

Four one-sample B-arm Lighthouse diagnostics were run separately from the frozen 11-route seven-sample A/B experiment. The candidate HTML comes from source commit `1e1f225ab17c2c83ade5d92c3e351758e223030e`; the local-only fixture server used Chromium 143, Playwright 1.58.2 and Lighthouse 12.8.2. The diagnostic launcher now writes the requested route and arm to the fixture selector before navigation, preventing the earlier `/services` 404 caused by stale route selection. Each invocation launched a fresh Chromium browser. The results are attribution evidence only, not release metrics.

Raw Lighthouse JSON:

| Route | LCP (ms) | CLS | TBT (ms) | Raw artifact |
|---|---:|---:|---:|---|
| `/` | 3511.80 | 0.055063 | 0 | `phase-32-cls-home-candidate-diagnostic.json` |
| `/services` | 4231.50 | 0.026096 | 0 | `phase-32-cls-services-candidate-diagnostic.json` |
| `/about` | 3856.24 | 0.020411 | 0 | `phase-32-cls-about-candidate-diagnostic.json` |
| `/blog/` | 2281.49 | 0 | 0 | `phase-32-cls-blog-index-candidate-diagnostic.json` |

The three reference CLS readings exactly reproduce the corresponding run01 B medians. The metric-matched Arial/Times fallback candidate therefore did not demonstrate a reduction in these diagnostics. The Services single sample exceeds the 4,000ms reference LCP ceiling; this does not replace the seven-sample route result.

## Attribution observations

- Home recorded two observer shift entries with values 0.055063 and 0.056188. The first recorded geometry changes included `#hH1` shrinking from 85.27px to 46px tall, `#hSub` from 105px to 78.75px, `.seo-opening` moving upward, `#hBtns` changing height, and `#hStats` growing from 60.28px to 120.80px. Lighthouse's layout-shift audit identifies web-font loads as a cause. Both observer entries have `hadRecentInput=true`; that flag is not evidence that the reported Lighthouse aggregate should be disregarded.
- Services recorded CLS 0.026096. The H1 geometry stayed the same in the observed event, while `#heroSub` moved upward about 27.8px and the following `.s-wrap` section changed height/position by a similar amount. The Lighthouse audit identifies font loads among the shift causes. Observer entries have `hadRecentInput=true`.
- About recorded CLS 0.020411 with `hadRecentInput=false`. The visible movement was associated with `.story-sec` and `.mob-hero-stats`; the Lighthouse audit lists loaded Cormorant and Outfit faces among the causes. This indicates the issue is not limited to the Home H1 fallback.
- Blog index recorded no shift in this mobile diagnostic. Its TBT value is 0ms in this one mobile sample only; it is not the required desktop Blog TBT result.

## Decision and limits

The metric-fallback hypothesis is not confirmed as a fix and no CLS pass is claimed. Keep the run01 failures open until a controlled candidate change is measured against frozen A and all 11 routes. Do not change the place/article/blog font policy based on these diagnostics. Continue to treat all reported values as local lab evidence, not production field data. Contact `#miniHero` still requires its separate tail inspection, and desktop reference-scene TBT remains open.
