# Phase 23 release check

Date: 2026-10-22. Baseline: `6befa0f`.
PR #1: https://github.com/fawazbhseo/ilmerastudyabroad/pull/1
Branch: `arena/48320ee5-ilmerastudyabroad` only.

## Deployment readiness

Local candidate: PASS, including final Task 8 full suite (487.28 seconds).
Final sign-off: 92 PHP files, 43 routes, 258 browser cases, 18 team-photo
checks, 213 exact FAQ pairs and 1,278 interactions. All required checks PASS.
Live deployment: NOT CLEARED by these tests and NOT PERFORMED. No main push
or merge. A complete live backup, all-file/settings restore readiness, native
Apache redirects/headers, public raw HTTP, actual enquiry delivery and live
asset MIME acceptance were not verified. Retain the existing backup-first
workflow and require explicit authorization before direct live work.

The large/format-mismatched Fawaz image is a documented original-preservation
exception, not an unreported optimisation or a fabricated photo. All required
portrait loads/layout/Person checks passed. No claim that every file is under
300 KB, that media is optimised or that live performance was established.
Missing optional proof is not invented. Policy details remain transparently
unpublished and families are told to obtain them before paying.

## Scan results

Report-only scan covers all 38 published pages, metadata, recursive schema,
FAQs/articles and both LLMs: ten finding groups and five classified negative/
prospective review-result references. Payment-policy/unknown-amount wording,
an unqualified hidden-fee assurance and incomplete no-feedback wording were
updated from the actual owner facts. No joint-founder variant was found;
there were no biography wording substitutions or university-name exemptions.
All three existing photos/bios and prior Person records were inventoried.
The final media annotation reports the actual PNG content of the Fawaz file.
No country fact, status, original summary/provenance or original direct answer
was changed. Six answered/15 partial/29 gap prompt counts remain conservative.

## Exact disclosure published on the four requested pages

The following is the visible section text, also represented by the two
same-source FAQ answers below. It does not state inclusions, a schedule,
refund conditions, routing or individual partner identities.

> ILMERA charges the student a service charge between ₹3 lakh and ₹15 lakh, depending on destination and university. This is on top of the university's own fee.

> ILMERA also receives payments from some partner universities.

> ILMERA has a written service-fee and payment policy covering service inclusions and refund terms. The policy terms are not yet published on this site.

> Before paying, families should ask for the policy terms in writing and confirm in writing which amounts are university fees and which are ILMERA's service charge.

### Exact FAQ text

**Does ILMERA charge a fee?**

ILMERA charges the student a service charge between ₹3 lakh and ₹15 lakh, depending on destination and university. This is on top of the university's own fee. ILMERA has a written service-fee and payment policy covering service inclusions and refund terms. The policy terms are not yet published on this site. Before paying, families should ask for the policy terms in writing and confirm in writing which amounts are university fees and which are ILMERA's service charge.

**Does ILMERA receive payments from universities?**

ILMERA also receives payments from some partner universities.

These appear visibly and as identical FAQPage text on Services, Contact,
choosing-consultant and cost guides. The range is never in metadata,
Organization/Person/Service descriptions or numeric price/Offer properties.
LLM range occurrences are explicit FAQ answer text only. Canonical company
payment copy is nonnumeric. Fee proof stays empty.

## Team inventory and preservation

All existing About/Home biography variants and all five image asset files
match the baseline bytes. No shortening, substitute biography, replacement
photo, placeholder or new credential. About/Home display labels use full
approved titles; image alt follows Name, Title, ILMERA Study Abroad. All team
photos are below the fold, with lazy loading and explicit layout dimensions.
Canonical Person images use the real original fallback photo URLs; the WebP
sources remain unchanged. One Person per member, worksFor the Organization,
existing exact card-bio description; only existing Jabir/Fawaz profile URLs.
Organization founder remains Jabir KJ alone.

### Jabir KJ, Founder

Existing retained bio: Jabir KJ is the founder of ILMERA Study Abroad, focused on helping students explore affordable international education opportunities.

Baseline source: `about.php:652`. Existing Person: Canonical Jabir Person on published routes. Prior alt: `Jabir KJ, Founder of ILMERA Study Abroad`.

Current alt: `Jabir KJ, Founder, ILMERA Study Abroad`. About display 88 x 88; Home display 96 x 96.

- `/assets/images/jabirkj.png`: 192 x 192, 46,374 bytes; unchanged.
- `/assets/images/jabirkj.webp`: 192 x 192, 8,302 bytes; unchanged.

### Fawaz BH, Chief Marketing Officer

Existing retained bio: Fawaz BH is CMO at ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kushal Nagar, Kodagu, Karnataka. He runs his own practice at fawazbhseo.in, holds certifications from Ahrefs Academy and Semrush, and built ILMERA's content strategy around the questions students in Kodagu actually ask.

Baseline source: `about.php:663`. Existing Person: Existing About JSON-LD Person. Prior alt: `Fawaz BH, CMO at ILMERA Study Abroad`.

Current alt: `Fawaz BH, Chief Marketing Officer, ILMERA Study Abroad`. About display 88 x 88; Home display 96 x 96.

- `/assets/images/fawazbh.webp`: 1254 x 1254, 1,541,656 bytes; unchanged.

### Zaheer KJ, Chief Financial Officer

Existing retained bio: Zaheer KJ is CFO at ILMERA Study Abroad. Ask ILMERA to identify the person responsible for any additional tasks in your written service scope.

Baseline source: `about.php:671`. Existing Person: Existing About JSON-LD Person. Prior alt: `Zaheer KJ, CFO at ILMERA Study Abroad`.

Current alt: `Zaheer KJ, Chief Financial Officer, ILMERA Study Abroad`. About display 88 x 88; Home display 96 x 96.

- `/assets/images/zaheer.png`: 192 x 192, 47,311 bytes; unchanged.
- `/assets/images/zaheer.webp`: 192 x 192, 11,014 bytes; unchanged.

The Fawaz file is PNG data under the pre-existing .webp name. It is not a
generic placeholder and loads in all tested browser modes. Preserve its
name/bytes per instruction; any optimisation/format/MIME change is separately
authorized work. No missing photo or bio is reported under Task 3c.

Existing claims retained and listed in PR #1 for owner reconfirmation:
Fawaz's ILMERA CMO role, independent SEO/AEO/GEO practice in Kushal Nagar/Kodagu,
fawazbhseo.in/FawazBHSEO, Ahrefs Academy and Semrush certifications, content/
search responsibilities and the FAQ's Advanced Diploma in Digital Marketing
from Adrex Media School. Legacy source credential labels are retained,
including the two Semrush named certifications. Jabir founder/focus and
Zaheer CFO bio remain exact. No new institution, award or experience duration.

## Check-by-check results

All required completed Task 7 checks below passed. Final Task 8 uses the
same entire matrix. PHP 8.5 WASM/Chromium, external browser requests aborted;
local output is not independent native/live HTTP, performance or delivery.

| Check | Result |
| --- | --- |
| PHP syntax | PASS |
| test_discovery.py | PASS |
| test_citations.py | PASS |
| test_italy_claims.py | PASS |
| test_llm_directory.py | PASS |
| test_llm_policy.py | PASS |
| test_presence.py | PASS |
| test_wording.py | PASS |
| check_destination_sources.php | PASS |
| check_place_contact.php | PASS |
| check_place_publication.php | PASS |
| test_proof.php | PASS |
| test_strategy_schema.php | PASS |
| authored location overlap | PASS |
| check_discovery.py | PASS |
| check_publication_review.py | PASS |
| check_italy_claims.py | PASS |
| check_phase19.py | PASS |
| check_technical_seo.py | PASS |
| build_llms_directory.py | PASS |
| check_phase20.py | PASS |
| check_phase22.py | PASS |
| check_phase23.py | PASS |
| render schema and strict policy | PASS |
| independent cycle consistency | PASS |
| browser | PASS |
| rendered location overlap | PASS |
| whitespace | PASS |

Additional explicit confirmations:

- PASS: 92 PHP lints, 43 route renders, 258 browser cases at 375/768/1280
  widths with JavaScript off/on; 213 exact FAQ pairs, 1,278 expansions.
- PASS: 18 browser team-photo checks; 11 published team/author image
  instances have correct alt, dimensions and lazy loading; three exact
  canonical Persons per page with real image URLs and preserved bios.
- PASS: original image bytes, all About/Home bio variants, metadata,
  destination/place data, summaries/provenance, journals, statuses and proof.
- PASS: no university-name exception needed; no prohibited cost wording,
  joint-founder variant, ILMERA superiority claim, em dash or premises claim.
- PASS: no per-service inclusion, schedule, refund condition, routing,
  testimonial, result, student/placement number or unsupplied registration.
  General guidance is explicitly separate from contractual fee inclusions.
- PASS: no Offer, price property, Review, aggregateRating or LocalBusiness
  schema. Range is visible/FAQ text only; all five proof slots remain empty.
- PASS: no draft URL in discovery, schema links, navigation or sitemap;
  self-referencing canonicals, no noindex sitemap target, no broken internal
  links/fragments, duplicate metadata or orphaned published page.
- PASS: existing LLM generator is idempotent; both documents retain
  32 rendered metadata entries and all 38 published routes, exact owner
  facts/bios, and mandatory conditional Italy/GCC cautions.
- PASS: 17 location guides retain 382-396 authored prose words; 136 pairs,
  authored maximum 6.41 percent, full rendered-main maximum
  13.24200913242009 percent, below the limit.
- PASS: dated append-only CHANGELOG/flagged additions retain all baseline
  bytes. Index CRLF, About CRLF plus three bare LF, unchanged htaccess CRLF.
- PASS: one clean required-check Task 7 cycle, early stop; no cycles 2-4
  claimed and no required repeated failure.
- REPORTED EXCEPTION: original Fawaz asset exceeds 300 KB and has a container/
  filename mismatch. It is preserved, not claimed to meet an optimisation
  budget; native live MIME acceptance remains unverified.

## Only the owner can supply

See owner-inputs-needed.md for fields and pages that each would update:
actual per-service inclusions, payment schedule/conditions, refund terms,
BOTH real Udyam number/business name, and future genuine feedback only when
it exists, with written permission and verified video. No team item is missing.
No current customer feedback exists; no actual review/result is fabricated.
Official rules/individual decisions require separate official evidence, not
owner answers. Held Russia/Czech destinations and APS/DSU articles stay held.
All applicable older official-source/live blockers remain intact.

## Every changed page and discovery document

Baseline/current render bytes were compared: exactly the following 38
published routes change. No held/utility status or utility content changes.
All receive the updated canonical Organization/three existing Persons;
additional visible surfaces are noted below. Changes through shared image,
entity and disclosure components are not individual page rewrites.

| Published route | Visible/shared surface |
| --- | --- |
| `/` | Existing title/alt labels, non-hidden-agent wording; bios retained |
| `/about` | Fee FAQs/assurance, full team titles/alts, shared entity/team summary; bios retained |
| `/all-pages` | Shared canonical entities only |
| `/blog/` | Shared canonical entities only |
| `/blog/cost-of-studying-abroad-for-indian-students` | Disclosure/FAQs and shared author-photo alt |
| `/blog/documents-needed-to-study-abroad-from-india` | Shared author-photo alt and canonical entities |
| `/blog/how-to-choose-study-abroad-consultant-karnataka` | Checklist/disclosure/FAQs, no-feedback and general-scope distinction |
| `/blog/scholarships-for-indian-students-study-abroad` | Shared author-photo alt and canonical entities |
| `/blog/study-abroad-counselling-from-coorg` | Actual no-feedback FAQ and shared author-photo alt |
| `/blog/study-abroad-with-academic-backlogs` | Shared author-photo alt and canonical entities |
| `/contact` | Exact disclosure/FAQs and old fee FAQ; shared entity/team summary |
| `/privacy-policy` | Shared canonical entities only |
| `/services` | Exact disclosure/FAQs and shared team label |
| `/study-abroad-consultants-in-karnataka` | Shared visible entity/payment/team summary |
| `/study-abroad-consultants-in-kodagu` | Shared canonical entities only |
| `/study-abroad-counselling-belagavi` | Shared canonical entities only |
| `/study-abroad-counselling-bengaluru` | Shared canonical entities only |
| `/study-abroad-counselling-chikkamagaluru` | Shared canonical entities only |
| `/study-abroad-counselling-gonikoppal` | Shared canonical entities only |
| `/study-abroad-counselling-hassan` | Shared canonical entities only |
| `/study-abroad-counselling-kushalnagar` | Shared canonical entities only |
| `/study-abroad-counselling-madikeri` | Shared canonical entities only |
| `/study-abroad-counselling-mangaluru` | Shared canonical entities only |
| `/study-abroad-counselling-mysuru` | Shared canonical entities only |
| `/study-abroad-counselling-ponnampet` | Shared canonical entities only |
| `/study-abroad-counselling-shivamogga` | Shared canonical entities only |
| `/study-abroad-counselling-siddapura` | Shared canonical entities only |
| `/study-abroad-counselling-somwarpet` | Shared canonical entities only |
| `/study-abroad-counselling-udupi-manipal` | Shared canonical entities only |
| `/study-abroad-counselling-virajpet` | Shared canonical entities only |
| `/study-in-gcc` | Shared canonical entities only |
| `/study-in-germany` | Shared canonical entities only |
| `/study-in-italy` | Shared canonical entities only |
| `/study-in-latvia` | Shared canonical entities only |
| `/study-in-lithuania` | Shared canonical entities only |
| `/study-in-slovakia` | Shared canonical entities only |
| `/study-in-uk` | Shared canonical entities only |
| `/terms` | Actual payment/charge policy paragraph, no unsupplied terms |

Discovery: `/llms.txt` and `/llms-full.txt`, generated team/payment/FAQ text and canonical reference; existing country facts/directory order retained.

## Every changed repository file

Exactly 33 files against `6befa0f`, including this report.
No image asset changed. Runtime/captures/scratch files remain outside Git.

- `CHANGELOG.md`
- `about.php`
- `blog/how-to-choose-study-abroad-consultant-karnataka.php`
- `contact.php`
- `data/answer-map.json`
- `data/entity.json`
- `data/payment-disclosure.json`
- `data/service-scope.json`
- `data/team.json`
- `flagged-items-for-verification.md`
- `includes/entity.php`
- `includes/payment-disclosure.php`
- `includes/site-presentation.php`
- `index.php`
- `llms-full.txt`
- `llms.txt`
- `reports/owner-inputs-needed.md`
- `reports/phase-23-checks.json`
- `reports/phase-23-cycles.md`
- `reports/phase-23-map.json`
- `reports/phase-23-progress.md`
- `reports/phase-23-registration-check.md`
- `reports/phase-23-release-check.md`
- `reports/phase-23-scan.md`
- `reports/phase-23-team-inventory.json`
- `reports/prompt-map.md`
- `terms.php`
- `tools/build_llms_directory.py`
- `tools/check_phase20.py`
- `tools/check_phase23.py`
- `tools/phase23/browser.cjs`
- `tools/phase23/build_prompt_map.py`
- `tools/phase23/run.py`
