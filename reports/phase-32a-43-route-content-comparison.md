# Phase32a 43-route rendered-content comparison

## Method

Frozen A HTML is from pre-phase source `796879d7b3d5ca0fa1e398562e937e9f364a5f62`, archive SHA-256 `2b20187771f9117a16099754e4f579f6eb3f6f752b8c11a8ec25d255785b9dee`. Current B source snapshot is `ba5e97dc4038bae315ae5612ad9a5ef5061f9ea0`; it contains the `place`/`article` palette fallback while retaining `ILMERA_SCENES_ENABLED=true`. The comparison is local-only, not native-host or production evidence.

## Protected invariants

Result: **PASS**. 43 routes, 43 A/B HTTP 200 responses, 0 byte-identical HTML responses. Checks cover normalized rendered body text/order, title, headings, meta, robots, canonical, anchor semantics/text/order/multiplicity, image and picture-source attributes, and parsed JSON-LD graphs.

| Route | A/B HTML bytes | A/B visible text chars | Anchors | Images | HTML bytes identical | Content invariants |
|---|---:|---:|---:|---:|---|---|
| `/` | 102983/106786 | 15721/15721 | 100/100 | 5/5 | no | PASS |
| `/404` | 38352/38534 | 581/581 | 26/26 | 1/1 | no | PASS |
| `/about` | 89613/93375 | 13200/13200 | 79/79 | 5/5 | no | PASS |
| `/all-pages` | 52801/52983 | 2276/2276 | 99/99 | 2/2 | no | PASS |
| `/blog/` | 61207/63890 | 3610/3610 | 68/68 | 2/2 | no | PASS |
| `/blog/cost-of-studying-abroad-for-indian-students` | 70116/70028 | 9151/9151 | 88/88 | 3/3 | no | PASS |
| `/blog/documents-needed-to-study-abroad-from-india` | 69600/69512 | 8771/8771 | 89/89 | 3/3 | no | PASS |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | 69812/69724 | 12341/12341 | 70/70 | 2/2 | no | PASS |
| `/blog/italy-dsu-scholarship-eligibility` | 53313/53225 | 3085/3085 | 72/72 | 3/3 | no | PASS |
| `/blog/scholarships-for-indian-students-study-abroad` | 67712/67624 | 8020/8020 | 84/84 | 3/3 | no | PASS |
| `/blog/study-abroad-counselling-from-coorg` | 63871/63783 | 5901/5901 | 73/73 | 3/3 | no | PASS |
| `/blog/study-abroad-with-academic-backlogs` | 63114/63026 | 6157/6157 | 72/72 | 3/3 | no | PASS |
| `/blog/study-in-germany-free-aps-certificate` | 54422/54334 | 3770/3770 | 72/72 | 3/3 | no | PASS |
| `/contact` | 91216/95019 | 10938/10938 | 91/91 | 3/3 | no | PASS |
| `/privacy-policy` | 57050/57232 | 6023/6023 | 64/64 | 2/2 | no | PASS |
| `/services` | 124686/128489 | 18668/18668 | 135/135 | 2/2 | no | PASS |
| `/study-abroad-consultants-in-karnataka` | 65697/65609 | 7405/7405 | 70/70 | 2/2 | no | PASS |
| `/study-abroad-consultants-in-kodagu` | 62658/62570 | 5426/5426 | 73/73 | 2/2 | no | PASS |
| `/study-abroad-counselling-belagavi` | 62015/61927 | 5294/5294 | 68/68 | 2/2 | no | PASS |
| `/study-abroad-counselling-bengaluru` | 61994/61906 | 5432/5432 | 66/66 | 2/2 | no | PASS |
| `/study-abroad-counselling-chikkamagaluru` | 62331/62243 | 5555/5555 | 66/66 | 2/2 | no | PASS |
| `/study-abroad-counselling-gonikoppal` | 62344/62256 | 5471/5471 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-hassan` | 61676/61588 | 5239/5239 | 66/66 | 2/2 | no | PASS |
| `/study-abroad-counselling-kushalnagar` | 62089/62001 | 5290/5290 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-madikeri` | 62262/62174 | 5405/5405 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-mangaluru` | 61983/61895 | 5453/5453 | 66/66 | 2/2 | no | PASS |
| `/study-abroad-counselling-mysuru` | 61896/61808 | 5424/5424 | 66/66 | 2/2 | no | PASS |
| `/study-abroad-counselling-ponnampet` | 62283/62195 | 5461/5461 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-shivamogga` | 62047/61959 | 5322/5322 | 68/68 | 2/2 | no | PASS |
| `/study-abroad-counselling-siddapura` | 62306/62218 | 5466/5466 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-somwarpet` | 62378/62290 | 5521/5521 | 69/69 | 2/2 | no | PASS |
| `/study-abroad-counselling-udupi-manipal` | 62534/62446 | 5587/5587 | 68/68 | 2/2 | no | PASS |
| `/study-abroad-counselling-virajpet` | 62181/62093 | 5375/5375 | 69/69 | 2/2 | no | PASS |
| `/study-in-czech-republic` | 93597/96171 | 4671/4671 | 82/82 | 2/2 | no | PASS |
| `/study-in-gcc` | 110846/113420 | 11288/11288 | 106/106 | 2/2 | no | PASS |
| `/study-in-germany` | 101790/104364 | 6149/6149 | 86/86 | 2/2 | no | PASS |
| `/study-in-italy` | 99757/102331 | 5368/5368 | 87/87 | 2/2 | no | PASS |
| `/study-in-latvia` | 99393/101967 | 5314/5314 | 89/89 | 2/2 | no | PASS |
| `/study-in-lithuania` | 99366/101940 | 5037/5037 | 82/82 | 2/2 | no | PASS |
| `/study-in-russia` | 92069/94643 | 4303/4303 | 74/74 | 2/2 | no | PASS |
| `/study-in-slovakia` | 99095/101669 | 4949/4949 | 89/89 | 2/2 | no | PASS |
| `/study-in-uk` | 102108/104682 | 6719/6719 | 88/88 | 2/2 | no | PASS |
| `/terms` | 58341/58523 | 7475/7475 | 64/64 | 2/2 | no | PASS |

Sitemap byte identity: **True**; current B contains 38 unique URLs. Full per-route hashes/checks are in `reports/phase-32a-43-route-content-comparison.json`.

## Limits

This validates protected rendered content for the two frozen local source snapshots. It does not require HTML byte identity when visual/resource markup differs. It does not measure live routes or prove native-host rewrite, access-control or cache behavior.
