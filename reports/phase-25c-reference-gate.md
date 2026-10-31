# Phase25c reference gate

Immutable Stage1 3f0e141 independently rendered with PHP8.5; current frozen separately. All four HTML byte hashes match. Source files Home/Services/About/Contact remain byte-exact. No source edits.

Pass criterion: every visible element DOM order/direct text, bounding box rounded to0.1px, computed font family/size/weight/colour/background, each margin/padding/border/radius, and pseudo paint match. Full baseline/current structures and diff arrays are saved as compressed JSON under phase-25c-structures/. Team card source remains the exact approved Stage1 bio/equal-height work. No structural exception was needed.

Identical capture-only seeded clocks/settled animation instrumentation for both arms; no application code changed. Six independent baseline captures form three predefined self-comparison pairs. Pixel backstop uses full-resolution RGB7x7 SSIM, no resizing; approved card rectangles and intersecting SSIM windows excluded.

| Reference | Width | Structural diffs | Noise max delta / max pixels / min SSIM | Current delta / pixels / SSIM | Verdict |
|---|---:|---:|---|---|---|
| home | 360 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| home | 768 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| home | 1280 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| services | 360 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| services | 768 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| services | 1280 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| about | 360 | 0 | 3 / 505576 / 0.999324385 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| about | 768 | 0 | 4 / 690547 / 0.999566359 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| about | 1280 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| contact | 360 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| contact | 768 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
| contact | 1280 | 0 | 0 / 0 / 1.000000000 | 0 / 0 / 1.000000000 | PASS: Structure exact; pixel backstop met |
