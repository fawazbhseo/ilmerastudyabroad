# Technical SEO audit

Date: 2026-10-16. Fresh local evidence: `phase-19-technical.json` and task 7
in `phase-19-checks.json`. The local adapter is not native Apache.

| Check | Result | Evidence or limit |
| --- | --- | --- |
| Canonical and publication robots | PASS | All 38 published HTML routes match the sitemap and their own canonical |
| One H1 and main heading sequence | PASS | All 38 pages; no skipped main-content heading level |
| Unique short titles/descriptions | PASS | Central map matches fresh visible/social/page-schema output |
| Breadcrumbs | PASS | Names, positions and addresses exactly match the visible trail |
| Image alt and dimensions | PASS | All 88 image instances have descriptive alt and positive dimensions |
| Image loading | PASS | First brand image remains eager/default; subsequent images are lazy |
| Click depth and orphans | PASS | Maximum one click through actual home-page links; zero orphans |
| Internal links, resources, fragments | PASS | Full discovery check, with all held routes excluded |
| Sitemap and robots | PASS | Static/runtime parity, self-canonical indexable targets, existing robots allowance |
| Structured data and FAQ parity | PASS | Parsed graphs, exact visible answers and one canonical Organization |
| Actual native redirect chains | FAIL: not verified | Clean local canonical targets work; native server rules need live checks |
| Live render performance | FAIL: not verified | Browser replay blocks external requests; no real Core Web Vitals claim |

## Safe correction

A secondary Contact logo lacked a loading hint. The shared renderer now
preserves the first brand image as eager/default and adds lazy loading only
where subsequent images lacked it. Existing alt, dimensions and design remain.
Passing headings, breadcrumbs and navigation were not rewritten.

## Retained owner/live work

Two existing Google Fonts stylesheet variants remain render-blocking. No new
third-party script was added and no unmeasured performance gain is claimed.
Self-hosting or changing the font delivery needs a measured live performance
review and appropriate font assets/licensing; the design system is retained.
Test native redirect behavior, missing-address responses, security headers,
actual image/font delivery and server caching after the owner backs up and
uploads to live. External citation status is not proved by local link checks.
