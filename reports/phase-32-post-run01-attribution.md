# Phase32 post-run01 one-sample diagnostics

These two local Lighthouse diagnostics were run after the frozen 154-sample session had completed. They are source-attribution probes only and are not included in run01 medians, route gates or release claims.

## Home CLS probe

- Candidate B `/` one-sample result: LCP 3,486.7ms, CLS 0.000728, TBT 0ms. This does not reproduce the run01 median CLS of 0.055063.
- The browser layout-shift observer recorded two entries. The large 0.0550629 entry was marked `hadRecentInput=true` and excluded from the reported Lighthouse CLS. Its source nodes included `#hH1`, `.seo-opening`, `#hSub`, `#hBtns` and `#hStats`; their text wrapping and geometry changed substantially. This is consistent with a late font/fallback reflow, but one sample is not enough to attribute the three run01 route failures conclusively.
- Raw diagnostic: `reports/phase-32-cls-home-diagnostic.json`, SHA-256 `95b15239f3599e52907c70b31372b6b9307eb0b74d369a851f70a7d4d9d5cb2f`.

## Blog-index TBT probe

- Candidate B `/blog/` one-sample result: LCP 2,356.6ms, CLS 0, TBT 52.7ms. This is near, but below, the run01 seven-sample median of 59.3ms; it does not pass the +50ms median delta gate by itself.
- Lighthouse listed five long-task entries between 63ms and 97ms, attributed to the document or unattributable. The main-thread-task audit did not provide a source stack. One separate PerformanceObserver entry reported a 1,003ms task on its renderer clock, which is not comparable to Lighthouse simulated-clock TBT. The still-loader may contribute, but this diagnostic does not isolate it.
- Raw diagnostic: `reports/phase-32-blog-tbt-diagnostic.json`, SHA-256 `87f1ad5bb16b27fc85a97728111cdb5ef1ab4a02f313be05170cfb58a8605af9`.

## Decision

Run01 failures remain open. The candidate needs a conservative font-fallback/CLS treatment on the four reference pages and a less main-thread-intensive still presentation on destination/place/article/blog-index pages, followed by a fresh full frozen-A run if runtime output changes. Do not claim a font or loader fix from these single probes.
