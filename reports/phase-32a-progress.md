# Phase32a progress

**Current branch:** `arena/48320ee5-ilmerastudyabroad`
**Remote match:** local `HEAD` equals `origin/arena/48320ee5-ilmerastudyabroad` at `a4ca3434e8115d903db77f9ac50517983e177fd6`. Worktree was clean after fast-forward.
**Scope:** Destination, place, article and Blog-index hero stills and font request-chain diagnosis. No ZIP. No new changes to Home, Services, About or Contact. Those four may be used only as the requested controls; the existing pushed Phase32 reference changes are not repeated or expanded here.

## Gate and prior evidence

- `reports/phase-31-release-check.md` exists and records Task5 verification PASS, 31/31 groups. The branch contains the Phase31 source baseline and later work. Gate passed.
- `reports/phase-31-task4-ab-summary.md` records frozen A `7d1bb9e`, B `806769a`, 112 samples, 2/8 routes passing the unchanged budgets. Known target LCP-ratio failures: Germany 1.2233, the chosen article 1.1366 and Blog index 1.1362. This is local simulated evidence and the reason for Phase32a, not a stop condition.
- Previously pushed Phase32 Task1 assets and safeguards already meet the requested file-size and contrast limits: mobile `assets/images/hero-still-640.webp`, 640x800, 9,738 bytes; desktop `assets/images/hero-still-1440.webp`, 1440x900, 37,226 bytes. Existing `phase-32-hero-assets.json`, `phase-32-hero-smoke.json` and `phase-32-hero-contrast.json` record 360/768/1280 review, post-load loading, text LCP, no-JS, Save-Data/slow-connection and scene-switch fallback checks, and minimum contrast 5.339:1. These pushed results will not be regenerated unchanged.
- The existing Phase32 font-chain audit and candidate experiment are already committed. The only tested font-display candidate did not produce a coherent LCP gain without worse CLS: Mysuru B/A 1.3639, article 0.9997 (0.45ms difference), Blog index 1.3640. Existing decision is no font change. Do not repeat that experiment unchanged.
- Frozen Phase32 run02 used a different A (`796879d`) and 11 routes; it is not a substitute for the newly requested six-route Task2 run against A `7d1bb9e`. Its three LCP misses remain in the existing report and are not erased.

## Completed this checkpoint

- Fetched the existing session branch and fast-forwarded the local branch to the exact remote tip `a4ca343`. No branch switch, new branch, PR, merge or deployment.
- Read the required Task4 summary, Phase31 release-check, Phase32 progress and branch history. Confirmed the gate above.
- Confirmed the previous pinned runtime directory `/home/user/phase32-runtime` is absent in this workspace, and native PHP is unavailable. The frozen Task4 fixture archive is present and hashes to `806e5ab8df048c1bda227211a57a67fe8331b6121a045eccc43c8c5629d2f1d6`.
- No runtime code changed in this checkpoint. No ZIP will be built.

## Exact next step

Recreate a temporary pinned PHP-WASM/Chromium/Lighthouse runtime outside the tracked payload, extract the existing Task4 fixture archive, and render the current pushed candidate B from its unchanged runtime source (`4e709ed`). Freeze a new six-route fixture containing exactly `/study-in-germany`, `/study-abroad-counselling-mysuru`, `/blog/how-to-choose-study-abroad-consultant-karnataka`, `/blog/`, `/services` and `/contact`, with A fixed at `7d1bb9e`. Then run the fast affected-template lint/render/content checks, commit and push the fixture checkpoint, and only then run the fresh interleaved 7-sample-per-arm Lighthouse measurement. Save and push raw results before analysis. No reference-page source change is planned.

## Remaining sequence

1. Complete the six-route Task2 A/B run and commit/push raw data before any analysis.
2. Report the per-route medians, IQRs, absolute LCP/TBT/CLS/transfer, ratios and unchanged budgets. Any still-bearing target that fails falls back to its plain palette hero; preserve the failure in the report.
3. Reuse existing font-chain diagnostics and no-change experiment unless a new, justified candidate is proposed. Any font change requires a fresh interleaved A/B on Mysuru and the chosen article, with LCP improvement and CLS no worse.
4. Run the full Phase32a verification suite once at the end, including lint/render, 258 browser cases, discovery/wording, sitemap, palette, schema, one-page-per-template axe and 360/768/1280 overflow checks.
5. Update `CHANGELOG.md`, append any new blocker to `flagged-items-for-verification.md` without rewriting older entries, and create `reports/phase-32a-release-check.md` with a result per check, the before/after lab table, fallback templates and every changed path since `796879d`. No ZIP. Push the final checkpoint and PR #1 comment; do not merge.
