# Phase25c progress

2026-10-23. Session branch arena/48320ee5-ilmerastudyabroad, PR1. Fetched remote and confirmed clean local/remote equality at Stage2 endpoint4dc4c5cb81c9cde4861012be61f5d5e0de755bbd. Read release check, Stage2 progress and log. No earlier Phase25c work found. No reference source changes, business/content/SEO changes, main push, merge or deployment permitted.

## Tasks

1. Reference structural gate and three-pair pixel noise calibration: complete.12/12 PASS;0 structural differences; all meet pixel backstop. Source refs untouched.
2. Serial fresh-process interleaved7-by7 A/B measurement, controls and IQR: pending.
3. Template diagnosis and uniform tier choice: pending.
4. Chrome geometry tolerance below0.1px, accepted404 abbreviated footer: pending.
5. Reference accessibility/overflow report only: pending.
6. Re-verification, maximum2 cycles, release report/sign-off: pending.

## Decisions

- Use an independent git archive of immutable Stage1 commit3f0e141 for reference HTML, not HTML relabelled from current. Use immutable Phase24b HTML for non-reference performance A; Stage1 HTML for all four reference controls. About is added as a fourth control to the thirteen explicitly listed routes. Both A and B use identical local fixture HTTP delivery.
- Three baseline self comparisons means three independent pairs (six captures), not three captures compared selectively. Structural geometry rounded to0.1px is the pass gate; max channel delta4 and SSIM0.999 are backstops and baseline noise is retained.
- Existing native-host, proof, delivery, runtime-layout and backup/restore blockers stay open. Local simulated data only.

## Task1 checkpoint

All12 combinations have0 structural differences. Three independent baseline pairs per combination are retained with noise max delta, differing pixels and SSIM. Current About360 is assessed against that exact noise floor, not older Stage2 zero-delta policy. All current cases meet max4/SSIM0.999. Full raw structures saved compressed; numerical pixel and structural reports saved. No presentation change needed and no reference source edited.
