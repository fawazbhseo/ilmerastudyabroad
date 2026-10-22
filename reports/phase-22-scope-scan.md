# Phase 22 scope and conflict scan

Date: 2026-10-22. Baseline: `95ab613`. Authority: the owner's final answers dated 2026-10-22. This task changes reports and verification administration only, not site output.

## Coverage and method

Read all 38 published pages in freshly rendered HTML, including metadata, decoded page/Organization/Person/Service/FAQ data, visible answers and shared navigation/footer. Read all published article entry points, the presentation/answer/entity data and both complete LLM documents. Four held editorial routes and the separate utility remain unchanged; they were rendered for gate checks, not treated as published content. Official country work/stay facts are not business service offers and will not be rewritten. Source-only legacy descriptions that the canonical presentation already replaces are distinguished below.

The baseline full lint/render/browser/discovery/strict suite passes technically. That does NOT resolve the service-scope conflicts listed here. No service answer from the Phase 21 illustrative questionnaire is accepted as an owner fact. The new owner answers clarify assistance, not legal rules or individual outcomes.

## Findings and planned fixes

Line references below are baseline source lines. Repeated visible/schema copies are included in each file's references. No restricted cost phrase or academic institution name is reproduced in this report.

| ID | File and baseline line(s) | Finding | Planned task and fix |
| --- | --- | --- | --- |
| S01 | `services.php`: 65, 70, 102, 115, 709 | Employment/post-study service offer contradicts answer 6. | 2: replace service cards with the approved eight assistance topics and the explicit work/stay exclusion. |
| S02 | `services.php`: 126, 127, 370, 704, 705, 706, 708, 727, 728 | Application management, test coaching, interview coaching and arrival/orientation scope exceed final answers. | 2: narrow business statements to reviews/guidance; preserve separate existing country facts and exact Italy sentence. |
| S03 | `services.php`: 14, 32, 70, 102, 114, 123, 127, 140, 708, 724, 728, 732, 772 | Unprovided zero-charge claim and pre-departure service/process scope. | 2: neutral online enquiry/process wording, no amounts or additional services. |
| S04 | `index.php`: 500 | Business recommendation tied to post-study work conflicts with the exclusion. | 3: replace the business clause with owner-approved budget comparison; retain the already sourced policy fact as a separate factual example. |
| S05 | `index.php`: 178, 180, 182, 387, 459, 607, 611, 615, 673, 674 | Unprovided consultation pricing and a fixed counsellor/arrival promise. | 3: narrow service clauses and preserve visible/FAQ parity. |
| S06 | `contact.php`: 111, 174, 392, 519 | Career enquiry option and post-arrival service commitment. | 3: approved enquiry choices and owner-scope FAQ instead; no work/stay service. |
| S07 | `contact.php`: 15, 16, 17, 30, 31, 42, 43, 56, 57, 97, 147, 151, 160, 167, 171, 175, 329, 441, 442, 463, 495, 527 | Unprovided consultation pricing, package/timing detail and additional operational promises. | 3: scope-only enquiry and fee-policy statements, no timings or refund conditions. |
| S08 | `about.php`: 190, 306, 576, 677, 714 | Existing biography/assigned specialisms exceed the exact new approved biography and role. | 4: exact supplied biography in existing profile/Person only; approved research/admissions/application responsibility, no inferred credential. |
| S09 | `about.php`: 243, 322, 693, 718 | Another team member is assigned document/APS/appointment responsibilities not confirmed in the final answers. | 4: retain existing identity labels only; remove unsupported service assignments, request owner-confirmed additional roles. |
| S10 | `about.php`: 17, 44, 281, 335, 338, 346, 351, 354, 649, 656, 720, 722, 726 | Unprovided zero-charge pricing in visible/schema fee-related answers. | 4: existing policy acknowledged, detailed prices and refund terms not yet published. |
| S11 | `blog/how-to-choose-study-abroad-consultant-karnataka.php`: 79 | Self-assessment still lacks the now-approved service scope, founder responsibility and disclosure policy. | 4: factual checklist table, fees/refund terms remain not yet published; do not infer whether partner payments occur. |
| S12 | `data/answer-map.json`: 40, 82, 120 | Existing limited FAQ answers need the newly approved scope, not a claim that official procedures or proof are supplied. | 3/4: scope-only answers on fitting pages; official-rule gaps retained. |
| S13 | `data/entity.json`: 5, 22, 23, 24, 25, 26 | Canonical scope omits newly confirmed topics and includes a service not in the final scope. | 5: one consistent description/list with the exclusion; no extra Organization or paid offer. |
| S14 | `llms.txt`: 15, 21, 27, 116, 168, 171, 202 | Leadership, business list and process/pricing need final owner scope. | 5: maintain through existing generator, published-only directory unchanged. |
| S15 | `llms-full.txt`: 14, 31, 42, 45, 48, 53, 54, 57, 192 | Extended leadership and service breakdown overstate scope. | 5: generator-owned approved service text and founder role; preserve country fact sections. |
| S16 | `terms.php`: 127, 143 | Arrival scope, consultation price and default refund condition are not supplied in the final policy answer. | 3: narrow service paragraph and replace unsupported business-policy terms with unpublished-detail statement; do not invent legal/refund terms. |
| S17 | `blog/study-abroad-counselling-from-coorg.php`: 148, 173, 174 | Process step and CTA add unconfirmed service/pricing detail. | 3: approved application/visa/document guidance and neutral online enquiry. |
| S18 | `blog/study-abroad-with-academic-backlogs.php`: 171, 172 | Unprovided consultation-pricing CTA. | 3: neutral online discussion; leave all academic facts unchanged. |
| S19 | `blog/index.php`: 169, 170 | Unprovided consultation-pricing CTA. | 3: neutral online discussion; post statuses/metadata unchanged. |
| S20 | `includes/footer.php`: 99 | Shared CTA repeats unprovided consultation pricing on published pages. | 3: neutral online counselling CTA; no service offer added. |

## Source-only and retained facts

Legacy Organization descriptions in About/Home/Services may mention career scope in raw PHP source, but the canonical Organization replaces them in published HTML. Clean up relevant source wording with the scheduled owner-scope edit; do not count a suppressed description as a separately rendered Organization. Existing official work/stay facts and admission/visa/cost numbers are retained, not transformed into ILMERA advice. The exact Italy owner sentence, immediate owner attribution and written-award caution remain unchanged.

No published factual denial of all loan, visa or local-document help was found. The main issues are overbroad old services, missing newly confirmed assistance, old responsibility assignments and unprovided pricing/refund assertions. Scope additions do not complete the 29 official-fact gaps. Actual feedback text/permission records, registration identifier and fee terms remain absent; a placement figure is expressly not authorized.

## All published routes reviewed

- `/`: visible copy, metadata, schema and FAQs inspected.
- `/about`: visible copy, metadata, schema and FAQs inspected.
- `/all-pages`: visible copy, metadata, schema and FAQs inspected.
- `/blog/`: visible copy, metadata, schema and FAQs inspected.
- `/blog/cost-of-studying-abroad-for-indian-students`: visible copy, metadata, schema and FAQs inspected.
- `/blog/documents-needed-to-study-abroad-from-india`: visible copy, metadata, schema and FAQs inspected.
- `/blog/how-to-choose-study-abroad-consultant-karnataka`: visible copy, metadata, schema and FAQs inspected.
- `/blog/scholarships-for-indian-students-study-abroad`: visible copy, metadata, schema and FAQs inspected.
- `/blog/study-abroad-counselling-from-coorg`: visible copy, metadata, schema and FAQs inspected.
- `/blog/study-abroad-with-academic-backlogs`: visible copy, metadata, schema and FAQs inspected.
- `/contact`: visible copy, metadata, schema and FAQs inspected.
- `/privacy-policy`: visible copy, metadata, schema and FAQs inspected.
- `/services`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-consultants-in-karnataka`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-consultants-in-kodagu`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-belagavi`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-bengaluru`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-chikkamagaluru`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-gonikoppal`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-hassan`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-kushalnagar`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-madikeri`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-mangaluru`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-mysuru`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-ponnampet`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-shivamogga`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-siddapura`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-somwarpet`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-udupi-manipal`: visible copy, metadata, schema and FAQs inspected.
- `/study-abroad-counselling-virajpet`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-gcc`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-germany`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-italy`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-latvia`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-lithuania`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-slovakia`: visible copy, metadata, schema and FAQs inspected.
- `/study-in-uk`: visible copy, metadata, schema and FAQs inspected.
- `/terms`: visible copy, metadata, schema and FAQs inspected.

## Verification boundary

Fresh Task 1: all 90 PHP files parsed, all 43 routes rendered, 258 browser cases and 1,110 FAQ interactions, strict discovery/names/wording/schema, sitemap/LLM/FAQ parity and both overlap checks passed. The scan is report-only; the listed business inconsistencies remain scheduled work. No deployment, external raw HTTP proof, native Apache acceptance or enquiry delivery is inferred.
