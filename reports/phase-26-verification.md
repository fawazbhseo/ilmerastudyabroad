# Phase26 isolated content verification

**Candidate PASS locally; release-branch verification BLOCKED.** No release branch or content PR exists in this session. Baseline: `164d6de41159385e151ecefec54763eab59141a5`. Only approved team cards/two inline grid rules plus policy/check expectations are patched. Original Phase24b run.py and browser.cjs unchanged. Original0c5c437 pre24b renders independently recreated for inherited source/schema guards;164d6de snapshots separately recreated for the four-reference comparison. Git lookup uses an external index loaded from164d6de, not the design checkout index. No other branch/worktree created.

Full Phase24b stage5 suite: **PASS**, 545.13s. Fresh43 routes,38 published; sitemap38 URLs. Unit tests, PHP lint, browser JSon/off375/768/1280, publication/discovery/wording/schema/FAQ parity/robots/LLMs/source/exposure/portrait/overlap checks all executed. All full outputs summarized in phase-26-verification.json. Historical parent field is the lookup repository HEAD, not a candidate commit.

| Check | Result |
|---|---|
| PHP syntax | PASS |
| test_discovery.py | PASS |
| test_citations.py | PASS |
| test_italy_claims.py | PASS |
| test_llm_directory.py | PASS |
| test_llm_policy.py | PASS |
| test_presence.py | PASS |
| test_wording.py | PASS |
| test_team_bio_policy.py | PASS |
| check_destination_sources.php | PASS |
| check_place_contact.php | PASS |
| check_place_publication.php | PASS |
| test_proof.php | PASS |
| test_strategy_schema.php | PASS |
| access policy patterns, not native engine | PASS |
| portrait encoding and original integrity | PASS |
| authored location overlap | PASS |
| check_discovery.py | PASS |
| check_publication_review.py | PASS |
| check_italy_claims.py | PASS |
| check_phase19.py | PASS |
| check_technical_seo.py | PASS |
| build_llms_directory.py | PASS |
| check_phase20.py | PASS |
| check_phase24b.py | PASS |
| render schema and strict policy | PASS |
| baseline render delta | PASS |
| independent cycle consistency | PASS |
| browser | PASS |
| rendered location overlap | PASS |
| whitespace | PASS |

## Reference appearance and explicit team reflow

12/12 comparisons PASS: same visible outside-team text/order, computed typography/colour/spacing/borders and relative geometry after the approved team-height reflow. Services/Contact source bytes unchanged. Header/footer source/styles unchanged. All images/links/schema/headings/FAQ untouched. Home/About cards have exact short texts and equal outer heights. **Not a claim of identical full-page pixels or absolute footer position:** shorter cards and equal-row styling alter team-section height and shift later sections vertically. Preserving the old footprint would require extra styling beyond the requested minimum, so no such design work was imported.

| Page | Width | Team height before/after | Outside-team differences after explicit reflow normalization |
|---|---:|---:|---:|
| / | 375 | 1740.0/1668.5 | 0 |
| / | 768 | 1485.0/1515.5 | 0 |
| / | 1280 | 962.2/809.2 | 0 |
| /services | 375 | 0.0/0.0 | 0 |
| /services | 768 | 0.0/0.0 | 0 |
| /services | 1280 | 0.0/0.0 | 0 |
| /about | 375 | 2018.9/1812.1 | 0 |
| /about | 768 | 1292.8/1015.7 | 0 |
| /about | 1280 | 1152.7/991.1 | 0 |
| /contact | 375 | 0.0/0.0 | 0 |
| /contact | 768 | 0.0/0.0 | 0 |
| /contact | 1280 | 0.0/0.0 | 0 |

Initial Services comparisons sampled unset .anim-fade-* opacity states. The identical test-only settling rule was extended to those existing reveal classes; initial result retained externally. No source change or production threshold relaxed.

## No design import

No Phase25 filenames, design stylesheet/shared visual PHP, hero stills, font files or Phase25 reports exist in the164d6de archive or six-file candidate patch. Full descriptions remain unchanged in canonical data/Person JSON-LD, About FAQ answers and both LLM files. Registration block, WebP portraits, disclosures and protected runtime inputs are retained from164d6de. Exact38 sitemap URLs and the38 published route list are in phase-26-base-inventory.json.

Local adapter manually mirrors routes/access policy and does not execute .htaccess. No native Apache/cache/CSP/ACL/contact-delivery/live-site proof, no deployment. Full candidate/content-branch checks must be re-run in the separately authorized release checkout before opening/approving its PR.
