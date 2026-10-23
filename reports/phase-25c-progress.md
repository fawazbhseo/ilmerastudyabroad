# Phase25c progress

2026-10-23. Session branch arena/48320ee5-ilmerastudyabroad, PR1. Fetched remote and confirmed clean local/remote equality at Stage2 endpoint4dc4c5cb81c9cde4861012be61f5d5e0de755bbd. Read release check, Stage2 progress and log. No earlier Phase25c work found. No reference source changes, business/content/SEO changes, main push, merge or deployment permitted.

## Tasks

1. Reference structural gate and three-pair pixel noise calibration: complete.12/12 PASS;0 structural differences; all meet pixel backstop. Source refs untouched.
2. Serial fresh-process interleaved7-by7 A/B measurement, controls and IQR: complete, acceptance FAIL. All3 permitted sessions unreliable; final session has14 routes with7A/7B. All failed/partial runs retained. No more performance retries.
3. Template diagnosis and uniform tier choice: complete assessment. Uniformity PASS; reliable budget/necessity proof FAIL. Existing whole-template policy retained, no unsafe source edits.
4. Chrome geometry tolerance below0.1px, accepted404 abbreviated footer: complete.120/120 PASS; max tolerated0.016px; zero differences>=0.1px. No source edits.
5. Reference accessibility/overflow report only: complete. All24 contrast groups/387 node instances and5 overflow cases documented; no fixes applied to refs.
6. Re-verification, maximum2 cycles, release report/sign-off: pending.

## Decisions

- Use an independent git archive of immutable Stage1 commit3f0e141 for reference HTML, not HTML relabelled from current. Use immutable Phase24b HTML for non-reference performance A; Stage1 HTML for all four reference controls. About is added as a fourth control to the thirteen explicitly listed routes. Both A and B use identical local fixture HTTP delivery.
- Three baseline self comparisons means three independent pairs (six captures), not three captures compared selectively. Structural geometry rounded to0.1px is the pass gate; max channel delta4 and SSIM0.999 are backstops and baseline noise is retained.
- Existing native-host, proof, delivery, runtime-layout and backup/restore blockers stay open. Local simulated data only.

## Task1 checkpoint

All12 combinations have0 structural differences. Three independent baseline pairs per combination are retained with noise max delta, differing pixels and SSIM. Current About360 is assessed against that exact noise floor, not older Stage2 zero-delta policy. All current cases meet max4/SSIM0.999. Full raw structures saved compressed; numerical pixel and structural reports saved. No presentation change needed and no reference source edited.

## Task2 checkpoint

276 recorded samples across3 sessions. First stopped after Home reliability failed (Home7A/7B and partial Services5A/5B retained); second contains all4 controls7A/7B; final contains all14 routes7A/7B. Every run uses a fresh Chromium process, serial A/B alternating by round. Same frozen HTTP delivery and CDN mirrors for both arms, no overlapping benchmark/QA. Median and IQR saved for LCP/CLS/TBT/bytes/requests. Final Home symmetric ratio5.0419 and Services4.8435 fail control reliability. No session certified; no passing non-reference numbers promoted to release PASS. Independent HTML blocking-request scan supplements potentially missing Lighthouse audit. Post-trace report screenshot disabled in reruns only; real animations/metric trace/throttling unchanged. Initial target-closed setup probe fixed with passive early observers; log retained externally, not used as a pair/median.

## Task3 checkpoint

Germany, Italy, GCC, Mysuru and Bengaluru each have7A/7B observations under Task2 method. Dominant LCP in every probe/arm is P.direct-answer in Outfit16px300, not hero image/title. Identified all-font-set gate dependency, removed external font network in destination inline tier and immutable paragraph variation; no unique German markup fault or reliable necessity proof established. No speculative font-gate edit from an unreliable session. Existing template-level lighter policy retained for all9 destinations (including held), gradient/selfhost for all17 places and all8 articles (including held), and other rebuilt templates. Choosing article raw LCP ratio2.2117 also FAILS; nine of ten rebuilt routes numerically pass, none certified. All underlying data retained, no added performance rerun.

## Task4 checkpoint

Full120-row comparison PASS. Every visible header/footer node geometry/text/order plus canonical computed styles compared. Maximum tolerated0.016px, no>=0.1px differences. Active-link transition normalization artifact corrected in test harness only and initial result retained externally.404 short footer accepted, header still checked.

## Task5 checkpoint

Report-only reports/phase-25-reference-a11y.md lists every node across24 original contrast groups (387 node instances), selector, measured foreground/background/ratio vs4.5 and nearest passing existing-palette single-foreground suggestion. All5 overflow cases reproduced exactly: Home360/768 rightmost hidden article.testi-card.reveal-r translateX60 yields+40px; About360/768 hidden div.stats-block translateX55 yields+33px; Contact360 hidden contact-info translateX60 yields+36px. Effective opacity0 at sampled layout-edge frames, body overflow hidden, horizontal-wheel scrollX0. Document scrollWidth remains enlarged in offscreen start states even after returning to top; not asserted resolved or compositor noise. No reference source/style fix applied.
