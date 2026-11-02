# Phase32a six-route frozen fixture

Status: **PASS**. A source `7d1bb9ec0522bcbc7953262920fafb50bf04ab72`; B render source `b0dc2652c281720027e3d44ae0da6471a1b2c8fb`; B runtime tree matches current HEAD `da2503b10c37d6bf71bf3dd74f0cf8a1da78bf11`. Fixture SHA-256 `31acc1582b723779b65a9c9f388f7fc4b864e197b3e2b5de21609842553a0aea` (1065165 bytes), stored externally at `/home/user/phase32a-runtime/phase32a-ab-run01/fixtures.json`.

| Route | Role | A/B HTML bytes | A/B text chars | Anchors | Images | Protected content | HTML bytes identical |
|---|---|---:|---:|---:|---:|---|---|
| `/study-in-germany` | still target | 101000/104364 | 6149/6149 | 86/86 | 2/2 | PASS | no |
| `/study-abroad-counselling-mysuru` | still target | 61106/64579 | 5424/5424 | 66/66 | 2/2 | PASS | no |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | still target | 69022/72495 | 12341/12341 | 70/70 | 2/2 | PASS | no |
| `/blog/` | still target | 60417/63890 | 3610/3610 | 68/68 | 2/2 | PASS | no |
| `/services` | reference control, existing pushed B differs | 124686/128489 | 18668/18668 | 135/135 | 2/2 | PASS | no |
| `/contact` | reference control, existing pushed B differs | 91216/95019 | 10938/10938 | 91/91 | 3/3 | PASS | no |

Content check covers normalized body text/order, title, headings, meta, robots, canonical, semantic anchor attributes/text/order, image and picture-source attributes, and parsed JSON-LD. All six pass with no content invariant failures.

Services and Contact HTML are compared to the Task4 A snapshot, but B includes already-pushed shared Phase32 presentation changes. They are measurement controls, not byte-identical no-op controls. Phase32a makes no new reference-page change.

This fixture is local-only. The Task2 A/B measurement has not started; no sample is included in this file.
