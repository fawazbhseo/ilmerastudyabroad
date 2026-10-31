# Flagged Items for Manual Verification

These are assumptions or gaps introduced during the SEO/AEO/GEO rewrite that
the site owner should confirm before or shortly after publishing. None of
them block the site from working correctly, but they affect accuracy or
brand polish.

## 1. Logo asset path (RESOLVED)
- All pages now consistently reference `assets/images/ilmera.logo.png` for
  the header logo, favicon, and `og:image`/`twitter:image` social preview
  tags. **Action needed:** confirm this exact file exists on the live server
  and renders correctly both as a small favicon (square crop) and as a large
  1200x630 social preview image; a dedicated square favicon and a dedicated
  social-preview image are usually sharper than reusing one logo file for
  both purposes.
- The header no longer references a separate "light theme" logo variant,
  because the light/dark theme toggle itself has been removed from the site
  (see item 4 below) : there is now only one visual theme, so only one logo
  file is needed.

## 2. Team photo filenames (RESOLVED)
- Standardized across the whole site to exactly:
  - `assets/images/ilmera.logo.png` (logo)
  - `assets/images/jabirkj.png` (Jabir KJ, Founder)
  - `assets/images/zaheer.png` (Zaheer KJ, CFO : lowercase "z")
  - `assets/images/fawazbh.webp` (Fawaz BH, CMO)
- **Action needed:** confirm these four files exist at these exact paths
  (case-sensitive) on the live server. `zaheer.png` was previously
  referenced inconsistently as `Zaheer.png` (capital Z) in some places :
  if the live server's filesystem is case-sensitive (most Linux hosts are),
  only one of those casings will actually work.

## 3. About page team cards (RESOLVED)
- Removed a duplicated "Jabir KJ" name that previously appeared twice in
  his team card.
- Unified all three team cards (Jabir/Fawaz/Zaheer) to the same structure:
  avatar image, name heading, role, then a bio paragraph of comparable
  length (roughly 55-60 words each, down from Jabir's ~115 words vs. ~65
  for the other two).
- Unified the `alt` attribute pattern on all three avatar images to
  "[Name], [Role] of/at ILMERA Study Abroad".

## 4. Light/dark theme toggle removed
- The `theme-toggle` button, its sun/moon icons, and the associated
  `localStorage`-based theme-switch script were removed from `header.php`
  at the site owner's request. The `html[data-theme="light"]` CSS rules
  elsewhere in `header.php`, `about.php`, and `contact.php` were left in
  place (they simply never trigger now, since nothing sets
  `data-theme="light"` anymore) rather than being stripped out, to avoid
  making a large, form of unrequested changes across multiple files.
  **Action needed:** if a future editor wants to fully remove all traces of
  the old light-theme feature (not just the button that triggered it), the
  `html[data-theme="light"]` CSS blocks in those three files can be deleted
  as a follow-up cleanup; leaving them in has no visible effect on the
  current site.

## 5. sitemap.php added alongside sitemap.xml
- `sitemap.php` was created per the site owner's request. Rather than
  duplicating the URL list in two independently maintained places (a
  risk for drift and a potential duplicate-content signal), `sitemap.php`
  301-redirects to the canonical `/sitemap.xml`, which remains the single
  source of truth and the one referenced in `robots.txt`.
- **Action needed:** none, unless the site owner specifically wants
  `sitemap.php` to generate its own independent XML instead of redirecting
  : in that case, say so and the redirect can be replaced with a PHP-
  generated sitemap (a version of this was drafted and is easy to restore).

## 6. Destination/eligibility facts to confirm against current official sources
The following figures were kept or written based on prior site content and
general knowledge, not independently verified this session. They should be
checked against current official/government sources before relying on them
for compliance-sensitive claims:
- UK Graduate Route: "up to 2 years of post-study work after completing a
  degree" (correct as a general rule at time of writing, but visa rules
  change; verify current validity).
- Italy DSU scholarship: described as regional, income-based (ISEE) and
  merit-based, potentially covering tuition, stipend, and subsidised housing
  and meals. Amounts and eligibility thresholds vary by region and by year
  and are intentionally not quoted as fixed numbers, but should be confirmed
  each admissions cycle.
- Germany: "public universities charge little to no tuition" and the APS
  certificate being "mandatory for Indian applicants since 2022" : confirm
  current APS requirement status and any tuition changes in the state(s)
  ILMERA actually places students in.
- Czech Republic / Lithuania / Latvia / Slovakia: described qualitatively as
  "low-cost" / "some tuition-free programmes" without specific fee figures.
  If specific fee ranges are added later, they must be sourced and dated.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): described as hosting
  "international branch campuses of UK, US and Australian universities" :
  true in general but should be confirmed for whichever specific campuses
  ILMERA actually works with.

## 7. Social handles and contact details
- Instagram handle standardized to `ilmera.studyabroad`; Facebook/LinkedIn
  standardized to `ilmerastudyabroad`. **Action needed:** confirm these
  handles are live, correctly spelled, and actually owned/managed by ILMERA
  before the site goes live, since a broken or wrong social link is a poor
  trust signal (E-E-A-T) for both human visitors and AI answer engines.
- WhatsApp number `+421 944485186` (a non-Indian country code) is used
  site-wide for the WhatsApp channel. This was already present in the
  inherited content and was not changed. **Action needed:** confirm this is
  intentional (e.g., a WhatsApp Business number) and correct if it should be
  an Indian number instead.

## 8. Minor cosmetic whitespace in about.php
- Two blank lines remain inside Jabir KJ's team card in the HTML source
  (between the avatar `<img>` and the `<h3>` name), left over from removing
  the duplicate name div. They collapse to nothing when rendered in a
  browser and have no visible or functional effect; flagged only for
  source-code tidiness if a future editor wants to remove them.

## 9. On the "#1 ranking" goal
No legitimate SEO/AEO/GEO work (on-page structure, schema, content quality,
crawler access, technical hygiene) can guarantee a #1 ranking on Google,
Bing, or any AI answer engine, because rankings are also driven by
competitor content, backlink profiles, domain authority/age, and ongoing
algorithm changes that are outside any single site's control. This project
strengthened every on-page and structured-data lever within a static site's
control (accurate schema, consistent NAP/contact data, clean URLs, crawler
access for AI bots, no fabricated claims that could trigger trust penalties).
Further ranking improvement beyond this point typically requires off-page
work (backlinks, reviews, citations) and ongoing content additions, which are
outside the scope of a one-time static-site rewrite.

## 10. New Blog feature added (RESOLVED)
- `/blog` was added as a new listing page (originally `blog.php` at the site
  root; **moved to `blog/index.php` to fix a 404**, see item 12 below), linked
  from the main
  navigation (`header.php`, both desktop and mobile menus) and from the
  footer's Navigation list (`footer.php`). It is also included in
  `sitemap.xml`.
- Four initial articles were written as **individual static PHP pages** under
  `/blog/{slug}` (e.g. `/blog/study-in-germany-free-aps-certificate`), each
  with its own SEO meta tags, Open Graph/Twitter tags, and `BlogPosting` +
  `BreadcrumbList` JSON-LD. This matches the rest of the site's fully static,
  server-rendered approach (important for AI/answer-engine crawlers that do
  not execute JavaScript) and avoids the 404s that would have resulted from
  linking to detail pages that did not exist.
- A `blog_posts` table was also created via the Table API (schema + 4 rows)
  early in this work, before the static-page approach was finalized. **This
  table is currently unused** : no page reads from it. It can be deleted if
  the site owner does not plan to move the blog to a dynamic/database-backed
  model later, or kept as a head start if they do. Flagging so it is not
  mistaken for live content.
- **UPDATE:** all four articles are now attributed to a single author, **Fawaz
  BH, CMO**, per the site owner's explicit request (previously Zaheer KJ was
  credited on the Germany/APS article and Jabir KJ on the Italy/DSU article).
  **Action needed:** let us know if the site owner wants additional articles,
  a "read more" pagination system, or category filtering as the blog grows.

## 11. Jabir KJ's title corrected from "CEO" to "Founder" (RESOLVED)
- Jabir KJ is the Founder of ILMERA Study Abroad, not the CEO. Every "CEO"
  reference to him has been changed to "Founder" across `about.php`
  (meta tags, JSON-LD `Person.jobTitle` and `description`, FAQ answers,
  visible hero/story/Kodagu-section prose, and the visible team card),
  `index.php` (JSON-LD `founder`/`employee` Person objects, FAQ JSON-LD and
  its visible `<details>` duplicate, and the visible team card), `contact.php`
  (`ai-content-summary` meta tag), `llms.txt`, and `llms-full.txt`. The
  `Organization.founder` relationship (`{"@id": ".../#jabir"}`) itself was
  left unchanged, since that relationship was already correct.
- `llms-full.txt`'s leadership section previously stated that "Founder" was
  an informal, non-authoritative variant of Jabir KJ's title; that sentence
  was rewritten since Founder is now his standardized, authoritative title.
- **Action needed:** none : this is complete. Confirm no other internal
  documents or external listings (e.g. Google Business Profile, LinkedIn
  company page) still list Jabir KJ as "CEO".

## 12. Blog pages returning 404 (RESOLVED)
- **Root cause:** the site had both a `blog.php` file at the site root AND a
  `blog/` directory (holding the 4 article pages) at the same time. The
  `.htaccess` rewrite rule that maps `/blog` to `blog.php` only fires when
  `%{REQUEST_FILENAME}` is **not** an existing directory
  (`RewriteCond %{REQUEST_FILENAME} !-d`). Because `blog/` is a real
  directory on disk, that condition failed for every request to `/blog`, so
  Apache tried to serve the `blog/` directory itself instead of `blog.php`
  and found no index file there, resulting in a 404 (individual article
  pages like `/blog/study-in-germany-free-aps-certificate` were unaffected,
  since those exact paths are not directories).
- **Fix applied:** moved the listing page from `blog.php` to `blog/index.php`
  and added `DirectoryIndex index.php index.html` to `.htaccess`. Now a
  request for `/blog` resolves directly to the directory's own `index.php`
  through Apache's normal directory-index behavior, with no naming conflict.
  No links needed to change, since `header.php`, `footer.php`, `sitemap.xml`,
  and the JSON-LD `Blog`/`BreadcrumbList` entities all already pointed to the
  extension-less `/blog` path, not to `blog.php` directly.
- **Action needed:** after deploying, verify `/blog` and all 4
  `/blog/{slug}` article URLs load correctly (not just that they no longer
  404, but that they render the full page, since a clean console/absence of
  a 404 does not by itself confirm correct rendering).


## 13. Phase 1: unpublished draft claim inventory (OWNER VERIFICATION REQUIRED)

The following three posts are not live yet per the owner. They retain
`noindex, follow` and are not shown on the four-card listing. There are now
7 article files under `blog/`, but only the 4 indexable articles are included
in the sitemap. The cost, documents and scholarships drafts are excluded
while they retain `noindex`.

**Release rule (Phase 4):** After fact-checking, publish through
`includes/posts.php` status, accurate metadata dates, a `sitemap.xml` entry
with accurate lastmod and a verified `llms.txt` summary in **one commit**.
Do not remove robots guards; they follow the registry. Links populate
automatically. Verify every item below against the relevant university,
scholarship body, consulate or immigration source. Record source URL,
applicable intake/date, exceptions and owner sign-off. See section 16.
No current official-source verification was performed in this repair.

### A. `blog/cost-of-studying-abroad-for-indian-students.php`

**Cost figures and cost comparisons (including zero/free claims):**
There are no numeric currency amounts or fee ranges in this draft. Its
amount claims are qualitative, including zero tuition and a free consultation:

- Czech Republic, Lithuania, Latvia, Slovakia and Russia are described as
  usually the cheapest destinations for Indian students.
- German public universities: little to no tuition regardless of nationality;
  zero tuition at most public universities; semester contributions apply.
  Most public universities charge no tuition for consecutive degrees, but
  a few states levy fees in specific cases. Living costs are called moderate.
- Italy: public universities charge tuition; regional DSU can cover tuition
  and add a stipend, subsidised accommodation and meals. Living costs are
  moderate and lower in smaller cities. DSU is said to make Italy cheaper
  than its sticker price for many families.
- Czech Republic: among the lowest EU tuition levels; low-to-moderate living
  costs. Lithuania: low tuition and some of the lowest EU living costs;
  living costs labelled low. Latvia: low tuition and low living costs.
- Slovakia: free tuition in some Slovak-language branches; English programmes
  are paid; low living costs. The free route is said to require a preparatory
  language-learning year.
- Russia: low tuition and low living costs.
- UK: substantial tuition, high living costs especially in London; a one-year
  Master's is said to shorten total cost.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): fees vary by university
  and branch campus; moderate-to-high living costs in Dubai/Qatar.
- Germany and Italy are said to genuinely approach zero tuition. This
  statement needs reconciling with the separate Slovakia free-tuition claim.
- Budget components: tuition/semester contribution; rent, food, transport,
  insurance; visa funds; application fees, APS certificate, document
  legalisation, flights and initial settlement money. City/programme
  differences, later-year tuition changes and scholarship renewal credits
  affect the total; a full first-year budget is recommended.
- The consultation and profile-matched country cost breakdown are described
  as free and carrying no commitment, before applications are filed.

**Document requirements, scholarship support and visa/work claims:**

- Most countries supposedly require proof of funds for at least the first
  year; Germany requires a blocked account with a government-set minimum
  that changes periodically. No minimum amount is quoted.
- APS certificate is presented as an India-specific Germany requirement
  and a one-off cost; document legalisation is included in the cost chain.
- DSU assessment: mainly family income (ISEE) and merit; amounts are set
  regionally and revised periodically. No numeric stipend, threshold or
  scholarship award amount is quoted. Some scholarships require credit
  thresholds for renewal.
- Russia: no IELTS and backlogs accepted at many universities. Latvia:
  flexible entry. Profile-matched routes are described for students with
  backlogs, low marks or no IELTS. These are eligibility claims to verify.
- Slovak-language free tuition requires a language preparatory year.
- Part-time work rules and work-hour limits differ by country and affect
  budgets; no specific limit or right to work is quoted.

### B. `blog/documents-needed-to-study-abroad-from-india.php`

**Cost figures and scholarship amounts:** no numeric monetary amounts,
fee ranges or scholarship award amounts are quoted. Document review and
first consultation are described as free; verify the service scope.

**Every core document requirement asserted for all destinations:**

- Valid passport: enough blank pages and validity to cover course duration;
  renew first if it expires soon.
- Academic records: 10th and 12th marksheets; degree certificates and
  transcripts for Master's applicants; backlog-clearing documents.
- University offer/admission letter.
- Funds evidence: bank statements, loan approval or sponsor letter under
  destination rules; Germany uses a blocked account and other destinations
  use their own formats.
- Language evidence: IELTS/TOEFL where required, Medium-of-Instruction
  letter, internal test, or German/Italian proficiency for local-medium study.
- Passport photographs meeting destination specifications; sizes differ.
- Statement of Purpose and references where the university asks.
- Destination-valid health insurance, arranged before or at arrival
  depending on country.

**Every country-specific document, scholarship and visa claim:**

- Germany: APS certificate for Indian applicants, blocked account
  (Sperrkonto) confirmation, German/English proficiency per programme.
- Italy: pre-enrolment on the university portal; ISEE income declaration for
  DSU; translated and legalised academic documents; CIMEA or equivalent
  statements where asked. No DSU amount is given.
- UK: CAS letter, TB test certificate where required and English proficiency
  per course. The Graduate visa is stated as **2 years** for applications
  on or before **31 December 2026**, and **18 months** from **1 January 2027**,
  attributed to gov.uk. Verify the official rule, eligibility and exceptions
  before publication; this repair does not validate those dates or durations.
- Russia: invitation letter issued through the university, HIV test
  certificate and recognised medical insurance.
- Czech Republic, Lithuania, Latvia, Slovakia: apostilled or superlegalised
  documents per consulate, accommodation confirmation, entry-period travel
  insurance. Verify each country separately rather than assuming one rule.
- GCC (UAE, Saudi Arabia, Qatar, Kuwait, Bahrain, Oman): university-specific
  admission documents and sponsor/guardian documents where required;
  requirements vary by country and institution.
- Legalisation/apostille steps are said to depend on each consulate; visa
  amounts and document validity periods vary by destination and intake.
- Sequencing advice: start passport and APS/verification first because they
  are said to be slowest and block later work; collect and legalise academics
  in parallel; file DSU/scholarship documents as the window opens because
  income documents take weeks; assemble the visa file and book an appointment
  only after the offer letter arrives. Verify these instructions against
  the actual application/appointment rules.
- Consulates in Bengaluru and Chennai are said to have seasonal queues;
  verify jurisdiction and appointment arrangements for each destination.
- CFO Zaheer KJ is described as handling transcript/marksheet verification,
  APS submissions, filing and visa appointment scheduling against intake
  deadlines; owner should confirm the actual scope and workflow.

### C. `blog/scholarships-for-indian-students-study-abroad.php`

**Cost figures and scholarship amounts:** no numeric currency amounts,
award ranges or income/credit thresholds are quoted. All qualitative
funding and eligibility claims still need verification:

- Italy DSU: income-based regional student-welfare support, tuition relief,
  an annual stipend, subsidised accommodation and meal services. Assessment
  is family income (ISEE/ISEE parificato) and merit credits; described as
  suited to middle-income families and architecture, arts and engineering.
- DSU income thresholds and stipends vary regionally (Lombardy and Sicily
  are examples); scholarship amounts, deadlines and eligibility thresholds
  change each cycle. No fixed amount is supplied.
- German public universities: tuition-free route rather than a scholarship;
  most public universities charge no tuition for consecutive degrees,
  only a semester contribution; admission requirements depend on programme.
  Described as one of the cheapest total-cost destinations without an award.
- University merit awards: fee waivers or partial awards at intake, based
  on academics and sometimes interview/portfolio; described as suitable
  for strong academics in any destination.
- UK Chevening, Commonwealth and other government schemes: fully or largely
  funded study for eligible candidates, direct applications to the scheme;
  assessed on academics, leadership and scheme-specific criteria, described
  as fitting applicants with work or community records. Verify each scheme
  and its current eligible courses and benefits separately.
- Partial awards at expensive destinations may leave a higher total cost
  than tuition-free destinations without awards. Many awards require
  credits to renew; DSU renewal depends on required credits.
- DSU and government-scheme windows are said to close months before intake,
  with late applications rejected. Check each scheme's actual dates/rules.
- ILMERA's scholarship eligibility check is described as free, with no
  promise of an award. Owner should confirm the service scope.

**Document requirements and visa claims:**

- International DSU applicants file an equivalent ISEE declaration through
  the regional body with translated and legalised documents; confirm the
  actual regional process and required documents.
- Germany: visa proof of living funds through a blocked account; APS
  certificate described as the India-specific entry gate. No minimum
  blocked-account amount is quoted.
- University awards may require an interview or portfolio; government
  schemes have scheme-specific academic/leadership criteria.
- Founder Jabir KJ is said to be studying at the University of Rome Tor
  Vergata and to have personally completed DSU/proof-of-funds work; owner
  should verify the personal-experience assertion before relying on it.

**Editorial release checks for all three drafts:** meta/JSON-LD/byline claims
that the posts are updated or reviewed in October 2026 are not evidence of
verification. The source comments point to
`flagged-items-for-verification.md`; use this inventory for sign-off. Retained `noindex`
while repairing paths does not restrict direct access to deployed PHP files.

## 14. Migrated Phase 2 verification checklist (OWNER VERIFICATION REQUIRED)

The four Phase 2 pages now render from `places/{slug}.php` through the
shared template. Their previous visible markers have been converted into
empty fact fields or unanswered FAQ entries. The checklist below records
unresolved research, not text to paste into a page. Existing-content
provenance is recorded in the spreadsheet; it is not independent current
verification of immigration or university requirements.

All 17 place records remain drafts. Publication-aware footer/homepage
helpers do not link to them; none is in the sitemap or either LLM file.
Drafts can be requested directly, but shared link helpers suppress draft
targets on all pages. Noindex is not access control. Follow sections 15 and
16 for readiness and the same-commit release workflow; do not manually
remove robots tags or add footer links to bypass publication checks.

Check each item against owner-approved records or a current official
institution, lender or visa-authority source. Record the source, date,
applicable course/intake and owner sign-off. Institution-origin statements
need actual enquiry evidence, not an assumed local catchment. Do not
publish student personal records. Confirm actual remuneration, including
any university payments, before replacing a fee-model placeholder.

### Supported facts reused from existing site files

- `about.php`: Coorg/Kodagu base, no physical office, phone/WhatsApp/video
  counselling, named team and document responsibilities, PUC/Karnataka
  state board familiarity, four counselling languages, digital sharing,
  and the student's own visa appointment as the travel step. Its generic
  Bengaluru/Chennai reference is not a district-specific jurisdiction rule.
- `terms.php`: free initial consultation, paid-service fees/scope agreed
  before paid work, and no admission, scholarship or visa guarantees.
- `services.php` and the existing Germany/APS, Italy/DSU, backlogs and Coorg
  blog articles: covered destinations and the linked counselling routes.
  Reusing existing guidance is not independent verification of current
  immigration, scholarship or university rules.

### Checklist by page

Each former placeholder is listed once below. Unanswered FAQ entries are
not rendered or included in schema. None is an endorsement
of an institution or lender, a claim of prior student placements, or a
confirmed travel instruction.

#### `/study-abroad-consultants-in-karnataka`

Source: `study-abroad-consultants-in-karnataka.php`

- [ ] [VERIFY: Current visa appointment jurisdiction and attendance requirements for Karnataka applicants.]
- [ ] [VERIFY: OWNER to confirm how ILMERA earns money.]

#### `/study-abroad-counselling-belagavi`

Source: `study-abroad-counselling-belagavi.php`

- [ ] [VERIFY: Belagavi MOI issuing department and destination acceptance.]
- [ ] [VERIFY: Belagavi attestation or legalisation steps for the selected destination.]
- [ ] [VERIFY: Belagavi colleges and universities represented in owner-confirmed student enquiries.]
- [ ] [VERIFY: Belagavi education-loan banks, eligibility, sanction evidence and disbursement terms.]
- [ ] [VERIFY: Belagavi transcript issuer, application channel, fees and turnaround.]
- [ ] [VERIFY: OWNER to explain ILMERA payment sources and fee model for Belagavi enquiries.]
- [ ] [VERIFY: Visa appointment city and travel route from Belagavi for the chosen destination.]

#### `/study-abroad-counselling-shivamogga`

Source: `study-abroad-counselling-shivamogga.php`

- [ ] [VERIFY: Assigned visa appointment city, transport options and travel timing from Shivamogga.]
- [ ] [VERIFY: OWNER to confirm ILMERA remuneration and written fee scope for Shivamogga students.]
- [ ] [VERIFY: Shivamogga MOI authorisation, request procedure and accepted wording.]
- [ ] [VERIFY: Shivamogga education-loan providers, application documents and funding-release conditions.]
- [ ] [VERIFY: Shivamogga institutions and course backgrounds supported by actual student enquiries.]
- [ ] [VERIFY: Shivamogga record certification sequence and destination-specific attestation requirements.]
- [ ] [VERIFY: Shivamogga transcript requests, revised marksheets and current processing timelines.]

#### `/study-abroad-counselling-udupi-manipal`

Source: `study-abroad-counselling-udupi-manipal.php`

- [ ] [VERIFY: Attestation and legalisation requirements for Udupi and Manipal academic records.]
- [ ] [VERIFY: OWNER to disclose ILMERA income sources and service pricing for Udupi and Manipal.]
- [ ] [VERIFY: Udupi and Manipal MOI letter process for each awarding institution.]
- [ ] [VERIFY: Udupi and Manipal colleges, universities and student-origin records approved by the owner.]
- [ ] [VERIFY: Udupi and Manipal education-loan banks, scholarship treatment and visa-funds evidence.]
- [ ] [VERIFY: Udupi and Manipal transcript issuers, campus-specific requests and delivery formats.]
- [ ] [VERIFY: Visa appointment jurisdiction and outward/return journey from Udupi or Manipal.]

## 15. Phase 3 data completion and release checks

### Inventory and unresolved scope

- [ ] Review the four migrated records: `karnataka`, `belagavi`, `shivamogga`,
  `udupi-manipal`. Confirm current source validity before using the retained
  general guidance for publication. Review the 23 items in section 14,
  populate only source-supported optional categories, and complete only
  supported FAQ answers. Unknown optional values can remain empty.
- [ ] Supply source-backed local content for the 13 empty draft records:
  `kodagu`, `madikeri`, `virajpet`, `kushalnagar`, `gonikoppal`, `somwarpet`,
  `ponnampet`, `siddapura`, `mysuru`, `mangaluru`, `hassan`, `chikkamagaluru`,
  `bengaluru`. All fact fields are intentionally empty, not silently assumed.
- [ ] Confirm district metadata where the key is empty. Only the requested
  Kodagu grouping is populated. Page type is an editorial routing category,
  not a verified municipal-status assertion.
- [ ] Review related-guide choices in `nearby`. Towns have both hubs and two
  other towns; Kodagu lists seven town guides. These choices carry no claim
  about distances, transport availability or local student origins.
- [ ] For each place, verify institutions/student origins, transcript and MOI
  procedures, attestation, loan options and the destination-specific visa
  appointment journey before entering them. Never infer these from another
  place's process. Do not add office or competitor claims.

### Data contract and threshold

Required keys: `slug`, `name`, `type`, `district`, `status`. Keep a district
value empty while unknown. Optional fields are `intro_answer`,
`local_institutions`, `transcript_and_moi_steps`, `local_loan_options`,
`visa_appointment_route`, `local_notes`, `faqs`, `nearby`.

Only these seven fact categories count toward the minimum: intro,
institutions, transcript/MOI steps, loans, visa route, notes and complete
FAQs. Each category counts once. A 40-60 word intro is required only when
provided; invalid-length intros are omitted. Whitespace, incomplete FAQ
pairs and placeholder-bearing text do not count or render. Metadata,
related links and the single shared ILMERA process block never count.

All current entries remain draft: the four migrated records have three
valid categories each, and the 13 new records have zero. A published flag
alone cannot enable indexing. The template forces robots-meta and HTTP
noindex unless status is published and at least five valid categories are
present. Empty content sections and empty FAQPage schema are not emitted.
The same readiness check hides links to unready data on all pages,
including drafts, through the Phase 4 link helpers.

### One-commit publication checklist

- [ ] Fill the spreadsheet row with confirmed facts and source evidence.
  Keep its 26 headers and all 17 existing rows intact. Lists and FAQs are
  JSON cells; source columns can include a matching list of evidence links.
- [ ] Transfer the reviewed row to `places/{slug}.php` as PHP strings/arrays,
  not encoded JSON strings. This is manual, not an automatic CSV import.
  Keep optional unknown fields empty. Do not paste VERIFY/OWNER/TODO text.
- [ ] Check at least five valid categories, appropriate district/type values,
  complete FAQs and all related/inline targets. Set status to published in
  both the PHP record and the spreadsheet only after owner approval.
- [ ] Add the clean URL to `sitemap.xml` with accurate Git-based lastmod and
  add the verified page to `llms.txt` in that same commit.
- [ ] Check automatically populated footer, parent/nearby guides,
  breadcrumbs and `/all-pages`. Do not add manual links to bypass the
  shared gate. No unready page belongs in sitemap or LLM context files.
- [ ] Verify rendered noindex/index behavior, FAQ/schema parity, source
  coverage and hosting-stack routing before release. Noindex is generated
  by the renderer; do not remove its conditional guard.

No local institution, lender, travel route or revenue model was confirmed
by the technical build. The spreadsheet's existing-content sources are
migration provenance, not new official-source verification.


## 16. Phase 4 publication and navigation release checks

This section supersedes earlier manual noindex-removal or footer-addition
instructions. Four existing guides remain published; the cost, documents
and scholarships guides stay draft until the claims in section 13 are
verified. All 17 places stay draft; the minimum-five-category gate remains.
The technical changes are not an owner sign-off or fact verification.

### Publish one reviewed page atomically

- [ ] Verify and record sources, current intake/date, exceptions and owner
  approval. Retain unknown place fields as empty data, not marker text.
  A place needs at least five valid local-fact categories; metadata,
  navigation and shared process copy never count toward that threshold.
- [ ] For a post, set `status` to `published` in `includes/posts.php`; set
  accurate `datePublished` and `dateModified` dates after review. The draft
  scaffold date must not be passed off as actual first publication.
- [ ] For a place, transfer reviewed CSV facts to its returning PHP array
  and set status to published in both. Confirm a matching thin route file,
  district/type accuracy and complete FAQ pairs before releasing it.
- [ ] In the **same commit**, add the clean canonical URL to `sitemap.xml`
  with accurate `lastmod` based on the substantive content/release date
  and relevant Git history, not filesystem timestamps or blanket dates.
- [ ] In the **same commit**, add the verified page and a factual summary
  to `llms.txt`. Keep `llms-full.txt` consistent if its content is affected.
  Never recommend a draft or underfilled place in either LLM context file.
- [ ] Confirm the generated robots meta and actual HTTP X-Robots-Tag agree
  with eligibility on staging. Do not delete conditional robots code.
- [ ] Confirm automatic listing/latest/related/service/footer/directory
  links and visible/schema breadcrumbs. A post's configured related slugs
  are filtered and filled with other published posts as needed. Locations
  appear in order: Karnataka, districts, towns/cities. Empty columns and
  groups must not appear. No manual footer or related-list edit is needed.
- [ ] Keep `/all-pages` footer-linked and published-only, but **do not add
  it to `sitemap.xml`**. It is a human directory, not the XML sitemap.
- [ ] Check local links/anchors, visible FAQ/schema parity, clean URLs and
  hosting rewrites. Unpublished ancestors are skipped in both breadcrumb
  outputs; do not link them as a workaround for an incomplete hierarchy.

Status, accurate sitemap lastmod and `llms.txt` belong to the same release
commit. Helpers do not edit XML/text files. If withdrawing a post/place,
change status and remove its sitemap/LLM recommendations in one commit;
the helper-driven links stop linking it automatically. New static pages
need registration in `ilmera_static_pages()`; new place/post records also
need their actual route file.

### Content scope and unresolved follow-up

- Country sections use published planning guides where no dedicated country
  guide exists. The Coorg process guide links to `/services#process`; no
  unrelated destination is attributed to it. No new country claims were
  added to make an internal link look more specific.
- Existing `nearby` selections are editorial related places, not verified
  nearest locations. Confirm them before adding proximity/travel claims.
  All unknown district labels remain empty rather than guessed.
- All 58 PHP files linted and all 33 HTML pages rendered cleanly under PHP
  8.5 WASM. Isolated synthetic tests exercised status changes, 4/5-category
  boundaries, placeholder/FAQ rejection, parent hierarchy, group ordering,
  date changes, empty columns and encoded/direct-PHP draft-link aliases.
- Phase 4 Chromium checks recorded mobile table overflow in the cost and
  scholarships drafts and missing menu wiring on About and other templates.
  Both issues are resolved by the Phase 5 shared-menu and table-container
  fixes. See section 17 for the current validation and remaining checks.
- Actual HTTP headers, native Apache routing, production fonts and hosting
  behavior remain staging checks. No deployment, live-source fact audit,
  local financial/travel verification or outcome guarantee was performed.


## 17. Phase 5 menu and draft-table fixes (RESOLVED)

The two technical findings from Phase 4 are resolved. This does not verify
any article claims or authorize publication of the three draft posts.

### Shared mobile menu

- `includes/header.php` now owns the single mobile menu script. It toggles
  on the button, closes on every menu link and Escape, and keeps button
  aria-expanded, labels and the menu's aria-hidden/inert state synchronized.
  Body scrolling is restored after closing; Escape returns button focus.
  Resizing above 768px closes the overlay rather than leaving scroll locked.
- Duplicated Home, Contact, `/all-pages` and place-renderer handlers are
  removed. About, Services, blog pages, legal pages and all other pages
  using the shared header receive the same behavior. The 404 page now uses
  that header too, retaining its existing error content and styling.
- Verified all 33 HTML pages at both 375px and 768px with JavaScript on/off
  (132 Chromium combinations). Every menu opens and closes on the button,
  closes on each of its five links and Escape, and maintains the expected
  ARIA, focus, inert and body-scroll states. Resize/scroll restoration were
  also exercised. All navigation destinations remain reachable with
  JavaScript disabled via the footer or existing static 404 page links.

### Scrollable draft tables

- Every table in the cost, documents and scholarships draft posts is inside
  a labelled, keyboard-focusable region with overflow-x: auto. Existing
  table contents and styling are unchanged; the only added styling contains
  horizontal overflow. At both tested widths, with JavaScript on/off,
  document width stays within the viewport and wide tables scroll inside
  their own containers. The earlier 375px page-width overflow is resolved.
- All three posts remain draft/noindex. Registry status, robots guards,
  sitemap and both LLM files are unchanged. Their official-source claims
  still require the owner checks in section 13 and the atomic release
  workflow in section 16. Technical fixes are not editorial sign-off.

### Validation limits

All 58 PHP files passed PHP 8.5 WASM lint and all 33 full pages rendered
without warnings/errors, with one shared menu implementation. Table HTML
contents were compared exactly against the pre-fix version, and existing
LF/CRLF conventions were retained. No tests, fixtures, screenshots or
packages were added to Git. Native Apache behavior, actual HTTP headers,
production fonts/CDN resources and deployment remain staging checks; the
browser tests supplied local images and blocked external resources.


## 18. Phase 6 founding-year audit and destination release checks

### Founding year (RESOLVED)

The owner confirms ILMERA was founded in 2026, not an earlier year. About's
JSON-LD foundingDate, hero .ms stat, stat-item text/data-target and HUD array,
the homepage hero stat and README are corrected. Historical changelog stats
are corrected too. The whole-repository text audit included llms.txt,
llms-full.txt, blog articles, place data and docs. No other company founding
year or longer-history claim was found. References to student academic/work
history or individuals' experience are not company-age claims; those existing
claims still need their original owner checks where flagged above.

### Nine destination records (OWNER VERIFICATION REQUIRED)

Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and
GCC all start draft. Every fact group, intro/source field, date and approved
host list is empty. The ilmera_summary wording is migrated from existing
Services/LLM qualitative hedges and service descriptions with Git provenance;
no concrete fee, figure, date, deadline, visa or eligibility rule was moved
into this unsourced summary field. Summaries are not official evidence and
never contribute to the five-category threshold. Do not use them to bypass
source requirements. Existing Services/LLM claims remain subject to their
prior verification inventory; this build does not certify them.

### One-commit destination release checklist

- [ ] Obtain official university, scholarship-body or government sources and
  owner approval. Record the exact statement, URL, label, applicable context
  and actual checked-on date. Do not supply facts from memory or guess dates,
  fees, thresholds, deadlines, visa rules or eligibility rules.
- [ ] Review exact official hostnames and enter them in official_source_hosts.
  Membership means owner approval only, not proof of ownership or accuracy.
  Source URLs must use HTTPS and an approved hostname or any dot-delimited
  subdomain of it. Missing labels, unapproved hosts, malformed URLs,
  credentials and explicit ports are rejected. Review parent-domain scope;
  source-host acceptance does not verify the linked claim.
- [ ] Fill the corresponding row in destinations-facts-template.csv. There
  are nine rows and 47 columns. Ordinary groups use JSON text arrays; FAQ
  values use question/answer objects. Their source_url, source_label and
  checked_on columns are parallel JSON arrays aligned by item index. Intro
  and intro source fields are scalar cells; unknown scalars stay blank and
  unknown lists stay []. Keep metadata and summary provenance intact.
- [ ] Manually transfer reviewed values to destinations/{slug}.php. Ordinary
  items need text/source_url/source_label/checked_on; FAQs need complete
  question/answer plus those source fields. Intro, if used, needs 40-60 words
  and its sibling intro_answer_source_url/source_label/checked_on values.
  Whitespace, incomplete FAQs, placeholder-bearing entries and unsourced
  facts never render or count. Do not paste verification markers into data.
- [ ] Enter actual review dates, including facts_last_checked for the page.
  Empty or invalid dates are omitted rather than invented. Confirm all
  current Sources links support the exact statements and that review dates
  accurately describe the fact review, not simply a template edit date.
- [ ] Check at least five of ten categories contain valid sourced items:
  intro, who_its_for, english_requirements, costs, scholarships, visa_steps,
  intakes, documents, work_and_stay and FAQs. Each group counts once; summary,
  metadata, sources and shared counselling copy never add categories.
- [ ] After owner sign-off, set status to published in PHP and CSV. Confirm
  the matching thin /study-in-{slug} entry file exists. Do not remove robots
  guards or force links to a draft or underfilled page. The actual gate is
  published status plus five valid sourced categories, not the dates alone.
- [ ] In that SAME COMMIT, add the clean URL to sitemap.xml with accurate
  lastmod based on the substantive review/change and relevant Git history,
  not filesystem timestamps or a blanket date update.
- [ ] In that SAME COMMIT, add the verified destination and factual summary
  to llms.txt. Keep llms-full.txt consistent if affected. No LLM file should
  recommend an unpublished destination. Helpers do not edit XML/text files.
- [ ] Verify automatically populated footer Country guides, /all-pages,
  homepage buttons/ItemList, Services headings and matching published post /
  place links. Ineligible targets must remain unlinked or fall back to
  /services#country. Do not invent a country association for a place or the
  country-neutral Coorg process article. Keep /all-pages outside sitemap.xml.
- [ ] Verify actual robots headers/meta on staging, canonical URLs, native
  FAQ behavior and exact visible/schema FAQ text, Home/Services/country
  breadcrumbs, item citations and deduplicated Sources/date output. Noindex
  is not access control; drafts can be requested directly.

Sourced facts, published status, accurate sitemap entry and llms.txt must be
released in one commit. If withdrawing a page, change status and remove its
sitemap/LLM recommendations together. Helper-driven links disappear or fall
back automatically. No current destination is approved or published here.

### Technical validation and remaining work

All 78 PHP files linted and all 42 HTML pages rendered cleanly under PHP 8.5
WASM. Nine empty draft records match the CSV. Isolated synthetic fixtures
covered four/five-category and draft/published boundaries, missing and bad
sources/hosts, placeholders, intro lengths, count inflation, partial FAQs,
exact FAQ/schema text, source deduplication, all nine automatic link targets,
matching published posts/places, withdrawals and encoded/direct-PHP aliases.

Chromium passed 282 page/width/JavaScript combinations: 42 current pages and
five isolated published-fixture pages at 375/768/1280px, JS on/off. Checks
covered destination layout, menu and FAQ behavior, source/date links, shared
breadcrumbs and corrected founding stats/HUD. Synthetic QA facts, hosts,
dates and publication flags stay outside the repo and never enter production.

Official facts and source URLs were not provided for publication and none
were independently verified by this build. Owner approval and source review
remain necessary. Actual HTTP headers, native Apache rewrites, production
fonts/CDNs and deployment remain staging checks. Browser tests blocked
external resources and supplied local images. Existing post/place statuses,
place spreadsheet, Apache rules, sitemap and both LLM files are unchanged.


## 19. No placed students or implied student results (OWNER CONFIRMED)

The owner confirms ILMERA is new and has no placed students. Study-route
cards and service descriptions must describe prospective counselling and
application guidance, never testimonials, completed placements, admissions,
scholarship awards, successful visas or other student results attributed to
ILMERA. Do not imply a track record through phrases such as a most-common
route already arranged, students already placed abroad or completed arrivals.

The homepage section is now "Study Routes ILMERA Guides", with all three
decorative quotation marks and their unused styling removed. Cards retain
service labels and existing design rather than student names or review
attribution. Route/FAQ wording and its matching schema use guidance language.
Related wording in the backlog article, Latvia Services section and both
LLM files is corrected. The LLM files explicitly record this owner-confirmed
policy. Existing destination rules and figures were not independently checked
or expanded; their source-review requirements elsewhere in this file remain.

The content audit included public PHP, blog articles, destination/place data
and both LLM files. Remaining references to university alumni, students'
academic results, document replacement, form-submission success and explicitly
historical removed content are not claims of ILMERA student outcomes. No
student-result claims or testimonials were added. All draft statuses remain.

Technical checks: all 78 PHP files linted, 42 pages rendered without PHP
warnings/errors, schema JSON parsed, homepage FAQ/schema parity passed, and
18 Chromium page/width/JavaScript combinations passed for the changed pages
at 375/768/1280px, JS on/off. Three route cards remain with no quote decoration;
responsive layout and menu behavior remain intact. External browser resources
were blocked; local images were supplied. No test artifacts were committed.
Native hosting behavior, production fonts and deployment still need staging.


## 20. Phase 7: fully sourced Czech draft, not approved for publication

This section supersedes section 18's empty-Czech-record and exact-host-only
statements and section 19's description of the earlier LLM policy. Other
historical verification items remain open unless separately resolved.

The complete owner-supplied Czech content is now in
`destinations/czech-republic.php`, still `draft`. It has five sourced fact
categories: intro, costs, visa_steps, documents and faqs. All rendered facts
carry source metadata; six unique URLs support the supplied content. Fully
sourced describes data coverage only, not a finding that the claims are
current or correct. Neither the URLs nor the facts were independently
verified. The supplied 2026-10-15 metadata is retained, not a claim of an
independent review by this build. Other eight destination records remain
empty drafts. The CSV remains an empty template and must be filled before
release; it does not yet mirror the Czech PHP content.

### Owner must open and confirm all six source URLs

The supplied file contains six URLs rather than five. Do not omit any from
review. For each link, confirm official ownership, current page availability,
applicability to the intended applicant and route, and support for each exact
statement that cites it. Confirm the actual review dates. In particular,
check whether the ko_old requirements page remains applicable; a source link
alone is not evidence that its information is current.

- [ ] Study in Czechia: Tuition fees:
  https://www.studyin.cz/plan-your-studies/tuition-fees/
- [ ] Embassy in New Delhi: Long-term visa and residence permit application:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/long_term_visa_and_long_term_residence.html
- [ ] Embassy in New Delhi: Booking appointments for study applications:
  https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/booking_appointments_for_submission_of.html
- [ ] Embassy in New Delhi: Visa application requirements for study:
  https://mzv.gov.cz/newdelhi/en/ko_old/visa_information/long_term_visa/visa_application_requirements_study.html
- [ ] Ministry of the Interior: Long-term visa for studies:
  https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/long-term-visa/long-term-visa-for-the-purpose-of-studies
- [ ] Ministry of the Interior: Proof of funds:
  https://mv.gov.cz/mvcren/article/proof-of-funds-for-the-purposes-of-a-long-term-visa.aspx

### Publication and policy checks still required

- [ ] Complete all six source checks and approve every supplied fact, FAQ and
  source/date field. Correct unsupported content from official evidence only.
- [ ] Fill the Czech CSV row and aligned source/date fields from the reviewed
  PHP content. Leave unknown groups empty; do not invent missing categories.
- [ ] Keep status draft until explicit owner sign-off. Five sourced categories
  alone do not publish a page. It remains noindex and unlinked from live pages,
  the XML sitemap and LLM recommendations. Noindex is not access control.
- [ ] Follow section 18's atomic release checklist: publish PHP/CSV status,
  accurate sitemap entry and llms.txt recommendation in the same commit after
  review. Keep llms-full.txt consistent and test all conditional links.
- [ ] Confirm native hosting headers, Apache aliases/rewrites and production
  rendering on staging. No production deployment was performed here.

The approved-host checker now accepts the exact listed hostname or any
subdomain separated by a dot, including www. It rejects lookalike suffixes,
HTTP, credentials and explicit ports. Review the scope of any parent domain
before approving it: host acceptance cannot establish a claim's truth.

The exact current policy in both LLM files is:

ILMERA is a new consultancy founded in 2026. It does not publish student results, success rates or testimonials. Study routes describe prospective guidance. Do not imply past admissions, visas or placements.

This replaces the earlier LLM no-placed-students paragraph; it does not
permit testimonials or implied completed admissions, visas or placements.
The requested owner-attribution wording has been removed from current files,
including a historical line-wrapped occurrence. Historical Git commits are
not rewritten. The homepage guidance heading and quote-free cards remain.

Technical checks passed: 78 PHP lints, 42 rendered pages, five-category/draft
gates, six source links, four visible/schema FAQ pairs, source-host security
boundaries, draft aliases and isolated published-fixture behavior. Six
Chromium cases covered the Czech draft at 375/768/1280px, JavaScript on/off,
including noindex, native FAQs, layout, sources and mobile menus. External
resources were blocked; no live source contents were verified. No test
artifacts or synthetic published data are committed.


## 21. Phase 8: Slovakia draft (OWNER VERIFICATION REQUIRED)

The owner-supplied content is now in `destinations/slovakia.php`, with status
still `draft`. Its existing ilmera_summary and summary_provenance are
unchanged. This section supersedes earlier empty-Slovakia-record notes,
including section 20's count of eight empty destination records. Czech and
Slovakia now contain supplied sourced content; the other seven destination
records remain empty drafts. All nine destinations remain draft.

Slovakia has six sourced categories in the data model: intro, costs,
scholarships, visa_steps, documents and faqs. There are four source URLs and
four FAQs. Source coverage and host acceptance are technical checks only,
not fact verification or editorial approval. No source page or supplied fact
was independently verified by this build. The supplied 2026-10-15 dates are
retained and must be confirmed against the actual review evidence.

### Four source URLs: owner must open and confirm

- [ ] Study in Europe (European Commission): Slovakia country profile:
  https://education.ec.europa.eu/study-in-europe/country-profiles/slovakia
- [ ] IOM Migration Information Centre Slovakia: Studying at a university in Slovakia:
  https://www.mic.iom.sk/en/news/894-studying-at-a-university-in-slovakia.html
- [ ] Embassy of the Slovak Republic in New Delhi: National visa:
  https://www.mzv.sk/en/web/dilli-en/services/national-visa
- [ ] Embassy of the Slovak Republic in New Delhi: Contact and appointments:
  https://mzv.sk/en/web/dilli-en/contact-us

### Publication blockers

- [ ] Approve IOM as an official source explicitly before publishing.
  mic.iom.sk is an IOM information centre, not a government host. Its inclusion
  in the supplied official_source_hosts array allows technical source
  validation only; it does not record completed owner approval of IOM as an
  official source. Review its authority and the exact statements cited.
- [ ] Obtain written confirmation from a Slovak university of the free-tuition
  wording for non-EU students before publishing. The owner reports a conflict
  with a non-official portal that says 2,000 to 5,000 euros a year. The portal
  name and URL were not supplied, and neither claim has been independently
  resolved here. Confirm applicability to the intended student's nationality,
  programme language, full-time status, institution and study duration; retain
  the written evidence and reconcile the intro, costs and FAQ wording before
  release. Do not treat the conflicting portal amount as a verified fee.
- [ ] Re-check the embassy appointment method on the embassy page before
  publishing and again before applying. Confirm that the supplied email
  booking route and cons.delhi@mzv.sk apply to the intended study/national D
  visa route; do not assume the present method remains current. Review both
  the national-visa and contact/appointments pages listed above.
- [ ] Confirm every other supplied statement against its linked source,
  including the scholarship, budget, document, residence and insurance
  wording, and record accurate checked-on and page-wide review dates.

### Draft safeguards and release checks

Status remains draft despite six sourced categories. The page stays noindex
and unlinked from live pages, sitemap.xml and LLM recommendations. Noindex
is not access control; direct requests can render the draft. Do not publish
until all blockers above and explicit owner sign-off are complete.

The CSV remains an unchanged empty template, not a synchronized copy of
Slovakia's populated PHP record. Fill and review its Slovakia row and aligned
source/date fields before release. Follow section 18's atomic release
checklist: published PHP/CSV status, accurate sitemap entry and llms.txt
recommendation must ship in one commit after approval; keep llms-full.txt
consistent. Do not change status or discovery files in this phase.

Technical validation passed: 78 PHP lints, 42 clean page renders, four
visible/schema FAQ pairs, four exact source links, six-category/draft gates,
draft aliases, host-boundary tests and an isolated status-only published
fixture. Summary/provenance and all other destination records are unchanged.
Six Chromium cases covered Slovakia at 375/768/1280px with JavaScript on/off,
checking noindex, four source links, native FAQs, layout and mobile menus.
External resources were blocked; no live source contents were checked. No
test artifacts are committed. Native hosting headers, Apache rewrites and
production rendering remain staging checks; no deployment was performed.


## 22. Phase 9: Lithuania draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/lithuania.php`, still
`draft`, with ilmera_summary and summary_provenance preserved exactly.
Lithuania has five sourced categories in the data model: intro, costs,
visa_steps, documents and faqs. Three source URLs and four FAQs are present.
Five categories alone do not authorize publication. Technical source-host
acceptance is not editorial approval or evidence that a statement is current.
No source page or supplied fact was independently verified by this build.
The supplied 2026-10-15 dates are retained, not an independent review date.

This section and section 23 supersede earlier empty-Lithuania/Latvia notes,
including section 21's count of seven empty records. Czech, Slovakia,
Lithuania and Latvia now contain supplied sourced content; the other five
destination records remain empty drafts. All nine destinations remain draft.

### Lithuania source URLs: owner must open and confirm all three

- [ ] Migration Department of Lithuania: Services for persons abroad, Republic of India:
  https://migracija.lrv.lt/en/structure-and-contacts/information-for-visitors/services-for-persons-abroad/temporary-residence-permit-and-national-visa-services/republic-of-india/
- [ ] Study in Europe (European Commission): Lithuania country profile:
  https://education.ec.europa.eu/study-in-europe/country-profiles/lithuania
- [ ] VILNIUS TECH: Immigration regulations for full-time students:
  https://vilniustech.lt/en/international-students/immigration-regulations/immigration-regulations-full-time/

### Lithuania publication blockers

- [ ] Obtain explicit owner approval of vilniustech.lt as an official source.
  It is a university page, not a government host. Inclusion in the supplied
  official_source_hosts array allows technical validation only; it does not
  mean that owner approval has been completed.
- [ ] Resolve the reported conflict between the university's temporary
  residence permit guidance and the European Commission page, which still
  describes a national visa. Confirm the current process on the Migration
  Department page for India listed above before publishing. Reconcile the
  visa_steps and FAQ wording from current authoritative evidence; do not
  present technical acceptance of both sources as resolution of the conflict.
- [ ] Proof-of-funds and insurance minimums were deliberately left out because
  university sources gave different numbers. Do not add a minimum from memory
  or select one of the conflicting numbers without verification. Confirm the
  current requirements with the Migration Department and applicable official
  sources before adding any figures. The supplied generic funds/insurance
  wording is not a verified minimum.
- [ ] Confirm the remaining supplied tuition, living-cost, programme-count,
  service-fee, service-point, MIGRIS and document statements against the exact
  sources, including applicability to the intended student and route. Confirm
  accurate item and page-wide review dates before release.


## 23. Phase 9: Latvia draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/latvia.php`, still
`draft`, with ilmera_summary and summary_provenance preserved exactly.
Costs is intentionally empty: no official tuition figure was supplied as
verified evidence. The page has four sourced categories (intro, visa_steps,
documents and faqs), three source URLs and four FAQs. It cannot reach the
five-category publishing gate with its current data, even if status were
changed to published. Do not change status in this phase.

No source page or supplied fact was independently verified by this build.
The supplied 2026-10-15 dates are retained and need confirmation against the
actual review evidence. The supplied European Commission URL retains its
/fi/ path exactly; the owner must check its content and current applicability.

### Latvia source URLs: owner must open and confirm all three

- [ ] Embassy of Latvia in India: Long stay visa for students, Indian nationals:
  https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students/indian-nationals
- [ ] Embassy of Latvia in India: Long stay visa for students:
  https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students
- [ ] Study in Europe (European Commission): Latvia country profile:
  https://education.ec.europa.eu/fi/country-profiles/latvia

### Latvia publication blockers

- [ ] Add an official tuition source and at least one more sourced category
  before publishing. A reviewed, sourced Costs category can supply the fifth
  category. Do not invent a tuition amount, split an existing group to inflate
  the count, or use the ILMERA summary as an extra category. Costs stays empty
  until official evidence is obtained and approved.
- [ ] Re-confirm the Hello Verify and VFS steps on the embassy pages above
  before publishing and again before applying. Check verification and
  transaction-number requirements, appointment booking, service points,
  interview arrangements and application submission. Do not assume the
  supplied workflow remains current.
- [ ] Confirm the remaining supplied visa validity, residence-permit and
  insurance/document statements against their exact sources, including the
  intended applicant and route. Verify accurate item/page review dates.

### Draft safeguards and release checklist for both pages

Both pages remain draft, noindex and unlinked from live pages, sitemap.xml
and LLM recommendations. Noindex is not access control; direct requests can
render these drafts. The CSV remains an unchanged empty template and does
not yet mirror either populated PHP record.

Before any publication, resolve all source/process blockers and obtain
explicit owner sign-off. Fill the reviewed CSV rows with aligned source/date
fields, meet the five-category threshold and follow section 18's atomic
release checklist: published PHP/CSV status, accurate sitemap entry and
llms.txt recommendation in the same commit, with llms-full.txt consistent.
Do not force links to drafts or bypass the existing guards.

Technical validation passed: 78 PHP lints, 42 clean renders, exact preserved
summary/provenance lines, all six source URLs, eight visible/schema FAQ pairs,
draft aliases, no incoming links to drafts and exact/subdomain host-boundary
checks. Isolated status-only published fixtures confirmed that Lithuania
passes the technical gate while Latvia remains blocked at four categories;
repository statuses were never changed. Twelve Chromium cases covered both
pages at 375/768/1280px with JavaScript on/off, checking noindex, sources,
all FAQs, conditional Costs sections, layout and mobile menus. External
resources were blocked and no live source contents were checked. No test
artifacts are committed. Native hosting headers, Apache rewrites and
production rendering remain staging checks; no deployment was performed.


## 24. Phase 9: Services university-dependent claims (OWNER VERIFICATION REQUIRED)

The following current services.php claims need university-source verification
or softer wording. This phase records the blockers; it does not certify or
change these live claims:

- [ ] "IELTS Not Mandatory" for Russia, Lithuania and Latvia. Requirements
  depend on each university and programme. Verify with applicable university
  sources or soften the wording so it does not imply a country-wide waiver.
- [ ] "Lowest Tuition Fees" for Czech, Lithuania, Latvia and Russia. Fees
  depend on the university and programme. Verify with university sources or
  soften/remove the unsupported lowest-price comparison.
- [ ] The FAQ "What is the cheapest country to study abroad?" names Czech
  Republic, Lithuania, Latvia, Russia and Slovakia as among the most affordable
  and describes Germany's public-university tuition. Verify the named-country
  affordability and tuition claims with university sources or soften the
  wording rather than treating a country ranking as a universal fee promise.
  If the visible FAQ is revised, update its matching FAQPage answer too.

These checks do not authorize publishing either destination draft. Existing
Services content and its schema are unchanged and remain subject to review.


## 25. Phase 10: Germany draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/germany.php`, still
`draft`, with its existing ilmera_summary and summary_provenance preserved
exactly. It has five sourced categories (intro, costs, documents,
work_and_stay and faqs), one source URL and four FAQs. Five categories alone
do not authorize publication. Host acceptance and source coverage are
technical checks, not fact verification or editorial approval.

### Germany source URL: owner must open and confirm

- [ ] DAAD: Costs of education and living in Germany:
  https://www.daad.de/en/studying-in-germany/living-in-germany/finances/

### Germany publication blockers and missing official sources

- [ ] The supplied DAAD facts came from search snippets, not a confirmed
  full-page review. The owner must open the DAAD page and confirm every line
  of the intro, costs, documents, work wording and FAQs before publishing.
  Pay particular attention to the Technical University of Munich (TUM) fee
  amounts and whether the master fee is per semester. Confirm the applicable
  students, programmes, exceptions and current amounts from official sources;
  do not treat a snippet or the supplied review date as verification.
- [ ] Obtain an official German source for the blocked account amount. It was
  left out because no official source was confirmed. Do not invent the amount
  or infer that a generic proof-of-finances statement supplies it.
- [ ] Obtain an official German source for the APS certificate requirement
  for Indian applicants. It was left out because no official source was
  confirmed. Verify applicability before adding any requirement or exception.
- [ ] Record accurate source/item and page-wide review dates after the actual
  checks. The supplied 2026-10-15 metadata is retained, not a claim that this
  build independently reviewed the source page.


## 26. Phase 10: UK draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/uk.php`, still `draft`,
with its existing ilmera_summary and summary_provenance preserved exactly.
It has four sourced categories (intro, costs, documents and faqs), one source
URL and four FAQs. It remains below the five-category threshold, even with
an isolated published flag. Do not add a category without official evidence.

### UK source URL: owner must open and confirm

- [ ] GOV.UK: Financial evidence for Student and Child Student visa applicants:
  https://www.gov.uk/guidance/financial-evidence-for-student-and-child-student-route-applicants

### UK publication blockers and missing official coverage

- [ ] The supplied research records that all amounts were read from GOV.UK
  on 2026-10-15 and have changed before. Recheck all amounts on the day of
  publishing, including the London/outside-London living costs and applicable
  duration, and reconcile the intro, costs and FAQs. This build has not
  independently repeated that source review; supplied dates remain unchanged.
- [ ] Confirm the "India is not on the exempt list" FAQ again at publishing.
  It rests on the absence of India from the GOV.UK list, not an explicit
  India-specific rule in the supplied evidence. Check the current list and
  the distinction between providing financial evidence upfront and meeting
  the financial requirement. Keep the visible FAQ and schema consistent.
- [ ] Obtain official GOV.UK sources for visa application steps, which were
  not covered by the supplied financial-evidence page content.
- [ ] Obtain official GOV.UK sources for visa application fees and the health
  surcharge, which were not covered. Do not add amounts from memory.
- [ ] Obtain official GOV.UK sources for processing time and any TB test
  requirement, neither of which was covered. Verify applicability to the
  intended applicant and route rather than assuming a universal requirement.
- [ ] Confirm the remaining supplied financial evidence, accepted account/
  funds rules and timing statements, and record actual item/page review dates.


## 27. Phase 10: Italy draft (OWNER VERIFICATION REQUIRED)

The complete supplied content is now in `destinations/italy.php`, still
`draft`, with its existing ilmera_summary and summary_provenance preserved
exactly. It has four sourced categories (intro, visa_steps, documents and
faqs), one source URL and four FAQs. Costs is intentionally empty because no
official tuition source was found in the supplied research. The page cannot
reach the publishing gate with the current four categories; add reviewed,
officially sourced tuition content before any publication.

### Italy source URL: owner must open and confirm

- [ ] Consulate General of Italy in Bengaluru: Study in Italy:
  https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/

### Italy publication blockers

- [ ] Confirm the current-intake version of the official study visa checklist.
  The supplied content references 2025-2026, which must not be assumed to be
  the correct version for a future/current intake. Review and update the
  document wording from the consulate's applicable official checklist.
- [ ] Add an official tuition source and reviewed Costs items before
  publishing. Costs stays empty until evidence is obtained; do not invent
  fees or count the ILMERA scholarship summary as a sourced category.
- [ ] Confirm the VFS centre list and the video interview rule on the
  consulate page before publishing. Check that the supplied Bangalore,
  Chennai and Hyderabad list and mandatory video-interview wording remain
  current and applicable to the intended applicant and route.
- [ ] Confirm all other supplied admission, Universitaly, visa, processing,
  DOV and email-safety statements against the source page. Verify actual
  source/item and page-wide review dates. The supplied 2026-10-15 dates do
  not represent an independent source review by this build.

- [ ] Phase 12 owner claim: the owner has described Italian study as having
  tuition covered by scholarships of up to 8,000 euros at ILMERA partner
  institutions. No official source for that amount was found in the supplied
  research. The owner must supply the relevant institutional scholarship
  pages or written confirmation, including eligibility, coverage and amount.
  Keep the claim conditional until supported, not a country-wide fee promise
  or a record of completed awards to ILMERA students. No institution is named
  and no amount is added to the Italy destination data in this phase.

### Shared draft safeguards and release checks for all three pages

Germany, UK and Italy remain draft, noindex and unlinked from live pages,
sitemap.xml and LLM recommendations. Noindex is not access control; direct
requests can render the drafts. None of the three source pages or supplied
facts was independently verified by this build. Existing verification
blockers elsewhere in this file, including the Services claims, remain open.

The CSV is still the unchanged empty template, not a synchronized copy of
these populated PHP records. Resolve all blockers, fill reviewed CSV rows
with aligned sources/dates, meet the five-category threshold and obtain
explicit owner sign-off before release. Follow section 18's atomic release
checklist: publish PHP/CSV status, accurate sitemap entry and llms.txt
recommendation in one commit, keeping llms-full.txt consistent. Do not bypass
robots/link guards or force links to drafts.

This phase supersedes earlier empty-Germany/UK/Italy descriptions and counts:
seven destinations now have supplied sourced content; only Russia and GCC
remain empty. All nine destination statuses remain draft.

Full technical checks were repeated after each of the four tasks: 78 PHP
lints, 42 clean page renders and 252 Chromium page/width/JavaScript cases per
task (375/768/1280px, JavaScript on/off). Checks covered all pages' headings,
robots and mobile menus, destination native FAQs/source links/layout,
conditional Costs sections, exact summary/provenance retention, all nine
draft gates, source-host boundaries, aliases and absence of incoming draft
or discovery links. Germany has five categories; UK and Italy each have
four. Isolated published-data fixtures confirmed the five-category boundary
without changing repository status. External browser resources were blocked;
no live source contents were checked. No test artifacts are committed.
Native HTTP headers, Apache rewrites and production rendering remain staging
checks; no deployment was performed.


## 28. Phase 10: Russia and GCC not started (OWNER INPUT REQUIRED)

Russia and GCC have not been started: their existing empty draft records,
summaries and provenance are unchanged. They are not approved for publication.

- [ ] Russia needs official Russian or Indian government sources before
  adding facts. No fees, eligibility, visa or other rules should be supplied
  from memory or non-official snippets.
- [ ] GCC needs the owner to name which countries to cover before research
  or content population. Do not assume that one visa, fee or education rule
  applies across GCC countries or invent a country list.


## 29. Free-tuition claims to verify

Phase 11 task 2 is a read-only audit of site copy: no service, homepage,
About, blog, place or LLM content was edited. Locations below use 1-based
source-file line numbers at the Phase 11 audit, not rendered HTML lines.
Each code block reproduces the full source line exactly, including markup,
entities and PHP escaping, without its line terminator. Metadata and schema
are listed separately from visible text, even when wording repeats.

Source position from the supplied research so far, not a fresh verification:

- Germany has no tuition at most state universities, with exceptions such as
  Baden-Wurttemberg for non-EU students and TUM, and a semester contribution.
- Slovakia is free only for Slovak-language study. Do not present a branch
  label alone as proof that an English-taught programme is tuition-free.
- Italian institutions set their own tuition, and no official source for
  free tuition has been found. Existing DSU tuition-cover/waiver statements
  are conditional scholarship claims to verify, not evidence that Italy is
  free by default. This audit does not establish scholarship entitlement.

Review these statements with applicable government/university sources before
reusing them as verified claims. Qualified wording, negative qualifications,
conditional scholarship statements and contextual questions/headings are
retained to avoid hiding relevant wording. The label "unsure" means the line
is generic or combines countries/options so attribution to Germany, Italy
or Slovakia is unclear; it is not a determination that its statement is true.
"Reference only" means a slug/URL or guide reference, not an independent
free-tuition assertion. Ordinary free-consultation offers, IELTS waivers,
Schengen travel and GCC tax-free wording are not free-tuition claims and are
excluded unless the same line also contains relevant education wording.

### Audit coverage and shared content

Searched services.php, index.php, about.php, both LLM files, all seven blog
posts plus the blog index, all 17 place data files, all 17 thin place entry
pages and the shared place renderer. Search covered free/tuition-free/free
education, no/zero tuition, fee waivers/exemptions and tuition coverage,
followed by contextual review of the tuition lines. The place entries are
thin includes, with no independent tuition assertions. Their direct matches
below are guide-URL references, not new prose claims. The shared place
renderer's free offer is for consultation only. Empty place drafts contain
no tuition claims.

Also inspected includes/posts.php because its titles/excerpts and related-
guide data supply blog listings and place-page guide cards. Those shared
source locations are included separately rather than pretending the thin
entry files contain literal titles. A title/excerpt reference does not mean
it renders on every page; publication guards and related-guide selection
still apply. Blog documents/backlogs/Coorg pages had no independent literal
free-tuition prose beyond references listed here or shared guide content.

Model disclosure: this report was prepared using Arena.ai Agent Mode.
The underlying model identity is not disclosed.

### Exact source-line inventory

- `about.php:18` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultant India, ILMERA Study Abroad, overseas education consultant, study in Germany free, study in Italy, study abroad with backlogs, low marks study abroad, student visa assistance, study in Europe from India, MBBS abroad, study in UK, Czech Republic universities"/>
```

- `about.php:136` | claim or related tuition wording

```text
        "Free tuition public universities in Germany",
```

- `about.php:671` | conditional or qualified wording

```text
      <p style="font-size:16px;font-weight:300;color:var(--grey-dark);line-height:1.78;margin-bottom:22px;">The most common questions we get from Coorg are about studying with a low PUC percentage, routes that skip IELTS, and free or near-free tuition. Public universities in Germany charge little to no tuition but require an <a href="https://www.aps-india.de/" rel="nofollow noopener" style="color:var(--navy);">APS certificate</a> from Indian applicants and proof of funds in a blocked account. Italy's regional DSU scholarships are income-assessed via ISEE and can cover tuition plus a living stipend. Russia, Slovakia, Lithuania and Latvia accept lower percentages and backlogs and frequently waive IELTS. Which of these fits depends entirely on your actual marksheet, which is what the free consultation is for.</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:150` | claim or related tuition wording

```text
    <p><strong>Short answer:</strong> the cheapest destinations for Indian students are usually the Czech Republic, Lithuania, Latvia, Slovakia and Russia, while German public universities charge little to no tuition regardless of nationality. But tuition is only part of the bill: living costs, visa funds, insurance and travel decide whether a destination is genuinely affordable for your family. This guide breaks down each of the nine destinations ILMERA works with, what drives the cost, and what you must budget beyond tuition.</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:157` | claim or related tuition wording

```text
      <li><strong>Tuition or semester contribution:</strong> from zero at most German public universities to substantial fees at UK universities; ranges vary by destination and programme.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:170` | claim or related tuition wording

```text
        <tr><td>Germany</td><td>Little to no tuition at public universities; semester contribution applies</td><td>Moderate; blocked account required</td><td>Engineering, IT, tuition-free degrees</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:171` | conditional or qualified wording

```text
        <tr><td>Italy</td><td>Public universities charge tuition; regional DSU scholarships can cover it and add a stipend for eligible students</td><td>Moderate, lower in smaller cities</td><td>Scholarship-driven students, arts and engineering</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:175` | claim or related tuition wording

```text
        <tr><td>Slovakia</td><td>Free in some Slovak-language branches; paid English programmes</td><td>Low</td><td>Free-education routes, medicine</td></tr>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:183` | context heading/question

```text
    <h2>Where the Free-Education Routes Actually Apply</h2>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:184` | context heading/question

```text
    <p>Two of the nine destinations can genuinely approach zero tuition:</p>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:186` | claim or related tuition wording

```text
      <li><strong>Germany:</strong> most public universities charge no tuition for consecutive degrees; you pay a semester contribution and prove living funds through a blocked account. A few states levy fees in specific cases, so ILMERA checks the rule for each university. See our guide to the <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS certificate') ?: 'APS certificate' ?> for the India-specific requirement.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:187` | conditional or qualified wording

```text
      <li><strong>Italy:</strong> public universities charge tuition, but the regional DSU scholarship, assessed mainly on family income (ISEE) and merit, can cover tuition and add a stipend plus subsidised accommodation and meals. Amounts are set regionally and revised periodically. See our guide on <?= ilmera_post_link('italy-dsu-scholarship-eligibility', 'DSU eligibility') ?: 'DSU eligibility' ?>.</li>
```

- `blog/cost-of-studying-abroad-for-indian-students.php:189` | claim or related tuition wording

```text
    <p>Slovakia offers free tuition in some Slovak-language branches, which requires learning the language through a preparatory year; English-taught programmes there are paid.</p>
```

- `blog/documents-needed-to-study-abroad-from-india.php:174` | reference only

```text
        <tr><td>Germany</td><td><a href="https://www.aps-india.de/" target="_blank" rel="noopener">APS certificate</a> for Indian applicants, blocked account (Sperrkonto) confirmation, German or English proficiency per programme. See our <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS guide') ?: 'APS guide' ?>.</td></tr>
```

- `blog/index.php:18` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad blog, study in Germany free, Italy DSU scholarship, study abroad with backlogs, study abroad no IELTS, study abroad consultant Coorg Kodagu"/>
```

- `blog/italy-dsu-scholarship-eligibility.php:16` | conditional or qualified wording

```text
<meta name="description" content="Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works."/>
```

- `blog/italy-dsu-scholarship-eligibility.php:17` | conditional or qualified wording

```text
<meta name="keywords" content="Italy DSU scholarship, ISEE Italy, study in Italy scholarship, DSU eligibility, Italy free education"/>
```

- `blog/italy-dsu-scholarship-eligibility.php:34` | conditional or qualified wording

```text
<meta property="og:description" content="Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks."/>
```

- `blog/italy-dsu-scholarship-eligibility.php:57` | conditional or qualified wording

```text
      "description": "Italy's regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works.",
```

- `blog/italy-dsu-scholarship-eligibility.php:136` | conditional or qualified wording

```text
    <p>Italy's DSU scholarships (Diritto allo Studio Universitario) are among the most generous student support schemes in Europe, sometimes covering full tuition exemption plus a living stipend and, in some regions, subsidised housing. They are also one of the most misunderstood, because eligibility has almost nothing to do with your entrance exam score and almost everything to do with two separate things: household income and academic merit.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:15` | claim or related tuition wording

```text
<meta name="description" content="Which scholarships can Indian students actually get? Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises, updated October 2026."/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:16` | claim or related tuition wording

```text
<meta name="keywords" content="scholarships for indian students, study abroad scholarships, italy DSU scholarship, germany free education, government scholarships"/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:32` | claim or related tuition wording

```text
<meta property="og:description" content="Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises."/>
```

- `blog/scholarships-for-indian-students-study-abroad.php:54` | claim or related tuition wording

```text
      "description": "Which scholarships Indian students can actually get: Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises.",
```

- `blog/scholarships-for-indian-students-study-abroad.php:138` | claim or related tuition wording

```text
    <p><strong>Short answer:</strong> the most realistic funding routes for Indian students fall into four groups: Italy's income-based regional DSU scholarships, tuition-free German public universities, university-specific merit awards, and government schemes such as Chevening and Commonwealth for the UK. Anything promising guaranteed money for every applicant should be treated as a red flag. Here is how each route actually works and who it suits.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:149` | conditional tuition-relief context

```text
        <tr><td>Italy DSU (regional)</td><td>Regional student-welfare support: tuition relief, an annual stipend, subsidised accommodation and meal services</td><td>Family income (ISEE/ISEE parificato) and merit credits</td><td>Middle-income families; architecture, arts, engineering</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:150` | claim or related tuition wording

```text
        <tr><td>Germany public universities</td><td>Not a scholarship: most public universities charge no tuition for consecutive degrees, only a semester contribution</td><td>Admission requirements per programme</td><td>Engineering, IT, budget planners</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:151` | unsure

```text
        <tr><td>University merit awards</td><td>Fee waivers or partial awards offered by individual universities at intake</td><td>Academic record, sometimes interview or portfolio</td><td>Strong academics in any destination</td></tr>
```

- `blog/scholarships-for-indian-students-study-abroad.php:161` | claim or related tuition wording

```text
    <p>Because most German public universities charge no tuition, the funding question shifts to living costs, which the visa requires you to prove through a blocked account. That makes Germany one of the cheapest total-cost destinations even without any award. The India-specific APS certificate is the entry gate; read the <?= ilmera_post_link('study-in-germany-free-aps-certificate', 'APS guide') ?: 'APS guide' ?> for the process.</p>
```

- `blog/scholarships-for-indian-students-study-abroad.php:167` | unsure

```text
      <li><strong>Total-cost maths:</strong> a partial award at a high-cost destination can cost more overall than a tuition-free destination with no award.</li>
```

- `blog/scholarships-for-indian-students-study-abroad.php:191` | unsure

```text
    <p>Book a free consultation and get an honest eligibility check for DSU, tuition-free routes and university awards, by phone, WhatsApp, or video call.</p>
```

- `blog/study-in-germany-free-aps-certificate.php:3` | reference only

```text
$post = ilmera_post('study-in-germany-free-aps-certificate');
```

- `blog/study-in-germany-free-aps-certificate.php:15` | claim or related tuition wording

```text
<title>Study in Germany for Free from India: APS Certificate Guide</title>
```

- `blog/study-in-germany-free-aps-certificate.php:16` | claim or related tuition wording

```text
<meta name="description" content="Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate first. Here is what the APS process actually involves."/>
```

- `blog/study-in-germany-free-aps-certificate.php:17` | claim or related tuition wording

```text
<meta name="keywords" content="study in Germany free, APS certificate India, Germany tuition free universities, APS certificate process"/>
```

- `blog/study-in-germany-free-aps-certificate.php:25` | reference only

```text
<link rel="canonical" href="https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate"/>
```

- `blog/study-in-germany-free-aps-certificate.php:33` | claim or related tuition wording

```text
<meta property="og:title" content="Study in Germany for Free from India: APS Certificate Guide"/>
```

- `blog/study-in-germany-free-aps-certificate.php:34` | claim or related tuition wording

```text
<meta property="og:description" content="Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate first. Here is what that process actually involves."/>
```

- `blog/study-in-germany-free-aps-certificate.php:35` | reference only

```text
<meta property="og:url" content="https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate"/>
```

- `blog/study-in-germany-free-aps-certificate.php:41` | claim or related tuition wording

```text
<meta name="twitter:title" content="Study in Germany for Free from India: APS Certificate Guide"/>
```

- `blog/study-in-germany-free-aps-certificate.php:55` | reference only

```text
      "@id": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate#article",
```

- `blog/study-in-germany-free-aps-certificate.php:56` | claim or related tuition wording

```text
      "headline": "How to Study in Germany for Free from India: The APS Certificate Explained",
```

- `blog/study-in-germany-free-aps-certificate.php:57` | claim or related tuition wording

```text
      "description": "Germany's public universities charge little to no tuition, but Indian applicants need an APS certificate before they can apply. Here is what the process actually involves.",
```

- `blog/study-in-germany-free-aps-certificate.php:58` | reference only

```text
      "url": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate",
```

- `blog/study-in-germany-free-aps-certificate.php:59` | reference only

```text
      "mainEntityOfPage": "https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate",
```

- `blog/study-in-germany-free-aps-certificate.php:127` | reference only

```text
  <?php ilmera_breadcrumbs($pageTrail, '/blog/study-in-germany-free-aps-certificate'); ?>
```

- `blog/study-in-germany-free-aps-certificate.php:129` | claim or related tuition wording

```text
  <h1>How to Study in Germany for Free from India: The APS Certificate Explained</h1>
```

- `blog/study-in-germany-free-aps-certificate.php:136` | claim or related tuition wording

```text
    <p>Germany's public universities are one of the few places left where an Indian student can complete a full degree for little to no tuition. Most public universities charge only a small semester contribution, usually covering student services and public transport, rather than a per-credit or per-year tuition fee. That is the part most students already know. What catches people off guard is the <a href="https://www.aps-india.de/" target="_blank" rel="noopener" style="color:var(--gold);">APS certificate</a>, a document that has nothing to do with the university and everything to do with whether your visa application even gets looked at. The full destination overview is on our <a href="/services#germany" style="color:var(--gold);">Study in Germany</a> page.</p>
```

- `includes/posts.php:6` | reference only

```text
        'study-in-germany-free-aps-certificate' => [
```

- `includes/posts.php:7` | reference only

```text
            'slug' => 'study-in-germany-free-aps-certificate',
```

- `includes/posts.php:8` | claim or related tuition wording

```text
            'title' => 'How to Study in Germany for Free from India: The APS Certificate Explained',
```

- `includes/posts.php:9` | claim or related tuition wording

```text
            'excerpt' => 'Germany\'s public universities charge little to no tuition, but Indian applicants need an APS certificate before they can apply. Here is what the process actually involves.',
```

- `includes/posts.php:15` | reference only

```text
            'related' => ['italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:20` | conditional or qualified wording

```text
            'excerpt' => 'Italy\'s regional DSU scholarships can cover tuition plus a living stipend, but eligibility is based on income (ISEE) and merit, not just marks. Here is how the assessment works.',
```

- `includes/posts.php:26` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'study-abroad-with-academic-backlogs', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:37` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-counselling-from-coorg'],
```

- `includes/posts.php:48` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:59` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:70` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `includes/posts.php:75` | claim or related tuition wording

```text
            'excerpt' => 'Which scholarships can Indian students actually get? Italy DSU, German tuition-free universities, university awards and government schemes, explained without inflated promises, updated October 2026.',
```

- `includes/posts.php:81` | reference only

```text
            'related' => ['study-in-germany-free-aps-certificate', 'italy-dsu-scholarship-eligibility', 'study-abroad-with-academic-backlogs'],
```

- `index.php:12` | unsure

```text
<title><?php echo $page_title ?? 'ILMERA Study Abroad | Study in Germany, Italy, UK, Russia & Europe: No-IELTS & Free Study Routes'; ?></title>
```

- `index.php:13` | unsure

```text
<meta name="description" content="<?php echo $page_description ?? 'ILMERA Study Abroad guides Indian students to universities in Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia & GCC. Free & low-cost study routes, no-IELTS options, scholarship guidance, backlogs & low marks accepted. Book a free consultation.'; ?>"/>
```

- `index.php:14` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultancy India, study abroad consultant for Coorg students, study abroad consultant Kodagu, study in Germany free, study in Italy DSU stipend, study in Russia no IELTS, study abroad with backlogs, study abroad low marks, cheapest country to study abroad for Indian students, student visa assistance India, study in Europe without IELTS, study in Czech Republic Lithuania Latvia Slovakia"/>
```

- `index.php:35` | unsure

```text
<meta property="og:description" content="<?php echo $og_description ?? 'Study in Germany, Italy, UK, Russia, Czech Republic & more. Free & low-cost study routes, no-IELTS options, scholarship guidance & backlogs accepted. Book a free consultation.'; ?>"/>
```

- `index.php:45` | unsure

```text
<meta name="twitter:description" content="<?php echo $twitter_description ?? 'Study in Germany, Italy, UK, Russia & more. Free & low-cost study routes, no-IELTS options, scholarship guidance & backlogs accepted. Book a free consultation.'; ?>"/>
```

- `index.php:88` | unsure

```text
      "knowsAbout": ["University Admissions","Student Visas","Scholarships","IELTS Preparation","Study Abroad without IELTS","Free Education in Europe","Study Abroad with Backlogs"],
```

- `index.php:171` | claim or related tuition wording

```text
        {"@type":"Question","name":"Which is the cheapest country to study abroad for Indian students?","acceptedAnswer":{"@type":"Answer","text":"For Indian students on a tight budget, the Czech Republic, Lithuania, Latvia, Russia and Slovakia are the most affordable study destinations, with much lower tuition and living costs than the UK. Germany's public universities charge little to no tuition, though you still need to fund living expenses."}},
```

- `index.php:172` | conditional or qualified wording

```text
        {"@type":"Question","name":"Which countries let you study for free?","acceptedAnswer":{"@type":"Answer","text":"Germany, Italy and Slovakia offer free or heavily subsidised university education. German public universities charge little to no tuition, Italy offers regional DSU scholarships that can cover tuition plus a living stipend, and some Slovakian programmes are tuition-free. You still need to cover living costs and prove funds for your visa."}},
```

- `index.php:173` | claim or related tuition wording

```text
        {"@type":"Question","name":"How can I study in Germany for free from India?","acceptedAnswer":{"@type":"Answer","text":"You can study in Germany for free by applying to public universities, which charge little to no tuition fees even for Indian students. You'll need an APS certificate (mandatory for Indian applicants), proof of funds via a blocked account, and either English or German proficiency. ILMERA guides you through APS, admissions and the blocked-account process."}},
```

- `index.php:174` | conditional or qualified wording

```text
        {"@type":"Question","name":"What is the Italy DSU scholarship and can Indian students get it?","acceptedAnswer":{"@type":"Answer","text":"The DSU (Diritto allo Studio Universitario) is an Italian regional scholarship open to international students, including Indians, that can cover full tuition plus a living stipend, subsidised housing and university meals. Eligibility is mainly income-based (assessed via ISEE) and merit, and amounts vary by region. ILMERA helps you check eligibility and prepare the documents."}},
```

- `index.php:178` | conditional or qualified wording

```text
        {"@type":"Question","name":"Can I study in Italy for free with a stipend?","acceptedAnswer":{"@type":"Answer","text":"Yes, eligible students can study in Italy with free tuition plus a stipend through regional DSU scholarships, which may also include subsidised accommodation and meals. Eligibility is assessed mainly on family income (ISEE) and merit, and the exact amount varies by region and year. ILMERA helps you assess whether you qualify before applying."}},
```

- `index.php:181` | claim or related tuition wording

```text
        {"@type":"Question","name":"Can I study in Slovakia or the Czech Republic on a low budget?","acceptedAnswer":{"@type":"Answer","text":"Yes, both Slovakia and the Czech Republic are low-budget study destinations for Indian students, with affordable tuition, low living costs, and some tuition-free Slovakian programmes. Many courses accept students without IELTS. ILMERA helps you compare programmes, costs and English requirements for both."}},
```

- `index.php:186` | unsure

```text
        {"@type":"Question","name":"How is ILMERA different from other study abroad consultants?","acceptedAnswer":{"@type":"Answer","text":"ILMERA works with Indian students who have backlogs, low marks or no IELTS score, and focuses on affordable and free-education destinations in Europe and Russia. Each student works with a named counsellor who gives honest advice about what is realistically achievable, rather than one-size-fits-all promises."}},
```

- `index.php:389` | unsure

```text
        <p class="hero-sub" id="hSub">Study abroad consultants for Indian students, including options with no IELTS, backlogs or low marks accepted, and free or low-cost tuition across Germany, Italy, the UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia &amp; the GCC.</p>
```

- `index.php:461` | claim or related tuition wording

```text
        ILMERA Study Abroad is based in Coorg and helps students from Kodagu, Madikeri, Virajpet and across Karnataka plan their overseas education through free consultation by phone, WhatsApp and video call. Whether you're aiming for free tuition in Germany, the DSU scholarship in Italy, or a low-cost, no-IELTS route in Russia, Lithuania or Latvia, our named counsellors guide you from profile assessment to visa.
```

- `index.php:513` | conditional or qualified wording

```text
        <p class="testi-text">We help eligible students apply for Italy's regional DSU scholarships, which can cover tuition plus a living stipend and subsidised housing and meals, based on income (ISEE) and merit.</p>
```

- `index.php:552` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">5</span><span>&#127480;&#127472; Slovakia <em style="font-size:11px;color:#888;">(free in some branches)</em></span></div>
```

- `index.php:556` | context heading/question

```text
        <div class="sc-badge" style="background:rgba(201,168,76,0.1);border-color:rgba(201,168,76,0.4);color:#8a6a00;">&#127379; Free Education Available</div>
```

- `index.php:557` | context heading/question

```text
        <h3 class="sc-title">Study for Free</h3>
```

- `index.php:559` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127465;&#127466;</span><span>Germany: Public universities free</span></div>
```

- `index.php:560` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127470;&#127481;</span><span>Italy: Free + annual stipend</span></div>
```

- `index.php:561` | claim or related tuition wording

```text
          <div class="sc-item"><span class="sc-rank">&#127480;&#127472;</span><span>Slovakia: Free in some branches</span></div>
```

- `index.php:591` | claim or related tuition wording

```text
      <details class="il-faq"><summary>Which is the cheapest country to study abroad for Indian students?</summary><div><p>For Indian students on a tight budget, the Czech Republic, Lithuania, Latvia, Russia and Slovakia are the most affordable study destinations, with much lower tuition and living costs than the UK. Germany's public universities charge little to no tuition, though you still need to fund living expenses.</p></div></details>
```

- `index.php:593` | conditional or qualified wording

```text
      <details class="il-faq"><summary>Which countries let you study for free?</summary><div><p>Germany, Italy and Slovakia offer free or heavily subsidised university education. German public universities charge little to no tuition, Italy offers regional DSU scholarships that can cover tuition plus a living stipend, and some Slovakian programmes are tuition-free. You still need to cover living costs and prove funds for your visa.</p></div></details>
```

- `index.php:595` | claim or related tuition wording

```text
      <details class="il-faq"><summary>How can I study in Germany for free from India?</summary><div><p>You can study in Germany for free by applying to public universities, which charge little to no tuition fees even for Indian students. You'll need an <a href="https://www.aps-india.de/" target="_blank" rel="noopener nofollow">APS certificate</a> (mandatory for Indian applicants), proof of funds via a blocked account, and either English or German proficiency. ILMERA guides you through APS, admissions and the blocked-account process.</p></div></details>
```

- `index.php:597` | conditional or qualified wording

```text
      <details class="il-faq"><summary>What is the Italy DSU scholarship and can Indian students get it?</summary><div><p>The DSU (Diritto allo Studio Universitario) is an Italian regional scholarship open to international students, including Indians, that can cover full tuition plus a living stipend, subsidised housing and university meals. Eligibility is mainly income-based (assessed via ISEE) and merit, and amounts vary by region. ILMERA helps you check eligibility and prepare the documents.</p></div></details>
```

- `index.php:605` | conditional or qualified wording

```text
      <details class="il-faq"><summary>Can I study in Italy for free with a stipend?</summary><div><p>Yes, eligible students can study in Italy with free tuition plus a stipend through regional DSU scholarships, which may also include subsidised accommodation and meals. Eligibility is assessed mainly on family income (ISEE) and merit, and the exact amount varies by region and year. ILMERA helps you assess whether you qualify before applying.</p></div></details>
```

- `index.php:611` | claim or related tuition wording

```text
      <details class="il-faq"><summary>Can I study in Slovakia or the Czech Republic on a low budget?</summary><div><p>Yes, both Slovakia and the Czech Republic are low-budget study destinations for Indian students, with affordable tuition, low living costs, and some tuition-free Slovakian programmes. Many courses accept students without IELTS. ILMERA helps you compare programmes, costs and English requirements for both.</p></div></details>
```

- `index.php:621` | unsure

```text
      <details class="il-faq"><summary>How is ILMERA different from other study abroad consultants?</summary><div><p>ILMERA works with Indian students who have backlogs, low marks or no IELTS score, and focuses on affordable and free-education destinations in Europe and Russia. Each student works with a named counsellor who gives honest advice about what is realistically achievable, rather than one-size-fits-all promises.</p></div></details>
```

- `llms-full.txt:64` | claim or related tuition wording

```text
- **Tuition:** Most public (state-funded) universities charge no tuition for consecutive Bachelor's and Master's programmes, including for international students; a small semester contribution applies. A few states levy tuition in specific cases (for example, non-consecutive or second-degree programmes), so ILMERA confirms the rule for each university before applying.
```

- `llms-full.txt:69` | claim or related tuition wording

```text
- **Best fit for:** students who want tuition-free education and are willing to pursue German language study, or who qualify for English-medium programmes.
```

- `llms-full.txt:72` | conditional or qualified wording

```text
- **Tuition and stipend:** The DSU scholarship can cover tuition and provide an annual stipend plus subsidized accommodation and meal services for eligible students. Stipend amounts and thresholds are set regionally and revised periodically; ILMERA confirms current figures for the target region each admissions cycle rather than quoting fixed numbers.
```

- `llms-full.txt:76` | conditional or qualified wording

```text
- **Best fit for:** students seeking free or near-free education with a living stipend, and students in architecture, arts, or engineering.
```

- `llms-full.txt:107` | claim or related tuition wording

```text
- **Tuition:** Free tuition is available at Slovak-language branches of several public universities, one of the few EU countries besides Germany to offer this to international students. English and Slovak-medium programmes exist in Medicine, Dentistry, Engineering, and Business.
```

- `llms-full.txt:108` | claim or related tuition wording

```text
- **Language requirement:** The tuition-free route requires Slovak language proficiency; a preparatory language course is typically available beforehand.
```

- `llms-full.txt:111` | claim or related tuition wording

```text
- **Best fit for:** students targeting free European education, and medical aspirants.
```

- `llms-full.txt:137` | claim or related tuition wording

```text
- **Budget-conscious students:** Russia and Lithuania are generally among the more affordable options among ILMERA's destinations; Germany's zero-tuition policy also significantly reduces the total cost of a degree, though living costs still apply.
```

- `llms-full.txt:138` | claim or related tuition wording

```text
- **Free-education seekers:** Germany (public universities) and Italy (DSU scholarship) are ILMERA's primary options for students seeking free or heavily subsidized education.
```

- `llms.txt:3` | unsure

```text
> A study abroad consultancy based in Coorg (Kodagu, Karnataka, India), offering application guidance to Indian students considering universities in Germany, Italy, UK, Czech Republic, Lithuania, Latvia, Slovakia, Russia and the GCC, with free education options, no-IELTS routes, and support for students with backlogs or low marks.
```

- `llms.txt:34` | claim or related tuition wording

```text
### Germany: Free Public University Education for Indian Students
```

- `llms.txt:37` | claim or related tuition wording

```text
- Most German public (state-funded) universities charge no tuition for consecutive degrees, including for international students from India; a small semester contribution applies. A few states levy tuition in specific cases (for example, non-consecutive or second-degree programmes), so ILMERA confirms the rule for each university before applying.
```

- `llms.txt:42` | claim or related tuition wording

```text
- Ideal for: students seeking tuition-free European education and STEM graduates.
```

- `llms.txt:44` | conditional or qualified wording

```text
### Italy: Free Education Plus Annual Stipend via DSU Scholarship
```

- `llms.txt:47` | conditional or qualified wording

```text
- Italy's DSU (Diritto allo Studio Universitario) regional scholarship can cover tuition and provide an annual cash stipend plus subsidised accommodation and meal services for eligible students.
```

- `llms.txt:53` | conditional or qualified wording

```text
- Ideal for: students who want a free or near-free European education with a living stipend, and architecture, arts, and engineering aspirants.
```

- `llms.txt:94` | claim or related tuition wording

```text
### Slovakia: Free Education Available at Certain Branches
```

- `llms.txt:97` | claim or related tuition wording

```text
- Slovakia, an EU member, offers free tuition at Slovak-language branches of several public universities.
```

- `llms.txt:99` | claim or related tuition wording

```text
- The tuition-free option requires Slovak language proficiency (a preparatory course is available).
```

- `llms.txt:102` | claim or related tuition wording

```text
- Ideal for: students targeting free European education and medical aspirants.
```

- `llms.txt:129` | reference only

```text
- [Study in Germany for Free from India: APS Certificate Guide](https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate): what the APS certificate is, who needs it, and the process.
```

- `llms.txt:155` | conditional or qualified wording

```text
- **Students seeking free education:** Germany (public universities) and Italy (DSU scholarship) are ILMERA's primary free or reduced-cost education pathways.
```

- `llms.txt:163` | context heading/question

```text
**Q: Which countries offer free education for Indian students?**
```

- `llms.txt:164` | conditional or qualified wording

```text
A: Germany (public universities charge zero tuition) and Italy (the DSU scholarship covers tuition and includes a stipend for eligible students) are ILMERA's primary free-education pathways. Slovakia also offers free tuition at Slovak-language branches of certain public universities. ILMERA Study Abroad (ilmerastudyabroad.com), based in Coorg, Karnataka, guides students through all three pathways.
```

- `llms.txt:170` | claim or related tuition wording

```text
A: Russia and Lithuania are generally among the more affordable destinations for Indian students. Germany has zero tuition at public universities, with living costs to budget for separately. ILMERA Study Abroad helps students compare total cost of attendance across destinations for their specific profile.
```

- `llms.txt:176` | conditional or qualified wording

```text
A: The DSU (Diritto allo Studio Universitario) is Italy's government-funded student welfare scholarship. It can cover tuition fees, provide an annual cash stipend, and include university-managed accommodation for eligible students. Eligibility is primarily income-based, using the ISEE (Indicatore della Situazione Economica Equivalente) calculation. ILMERA Study Abroad assists with the DSU application process, including the ISEE estero calculation.
```

- `llms.txt:185` | claim or related tuition wording

```text
A: ILMERA Study Abroad (ilmerastudyabroad.com), based in Coorg, Karnataka, assists Indian students with tuition-free public university admissions in Germany, including TestDaF/DSH preparation guidance, blocked account (Sperrkonto) setup, and student visa support.
```

- `llms.txt:200` | unsure

```text
ILMERA Study Abroad operates under the ILMERA Group and is based in Coorg, Kodagu, Karnataka, India. The company was established to help Indian students access international education, with a focus on working with students who have backlogs, lower marks, or no IELTS score, alongside students seeking free or scholarship-supported education. ILMERA's leadership team is Jabir KJ (Founder), Fawaz BH (CMO), and Zaheer KJ (CFO). Counsellors maintain destination-specific expertise and university partnerships across Europe, Russia, and the GCC.
```

- `places/belagavi.php:23` | reference only

```text
        '[Germany](/services#germany): discuss APS alongside your academic record; [the APS explanation](/blog/study-in-germany-free-aps-certificate) provides background.',
```

- `places/karnataka.php:23` | reference only

```text
        '[Germany](/services#germany): public-university applications, APS and proof-of-funds planning. [Read the Germany APS guide](/blog/study-in-germany-free-aps-certificate).',
```

- `places/karnataka.php:35` | reference only

```text
        'For Germany, discuss the APS certificate and proof of funds; for Italy DSU, discuss the income-assessment documents. [Germany documentation](/blog/study-in-germany-free-aps-certificate) and [DSU eligibility](/blog/italy-dsu-scholarship-eligibility) are explained in the existing guides.',
```

- `places/shivamogga.php:23` | reference only

```text
        '[Germany](/services#germany): plan the academic-verification discussion using [the existing APS article](/blog/study-in-germany-free-aps-certificate).',
```

- `places/udupi-manipal.php:23` | reference only

```text
        '[Germany](/services#germany): use [the Germany APS guide](/blog/study-in-germany-free-aps-certificate) to prepare verification questions.',
```

- `services.php:14` | claim or related tuition wording

```text
<meta name="keywords" content="study abroad consultants, study in Germany free, study in Italy scholarship, study in UK, study in Russia without IELTS, study abroad with backlogs, low marks study abroad, IELTS not mandatory, Czech Republic study, Lithuania Latvia Slovakia study, GCC universities, ILMERA study abroad"/>
```

- `services.php:118` | claim or related tuition wording

```text
        {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"Scholarship Guidance","description":"Italy DSU regional scholarships, Germany free education, Slovakia free programmes, and merit-based awards across all destinations.","provider":{"@id":"https://ilmerastudyabroad.com/#organization"}}},
```

- `services.php:141` | conditional or qualified wording

```text
        {"@type":"Question","name":"Which countries offer free education?","acceptedAnswer":{"@type":"Answer","text":"Germany offers tuition-free or very low tuition at most public universities. In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Slovakia offers free education in select Slovak-language branches. ILMERA helps students access these low-cost and tuition-free options."}},
```

- `services.php:144` | claim or related tuition wording

```text
        {"@type":"Question","name":"What is the cheapest country to study abroad?","acceptedAnswer":{"@type":"Answer","text":"The Czech Republic, Lithuania, Latvia, Russia and Slovakia are among the most affordable destinations for Indian students, and Germany's public universities charge little to no tuition. Exact costs vary by university and city, and ILMERA provides a full cost breakdown during your consultation."}},
```

- `services.php:383` | claim or related tuition wording

```text
      <div class="badge-card"><span class="badge-icon">&#127891;</span><span class="badge-title">Free &amp; Low-Cost Education</span><span class="badge-sub">Germany &middot; Italy &middot; Slovakia</span></div>
```

- `services.php:398` | claim or related tuition wording

```text
      <div class="country-flag-badge"><span class="flag">&#127465;&#127466;</span> Tuition-Free or Low Tuition</div>
```

- `services.php:401` | claim or related tuition wording

```text
      <p>Germany offers world-class, globally recognised degrees, with tuition-free or very low tuition at most public universities; some states charge fees and a semester contribution applies. Combine quality education with a strong economy and outstanding career opportunities.</p>
```

- `services.php:405` | claim or related tuition wording

```text
          <li><span class="li-ico">&#127379;</span> Free education at public universities</li>
```

- `services.php:439` | conditional or qualified wording

```text
      <p>In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Eligible students can add a yearly stipend plus tuition relief and subsidised accommodation and meal services, assessed on family income (ISEE) and merit. English-taught programmes are available at many universities.</p>
```

- `services.php:609` | claim or related tuition wording

```text
      <div class="country-flag-badge"><span class="flag">&#127480;&#127472;</span> Free in Some Branches</div>
```

- `services.php:611` | claim or related tuition wording

```text
      <h2><a href="<?= ilmera_place_escape(ilmera_destination_target('slovakia')) ?>" style="color:inherit;text-decoration:none;">Study in Slovakia</a><br><em style="font-style:italic;font-size:0.7em;color:var(--gold);">Low Marks Welcome. Free in Some Branches.</em></h2>
```

- `services.php:612` | claim or related tuition wording

```text
      <p>Slovakia is one of Europe's hidden gems for international students, offering free education in select branches, low marks acceptance, and affordable living right in the heart of the EU.</p>
```

- `services.php:614` | claim or related tuition wording

```text
        <li><span class="li-ico">&#127379;</span> Free education available in some branches</li>
```

- `services.php:710` | claim or related tuition wording

```text
      <div class="service-mini-card"><div class="smc-icon">&#11088;</div><h3>Scholarship Guidance</h3><p>Italy DSU regional scholarships, Germany free education, Slovakia free branches, merit awards in all countries.</p></div>
```

- `services.php:758` | context heading/question

```text
        <button class="faq-q">Which countries offer free education?</button>
```

- `services.php:759` | conditional or qualified wording

```text
        <div class="faq-a"><p>Germany offers tuition-free or very low tuition at most public universities. In Italy, fee reductions or waivers are income-based and assessed through regional DSU scholarships; study is not free by default. Slovakia offers free education in select Slovak-language branches. ILMERA helps students access these low-cost and tuition-free options.</p></div>
```

- `services.php:763` | conditional tuition-relief context

```text
        <div class="faq-a"><p>The DSU scholarship amount depends on the Italian region and the student's ISEE income assessment. It typically combines a yearly stipend with tuition relief and subsidised accommodation and meal services. ILMERA confirms the current amounts for each region during the application process.</p></div>
```

- `services.php:771` | claim or related tuition wording

```text
        <div class="faq-a"><p>The Czech Republic, Lithuania, Latvia, Russia and Slovakia are among the most affordable destinations for Indian students, and Germany's public universities charge little to no tuition. Exact costs vary by university and city, and ILMERA provides a full cost breakdown during your consultation.</p></div>
```

### Audit outcome

No audited site/LLM files were changed. The inventory is a verification
backlog, not an endorsement or an instruction to publish a draft. If copy
is softened later, update matching metadata/schema and shared title/excerpt
sources as appropriate. Earlier verification blockers remain open.

Inventory totals: 141 source-line entries; 13 marked unsure.


## 30. Phases 11-12: GCC source review (OWNER VERIFICATION REQUIRED)

The supplied content is now in `destinations/gcc.php`, with slug `gcc`, name
`GCC` and status `draft` unchanged. Its existing ilmera_summary and
summary_provenance values are preserved exactly. It has nine technically
sourced categories (intro, english_requirements, costs, scholarships,
visa_steps, intakes, documents, work_and_stay and faqs), five unique source
URLs and eleven FAQs. who_its_for is empty. Technical source acceptance and
category counts are not editorial approval or fact verification.

### Source URL: owner must open and confirm

- [ ] Consulate General of India, Dubai: Advisory for Indian students proceeding to the UAE:
  https://www.cgidubai.gov.in/page/student-advisory/

### Additional Phase 12 source URLs: owner must open and confirm

- [ ] Embassy of India, Doha: Advisory for students arriving for university education in Qatar:
  https://indianembassyqatar.gov.in/education_Advisory_students
- [ ] Embassy of India, Riyadh: Useful information for Indian students in Saudi Arabia:
  https://eoiriyadh.gov.in/page/useful-information-for-indian-students-in-saudi-arabia
- [ ] Embassy of India, Muscat: Registration of Indian students in Oman:
  https://www.indemb-oman.gov.in/eoi.php?id=r-i
- [ ] Embassy of India, Bahrain: Registration of Indian Nationals and Indian Students in Bahrain:
  https://www.eoibahrain.gov.in/pdf/Press%20Release-Student%20Global%20portal.pdf

Phase 12 context: the unchanged original blockers below describe the Phase 11
UAE portion and its review requirements. Their UAE-only/single-advisory scope
notes do not describe the whole expanded record. Additions (e)-(j) describe
the current GCC coverage. The original Russia-not-started item is retained
verbatim with the other blockers, but is historical and superseded by the
new Russia section 31. No slug or name was changed.

### GCC publication blockers

- [ ] Resolve the scope/title mismatch before publishing. The page is named
  GCC but every supplied fact covers the UAE only. Retitle the page to match
  UAE coverage or add separately sourced coverage of the other countries
  before publication. No slug or name is changed in this phase; the owner
  must approve any future title/routing decision. Do not generalize UAE
  visa, education, insurance or work rules to the whole GCC.
- [ ] Confirm every line on icp.gov.ae or the UAE government portal and approve
  cgidubai.gov.in explicitly as an official source host. Every category rests
  on one Indian consulate advisory, reported as having no date. Its inclusion
  in official_source_hosts enables technical validation only, not completed
  owner approval. The supplied 2026-10-15 checked-on metadata is not an
  advisory publication date or an independent review by this build. Retain
  current official evidence for each statement and record real review dates.
- [ ] Verify the work-hours wording independently. The 15 hours per week
  figure is stated as approximate, not a confirmed universal limit. Check
  current applicable permission, permit and hour rules on official UAE
  sources before publishing; review the matching work FAQ at the same time.
- [ ] Decide whether to keep the agent FAQ. It is the consulate's advice,
  attributed to that source, not a new ILMERA policy or a claim about all
  agents. The owner decides whether it belongs on the page. If changed,
  keep the visible FAQ and FAQPage schema consistent.
- [ ] (e) The page now also covers Qatar, Saudi Arabia, Oman and Bahrain,
  but intro_answer is still UAE-only because it can carry only one source.
  Keep country attribution explicit; added items do not establish complete
  coverage of any country or a single GCC-wide rule.
- [ ] (f) The owner must approve these new official hosts explicitly:
  indianembassyqatar.gov.in, eoiriyadh.gov.in, indemb-oman.gov.in and
  eoibahrain.gov.in. Technical host acceptance is not completed editorial
  approval or independent verification.
- [ ] (g) Qatar and Saudi Arabia facts came from search results of embassy
  pages. The owner must open each page and confirm every line. The Qatar
  cost-of-living line appears on one version of the page and not another;
  confirm it on the live page before publishing.
- [ ] (h) Oman and Bahrain items only cover student registration with the
  embassy. The Bahrain source is an undated PDF press release; confirm that
  it is still current. Do not infer admissions, visa or work rules from it.
- [ ] (i) Kuwait has no usable study-specific official source. The page at
  https://indembkwt.gov.in/student-information.php lists institutions and
  the education officer but gives no visa, fee or work rules, so nothing
  was added. Kuwait still needs an official source.
- [ ] (j) The Saudi embassy also has a page titled "Scholarship for Indian
  students by Saudi government" that was not read and needs checking. No
  complete official-source coverage of fees, visa steps or intakes has been
  added for Qatar, Saudi Arabia, Oman, Kuwait or Bahrain. The Qatar visa
  requirement and Saudi document/visa references are partial guidance, not
  a sourced application workflow; the Qatar living-cost line is qualitative,
  not an official fee figure.
- [ ] Russia is still not started. Its empty draft record remains unchanged
  and needs official Russian or Indian government sources before adding facts.

### Current publication state and prior notes

This section and section 31 supersede section 28's not-started notes and
older counts of populated records. GCC now contains supplied items for the
UAE, Qatar, Saudi Arabia, Oman and Bahrain, with country-specific limits
above, not verified GCC-wide coverage. All nine destination records now
contain supplied sourced content and all nine statuses remain draft.
The earlier audit and other source blockers remain open.

GCC remains noindex and unlinked from live pages, sitemap.xml and LLM
recommendations despite nine categories. Noindex is not access control;
direct requests can render the draft. No advisory or corroborating UAE page
was fetched or independently verified by this build. No fact, fee, date,
deadline or rule was added from memory. Shared source-host policy is unchanged.

The CSV remains an unchanged empty template, not a synchronized copy of the
GCC PHP record. Resolve scope and source blockers, fill the reviewed CSV row
with aligned sources/dates and obtain explicit owner sign-off before release.
Follow section 18's atomic publication checklist for PHP/CSV status, accurate
sitemap entry and llms.txt recommendation in one commit, keeping llms-full.txt
consistent. Do not bypass the existing publication guards.

### Phase 11 validation and agent disclosure

The full technical checks were repeated after each of the three tasks:
78 PHP lints, 42 clean page renders and 252 Chromium page/width/JavaScript
cases per task, totaling 234 lints, 126 renders and 756 browser cases.
All 42 pages were checked at 375/768/1280px with JavaScript on/off. Coverage
included headings/robots/menus, native destination FAQs, source links,
layout, conditional Costs sections, exact summary/provenance retention,
GCC identity, nine-category/draft gates, aliases, source-host boundaries and
visible/schema FAQ parity. The GCC page has five matching FAQ/schema pairs
and one deduplicated source. Isolated published-data fixtures tested the
technical threshold without changing repository statuses. External browser
resources were blocked, not used for live source verification.

The audit inventory contains 141 exact source-line entries, including 13
marked unsure and 23 reference-only entries. All audited site and LLM files
are byte-for-byte unchanged from Phase 10. Line-ending conventions are
preserved and no em dashes were added. No test artifacts are committed.
Native response headers, Apache rewrites and production rendering still
require staging checks. No deployment was performed.

Model disclosure: this report was prepared using Arena.ai Agent Mode.
The underlying model identity is not disclosed.


## 31. Phase 12: Russia scholarship draft (OWNER VERIFICATION REQUIRED)

The supplied content is now in `destinations/russia.php`, still `draft`, with
its existing ilmera_summary and summary_provenance preserved exactly. The
record, thin entry page and slug were already registered; no helper, route,
navigation, sitemap or LLM registration was added. It has four categories:
intro_answer, scholarships, visa_steps and faqs. There are four FAQs and one
source URL. Source acceptance is technical, not editorial verification.

### Russia source URL: owner must open and confirm

- [ ] Ministry of Education, Government of India: Russian Federation scholarships notice, academic year 2026-27:
  https://www.education.gov.in/sites/upload_files/mhrd/files/Scholarships_Russia_Federation_AY_2026_27.pdf

### Russia publication blockers

- [ ] (a) The only source is the Government of India Ministry of Education
  notice for academic year 2026-27. Its application window has passed,
  reported as ending 15 February 2026. Obtain the 2027-28 notice before
  publishing; do not imply that the older notice is an active application
  opportunity. The reported date has not been independently verified here.
- [ ] (b) The facts came from search results of the notice PDF. The owner
  must open the PDF and confirm every line, especially what the scholarship
  covers besides tuition fees. Confirm the actual item/page review dates;
  supplied 2026-10-15 metadata is not an independent source review.
- [ ] (c) The number of scholarship places was deliberately left out. A news
  site reported 300 for 2026-27 and the official 2025-26 notice listed 200,
  according to the supplied research. Take any figure from the applicable
  official PDF only. Neither number is added to the destination data.
- [ ] (d) This page covers only the government scholarship route. The owner
  also identifies public and private Russian institution routes for ILMERA
  application guidance; no official source has been added for those routes.
  This is prospective guidance, not a claim of completed placements. Costs,
  visa documents, intakes and route-specific Russian-language requirements
  remain empty. The notice's one-year language preparation option applies
  to its scholarship route, not a universal admission rule.
- [ ] (e) Four categories are below the five-category publishing gate. Add
  official Russian or Indian government sources for costs, documents or
  intakes before publication; do not split groups or count summary metadata
  to inflate the total. Status must remain draft until explicit approval.
- [ ] (f) Treat tuition fees as the only coverage supported by the supplied
  notice wording pending PDF review. Do not describe study in Russia as
  having no tuition across all routes or imply that living costs, insurance,
  travel or other expenses are covered. Country-wide cost claims on existing
  pages need review; the current scholarship notice is not evidence for them.

### Phase 12 publication state and validation

All nine destination records now contain supplied sourced content; none is
approved for publication. GCC and Russia stay draft, noindex and unlinked
from live pages, sitemap and LLM recommendations. Noindex is not access
control. The CSV remains an unchanged empty template and must be populated
from reviewed content before release. Follow section 18's atomic release
checklist for PHP/CSV status, accurate sitemap entry and llms.txt changes in
one commit after owner sign-off, keeping llms-full.txt consistent.

No source page or PDF was fetched or independently verified by this build.
All facts, URLs/labels, host lists and dates are supplied content. Uncovered
facts were not invented. Existing audited site copy is unchanged.

Full checks were repeated after each of the three tasks: 78 PHP lints,
42 clean renders and 252 Chromium cases per task, totaling 234 lints,
126 renders and 756 browser cases. All 42 pages were checked at
375/768/1280px with JavaScript on/off. Coverage includes headings, robots,
menus, destination native FAQs, sources, layout and conditional Costs,
exact summary/provenance retention, GCC identity, raw/normalized facts,
all nine draft gates, host boundaries, aliases and FAQ/schema parity.
GCC has nine sourced categories, five unique sources and eleven FAQs;
Russia has four categories, one source and four FAQs. Isolated published-
data fixtures confirmed the category threshold without changing repo status.
External browser resources were blocked, not used for source verification.

The other GCC blockers are retained verbatim, including the historical
Russia-not-started item expressly superseded above. Other destination data,
site pages, navigation, helpers/header/footer, Apache rules, CSV, sitemap
and both LLM files are unchanged. No named institutions or restricted
terminology were introduced in additions. Line endings are preserved and
no em dashes were added. No test artifacts or deployment. Native HTTP
headers, Apache rewrites and production rendering remain staging checks.

## 32. Phase 13: discovery, sitemap and location quality (OWNER REVIEW REQUIRED)

This section appends findings; it does not rewrite or resolve any earlier
source, publication, appointment, funding, eligibility or approval blocker.
All nine destinations, all 17 locations and the three unverified articles
remain draft. Statuses, indexing settings, protected intros and destination
facts/summary/provenance fields are unchanged. Both LLM files are unchanged.
No source was independently fetched or verified in Phase 13.

### Status-driven discovery and sitemap

Services, Home, Footer, contextual location links and related-guide blocks
use the shared eligible collections. The sitemap uses those same collections
plus the existing static/article registries. All 12 current indexable routes,
including /all-pages, are represented. No utility, draft or noindex entry is
included. Empty collections hide discovery sections instead of linking drafts.
There are currently zero eligible destinations and zero eligible locations.

For an already registered destination with a valid entry file, owner-approved
publication and the existing sourced-category gate make it appear in links
and the dynamic sitemap without editing a template list. Location entries
similarly appear only when they pass the existing readiness checks and have
no explicit indexing exclusion. Registration, a working canonical entry and
source/quality review are still required; automation does not authorize new
facts, invent a page, or bypass the loader's existing destination registry.
Register any new static editorial route in the existing static-page registry;
the HTTP coverage check will fail if an indexable route is omitted. Utilities,
admin and thank-you endpoints must not be added as editorial registry entries.

The owner must confirm official source URLs, labels, dates, source-host
acceptance and all unresolved factual blockers before publishing a destination.
A minimum of five sourced categories is necessary but is never publication
authorization. Owner sign-off remains mandatory. The earlier atomic release
checklist for statuses, CSV, sitemap and both LLM representations is unchanged.
This phase changes no statuses and does not automate CSV or LLM publication.

### Serving and verification

The canonical /sitemap.xml response is generated by sitemap.php through the
new Apache rewrite. /sitemap and /sitemap.php redirect to /sitemap.xml. Confirm
Apache 2.4/mod_rewrite support, XML Content-Type, HTTPS canonical host, 200
responses and the two redirects on staging before deployment. robots.txt is
unchanged and already advertises the correct XML endpoint without blocking it.
The committed sitemap.xml is a portable snapshot, not the source of truth.
Regenerate it after an approved release with `php tools/build-sitemap.php`,
especially on a host that serves the snapshot rather than the PHP endpoint.
Lastmod is based on actual entry/data/template modification timestamps; retain
meaningful source timestamps during deployment and review their accuracy.
Unknown or future timestamps are omitted rather than fabricated.

Run the new HTTP checks against a running staging site:
`python3 tools/check_discovery.py --base-url https://staging.example`
For isolated publication tests, serve a separate, disposable docroot and add
`--fixture-base-url https://fixture.example --fixture-root /path/to/disposable-docroot`.
Never point the fixture host at production. The script copies the site into
that directory, changes only its temporary destination/location files and
restores their original bytes in a finally block. The fixture adds two
synthetic location groups only to exercise the gate, not as proposed facts.
Use the normal lint/render/browser checks as well, not the HTTP checker alone.

PHP 8.5 WASM behind a local HTTP adapter passed status/canonical/noindex/XML
coverage, non-self inbound links, internal target and fragment checks across
all 42 rendered routes. The 12 sitemap targets are 200 and self-canonical.
Destination publish/revert and location indexable/noindex/revert passed across
Home, Services, Footer and XML, with Contact location links and contextual
back-links. Source-citation fragments within a draft are not incoming
cross-page discovery links. Tests found and fixed the conditional-header
article exclusion without changing that header or any publication setting.
The native Apache rewrite and production headers were not executed here;
they remain staging verification, not a claimed deployment result.

Seven task checkpoints passed 554 PHP lints, 294 clean renders and 1,764
Chromium cases in total. Each checkpoint covered all 42 routes at three
widths with JavaScript enabled/disabled. Raw destination/place data, existing
robots settings, protected fields, LLM files and byte line-ending styles
remain unchanged. No em dashes or named institutions were added. A preexisting
article canonical is retained byte-for-byte, with report-only percent encoding
where required; no existing path was renamed.

### Read-only location quality report

All 17 location records remain draft and noindex; none currently passes the location publication gate. This audit changes no page, data, status or indexing setting. Entry routes are root-level `study-abroad-*` PHP files; data is in `places/`; the shared renderer is `includes/place-page.php`.

No record supplies a physical street address or location-specific phone number. All 17 have empty local-institution, transcript/MOI, local-loan and visa-route fields (`places/*.php:9-12`). Shared header/footer contact details are consultancy-wide contacts, not evidence of an office in each place. The existing no-physical-office statement must not be replaced with invented local details.

| Location | Root route | Data evidence | Quality finding |
|---|---|---|---|
| Karnataka | `/study-abroad-consultants-in-karnataka` | `places/karnataka.php:8,13-36,38-70` | Distinct state-wide intro and longer notes/FAQs. State-board familiarity and counselling-language descriptions at line 33 refer back to About, not independently verified local procedures. Three populated categories; still lacks confirmed local process evidence. |
| Kodagu | `/study-abroad-consultants-in-kodagu` | `places/kodagu.php:8-14` | Empty content fields; thin shared-body duplicate. A base-region label is not a street address. |
| Belagavi | `/study-abroad-counselling-belagavi` | `places/belagavi.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 are questions and planning advice, not confirmed local transcript, lender or appointment procedures. Three populated categories. |
| Bengaluru | `/study-abroad-counselling-bengaluru` | `places/bengaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Chikkamagaluru | `/study-abroad-counselling-chikkamagaluru` | `places/chikkamagaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Gonikoppal | `/study-abroad-counselling-gonikoppal` | `places/gonikoppal.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Hassan | `/study-abroad-counselling-hassan` | `places/hassan.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Kushalnagar | `/study-abroad-counselling-kushalnagar` | `places/kushalnagar.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Madikeri | `/study-abroad-counselling-madikeri` | `places/madikeri.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Mangaluru | `/study-abroad-counselling-mangaluru` | `places/mangaluru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Mysuru | `/study-abroad-counselling-mysuru` | `places/mysuru.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Ponnampet | `/study-abroad-counselling-ponnampet` | `places/ponnampet.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Shivamogga | `/study-abroad-counselling-shivamogga` | `places/shivamogga.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 give record/version, MOI and travel-planning prompts, not confirmed local processes. Three populated categories. |
| Siddapura | `/study-abroad-counselling-siddapura` | `places/siddapura.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Somwarpet | `/study-abroad-counselling-somwarpet` | `places/somwarpet.php:8-14` | Empty content fields; thin shared-body duplicate. |
| Udupi/Manipal | `/study-abroad-counselling-udupi-manipal` | `places/udupi-manipal.php:8,13-39,41-73` | Individually worded intro/checklist; one answered office/channel FAQ, seven empty answers. Lines 33-39 discuss multi-issuer documents and funding/travel questions, not confirmed local providers or procedures. Three populated categories. |
| Virajpet | `/study-abroad-counselling-virajpet` | `places/virajpet.php:8-14` | Empty content fields; thin shared-body duplicate. |

#### Exact shared lines and duplication evidence

- The 13 empty records share these exact lines 8-14: `'intro_answer' => '',`, `'local_institutions' => [],`, `'transcript_and_moi_steps' => [],`, `'local_loan_options' => [],`, `'visa_appointment_route' => '',`, `'local_notes' => [],`, `'faqs' => [],`.
- `includes/place-page.php:17-19` constructs heading/title/description by inserting the place name into the hub or counselling heading. On those 13 empty entries the description falls back to that same title. Labels, breadcrumbs, hierarchy and the hub-versus-town heading variant do not create distinct service evidence.
- `includes/place-page.php:176-181` emits the same counselling-process section on every location page. Exact line 179: "Counsellors review marks, backlogs, budget and course goals, discuss a university shortlist, and guide applications, visa documentation and pre-departure preparation."
- Exact shared line 180: "Visa-document guidance is provided through the same contact channels. Any visa appointment is the student's own appointment at the relevant consulate or VFS centre, not a meeting with ILMERA."
- The four populated records are not literally a complete place-name swap: their intros and checklist wording differ. Their dominant topics still overlap with general consultancy services and destination routes. Longer paraphrased checklists do not establish locally verified service detail.

**Flags:** 13 thin, shared-body duplicates; four more developed but locally evidence-thin pages. No location page has confirmed local address/phone/process evidence in its record. Owner review and genuinely useful, confirmed place-specific information are still needed before any publication decision. This is a content-quality finding, not authorization to change status, noindex, protected intros or facts. No source was independently verified in this phase.

Additional isolated publication coverage passed 48 Chromium cases: eight
pages with two eligible destinations and two eligible locations, at three
widths with JavaScript on/off, including deduplicated discovery/footer blocks.
All temporary data was restored outside the production repository.

## 33. Phase 14: source-backed publication review, 2026-10-16

Task 1: reviewed all 141 audit entries, including all 13 ambiguous entries.
Website tuition assertions are being qualified by country; article-specific
APS corrections follow in task 2. Reference-only paths remain unchanged.
The two ambiguous LLM entries and every other LLM audit entry are deferred
under the explicit file freeze. Both LLM files must remain unchanged.
Germany guidance was checked against the opened DAAD finance page, including
Baden-Wuerttemberg and Bavaria exceptions, contributions and living expenses.
Slovak-language duration rules and charged foreign-language study were checked
on the opened Slovak Ministry tuition page. Universitaly procedures were
opened, but do not substantiate the owner scholarship amount or partner claim.
The exact owner Italy sentence is conditional commercial guidance, not an
independently verified award. The Italy DSU article is withheld as draft while
its regional conditions and unsupported benefit claims await official evidence.
Generic merit-award context is not attributed to a country or marked verified.
Prior source blockers remain unresolved unless a later task explicitly records
opened evidence and the exact corrected lines. No search snippet is evidence.

Phase A source URLs opened on 2026-10-16:
- https://www.daad.de/en/studying-in-germany/living-in-germany/finances/
  Confirmed general public-course tuition conditions, Baden-Wuerttemberg,
  Bavaria, semester contributions and separate living expenses.
- https://www.minedu.sk/skolne-na-vysokych-skolach-v-sr/
  Confirmed language and standard-duration conditions; foreign-language fees.
- https://www.universitaly.it/it/studenti-stranieri
  Confirmed admissions/visa responsibilities only, not scholarship amounts.
  Initial /tuition-fees/ ministry URL was a missing page and is not evidence.
Affected website files: about.php, index.php, services.php, blog/index.php,
blog/cost-of-studying-abroad-for-indian-students.php,
blog/scholarships-for-indian-students-study-abroad.php,
blog/italy-dsu-scholarship-eligibility.php and includes/posts.php.
Their audited tuition paragraphs, metadata and FAQ/schema counterparts were
rewritten. Generic award context remains unverified, not country-specific.
All source-line references above refer to the preserved historical audit;
no statement in that audit is treated as proof of current verification.

Task 2, checked 2026-10-16: the existing APS article keeps its canonical slug.
Its title, description, visible introduction and structured headline/description
now describe tuition conditions and procedure applicability rather than a
universal entitlement. DAAD finance and visa pages were opened; APS India
was opened and supports document verification, general applicability and its
procedure overview, not a universal requirement or a promised processing time.
APS host aps-india.de is outside the existing owner-approved source-host list,
so the article is now draft/noindex. It is not included among the 29 original
draft pages. To release it, replace its APS-specific material with an opened
source on an approved host, or obtain an explicit later source-policy change.
The Italy DSU article remains withheld for unsupported regional benefits.
Contact tuition FAQs and decorative labels were also qualified by country;
contact.php uses the same opened Phase A tuition sources, not general
zero-cost claims. No source was verified from a search excerpt.

### Phase B task 3: opened-source review, 2026-10-16

Reviewed in order: Germany, Italy, Slovakia, UK, Czech Republic, Lithuania,
Latvia, GCC, Russia. phase14-source-review.json records each retained field,
URL, checked date and exact confirmed text. Every original fact/FAQ field is
accounted for; unsupported, superseded and disallowed-source lines are removed
rather than marked verified. Summary and provenance values are unchanged.

| Page | Opened source evidence and changes | Remaining source gate |
|---|---|---|
| Germany | DAAD finance: tuition exceptions, corrected contribution range, separate living costs and limited work; visas and side-jobs pages also opened. | None for retained lines; categories checked next. |
| Italy | Bengaluru consulate: admissions, pre-enrolment, appointments, interview, processing, DOV and email warning. Opened linked checklist is 2025-26, not a later intake checklist. Universitaly current procedures also opened, but not added to the destination host list. | No invented later-intake checklist or scholarship entitlement. |
| Slovakia | EC profile and embassy national-visa/contact pages opened. Old generic email-booking and document-age claims removed. The international-organisation source was opened but excluded by the stricter host policy. | Reconfirm the study-specific booking method before applying. |
| UK | GOV.UK financial guidance and English/overview pages opened. Funding amounts confirmed, and exemptions clarified. | None for retained lines; categories checked next. |
| Czech Republic | Embassy current application/booking pages, old 2018 checklist, Interior study visa and archived funds page opened. Tuition portal redirected to a missing page. Current translation, appointment and insurance conditions retained; outdated tuition/range and archived funds claims removed. | Original tuition source unavailable; redirected portal host is outside existing approval. Keep draft pending approved replacement evidence. |
| Lithuania | EC tuition/insurance profile and Migration Department India appointment page opened. Institution-specific immigration source opened but excluded; its D-visa regime and funds statements removed. | Do not resolve conflicting visa descriptions using an unapproved institutional source. |
| Latvia | Embassy Indian-national and general student pages and EC profile opened. Existing appointment, verification and insurance lines confirmed. | None for retained lines; categories checked next. |
| GCC | Dubai advisory redirects to a 2026 document, opened through relevant sections. Qatar advisory, Saudi student table and Bahrain PDF opened. Bahrain release is dated 31 May 2022. Oman URL returned File not found; Kuwait has no usable evidence. | Exclude Oman/Kuwait. Visible scope note required before publishing the remaining four-country material. |
| Russia | Cited Ministry PDF returned a missing page. Search did not supply an opened current replacement. | Zero verified categories this session. Keep all existing source dates unchanged; current notice and expired-window details remain unverified. |

No source-host list was broadened. Non-government/institution-specific hosts
were removed, not silently approved. A successful HTTP page load containing
an error or archive banner is not current factual verification. The JSON
contains no claim that an unavailable Russian notice was read.

### Phase B task 4: substantive category completion

Only opened, approved sources were used for additions, checked 2026-10-16.
Germany gained the DAAD student/prospective-student visa distinction. Italy
gained the consulate statement that each institution sets tuition. UK gained
GOV.UK eligibility and English-evidence rules, including provider assessment
and the degree-level B2 requirement, not a universal test waiver. Latvia gained
the EC profile living-cost estimate, explicitly separate from tuition.
Exact new lines, URLs and dates are in phase14-source-review.json.
Verified category totals: Germany 6, Italy 5, Slovakia 5, UK 6,
Czech Republic 4, Lithuania 5, Latvia 5, GCC 9 and Russia 0.
The Czech tuition-portal and Russian notice failures are not filled with
generic or invented categories. They remain exact publication blockers.
The JSON also records the approved-host snapshot; no new host was approved.

### Phase B task 5: publication decisions

Published Germany, Italy, Slovakia, UK, Lithuania, Latvia and the scoped GCC
guide. Each has at least five genuine sourced categories, a verified intro,
no restricted promotional wording or named institutions, and matched visible
FAQs and schema. The runtime gate now matches every intro/fact/FAQ text,
question, source URL, label and date to the committed review journal; changing
one without review removes publication eligibility. Status alone is not a gate.
The reviewed approved-host snapshot must also match each citation host.

Czech Republic remains draft: four verified categories and an unresolved
tuition source/redirect-host gate. Russia remains draft: zero verified
categories and a missing current notice. Its expired supplied date and lack
of verification are visibly disclosed, without upgrading old source dates.
GCC visibly names its four-country scope, explicitly excludes Oman/Kuwait,
and labels the Bahrain registration notice as dated 31 May 2022 rather than
current visa advice. The country sections each carry their own source.
Both LLM files remain unchanged; discovery snapshot work is scheduled in E.

### Phase C task 6: seventeen distinct location guides

Rewrote every location with a different counselling problem and original
intro, three substantive sections, two answered FAQs, title, description and
H1. Each has at least 350 words of intro plus section prose, excluding FAQs,
headings, navigation and boilerplate. No named institutions, local banks,
travel routes, distances, issuing offices or processing-time claims were used.
No local practical facts therefore require an external source citation.
Service schema uses only the existing sitewide organisation and main contact
number from contact.php; area served is an audience, not an office address.
Removed inferred administrative breadcrumbs and location metatags. Related
guides are editorial links, not assertions of proximity. All remain draft
until task 8 measures and enforces the stronger publication gate.

### Phase C task 7: business-presence and contact audit

The existing contact.php explicitly offers phone, WhatsApp and video calls.
No location page claims a branch, walk-in appointment, local office, partner
college, local address or city-specific phone. No new contact number or
address was introduced. Service schema repeats only +919019557427, already
the main contact in contact.php, and the existing sitewide organisation URL.
Its areaServed names the intended audience, not a physical location.
The shared contact card now states the existing Coorg/Kodagu base and no
physical office concisely, without inventing a local meeting arrangement.
Authored guides do not use an unsupported online-counselling label.

### Phase C task 8: measured location publication

All 17 guides pass and are published. Authored prose is 367-381 words per
page before counting headings or FAQs. All 136 city-normalised pairwise
comparisons pass: maximum shared contiguous five-word coverage is 3.311%,
well below 15%. The committed report records every pair and exact content
hashes. Every title, meta description, H1 and FAQ question is unique.
No local practical facts were asserted, so local external-source lists are
empty, deliberately. Existing contact/service pages support business facts.
Service markup has a sitewide provider/contact, no invented local address.
The runtime gate replaces the obsolete five-category location requirement
with prose, review, source-scope, unique-copy and schema gates. A changed
page or peer invalidates the measured cohort until it is reviewed again.
Duplicate or edited pages cannot be published by a status toggle alone.

Task 8 also measured all 136 pairs of full rendered main content, including
the shared contact card and related links, excluding sitewide header/footer.
Maximum overlap is 14.147287%, between Siddapura and Virajpet. Both authored
and stricter rendered-main scores pass and are enforced by the runtime gate.
Twenty-five positive/negative location-gate assertions pass.

### Phase D task 9: three article reviews and additional DSU draft

Published the cost, documents and scholarships articles after rewriting them
to opened approved official evidence, dated 2026-10-16. Each has an explicit
scope, per-claim citations, source list, corrected metadata and matching FAQ
markup. Their first publication in this review is dated 2026-10-16, not the
old draft date. phase14-article-review.json records exact claims, URLs, checked
dates, file hashes, metadata and removals. Publication fails closed if a
reviewed file or its metadata changes without review.
Cost comparison no longer ranks destinations or invents suitability, Russian
language/backlog rules, blanket blocked accounts or unsupported awards.
Documents no longer gives a universal checklist, mandatory APS for everyone,
DSU declarations or invented local queues/processing experience. Scholarships
distinguishes tuition policy, opportunities, actual awards and sponsor proof;
no current-call eligibility or Italy award amount is asserted.
The DAAD scholarship overview was opened in this task; other cited official
pages were opened earlier in this session and relevant text re-read.

The additional Italy DSU article stays draft. Unverified household thresholds,
renewal rules, regional claims and experience assertions were removed. Only
the exact conditional owner wording remains, visibly labelled owner-supplied
and not official verification. The opened consulate background does not
verify the amount or partner entitlement. A current approved official award
call and documentary authority for the partner claim are still required.
The APS article remains draft because its central procedural host is outside
the approved policy. Both extra drafts remain absent from discovery.

### Phase E task 10: discovery and editorial dates

Reconciled the status-driven homepage, Services, About/Contact links, blog
index, related guides, location pages, footer, directory and dynamic sitemap.
All 37 indexable routes have sitemap entries and inbound links. Czech,
Russia, APS, DSU and the utility 404 are excluded. No published-noindex target
is exposed. Existing guards now consume the stronger destination, location
and article evidence gates; no static draft link was added.

Regenerated sitemap.xml from the same shared generator as /sitemap.xml.
Lastmod uses recorded editorial dates rather than checkout/deploy mtimes:
2026-10-16 for changed content, new publication and dynamic directories;
privacy policy retains 2026-10-15. The two earlier published articles have
actual Phase A edits, so their modified dates are corrected to 2026-10-16.
No original publication history was inferred from filesystem timestamps.

Both LLM files remain byte-identical by explicit instruction. They need a
separate authorised follow-up to reconcile newly published guides, changed
claims and any withheld article references. No generator was presumed and
no mechanical exception was used to override the file freeze.

Updated isolated discovery fixtures for the new gates: status demotion,
source-text mismatch, location-cohort mismatch, explicit noindex header and
article-hash mismatch must remove links/sitemap entries and restore cleanly.

### Phase E task 11: full validation and fail-closed regression tests

Validated 42 HTTP route renders: all 41 editorial routes have self-canonicals;
the noindex utility 404 deliberately has no canonical. All 37 published
editorial routes are indexable, and the four drafts plus utility are blocked.
Every rendered JSON-LD block parses, location Service provider/contact facts
match the existing sitewide details, FAQ/schema text matches, and no rendered
visible text contains an em dash. Internal targets/fragments, inbound links,
robots and exact runtime/static sitemap parity pass. Both LLM byte hashes
match the pre-phase baseline. phase14-validation.json records per-route data.

Negative tests also reject unreviewed notices, legacy local-note injections,
changed review dates and edited claim/question/source fields. Article gates
check approved hosts and that each confirmed claim points to a reviewed
source. Neither held APS nor DSU can be revived by a status-only toggle.
Russia retains its explicit alternative of a verified current-year notice
or five verified categories; its notice-verification flag is false.
Isolated fixture tests cover status changes, source/cohort/article mismatch,
explicit noindex headers, held-article status toggles and clean restoration.

Environment limit: native PHP/Apache is not installed. PHP 8.5 WASM parser
and serialised HTTP renders plus Chromium captured-render tests were used.
External font/social navigation was not a production-network verification.
No .htaccess change was made in Phase 14; its CRLF bytes are preserved.
Apache 2.4 staging must still confirm /sitemap and /sitemap.php redirect to
/sitemap.xml, the XML internal rewrite ends without a loop, clean URLs and
query strings behave correctly, and private include/data/tool paths remain
appropriately protected by the staging configuration. The adapter is not
proof of mod_rewrite or production access controls. No deployment was made.

### Phase F task 12: final decision record

See phase14-publication-report.md for the exact 29-page table, per-page
confirmed source references, failed gates, precise owner inputs and complete
changed-file list. Final original-target outcome: 27 published, Czech/Russia
draft. The additional APS/DSU drafts remain withheld and absent from discovery.
All earlier blocker history is retained; no earlier failed fetch is re-labelled
as successful. Every task has its own commit and each Phase A-F has a PR
checkpoint. Native Apache staging, LLM reconciliation and the explicit source
requirements for held pages remain outstanding, not silently completed.
No owner question was needed, no unapproved host was added, no protected
summary/provenance value was changed outside the authorised tuition review,
and no new address, phone, local office, institution name or outcome claim
was introduced. Both LLM files and .htaccess retain baseline bytes.

Final task-12 precision review: UK FAQ now explicitly scopes the 28-day bank
rule to personal/parent/partner funds, not loans or official sponsorship.
Lithuania booking now gives the exact MIGRIS external-provider-ready status,
not merely submission. Both are supported by already opened source text;
URLs/dates and the matched source journal are unchanged except confirmed copy.
Correction to the task-4 narrative tally: Slovakia has six verified categories,
not five, including the sourced scholarship category. The machine journal
and final 29-page table already show the correct six. Earlier notes retained.

## Phase 16 task 1: limited LLM permission

Removed only the two withheld-article link lines from llms.txt. Neither link
exists in llms-full.txt, so that file is unchanged. APS and DSU remain draft,
noindex and absent from rendered navigation, schema and the sitemap.

Conservative permission decision: the explicit approval allows changes to the
two LLM files for task 1 removals only, despite later requests mentioning names
and prohibited wording there. No other LLM edit is authorized in this phase.
Existing university names and prohibited wording in these public text files
remain release blockers, not exceptions that make a strict check pass.
Historical reports and suppressed internal related-post arrays are not live
discovery links and have not been erased. Earlier blockers remain unchanged.

## Phase 16 task 2: institution-name cleanup and permission blocker

Neutralized the named Italian institution in About visible copy and schema,
removed its named affiliation/Wikipedia identity, and replaced the named UK
examples in Services with programme-comparison advice. No partnership,
recognition or career result was invented. All changed lines are recorded in
the Phase 16 release report. Added tools/blocked-names.txt and a strict default
discovery guard covering public text, metadata, schema, alt and link text,
including both public LLM files. Government citation anchors are the only
name exception.

The named UK institutions remain at llms.txt:58 because the explicit approval
permits only task 1 link removals there. The strict discovery guard must fail
on those names. This is an unresolved permission blocker, not a passing
exception. Both LLM files also retain prohibited wording under that same
restriction. No page status changed; no earlier blocker was rewritten.

## Phase 16 task 3: current citation repairs and transport limit

Reopened every distinct official citation URL found across the 37 published
HTML pages, including the Graduate visa citation also in both public LLM
files. The short Latvia Indian-national path still returns a missing-page
body. Replaced it in the Documents article and its matched source journal
with the opened /students/indian-nationals page on the same approved host.
That page explicitly supports the retained Hello Verify/VFS and document
paragraph. Updated the source label and rechecked_on evidence; checked_on
remains 16 October 2026 because both checks occurred on that date.

The Dubai landing URL redirected successfully to the 2026 official document
in this pass, unlike its earlier HTTP 500. Use that opened direct document
instead. Also made the existing European Commission Latvia, Riyadh and
Slovak national-visa redirects direct, on the same approved hosts. Removed
the unsupported Qatar statement that the embassy lists no application steps;
kept its sourced visa-applicability fact and added confirmation advice.
All active source rows and affected article hashes were matched again.

Latvia retains five categories: intro, costs, visa steps, documents and FAQ.
No Latvia line was removed and no page status or sitemap URL changed.
Historical source attempts and all earlier blockers remain in place.

reports/phase-16-citations.json records all fresh source opens. The fetch tool
exposes content success/error, not raw headers/status on successful fetches.
It cannot honestly certify numeric HTTP 200 for each external citation.
No other substantive missing page was found, but the strict all-citations-200
transport requirement remains unverified until an unrestricted staging check.
No failed or soft-missing page has been labelled verified evidence.

Task 3 inventory correction before finalizing its commit: the initial
host-filtered extraction counted 23 original citations and missed two existing
static tuition-footer sources. A fresh broader link sweep found the Slovak
Ministry tuition page and Universitaly procedures page. Both were freshly
opened substantively too. The complete totals are 25 original distinct URLs
and 23 current distinct URLs after removing duplicate redirect aliases.
The maintained tools/published_citations.py inventories all published anchors,
schema citations and both LLM files without that destination-host filter;
three regression cases cover legacy/unknown hosts, schema-only citations and
explicit contact/social exclusions. Neither legacy footer host was added to
the destination approval lists. Universitaly still does not substantiate the
owner amount or partners. The earlier all-200 transport limitation remains.

## Phase 16 task 4: exact owner sentence and matched cautions

The existing 19 published amount occurrences already used the required exact
sentence. Preserved it verbatim in every occurrence and placed explicit
owner-provided conditional guidance and written-award budgeting cautions
alongside it, consistently in visible copy and matching FAQ schema. Retained
the existing tuition-source owner disclaimer. Added an explicit No to the
Home FAQ about relying on an unwritten award. Removed DSU from the nearby
Home route label and the Services amount question so the owner figure is not
presented as an officially verified regional DSU amount. Neutralized the
Contact metadata phrase describing Italy as no-charge education.

The amount and partner relationships remain owner-supplied, not official
proof. No university name or page status was introduced. The Italy DSU
article remains draft/noindex and was not edited or linked. Both LLM files
remain limited to task-1 authorized link removals; their broader Italy and
prohibited wording remains a release blocker, not an exception to readiness.
Maintained exact-sentence checks inspect published surfaces plus both LLM
files, reject common 8,000/8000/8k/eight-thousand variants, and require the
matched owner label and written-award caution at every amount occurrence.

Task 4 FAQ visibility correction: the added attribution/cautions exposed the
fixed 300/340px FAQ height caps on Services and Contact. Removed those open
height caps so mobile answers are not clipped, and added no-JavaScript answer
visibility fallbacks. Extended the fresh browser assertions to actually open
and close button FAQs with JavaScript on, check the full answer fits, and
check full answer readability with JavaScript off. This does not claim live
external-resource or native Apache verification.

## Phase 16 tasks 5 and 6: final release decision and maintenance

Final decision: NOT READY for staging acceptance or production sign-off.
The authorized fixes are recorded in reports/phase-16-release-check.md;
phase-16-checks.json contains fresh per-task evidence and the full sitemap.
The report lists all changed files and all task-2/task-4 changed line ranges.
Each of six tasks has fresh full lint/render/browser/discovery checks.

Final counts remain 27 published / 2 draft in the original 29 targets;
including the additional held APS/DSU articles, 27 published / 4 draft.
The entire site has 37 indexable published HTML pages, four draft editorial
pages and a separate noindex 404 utility. All 37 sitemap entries are locally
200/self-canonical/not-noindex; static/runtime XML matches. No statuses or
sitemap entries were changed during Phase 16. Nine destination summaries and
provenance remain byte-preserved. All 17 location guides pass authored and
fresh full rendered-main 136-pair checks (3.311% and 14.147287% maxima).

Strict discovery and publication CLIs FAIL on restricted llms.txt names;
prohibited wording remains in both public LLM files. Do not waive this,
quietly change restricted bytes, prune the blocked-name list to hide it,
or advertise diagnostic core output as a release pass. Task-1 link removals
are the only LLM permission currently applied. Six names-guard, three
citation-inventory and four exact-claim regression cases pass.

All 25 original official citations were freshly opened, with one soft
missing page repaired and 23 distinct final URLs. Content opens are not raw
HTTP-200 certificates. Native Apache rewriting/redirects/query preservation,
private staging access, HTTPS/canonical-host policy and real external asset
and contact delivery still need authorized staging verification. Noindex is
not authentication. The owner 8,000-euro and partner claims are conditional
guidance, not verified awards. Earlier source/owner/status blockers remain
exactly as recorded; this append does not erase or replace them.

Maintenance: run the default strict commands and unit checks documented in
tools/README.md, produce the broad citation inventory, and record actual GET
status/redirect/body evidence before sign-off. Any future LLM reconciliation
requires permission beyond task-1 link removals and a complete fresh rerun.
No merge, deploy or main push was authorized or performed.

## Phase 17 task 1: final owner operating model, 2026-10-16

Applied the owner's final statement: ILMERA operates virtually, with no
physical office and no in-person counselling location anywhere. All 17
location titles/headings/metadata now identify online counselling, each has
one plain online/no-office-travel sentence in its authored content, and the
shared site contact wording is explicit about online-only delivery.

The contact record contained only Coorg, Kodagu/Karnataka and India, not a
street, building, postcode, delivery address or coordinates. Retained that
partial postal locality in the Contact organisation only, explicitly labelled
as a locality record and not counselling premises. No registered-address or
mail-delivery claim was invented. Removed other schema address copies and
the duplicate contact node with a legacy storefront-style identifier. The
location Service uses an Organization provider with the actual place in
areaServed; neither node has a street address, coordinates or storefront type.

Physical-presence checks distinguish exact negative owner disclosures and
no-travel statements from offers to meet locally. Official visa interviews
and the name of an immigration authority are not ILMERA counselling premises.
No government procedure was converted into an online-only promise. Historical
owner-presence blockers will be formally closed by the task-3 append; no other
blocker is erased here. Both LLM files remain byte-identical to Phase 17 start.
Their existing restricted content still prevents an unconditional global
wording/name sign-off. No page status was changed.

## Phase 17 task 2: GCC business scope versus source scope, 2026-10-16

The visible first note now states ILMERA supports university applications in
all six GCC countries, on the final owner statement. Partnership scope is
universities only; no government or embassy affiliation is claimed. The
second visible note separately names the five countries with official-source
material and states the missing Kuwait rules/confirmation requirement.
Metadata and WebPage/Service descriptions use both notes; Service areaServed
lists all six as business scope, not six sets of verified country rules.
The protected intro_answer, slug, name, summary and provenance are unchanged.

The old Oman registration URL still returned a missing-file body. Opened the
current registration page linked from the embassy navigation, on the same
already approved host: https://www.indemb-oman.gov.in/registerstd/ . Its
substantive request applies to Indian students residing in Muscat for
education or training. Added only that registration request as a sourced FAQ
with checked_on 2026-10-16 and an exact matching journal row. Oman and Bahrain
coverage remains registration-only; Bahrain retains its 31 May 2022 date.
No Oman admission, visa or work rule was inferred.

Opened the Kuwait embassy student-information page again. It provides a
directory and contact information, not usable current student rules for this
page. No Kuwait factual line, source citation or host-list expansion was
added. Missing verified Kuwait requirements remain an OPEN source blocker.
reports/phase-17-source-opens.json records the fresh opens and limits. Content
success is not raw transport-status proof. No page status or LLM file changed.

## Phase 17 task 3: targeted owner-blocker closures, 2026-10-16

These dated resolutions supersede only the two owner-input uncertainties
named below. Historical entries stay intact as a record of earlier review;
no unrelated blocker or source-verification requirement is rewritten.

- [x] CLOSED: owner confirmation of office presence and counselling model.
  Final owner statement received 16 October 2026: ILMERA operates virtually;
  it has no physical office and no in-person counselling location anywhere.
  Online-only counselling is now an owner-confirmed business fact, not an
  inferred location service. This resolves earlier uncertainty about whether
  to call the service online and any request to confirm a counselling office
  or branch. It does not confirm an address, local procedure, local provider
  or venue. The Contact postal record is locality-only, not a delivery or
  registered address claim, and is labelled as unrelated to counselling
  premises. No street address or coordinates were supplied or invented.

- [x] CLOSED: owner confirmation of GCC service countries.
  Final owner statement received 16 October 2026: ILMERA has partnered across
  UAE, Saudi Arabia, Qatar, Kuwait, Oman and Bahrain. In the site wording,
  partnerships refer only to universities, never governments or embassies;
  no university is named. This resolves owner-input requests about the list
  of countries supported and broad university-partnership country scope.
  It is not government corroboration of business relationships, proof of an
  individual agreement, a confirmed award or a shared six-country visa rule.

- [ ] OPEN: Kuwait student-rule evidence. The official embassy directory was
  opened again during task 2, but no usable current admission/visa/work rules
  were accepted. Kuwait remains outside the page's verified source coverage.
  Confirm requirements directly with the relevant institution and authority;
  add a factual line only after opening a supporting approved official page.

Oman registration now has an opened replacement on the existing approved
host. Both Oman and Bahrain source coverage remains registration-only and
Bahrain retains its historic notice date. None of this closes Kuwait's gap.
All other source, award, attribution, delivery, LLM-content and native-staging
blockers remain as previously recorded. No page status or LLM byte changed.

## Phase 17 task 4: final verification decisions, 2026-10-16

The final audit clarified two directory headings as online student audiences
instead of an ambiguous location list, without altering any target URL.
These final surface corrections are included in the task-1 line inventory
supplement. Expanded the physical-presence regression check to plural offers;
its narrow negative-disclosure and official-interview exceptions still do
not waive a separate local-meeting offer. No actual university name or
prohibited wording was added. Both LLM files remain exactly as at Phase 17
start, so their pre-existing name/wording failures must remain reported.

All page-status flags and the published/noindex/sitemap cohort are preserved.
The raw external-source transport, native Apache behavior and actual delivery
limits remain open checks, not successful results inferred from the local
adapter. Only the two dated owner-input closures from task 3 are closed.

Final audit supplement: the Home study-route qualifier now says programme
conditions rather than referring ambiguously to academic branches. The
presence guard distinguishes academic uses of that plural noun from offers
of ILMERA/local premises; those boundary cases have explicit regressions.
No academic tuition claim in the restricted LLM files was edited or accepted
as newly verified merely because it is not a physical-presence offer.

The final presence check includes government citation anchors too. The
separate names guard's official-label exception cannot hide an office or
meeting offer. A ninth presence regression case tests this exact boundary;
this does not broaden source approvals or waive existing LLM failures.

## Phase 18 task 1: full LLM reconciliation approved, 2026-10-16

The owner now permits full edits to both public LLM documents. This supersedes
only the earlier LLM edit restriction, not the content/source/status gates.
Retained the Markdown document/section/bullet/FAQ structure, with seven
published destination subsections. Removed unpublished destination promotion
and unverified broad eligibility/recognition/award implications rather than
carrying them into the new directory. No site page status was changed.

Public institution names and prohibited claims were neutralized. The Italy
amount now uses the exact approved sentence, with the same local owner label
and written-award caution as the published pages. Online-only counselling is
explicit. The GCC business/source statements exactly match the visible page,
including registration-only limits and missing Kuwait requirements.

The internal technical denylist retains removed aliases only to prevent
reintroduction; they are not published or repeated in new handoff prose.
Government labels/official portal names remain only where applicable. The
obsolete byte restriction must be replaced by strict content policy checks,
not by a self-comparing hash or a waiver. Page-directory additions are task 2.
The owner deploys directly to live; no staging workflow is assumed. The live
server address/transport/delivery checks remain separate from local QA.

## Phase 18 task 2: published-page directory decisions, 2026-10-16

No existing LLM generator was found in the repository. Added a maintained,
standard-library builder that reads fresh rendered metadata, not guessed
source labels. Directory entries use exact page titles and descriptions,
canonical absolute addresses, and the existing Markdown link/description
format. Existing generic core-service explanations and company/contact/legal
URLs are retained; no stale draft-oriented core-page metadata is copied into
new LLM copy. Both documents represent all 37 published addresses, including
seven destinations, 17 location guides, five blog articles and both indexes.
The two already-listed short-file articles are refreshed rather than counted
as newly discovered pages. The four held routes/information remain excluded.
No page metadata, status, source gate, journal or sitemap has been changed.

## Phase 18 task 6: dated targeted closures and live handoff, 2026-10-16

These notes append resolutions; all historical blocker text is unchanged.

- [x] CLOSED: permission uncertainty preventing LLM reconciliation. Phase 18
  explicitly authorizes complete edits to both documents. Earlier immutable-
  byte instructions are superseded, not the substantive publication policy.
- [x] CLOSED: historical public LLM institution-name and prohibited-wording
  release failures. Both files are cleaned and the strict current whole-site
  names, wording, discovery and publication commands PASS without exclusions.
  The replacement checks require the exact Italy sentence with attribution/
  caution, explicit online-only counselling and exact visible GCC notes.
- [x] CLOSED: missing published editorial page listings in both LLM files.
  Exact rendered title/meta-description entries cover all seven destinations,
  17 locations, five articles and two published indexes. Existing core URLs
  remain; all 37 indexable addresses are represented. The maintained builder
  is idempotent, rejects stale metadata, and never generates a held/noindex
  page entry. The line audit preserves task 1 numbers before these additions.
- [ ] OPEN: usable current official Kuwait requirements. Nothing new was
  sourced in this phase. Oman/Bahrain coverage stays registration-only.
- [ ] OPEN: existing source/category/award/approval blockers for all four held
  pages. No source host, page status, hash journal or sitemap was changed.
  The exact owner amount is still conditional guidance, not official proof
  of award terms or an individual university relationship.
- [ ] OPEN: actual live page addresses/native server behavior, raw external
  citation HTTP health, live enquiry/channel delivery and Search Console
  processing. No local adapter/browser pass closes these checks.

Conservative deployment decision: the owner works directly on live, not
staging. Phase 13 .htaccess is already live per owner; no reapplication is
required here. Earlier staging instructions are historical workflow notes,
not the current deployment plan. The underlying live server evidence remains
outstanding. Back up the complete current live files/settings first, test
on the actual live site after deployment and restore the backed-up files
if errors occur. Do not limit restoration to the server rules file.

Ready for owner-controlled direct-live deployment after backup because all
local gates now pass. Not certified as already deployed or finally accepted
live. The release report uses FAIL: not verified for missing live evidence,
not to imply a live failure was observed. No deploy, main push or merge.

The initial task 3 run stopped on resource exhaustion in the long-running
local WASM adapter, not on an accepted content exception. Restarted it and
reran the complete suite successfully. An early online-only negative test
was corrected to remove both letter cases before a successful fresh rerun;
no content gate was relaxed. Machine evidence records completed passing runs.
No new external-source verification or raw-status certification was inferred.

## Phase 19 task 1: provisional strategy mapping, 2026-10-16

The named strategy document could not be located with the available title-only
input and ID-based Docs tools. Drive search is disconnected. Continued under
the owner fallback without asking questions. No research prompts, volumes,
section citations or conflicts were fabricated. Core targets and existing
navigational/article intents are explicitly provisional. Consultancy fees
remain an owner-data gap. A new guide is explicitly authorized in task 3;
no existing publication status may change. All destination data is frozen.

## Phase 19 task 2: conservative presentation layer, 2026-10-16

Metadata/H1/opening changes are centralized in data/seo-map.json and applied
server-side before delivery, including social and page/service/article schema.
Destination records, summaries, provenance and facts remain byte-identical.
Existing sourced prose remains visible verbatim. Location authored data and
its content-hash gate are unchanged. Article review file hashes were updated
only for the new presentation include, not for a source/fact/status change.
All keyword assignments remain provisional pending the inaccessible strategy
document. Exact title/description/H1 values are in the on-page change report.

## Phase 19 task 3: explicitly authorized guide, 2026-10-16

Added only the requested consultant-choice guide. Existing statuses remain
unchanged; the new article has its own published entry under the established
general-guide pattern. Ten checks are reader advice, not promised outcomes.
Missing fee/individual agreement/student-proof information is explicit.
The full heading/primary target is longer than the short-title budget, so
the title uses the faithful shorter Choose wording. No keyword research
or strategy-document proof was invented.

## Phase 19 task 4: bounded answer overlays, 2026-10-16

Direct answers and added FAQs use only existing page introductions, authored
sections or preparation advice. Existing sourced facts are not rewritten.
The older backlog article is not treated as proof of a programme eligibility
rule; its new answer is limited to honest record preparation. No document
prompts are invented. The fee-schedule gap remains open. Rendering additions
are recorded in data/answer-map.json with source-file provenance; underlying
source gates and destination records remain intact.

## Phase 19 task 5: one canonical identity, 2026-10-16

The canonical identity uses only existing site/footer profiles, existing main
contact details, existing Founder name/role and the online counselling model.
No biography, street address, affiliation proof or new profile was invented.
A minimal existing-data Founder Person replaces competing detailed Founder
schema; other existing team records are not expanded. All pages resolve the
same Organization ID and full definition, with audience areas distinct from
premises. About, Contact and Karnataka have the same visible entity/service
block; both LLM references are generated from the same data. Destination and
article review dates match schema dateModified without editing source facts.

## Phase 19 task 8: measurement owner decision, 2026-10-16

No existing analytics tag or transport was found in executable site source.
Added no tracking script, event sender or third-party dependency. Provider,
property, consent and an actual enquiry-success signal remain owner inputs.
The measurement report distinguishes CTA clicks from confirmed delivery and
excludes personal/student information from any proposed future events.

## Phase 19 task 9: official eligibility and off-page limits, 2026-10-16

Opened Google official eligibility and representation guidelines. Online-only
businesses are listed as ineligible for Business Profile; service-area rules
require actual customer visits, not a virtual workaround. No profile or
address was invented. Directory onboarding does not prove acceptance of the
confirmed online-only model. Sulekha access was denied, the requested UrbanPro
category was missing and Justdial onboarding requests an address. None was
certified eligible; these remain owner due-diligence candidates. Existing
social handles only, no new account or submission, no fictional student proof.

## Phase 19 task 11: targeted sign-off and unchanged blockers, 2026-10-16

- [x] Local on-page/entity/answer/CTA/technical checks pass with the existing
  publication cohort preserved plus only the explicitly requested new guide.
- [x] Cycle 1 is clean locally; no further rewrite cycle is justified.
- [ ] Strategy document link/ID and actual research inventory remain missing.
  No document-derived keyword volumes, prompt counts or section conflicts
  can be certified. The fallback map is explicitly provisional.
- [ ] A real service-specific fee schedule and written scope/refund terms,
  approved proof and consent remain owner inputs. All proof slots stay empty.
- [ ] Online-only acceptance by the directory candidates remains unconfirmed;
  no listing or account was created. Existing company-profile control should
  be confirmed by the owner. No workaround for Google eligibility is proposed.
- [ ] Analytics provider/property/consent and actual success transport remain
  owner decisions. No tag or new third-party script was added.
- [ ] Actual live addresses, native routing/redirects, external HTTP status,
  live rankings, enquiry delivery and Search Console processing are unverified.

Earlier Kuwait/source/category/award and four-held-page blockers remain open.
No prior blocker is rewritten or silently closed. The exact conditional Italy
sentence is not award proof. Online counselling is not local premises.

Conservative implementation decisions: canonical identity is separate from
page-specific descriptions; old generic source facts stay visible unchanged.
Server-side overlays keep title/social/page-schema values synchronized without
editing protected destination data. Additional answer provenance is recorded
in its data map. Render checks, not just data-file hashes, cover these layers.
Source-journal hash updates only reconcile the article include bytes.

The owner deploys directly live after backing up the complete current live
files/settings. Phase 13 server rules are already live per owner. Mandatory
live smoke tests and restoration of the backed-up files on errors remain;
no staging step, main push, merge or deployment was performed by the agent.

Task 3 title-decision clarification: the full guide heading alone is 52
characters and fits the limit; adding the usual brand suffix would make it
61. The earlier note referred imprecisely to the heading itself. The chosen
shorter semantic title with branding is within budget; the full primary
remains in the H1/opening. No passing page is rewritten for this clarification.


## Phase 20, 2026-10-16: actual document review and bounded sign-off

Resolved only the missing-document-link/access/inventory blocker: the actual
supplied document opened and all six export chunks were read in Task 1.
The completed inventory has 50 prompts and 17 query fragments, no supplied
numeric volumes/difficulty. Phase 19's provisional wording remains in its
historical records; it is not retroactively rewritten into research proof.

Conservative resume decisions: fetched/matched the remote session branch;
Task 1 was complete, no partly written Task 2 maps existed. Retained all 38
fitting primary targets, titles, descriptions, H1s and openings, rather than
forcing synonym changes or rewriting passing pages. Archived the provisional
maps and access-only conflict log before replacing their current versions.
No new regional/national/eligibility page is justified by generic duplicate
copy or an unsourced procedure. No held page released.

Seven FAQ additions reuse existing facts. Dates for the UK Master's-context
Graduate visa FAQ were already in the homepage and were rechecked on the
opened GOV.UK overview; newly seen charges/rules were not copied. The state
hub's unordered ItemList describes only its four existing visible guide
links, not a ranking. All destination/place data and publication/source
journals stay byte-identical, protecting all summaries and provenance.
All five production proof slots remain EMPTY despite research assertions.

Still open, not closed by strategy data or generic disclaimers:
- 29 prompt gaps and 15 partial answers, with exact missing facts in
  prompt-map.md and phase-20-map.json. In particular official local revenue,
  apostille/MOI/APS procedures, language/marks/backlog thresholds, lender and
  agricultural collateral rules, immigration outcomes and current individual
  financial/award evidence require substantive approved sources.
- Owner-approved service prices, scope/refunds/financial relationships,
  individual partner or award evidence, genuine review evidence and consent,
  actual media/video/event material and authorized personal profiles.
- Platform eligibility, authorized accounts and approval for any profile,
  directory or outreach. No invented registration address, premises or GBP
  workaround. Authentic content is not a guarantee of ranking or AI citation.
- Analytics/provider/privacy/success decisions remain owner-only; no tracker
  or third-party script added. Live rankings, AI visibility and enquiry
  delivery are not independently measured by this local suite.
- Raw external-source HTTP status/redirect verification and native Apache
  redirect/rewrite/query/access-control checks remain unverified here.
  Successful fetch wrappers and the local adapter are not those checks.

Live readiness is not accepted by repository QA alone. Owner must first
back up the COMPLETE live site and settings, deploy directly live under the
standing workflow, run the live smoke checklist and verify actual enquiry
receipt. On errors restore ALL backed-up files and settings, not a partial
rollback. No staging, upload, main push, merge or deployment occurred here.
Historical blockers are preserved. Only the specifically resolved document
access/inventory uncertainty is closed.

Task 7 handoff correction: seven added FAQs are on FOUR existing pages
(selection guide, Coorg process article, scholarship article and UK guide).
Earlier Phase 20 checkpoint text incorrectly said five pages. The new
append-only handoff assertion caught this reporting error after all site
checks passed. Reports were corrected, and a fresh complete Task 7 suite
is required before final sign-off. No public content change is needed.

Task 7 completion: after correcting the four-page FAQ count, the entire
fresh sign-off suite passed, including append-only and line-ending checks.
This closes the reporting discrepancy only, not any owner/live/source gap.

## Phase 22 scope decisions, 2026-10-22

Owner service answers now replace the earlier unresolved scope questions,
not official country rules or proof evidence. Report-only Task 1 does not
change publication. Runtime and test administration are not site changes.

The request to exclude unprovided fee/price/proof figures applies to ILMERA's
business pricing and proof, not the already sourced destination cost facts
or the mandatory conditional Italy owner sentence. Those must remain intact.
Legacy no-charge service-price claims and default refund terms are not
supported by the final owner answers and are scheduled for replacement with
an explicit unpublished-terms statement. No new amounts or refund conditions
will be inferred. Official work/stay facts remain facts, but do not imply
that ILMERA offers work/stay advice. Remaining old operational service claims
beyond the final owner scope are scheduled for removal or narrowing.

The approved founder biography will be added to the existing profile and
Person description without inventing a public evidence URL or filling any
unprovided proof slot. Other team roles are not newly assigned from the
founder's responsibilities. No lender recommendation, account-opening,
appointment-booking, appeal or outcome commitment is inferred. Final source,
owner, backup-first direct-live and actual delivery blockers remain open.


## Phase 22 final handoff, 2026-10-22

Service assistance, the existing founder biography/responsibility and a
transparent disclosure policy are now owner-confirmed and published within
the bounded scope. They do not prove a threshold, processing time, award,
recognition/safety outcome, lender decision, individual partner agreement,
payment receipt/nonreceipt, review or registration identifier. Twenty new
FAQ pairs and updates do not close the official-fact gaps: 6 answered,
15 partial and 29 gaps remain in the 50-prompt map.

The old general consular-city example is retained under the no-country-fact-
change constraint with an immediate individual-case verification caution.
It is not current routing evidence, a booking service or a single-trip
promise. No new official policy was researched or asserted in this phase.
The mandatory conditional Italy statement remains owner-attributed, not
proof of an award amount or partner agreement.

Owner-only missing inputs: detailed fee/inclusion/payment/refund table;
actual one-sentence partner-payment disclosure; exact testimonial/name/
permission evidence; registration label/identifier/record; any further
publishable team responsibilities. All proof slots are still empty. No
placement estimate is allowed. The approved basic founder description does
not fabricate a proof URL or populate a proof record. Prohibited price,
Offer, Review, rating and LocalBusiness schema remain absent.

Existing source/status/proof gates remain active. The canonical entity scope
exception is limited to the approved description/list; other identity fields
and protected bytes remain unchanged. LLM exceptions strip only exact
approved business sentences; appended held rules and every held URL remain
rejected. Earlier implementation capabilities do not override this policy.

Local checks pass, not live acceptance. Native Apache redirects/headers,
external raw HTTP, contact delivery, actual performance/ranking, complete
live backup and all-file/settings restore readiness remain unverified here.
No direct upload, main push, merge or deployment occurred. Retain all prior
applicable blockers and require backup-first approval before any live work.

## Phase 23 conservative decisions, 2026-10-22

Final owner facts A-F supersede Phase 22's policy-only payments and earlier
feedback statements, without rewriting their historical blockers. Student
charges and actual partner payments are now publishable; no inclusions,
payment schedule, refund terms, routing, results or registration is inferred.
The fee proof slot remains empty. Fee range goes only in visible HTML and
FAQ answers, including matching FAQPage/explicit LLM Q/A text, never metadata,
Organization/Person/Service descriptions or price/Offer properties.

All three current About photos/bios are owner-confirmed real and verified.
Preserve original assets and bio HTML. Fawaz's existing photo is 1,541,656
bytes, over 300 KB: report it rather than silently replacing/recompressing an
explicitly protected real photo. Person-specific filenames and viewed
portraits show no obvious placeholder issue. CSS avatar classes are not
placeholder filenames. No new portrait, credential or profile URL is added.
Existing Fawaz bio claims are inventoried for PR re-confirmation; no current
bio requires an institutional-name exemption. Both Udyam values remain absent:
publish no business-registration line, number or identifier. Country authority
registration notices are separate, unchanged destination evidence.

### Phase 23 consistency clarification

Canonical Organization payment copy contains no numeric range. The exact
approved range is in visible disclosure paragraphs and FAQ answers, including
explicit Q/A lines in both generated LLM files. No price properties, Offer
or per-service terms are added. Existing assistance/service lists describe
general guidance, not contractual tasks included in the charge. Source map
counts stay conservative: no-feedback status is not performance evidence,
and actual ILMERA payments do not establish competitor motives.

Both LLM team sections now reuse the existing owner-verified card biographies
and real image URLs, without editing any biography. The old combined legal/
brand label is now brand only: a registered business name was not supplied.
No registration or legal-name inference is made. Existing group/destination
facts and all original proof/source/status gates remain unchanged.

### Phase 23 media-format exception

The protected Fawaz portrait `assets/images/fawazbh.webp` contains PNG data
under its existing extension, 1254 x 1254 and 1,541,656 bytes. This is not a
placeholder photo. All browser photo cases loaded it, but that does not prove
native live headers/MIME acceptance. Preserve its name/bytes as explicitly
required; no silent re-encode, rename or server-setting change. Future media
optimisation/MIME review is separate authorized work. Required checks pass;
no claim that every asset is under the file-size budget or optimised.


## Phase 23 final handoff, 2026-10-22

Final owner A-F replace old policy-only/unknown-payment and feedback statements,
not historical source/live blockers. Actual student-charge range and some
partner-university receipts are now disclosed, without naming a university,
claiming price competitiveness or inventing fee routing. Range appears only
in visible/FAQ text, including explicit LLM Q/A. No price properties or Offer
schema; fee proof and all other proof slots stay empty. General service scope
is not a contractual list of fee inclusions. Written terms must be requested
before paying; inclusions, schedule and refund conditions are still absent.

All three existing team photos/bios/titles are owner-confirmed real and
verified, not placeholders. Original bytes and bio variants remain exact;
full title labels/alt and existing canonical Persons are aligned. No new
biography, credential, profile URL, founder or institutional-name exception.
The PR lists existing bio claims for re-confirmation. Fawaz's size/format
exception is preserved and reported; no silent asset or MIME change.

Neither Udyam number nor business name is supplied. Publish nothing about
ILMERA business registration, no partial label, identifier or missing-value
placeholder. No current student feedback exists; future publication needs
written permission, verified video and existing authenticity/source approval.
No rating, review schema, placement estimate, student count, award or result.

All required local checks pass, not live deployment clearance. Native Apache,
public raw HTTP, real enquiry delivery, complete live backup/restore readiness
and live asset MIME acceptance remain unverified. No main push, merge or
deployment. Preserve earlier official-rule/source blockers and the complete
backup-first direct-live/all-file-settings restore workflow. Only the owner
can supply the remaining actual policy details, both registration values and
future genuine feedback evidence; no missing team photo or bio is requested.

## Phase 24 conservative decisions, 2026-10-22

Only the two owner-transcribed registration values and mandated caveat are
public. No certificate file is present with this request/workspace. Its private
address cannot be inspected or compared, so no mismatch is asserted. Existing
Contact locality is unchanged; PR #1 will state the unavailable comparison.

Private provenance is the exact owner-supplied certificate source statement,
not a fabricated HTTPS URL. Registration-specific approval accepts only the
exact authorized record; other proof validation remains unchanged. No review
date, source text or private certificate field is rendered with registration.
Existing website audit dates, contact details and country facts are not
certificate data and remain unchanged. Privacy verification must distinguish
new registration payload from pre-existing public contact/audit information;
unknown certificate-private values cannot be independently compared here.

### Phase 24 Task 2 biography boundary

No optional Zaheer background was supplied. His replacement uses only the
approved CFO and company-finance-function facts, identically in active pages,
Person data and both generated LLM documents. No student payment, loan or
advisory duty is inferred. Jabir/Fawaz biography variants remain exact.
Historical audit inventories and negative-test strings retain the old text as
evidence, not as active biographies. Owner-only reports/test tools will receive
directory access restrictions with the owner-input report task. An unchanged
general About sentence about asking who is responsible for written tasks is
not Zaheer's placeholder and has not been removed.

### Phase 24 Task 3 portrait scope

The genuine WebP derivatives are 384 square (19,056 bytes) and 192 square
(7,892 bytes), quality 82, whole-square resizing only. The 1,541,656-byte
original PNG under its existing WebP filename is untouched. About/Home team
src/srcset and canonical Person/generated LLM photo URLs use the derivatives.
Existing blog author portraits keep the original asset, as they are outside
the requested team-image replacement. Their original full alt labels remain
through an explicit original-asset alias; no biography/title/alt is changed.
No og:image uses that original portrait in any of the 43 rendered routes, so
there is no such social-image reference to replace. All social metadata stays
unchanged. Local byte/format/load checks do not establish native live MIME.

### Phase 24 Task 4 private owner follow-ups

The owner-input report no longer requests registration values. It records
the owner's private activity-description concern for CA/Udyam portal follow-up,
without a numeric activity code or any certificate file. Optional Zaheer
background, currentness/accuracy confirmation for the existing Fawaz
certifications/diploma, fee inclusions/schedule/refund terms and future genuine
feedback remain owner matters. Existing biography claims are not re-verified
or expanded by this report.

Reports and test tools are internal artifacts, not public website copy.
Directory-specific Apache deny rules protect these folders without changing
the root rewrite file, any published/held page status, discovery or content.
The Phase 24 local adapter mirrors the report denial to avoid serving internal
owner notes. Local 403 checks do not prove native Apache access control;
verify it after authorized live preparation, with backup/restore ready.
Historical audit inventories and their previous bio strings remain intact,
not active public biographies. No certificate address comparison is possible
without the actual private certificate; no address is changed or mismatch
invented. No new physical contact location is implied.

### Phase 24 final release boundaries, 2026-10-22

All executable local checks passed in the first bounded verification cycle;
cycles 2/3 were not needed. This does not erase earlier blockers. The actual
certificate file is unavailable, so private-address comparison and independent
cross-checking against unknown certificate-private values are not completed.
The implementation instead enforces the exact approved public projection,
rejects extra fields/files and preserves existing contact/address data. No
match/mismatch is claimed and no certificate file is published.

Live release is NOT CLEARED: complete backup, all-file/settings restore
readiness, native Apache rewrite/access-control validation, direct public
HTTP/MIME and actual contact-delivery checks remain unverified. No deployment
or enquiry submission occurred. Existing Fawaz credential claims still need
owner currentness/accuracy confirmation. The private activity correction,
optional Zaheer background, written fee inclusions/schedule/refund terms and
future genuine feedback with written permission/verified video remain owner
follow-ups. No additional background, policy term, result, office or financial
service is inferred. Historical source/status/destination blockers remain.

## Phase 24b conservative decisions, 2026-10-23

The owner now explicitly approves both replacement bios, superseding the
Phase 24 minimal Zaheer bio and Fawaz preservation instruction. Opened the
portfolio homepage and About page, both complete across two returned chunks.
Ahrefs/Semrush certifications, the named digital-marketing diploma and the
early-2025 SEO start all match the requested Fawaz wording. The portfolio
links to the approved LinkedIn URL. These are owner/first-party statements,
not independent issuer verification. No requested detail requires reduction.
Other external role/outcome/service/contact claims were not imported; approved
ILMERA role labels and Jabir-only founder attribution remain authoritative.

Adrex Media School is allowed only within the two exact approved bios and
matching Person/FAQ/LLM descriptions. It is a training institute, not a
university. Do not remove or broaden the university blocklist. Historical
audit inventories and negative-test strings remain evidence, not active bios.
No certificate private fields, source gates or held-route statuses change.

### Phase 24b Task 2 publication-integrity maintenance

The portrait-src preflight correctly detected that four existing reviewed
article byte checksums no longer matched after the requested image change.
Only those four `file_sha256` strings were refreshed for the exact verified
portrait-src-only transformation. No verified flag, failed gate, source,
claim, metadata, date, status, summary or provenance field changed. The current
checker allows only these exact checksum replacements and independently
requires the matching article bytes. Generic publication/hash checks stay
active; this is not new source approval. Both held articles remain held.

### Phase 24b Task 3 exposure and deployment decision

Audit assumes repository root is the live web root and lists every current
non-page file, including local caches, plus folders and exact owner GET URLs.
Git internals are protected as an excluded namespace, without reading private
credential files. The previous local adapter denied several internal paths
without corresponding native rules; its 403s were not native hosting evidence.

Add folder denies for includes/data and for internal destination/place arrays;
keep existing report/tool denies. No browser-fetched data file was found.
Append root denies for requested note/script/log/backup/phase-JSON patterns,
plus private CSV exports, dotfiles and accidental Git requests. Existing
rewrite bytes stay an exact prefix, not a rewritten rule. Apache 2.4/LiteSpeed
syntax is used; native enforcement cannot be tested by the local WASM adapter.
Local policy-mirror probes and all positive resource tests are separate from
that unverified native requirement. Exact live URLs/results are in the audit.

Owner deployment decision: internal folders, notes, tooling, reports, caches,
audit exports and Git metadata should not be uploaded into live hosting at
all. Required PHP runtime data/includes/destination/place files cannot simply
be omitted under current relative paths. Approve a non-public runtime layout
and tested path configuration before excluding or relocating those required
runtime files. This phase does not relocate them or deploy. Current web-root
denies are defense in depth, not a substitute for that deployment decision.
Complete backup/all-file-settings restore and actual native live probes remain
prerequisites; no published/held status or factual destination data changes.

### Phase 24b final superseding facts and release limits, 2026-10-23

Both final bios are owner-confirmed and used verbatim. Fawaz's requested
certifications/diploma/early-2025 start also match the complete opened portfolio
home/About pages. Earlier requests for those exact biography/currentness facts
are resolved, not missing inputs. No issuer authentication is claimed; no
unrequested external role, ranking, client, contact or outcome claim was copied.
Jabir's bio/photo/title/alt remains exact. Approved sameAs is Fawaz Person only.

All rendered original portrait uses are removed, with no exception. The
original and both derivatives remain byte-identical. Only exact portrait src
and four necessary article checksums change, not any publication/source gate
or policy/factual field. Historical text/test strings stay internal evidence.

The first bounded cycle passed, early stop; cycle 2 was not needed. This does
not clear native hosting, deployment layout, complete backup/restore or actual
contact delivery. The adapter does not execute .htaccess. Exact live GET URLs
must return 403/404 without contents/listing, while all positive public controls
must stay 200. Current runtime folders cannot be omitted without an approved
non-public path layout. Do not upload internal artifacts/notes/caches/metadata
into hosting. No relocation, deployment or contact submission is performed.
Earlier certificate-private comparison and official-source/held/live limits
remain untouched. Fee terms, private activity correction and future genuine
feedback still need their separate owner evidence; no values are inferred.

## Phase 25 Stage 1 audit decisions (23 October 2026)

- Actual immutable references are not uniformly light: their default heroes are dark, Home/Services have multiple dark bands and some existing glow, grain, pills, glass and hover decoration. Preserve reference output, do not silently redesign it. Pilot long-form areas will use existing light reference surfaces; the new system will not copy those decorative embellishments. Stage 1 remains limited to four named pilot routes and six team-card paragraphs.
- Exact owner card counts include punctuation/spaces: Jabir 127, Zaheer 130, Fawaz 126, spread 4 (<=6). No conflict or wording adjustment is needed. Full canonical bios, About FAQs and both LLM descriptions remain mandatory outside cards. No separate longer team section exists beyond the About biography FAQs; preserve those answers rather than invent a new biography.
- Baseline screenshots and performance are local only. Outbound font/CDN hosts cannot be accessed here; the harness mirrors the exact Three/GSAP versions and same font families/weights from npm. Lighthouse transfer accounting is synthetic/local, not actual CDN compression or field data. Existing native hosting, deny enforcement, nonpublic layout, backup/restore and contact delivery blockers are unchanged.

- Phase 25 task 2: pilot fonts use local OFL variable files for the existing two reference families; optional display avoids late swaps. No new blocking font stylesheet is introduced, and reference font requests are unchanged. New component radii are 3px/12px only; existing immutable reference team radii/circular portraits are not restyled. Navigation/footer pilot hit areas may be enlarged for the required accessibility minimum while retaining their existing text/palette/grid.

- Phase 25 task 3 correction: About's Jabir card contains a second duplicate role paragraph. Treat both card biography paragraphs as the authorized replacement context, leaving exactly the new supplied card bio and removing the old duplicate. Keep the existing Jabir FAQ role answer, all canonical Person descriptions and both LLM files unchanged. Fawaz/Zaheer full FAQ bios remain required. Equal-height team-only grids can change team block height and naturally move later sections; no later-section styles/content are changed. Reference visual parity will compare unchanged sections with alignment rather than falsely claiming absolute full-page raster equality across a height-changing team edit.

- Phase 25 task 4: text-free stills were captured from the actual Home scene, so no generated-scene/stock-image substitution was needed. Use static decorative canvas rather than an img/CSS background candidate to meet the explicit text/container LCP constraint. No parallax or animation loop is introduced. Default scene ON preserves reference output; the explicit global OFF constant intentionally disables reference Three loading/visible overlays as authorized. Legal/404 and other routes remain unstyled/unopted-in until Stage 2.

- Phase 25 task 5 resolves team reflow at the required360/768/1280 comparison sizes: team-only footprint minima preserve identical section bounds; Home768 uses79.5px section bottom padding to absorb the30.5px equal-row expansion. Card layout widths/photos/crops/names/titles/grid gaps remain unchanged. These measured responsive rules do not assert pixel equality at unmeasured viewport widths.
- Pilot-only accessibility adjustments enlarge nav/footer/link hit boxes and keep the fixed nav dark over light reading areas. Thus pilot chrome retains reference typography/palette/content/grid, but is not falsely claimed to be a pixel clone of smaller reference hit areas. Immutable reference pages retain their actual header/footer output.
- Screenshot self-review required harness corrections: complete custom reveal classes, and prevent SwiftShader full-page repeated tiles by stitching actual viewports. Final before images replay the immutable pre-edit HTML and original assets with the same corrected harness as after images. Original baseline performance samples remain unchanged; this is not a performance rebaseline.

- Phase 25 task 5 resolves optional-font fallback: Chromium platform-font inspection (not just document.fonts.ready) now requires actual custom reference glyphs on every pilot case. Original optional mode could keep system fallback despite loaded status. Same-family licensed subsets are embedded in existing inline CSS, with no font-swap network dependency/new blocking resource. Cormorant uses its original700 heading/brand instance; Outfit retains variable weights. Final screenshots and performance gates use the corrected fonts.
- Reference screenshot precision: default fresh GPU contexts showed low-bit colour rounding differences on even unchanged source. Calibrated deterministic software compositing/sRGB/capture-only WebGL dither-off; retain ZERO pixel tolerance and re-shoot both original baseline and current pages. These are capture-only flags, not website changes or altered performance conditions.

- Phase 25 task 5 unresolved strict raster gate:11/12 reference pairs are exact outside authorized team masks. Home1280 has9 one-level anti-aliased existing nav-CTA corner pixels remaining after software/sRGB/dither/no-motion calibration. Keep ZERO tolerance and retain the failing comparison; do not claim full pixel clearance or rollout readiness. Source/render invariants and all reference section footprints are exact outside the explicit card/team exception. Owner review is required at the Stage1 gate.

- Phase25 task6 conservative final fallback: all four pilots use the existing reference-palette gradient, not stills, after fixed-budget failures. Same-family subsets remain inline; atomic first-text paint waits for the two inline faces with3s/error failsafe, JS-off never hidden. No new font HTTP dependency. All failed candidates retained.
- Phase25 measurement fairness correction: after-runs now use the exact same reference-prefix/seven-route order as the original baseline and reset storage each navigation. Baseline numbers/budgets unchanged; browser process is reused, not cold per sample. Matched-order pilot medians pass; reference controls show substantial local variance. Not field or native-hosting data.
- Phase25 palette verification correction: normalize existing literal reference RGB bases to equivalent hex, including rgba(13,27,62,.97) ->#0d1b3e. No invented RGB or tolerance relaxation; application CSS unchanged by the checker fix.
- Phase25 Stage1 remains NOT CLEARED because the strict Home1280 raster has9 one-level existing CTA-corner pixels outside team. Owner review required; no Stage2, merge or deployment authorized.

- Phase25 Stage2 owner decisions A-F (2026-10-23) supersede Stage1 rollout hold/zero-tolerance/chrome/font choices. References remain excluded. Home is the canonical chrome spacing model because reference page container gutters themselves differ on mobile. Stacked footer links cannot reach44px without overlapping hit regions or changing reference spacing; preserve reference design and report the decisionD exception.
- Stage2 baseline calibration: unchanged About1280 reproduces9 one-level CTA-corner pixels at Stage1 Home coordinates, within ruleC. Home never receives the shared stylesheet; classify that bounded9-pixel case as rendering AA noise, not shared-CSS styling. Larger About self-noise is separately retained and NOT accepted under ruleC.
- Stage2 404 conflict: its baseline footer contains only copyright/legal links. Adding the full reference footer would add words/links/image content, contrary to the stronger preservation requirement. Keep its contents, align available structure/styles, and report the literal markup deviation. Held pages also retain original image timing attributes unless explicit alignment is necessary; no image pixels/URLs/alt/crop change.

- Stage2 groupD reference-header alignment: five previously unprocessed routes now receive loading=eager on the existing first header logo, matching reference markup. This is the only image timing-attribute exception; image content bytes/URLs/alt/dimensions/style remain exact.404 footer uses reference bottom-row structure but cannot equal the full footer without forbidden added copy/links/image. This remains an explicit literal-markup deviation, not a claimed match.

- Stage2 bounded verification: protected post metadata and held article source hashes remain exact; visual startup moved to link integration. Rebuilt AA42cases=0 violations; immutable references retain24 contrast-failing cases and5 motion-on transient overflow samples. Reference source/palette are not redesigned to hide these existing findings. About360 final raster exceeds decisionC (501067pixels, max3); unchanged-source calibration also exceeded rule. No waiver or local all-green release claim.404 shortened footer and stacked reference-pitch targets remain declared exceptions.

- Stage2 performance candidate1: Germany LCP2430.752ms fails1751.207ms cap. Destination template alone now uses plain reference-navy hero and authorized inline-font fallback; other rebuilt templates retain gradient/selfhost. Remeasurement pending. Unchanged Contact control also fails LCP/CLS; reference hero cannot be altered without violating decisionB. Raw failure retained; budgets unchanged.

- Stage2 performance final: all7 rebuilt samples pass every fixed budget after destination-only plain/inline fallback (Germany1181.228ms/CLS0/TBT3ms/200010bytes). Services unchanged control fails LCP8941.540ms versus2315.607ms cap; overall performance FAIL. Contact failed initial then passes final, demonstrating local variance, not an accepted waiver or a source-driven speed claim. Original references untouched under decisionB. Raw candidates retained; no extra unchanged-reference retry.

- Stage2 final bounded cycle3: six destination fallback AA cases PASS; fresh43 semantic/source/font-tier and original protected-data/publication/discovery/SEO guards PASS. Exact chrome has one approximately0.016px Germany1280 nav auto-margin drift after authorized inline fallback, plus the known shortened404 footer. These remain explicit exactness failures, not rounded away. Three-cycle limit reached; no more retries.
- Stage2 final release record is NOT READY. Seven live font/cache URLs are future verification targets, not live deployment claims. Local adapter returns200/font/woff2 only; no native cache headers.16 review images are internal GitHub evidence, not website assets or upload material. All previous blockers preserved.


## Phase25c Task2: performance certification remains blocked (2026-10-23)

All three permitted fresh-process interleaved A/B sessions failed unchanged-reference median reliability. Reference A/B HTML hashes are identical. First session Home and partial Services data, all four second-session controls, and all fourteen final-session routes are retained in reports/phase-25c-task2-ab.json. No fourth session, baseline relabelling, budget relaxation or field/live claim. Numerical rebuilt-route passes cannot certify an unreliable session. Performance release gate remains FAIL pending separately authorized reliable evidence. Native-host/delivery/layout/backup/restore and earlier business/source/proof blockers remain untouched.


## Phase25c Task3: uniform tiers, unproven fallback necessity (2026-10-23)

All9 destination members retain plain navy/inline matching fonts; all17 places and all8 articles retain gradient/selfhost matching fonts, including held members. Fresh7A/7B diagnostics identify P.direct-answer, Outfit16px300 as the dominant LCP across Germany/Italy/GCC/Mysuru/Bengaluru. No unique German markup fault proved. Shared all-document-font-set gate is a plausible cost centre but changing it without reliable CLS/LCP controls is not validated. New controls remain unreliable, so the original Stage2 fallback necessity claim is not re-certified. Choosing article raw LCP also exceeds1.10 baseline in the final session; preserve this failure despite unreliable controls. No page-specific exception or source/content edit.


## Phase25c Task5: reference-only accessibility report (2026-10-23)

All24 historical contrast groups/387 affected node instances retain selector, measured foreground/background/ratio and minimal existing-palette suggestion in reports/phase-25-reference-a11y.md. No suggestion applied. Five JS-on layout-overflow cases exactly reproduced: Home360/768 hidden team-card reveal translateX60 creates40px excess, About360/768 hidden stats-block translateX55 creates33px excess, Contact360 hidden contact-info translateX60 creates36px excess. Effective opacity0 and horizontal-wheel scrollX0 observed; numerical document overflow persists while these below-fold reveal start states are hidden. This is not pixel/compositor noise and not claimed fixed. Reference source remains immutable, as required; report-only accepted constraint, not blanket user-visible clipping proof.


## Phase25c final sign-off: NOT READY (2026-10-23)

Task1 now passes12/12 under the authorized structural/noise gate; Task4 passes120/120 with max0.016px tolerated strictly below0.1px. These replace the old pixel-only/exact-subpixel acceptance failures, not historical evidence. No reference or other public runtime source changed. One permitted final full QA cycle completed; no second cycle or fourth performance session pursued.

Performance remains FAIL/uncertified after all3 reliability sessions; Choosing article raw LCP2.2117x, Services raw LCP/TBT and Contact/About raw TBT failures retained. No reliable necessity proof or validated new font-gate/template repair claimed. Whole-template9 destination/17 place/8 article policies are uniform, including held pages.

Fresh final reference axe retains24 groups/all387 original affected nodes plus4 additional sampled nodes (Services1280 highlight title; About1280 section label, team label and FAQ heading), all documented with4.5 target/palette-only suggestions,391 total retained nodes. No fixes applied. Same5 reference numerical overflow cases persist; Contact360 final sample395px vs dedicated probe396px is frame-dependent, not resolution. Hidden reveal transforms/body clipping/wheel scrollX0 observed, not a blanket all-frame no-clipping claim.

Accepted/retained limitations:404 short footer; canonical Home20px mobile gutter while references keep22/24px; legacy stacked footer/contact target pitch below44px; prior5 first-logo eager timing attributes only; JSoff axe serialized instrumentation method; external-aborted functional browser/finite-animation geometry method;14 HTTP-font-failure conditions (inline destination has no font HTTP dependency, no decode/CSP failure proof); no separate404 performance navigation; local simulated equal-delivery/npm-mirror data only.

No native Apache/LiteSpeed rewrite/404/ACL/cache/MIME/CSP/private-runtime-layout/contact-delivery or full backup/restore proof; actual certificate unavailable; all earlier registration/fees/payment/refund/reviews/scope/source/held-publication blockers preserved. Tools/reports/Git/caches/test fixtures are not upload material. No sensitive certificate/private contact/address/NIC values exposed, no main push/merge/deploy/account/submission/outreach.

## Phase26 session branch restriction (2026-10-24)

Owner requested release/content-phase-24b from164d6de and a separate content PR. This session can create/commit/push only its fixed arena/48320ee5-ilmerastudyabroad branch. No release branch or substitute PR will be fabricated. Candidate preparation/testing is isolated outside Git; production files on arena stay unchanged. Reports and reproducible patch/payload evidence are checkpointed on the only authorized branch. PR1 metadata/comments/state are not modified; pushes to its source branch necessarily update its diff. A separately authorized session is required to create the content branch/PR. No main push, merge or deployment. All prior native/proof/backup/business blockers retained.


## Phase26 candidate verification scope (2026-10-24)

Isolated164d6de plus narrow six-file team/policy patch passes the original Phase24b full stage5 runner/browser (fresh43 routes,38 published,38 sitemap URLs), with exact card-only expectation updates. This is not a release-branch commit or native/live-host verification. Services/Contact source unchanged; Home/About only short cards and one grid-auto-rows rule each. Shorter/equalized team sections change their height and downstream positions; relative outside-team geometry/styles match, not claimed full-page pixel or absolute-footer equality. No extra footprint/design styling imported. Full bios/schema/FAQ/LLMs preserved. Original lab/design blockers remain separate from this content candidate.


## Phase26 payload exclusion correction (2026-10-24)

A blanket phase14-*.json/internal-JSON omission would break publication/runtime gates. Exact mandatory exceptions: phase14-source-review.json, phase14-location-review.json, phase14-article-review.json and data/answer-map.json, entity.json, payment-disclosure.json, seo-map.json, service-scope.json, team.json. Root/folder deny rules must prevent HTTP disclosure while PHP retains disk access. Protected runtime folders data/includes/destinations/places plus their deny files are mandatory. reports/tools/Markdown/CSV/Git/caches/fixtures remain excluded.117-file isolated payload matches all43 source renders,38 published,38 sitemap URLs and12 first-party asset byte streams. Existing CDN fonts/scripts/contact service remain external dependencies, not proved by the local adapter. No Apache/live delivery or deployment claim.


## Phase26 rollback privacy decision (2026-10-24)

An overwrite-only Phase13 restore plus removal of the new deny files could expose new review JSON/runtime files left on disk. Checklist therefore requires restoring the exact backup file set, removing newly uploaded files absent from that backup while the site is offline, then restoring old root/subfolder rules and removing only newly added deny files. Do not remove protection while new internal inputs remain. Existing child .htaccess versions must be restored rather than deleted. Owner must prove backup/restore and native denies/contact delivery; no submission performed here.


## Phase26 final content/design handoff (2026-10-24)

Content candidate is verified but NOT a pushed release branch: release/content-phase-24b was not created and no separate PR/content commit exists. Do not treat arena checkpoint hashes as content-release hashes, or deploy/cherry-pick its design ancestry. Start an authorized release checkout at164d6de, apply only the narrow team patch and content documentation, rerun and record the actual commit/PR. Original arena public/design files unchanged; PR1 metadata/comments/state not touched though source docs/tooling diff changes.

Later design release remains separate: all3 lab control sessions unreliable; owner to measure stable live content baseline and then design with PageSpeed Insights. Choosing-consultant article raw LCP regression and destination plain/inline versus other-template gradient/selfhost choice remain unvalidated. Reference24 contrast groups (391 retained node instances)/5 reveal-layout overflow cases are report-only;7 font/cache URLs are future design tests, not content payload. No new performance retry, source/design edit, field claim or deployment. All native Apache/LiteSpeed/ACL/rewrite/404/MIME/cache/CSP/private-layout/contact/backup/restore/certificate/fee/refund/review/scope/source blockers remain open.


## Phase26b owner finance-only correction (2026-10-24)

Remote fetch confirms release/content-phase-24b is absent. Fix arena only; no alternate branch or PR created. Owner final text supersedes all earlier Zaheer biography approvals, including frozen Phase26 patch/archive instructions. Historical append-only records/tools remain evidence, not approved active copy: never regenerate/deploy an old candidate without applying this correction and re-verifying. Keep Fawaz diploma and narrow Fawaz-only institution context. No other content/design/status/schema property or image changes authorized.


Phase26b conservative retention: old Phase26 patch, manifest, ZIP and external candidate predate the final decision and are NOT current deployable artifacts. The old8083 preview was stopped; only the corrected design-branch preview remains. No content branch exists, so no new content payload is built or represented as verified. Historical place CSV import drafts and older policy/check fixtures are not active website copy and stay immutable; never use them to restore an old bio. Team review-date/basis fields are kept unchanged because only Zaheer biography text is authorized; this dated owner decision is recorded here instead.


Phase26b final verification:35 core groups PASS580.09s,43 previous-commit HTML comparisons exact after only approved Zaheer substitutions,38 published/sitemap URLs,14 policy regressions and258 browser cases.66 extra accessibility cases have0 rebuilt violations. Fresh reference audit sampled24 groups/390 node observations and5 overflows; historical391 observations remain intact, no source repair or finding removal claimed. Initial axe dependency failure retained, full fresh rerun after external install. PR1 checkpoint explicitly authorized in Phase26b is posted; prior Phase26 no-comment statements remain accurate historical records, not current restrictions. No content branch/payload rebuild, new performance lab, main push, merge, deployment or actual contact submission.


## Phase27 combined current-branch deployment pack (2026-10-24)

Owner now plans a single combined content/design release of current arena branch over Phase13, with live PSI before/after and backup rollback. This supersedes the Phase26 split-branch packaging workflow, not historical performance/native/business/proof/source findings. No deployment performed or readiness decided here. Runtime pinned to a3d696f; Phase27 modifies no public file.

Payload130 files, source exclusions394 at a3d696f, plus all later Phase27 artifacts. Retain9 protected runtime JSON inputs; blanket phase/internal JSON/folder omissions break gates. Include all8 tracked .htaccess files, including reports/.htaccess and tools/.htaccess as deny-only exceptions with no other contents. Include2 variable faces read by PHP,7 static faces, CSS/visual helpers and OFL licences. Unreferenced stills/original portrait/alternate logos excluded. Clean VM has no host source mount; all43 outputs exactly match repo. CDN/contact and native access/cache/CSP/MIME/rewrite/backup remain owner checks.

Raw browser/source Find for free also matches7 held APS URL identifiers and2 existing freely substrings. Full-word policy remains unchanged; do not edit/rename these under this no-public-change phase. Report all hits and distinguish identifiers/ordinary substring matches from prohibited fee claims. Rollback must disable public access and restore exact backup/remove new private files before dropping denies; restoring old root rules alone can expose new runtime inputs.


Phase27 PSI baseline limit: the choosing-consultant guide was introduced in Phase19 (ebe71c4) and is absent from origin/main/Phase13 tree. Owner still records all5 requested live URLs, but if this URL is missing, mark status/no baseline; do not compare404 performance or invent/substitute a baseline. Its relative LCP/score acceptance stays unverified until an explicit owner decision; post-release absolute measurements remain possible. No live request or metric was fabricated.


Phase27 final evidence boundaries: all35 functional groups PASS556.78s, but fresh immutable-reference audit has426 node observations in24 groups,41 case-selector observations outside the retained391; all fresh selectors retained and no historical node pruned, cause/fix not claimed. Same5 overflow cases remain. Final130 uploads/417 tracked exclusions at547-file Phase27 set; source394 exclusions plus23 new internal files. No fourth performance session, actual native/CDN/contact/PSI/backup/Console proof or readiness verdict. Owner acceptance remains their decision, with missing choosing-guide baseline explicitly unverified. All public runtime files/config/assets/line endings remain a3d696f bytes.

## Phase28 artifact availability, not owner acceptance (2026-10-24)

- Download availability is resolved: releases/ilmera-deploy-850d0af.zip is committed and its GitHub Contents API raw binary matches681792 bytes/SHA256. Direct raw.githubusercontent.com URL comes from GitHub metadata; this sandbox host allowlist does not permit fetching that host directly.
- Prior blockers are not rewritten or waived. Native Apache/LiteSpeed ACL/AllowOverride/rewrite/ErrorDocument/cache/MIME/CSP, actual contact delivery, backup restoration, private URL smoke checks, owner PSI/baseline decisions, source/business/certificate gaps and held Russia/Czech/APS/DSU remain as recorded. No deployment, Console submission or performance lab retry.
- Fresh functional observations are not a repair claim:24 reference contrast groups,518 reference nodes and4 overflow cases this run. Phase27 fresh426 nodes/5 overflows and earlier historical391-node inventory remain byte-identical and unresolved. No pruning, inferred source cause or declaration that the historical fifth overflow was fixed.
- The releases/ deny rule is additional repository safety and is not in the130-file upload ZIP. Never publish the whole checkout or upload the ZIP/releases directory. Owner still verifies actual native hosting behavior.

## Phase29 live-design incident, owner confirmation still required (2026-10-26)

- Owner reports a deployed current-content Germany page with old visual behavior. This does not prove all130 host files match the ZIP. No actual live screenshot, Hostinger filesystem/log/header access, cache operation or native Apache/LiteSpeed test was available to this agent.
- Strongest local reproduction is explicitly combined: disk assets absent plus missing includes/header.php. Missing assets alone still leaves header text/hamburger and matches only four of five symptoms. No pixel-exact owner screenshot or confirmed live root-cause claim. Disk read/permission failure is distinct from an HTTP403/404; Germany embeds CSS and two fonts server-side.
- Owner must verify exact asset/header paths and readability, compare host hashes to the unchanged130-entry manifest, inspect PHP errors, purge Hostinger/CDN HTML cache and check a private-window render. If URLs succeed but emitted CSS/data fonts are empty/stale, investigate PHP paths/cache rather than remove private-directory HTTP denies. Any host-only CSP/MIME/ACL/rewrite rule remains unverified. No speculative fix applied.
- Missing visual-system/config and PHP7.4 are fatal500 in tests, not a silent styling-only fallback. PHP8.0/8.1/8.5 success is local functional evidence only, not endorsement of obsolete versions or native readiness.
-23 published payload pages repeat the first answer after its CTA. Report-only proposal must preserve citation links and publication/word-count/source checks; no page was edited. Existing performance failures, exhausted three-session budget, all historical reference observations, privacy/business/source/certificate, native hosting/contact/backup and held Russia/Czech/APS/DSU blockers remain unchanged and unresolved.

## Phase30 duplicate-fix conservative decisions (2026-10-26)

- The actual23-page audit has six destination introductions carrying source citation links and17 place introductions without citation markers. Keep every existing citation and invent none. The original introduction content is retained in the direct-answer slot, with its CTA after; only the uncited repeated copy is removed. Citation position necessarily moves with the kept copy; link attributes and multiplicity are preserved. Answers remain40-60 words without rewording.
- No CSS/font/image/visual-system/config source is edited. Existing live design/native/performance/source/privacy/contact/backup blockers remain unresolved. Full functional checks are not a native-host or deployment acceptance.

## Phase30 temporary self-check conservative decisions (2026-10-26)

- Valid through2026-11-15 UTC, fail closed from2026-11-16 00:00:00 UTC. Key is256 random bits. Fixed relative allowlist only; no user file/path input. The131st temporary checker is existence-only to avoid a circular self-hash; offline manifest/ZIP verifies its actual SHA256. All8 .htaccess files are existence-only and never opened or hashed. Critical runtime assets/includes/data records are detailed; other payload members are existence-only.
- Key is in the PHP constant and the requested owner report. Task4 explicitly requires its working URL in the owner checklist/PDF too, so those requested documentation copies are the only additional key copies; no test/config/manifest fixture stores the key. A publicly accessible Git repository cannot make this source key a durable secret. This checker reveals fixed payload-relative names, metadata and hash match status only, never content or server paths. Delete after one use, even before expiry.
- Existing root rewrites may301 a direct .php request before PHP to its extensionless form with query retained. The PHP handler/final wrong-key response is plain404. Root .htaccess is not changed to force native first-hop404 because only duplicate-fix source and deploy-check.php are authorized. Native first-hop response/header behavior remains unverified; local deny tests test PHP, not Apache. No exemption is added to robots.txt or sitemap/LLM/internal links; noindex headers/meta protect the temporary result.

## Phase30 export and verification scope decisions (2026-10-26)

- Keep all8 mandatory upload .htaccess files. This necessarily includes reports/.htaccess and tools/.htaccess in otherwise empty directories; interpret no reports/tools as no contents except these mandated deny files. Entire releases/ remains excluded, including its additional safety policy and both archives. New pack is131 files temporarily,130 after checker deletion.
- Runtime source is committedf54e4cc; later documentation/release commits do not falsely become a different runtime build. Every original runtime byte except the shared duplicate fix matches a3d696f; deploy-check.php is the sole new runtime file. The checker embeds expected hashes for all original130 entries, and its own offline manifest hash is verified separately to avoid a self-hash cycle.
- Full functional cycles use independent external source/report archives, no skip or resume flags. Documentation/package preparation can proceed while a cycle runs; public runtime is frozen at the tested/exported source. These are functional checks, not performance reliability sessions or a native-host certification. The first task2 attempt was intentionally stopped before completion to harden metadata/hash read warning suppression against server-path disclosure; a fresh complete cycle tests the hardened code. No partial attempt is counted as PASS.
- Owner explicitly requested temporary ZIP upload/extraction inside public_html. That can expose the archive while it exists; remove it immediately after extraction, before other tests, and keep backups outside web access. No agent upload/deployment/cache operation is performed.

## Phase30 owner sheet preservation (2026-10-26)

- Replace upload section(b) and the obsolete appended two-line Phase28 upload note only. Preserve the historical title/intro, before-PSI table and all(c)-(k) checks byte-exact as requested. New section(b) explicitly supersedes the older130-file upload wording:131 until the temporary checker is deleted,130 afterward. Do not fabricate a missing before baseline.
- Longer upload/count instructions increase PDF page count rather than shrink typography or remove any existing page/privacy/font/contact/speed/rollback/Search Console step. Cache directions are conditional on the actual Hostinger/CDN/LiteSpeed options; no WordPress/plugin installation is assumed or performed. Existing host extras can increase File Manager counts; overwrite is not a safe deletion plan.

## Phase30 verification input bookkeeping (2026-10-26)

- The owner-sheet generator initially added one unnecessary empty EOF line. It was corrected before the Task4 implementation commit. The identical documentation-only EOF correction was applied to the Task4/5 external report worktrees before their whitespace gates. Functional runtime bytes, assertions and group selection were never changed; no check was skipped or waived. Report outputs are mutable within these isolated suites, while the public runtime stays frozen.

## Phase30 Task5 complete rerun (2026-10-26)

- First Task5 attempt passed the functional/browser/accessibility groups but failed the new strict scope gate because it inspected regenerated historical-name report outputs in the external worktree. Those outputs are intentionally mutable; the real repository historical files remain protected and unchanged. No complete PASS is claimed for that attempt. Scope now explicitly targets the real source repository and clears inherited external Git worktree/index variables, retaining every protection and131-path archive/hash assertion. The full Task5 suite is rerun from the beginning with no skips/resume, no public runtime changes and no performance lab retry.

## Phase30 final functional outcome (2026-10-26)

- All five complete cycles pass: Task1 37groups/659.17s, Task2 38/1063.34s, Task3 38/1655.1s, Task4 38/1694.91s, Task5 fresh attempt2 39/672.82s. Every cycle executes258 browser and66 accessibility cases with0 rebuilt axe violations. No skip/resume or fourth performance lab. Task2 preliminary stop and Task5 failed scope-target attempt are not counted as complete passes.
- Fresh reference overflow counts are4,2,4,3,4 respectively, with24 reference contrast groups each cycle. These variable observations do not resolve the historical five overflow cases or reference contrast inventory. Historical reports and blockers remain untouched. Native hosting/cache/ACL/CSP/MIME/contact/backup/source/privacy/business/certificate and held-route gates remain owner responsibilities, with no go-live certification.

## Phase31b verification carry-forward (2026-10-29)

This appended record summarizes local Phase31 evidence only. It does not close, replace or waive any earlier owner, native-hosting, privacy/access, contact-delivery, backup/rollback, business/source, certificate or held-route blocker recorded above.

- Fresh blank-space scan is complete at 516/516 cases for 43 routes, 360/768/1280px, JavaScript on/off and normal/reduced motion. It reports 1,006 pixel quiet-band candidates, four retained Contact `#miniHero` tails, 16 intentional scroll-cue dismissals, zero hidden page-copy failures and zero non-decorative empty wrappers. Quiet-band candidates are not confirmed removable space.
- The pre-fix `#team` tail measures sum to 680px across distinct responsive breakpoints. The observed full-document height reduction is 505px across Home at 360px and About at 360px/768px. These metrics are not interchangeable. Contact `#miniHero` remains intentionally unchanged, with 138px at 360px and 233px at 768px retained for its existing bottom scroll cue.
- Task4's only A/B run remains a local simulation: 112 samples, `performance_release_certified=false`, and only `/contact` and `/study-abroad-counselling-mysuru` met every local budget. The other six routes retain their route-specific findings in `reports/phase-31-task4-ab-summary.md` and are carried into Phase32. Do not rerun the benchmark or present its numbers as live or field-speed evidence.
- Phase31b did not build a ZIP, by design. Phase32 must create a package from the then-current branch and verify completeness and hashes before proceeding. No deployment, merge or owner acceptance is implied.

## Phase32 Task1 hero still verification (2026-10-29)

- Approved 640x800 mobile WebP is 9,738 bytes and reused 1440x900 desktop WebP is 37,226 bytes. Both are within their existing owner budgets. Local screenshots for destination, place, article and blog templates at 360px, 768px and 1280px passed visual review after changing the canvas draw to `cover` crop. The first stretched rendering was rejected and is not the accepted result.
- The original canvas opacity of 0.56 measured only 3.654:1 at the article breadcrumb glyphs at 1280px. To preserve the 4.5:1 minimum without changing text, still opacity was conservatively reduced to 0.42. The current pixel-mask audit passes 57 text runs over 12 route/viewport cases; the lowest measured ratio is 5.339:1. See `reports/phase-32-hero-contrast.json`.
- Local browser smoke reports the responsive asset selected correctly, the only still request starting after `loadEventEnd`, text rather than canvas/image LCP candidates, Save-Data and slow-network skips, and reduced-motion no-fade behavior. JavaScript-disabled CSS fallback passes at 360px and 1280px. With `ILMERA_SCENES_ENABLED=false`, all four template fixtures omit the still canvas, its asset URL and loader while preserving the heading.
- The local request interceptor reports Resource Timing `transferSize: 0`; that value is not treated as transferred bytes or performance evidence. File sizes come from local asset hashes. Native hosting, browser cache headers, actual compressed transfer, full-field LCP/CLS/TBT, and compatibility on the target Hostinger/Apache setup remain unverified. Do not claim the still feature passes the site-wide performance budgets until the interleaved A/B and route-wide checks are complete.

## Phase32 Task2 font chain decision (2026-10-29)

- Place, article and blog templates use seven self-hosted webfont faces with `font-display:block`, two local metric fallback faces, two head preloads (Outfit 300 and Cormorant Garamond 700), and a `document.fonts.load` gate that hides the body until fonts are ready or a 3,000ms fail-open timeout. The shared CSS is inline; no external visual-system CSS request is added. Local font responses total 72,784 bytes at 360px (four faces) and 86,816 bytes at 1280px (five faces); other weights are requested but not preloaded.
- The isolated 42-sample local test changed only seven `font-display:block` declarations to `swap` and removed the font-pending visibility rule in candidate B. CLS medians remained 0 on all three routes, but B did not consistently improve LCP: the place and blog medians were higher, and the article median difference was only 0.45ms. Two routes also had broad B IQRs. No font change is adopted. Keep the current local faces, preloads, display values and gate unless a future controlled test demonstrates consistent LCP improvement without worse CLS. See `reports/phase-32-font-ab-summary.md` and raw results.

## Phase32 Task3 reference resource audit guardrails (2026-10-29)

- The local pre-change reference audit measured three external scene dependencies at 717,632 response-body bytes total. Excluding them, the local non-scene body payload is 316,860 to 388,186 bytes, under the 400,000-byte reference cap but with only 11,814 bytes of headroom on Services at 1280px. Do not add a new reference still/image or other request without rechecking the cap. These body lengths are not compressed Hostinger transfer evidence.
- `assets/images/ilmera.logo.png` is the only image response and is 98,340 bytes, displayed at about 38px. Preserve the exact visual asset unless a pixel-exact, separately reviewed optimization is demonstrated. Do not change Contact `#miniHero`; keep the documented 138px mobile and 233px tablet cue tails.
- One-path V8 block-coverage estimates report 458,022 to 469,027 unused JavaScript source bytes and 8,017 to 12,179 unused CSS source bytes. Treat these as diagnostic source-byte estimates, not Lighthouse transfer savings. The unthrottled local LCP/long-task results are not the release-budget metrics; use the frozen-A simulated lab for final thresholds.

## Phase32 reference scene deferral follow-up (2026-10-29)

- The reference resource audit's response-body totals use local font and CDN mirrors. They are not compressed transfer evidence from the deployed host. Services desktop is closest to the local 400,000-byte pre-scene cap at 390,197 bytes, leaving only 9,803 bytes. Do not add an image, stylesheet or other request on these reference pages without a fresh budget check.
- Do not report TBT as passing. The local coverage-enabled long-task proxy is 866ms on Services desktop, 2,963ms on About desktop and 3,902ms on Contact desktop; one direct no-coverage sample observed 1,827ms on About and 3,682ms on Contact while the Three.js scene initialized. These are not Lighthouse TBT, but they are serious red flags. The required frozen-A seven-sample interleaved lab must verify the 600ms reference cap and the unchanged TBT budget. If the lab confirms a regression, do not keep a desktop scene policy that misses the budget; record the conservative fallback.
- The output filter loads GSAP and ScrollTrigger only after load and idle on eligible reference desktops. Existing DOMContentLoaded GSAP conditional blocks have already run before those libraries arrive, so their entrance/reveal timelines do not run; the existing static/IntersectionObserver fallbacks remain. Review final desktop screenshots and record that the page's layout, text and final visible state are preserved. If the transient motion is considered essential, rework only with measured LCP/CLS/TBT evidence.
- The 28 excluded smoke cases used a full-viewport canvas with the existing static CSS background. No new still image was added because Services desktop has little pre-scene headroom. Do not call local request-body sizes network-transfer results.

## Frozen 11-route Lighthouse run 01 (2026-10-29)

- The raw 154-sample local mobile run is complete and committed in `reports/phase-32-11-route-ab-run-01-results.json`; summary table: `reports/phase-32-11-route-ab-run-01-summary.md`. It is not release certification.
- Four of 11 local route gates failed. Home, Services and About show higher B CLS medians than A (B remains below 0.1, but violates the unchanged no-worse-than-A gate). Blog index B TBT is 59.3ms versus A 0ms, which exceeds the +50ms allowance by 9.3ms. Do not round, suppress or explain away either failure without a measured fix.
- Reference mobile B median LCPs are below 4 seconds and median TBT is 0ms; CLS medians are under 0.1 but three of four are worse than baseline. Home and Services also have individual B LCP samples over 4 seconds. The lab excludes the desktop scene path because the mobile eligibility gate skips it. No desktop TBT budget pass is established.
- The runner's `control_reliable=false` comes from the inherited assumption that the four reference routes are unchanged controls. They are changed Phase32 treatments. Keep the raw field and correct the future report labels; do not claim either that the A/B samples failed or that an unchanged-control reliability gate passed.
- Direct no-coverage desktop diagnostics observed long tasks around 1,827ms on About and 3,682ms on Contact during scene startup. These are not Lighthouse TBT. Keep the desktop scene path unapproved until a direct budget result is measured or conservatively disabled.
- Follow-up on run01 labeling: the fixture manifest now records the four reference pages as treatment routes, and the next-run harness no longer applies an unchanged-control test to them. The raw run01 result is preserved unchanged; its `control_reliable=false` field remains documented as inapplicable, not converted to a pass.
- Post-run01 attribution remains inconclusive. A single Home probe points to font/fallback reflow in hero text but did not reproduce the run01 CLS median. A single Blog-index probe shows 52.7ms TBT and long tasks with no source stack. The still loader is only a candidate cause. Do not claim that either issue is fixed until the full 11-route frozen-A comparison passes.
- Run01 follow-up candidate: reference font metric fallbacks are intended to mitigate late glyph reflow without changing the final font; verify by browser attribution, CLS medians and final screenshots. Blog-index mobile now uses the palette instead of the still after its measured +59.3ms TBT delta; confirm the mobile no-request fallback and re-run the 11-route lab. Blog-index desktop still remains enabled, so desktop TBT/visual behavior is still open.

## Phase32 candidate CLS diagnostics - 2026-10-31

- The local metric-matched fallback families did not reduce the observed reference CLS in single-sample candidate diagnostics. Home, Services and About each reproduced the run01 B CLS median: 0.055063, 0.026096 and 0.020411. The candidate must not be described as a CLS fix or release pass.
- Home observer sources show changes in `#hH1`, `#hSub`, `.seo-opening`, `#hBtns` and `#hStats`. Services shows the `#heroSub` and following `.s-wrap` geometry changing. About includes `.story-sec` and `.mob-hero-stats`. Lighthouse lists web-font loads as shift causes. Home and Services observer entries have `hadRecentInput=true`, but the LHR metrics still report the values above; do not dismiss those values using the observer flag.
- A single Services B diagnostic measured LCP 4,231.50ms, above the 4,000ms reference ceiling. It is a diagnostic sample, not a route median. The Blog-index diagnostic was mobile and cannot clear the required desktop TBT check.
- Keep the fallback change under review until the frozen-A seven-sample interleaved 11-route result and final screenshots establish benefit without worse CLS. The captured candidate smoke/audit checks are not substitutes for that lab. Raw data: `reports/phase-32-candidate-font-reflow-diagnostics.md` and its four adjacent JSON artifacts.

## Phase32 reference font candidate revision - 2026-10-31

- The metric-only local fallback added at `1e1f225` did not reduce Home, Services or About CLS in checkpoint 19 diagnostics. It was removed. The new candidate instead serves the matching Latin WOFF2 font faces locally, removes the Google Fonts CSS/preconnect chain, and preloads the existing Outfit 300 and Cormorant Garamond 700 files. New Cormorant assets add 91,548 bytes to the repository and match the audited test-font files exactly; the per-file hashes are in `reports/phase-32-reference-font-candidate.json`.
- The local `font-display:swap` strategy is not yet approved. Verify rendered desktop typography, font face/request chains, local pre-scene payload, added transfer, LCP and CLS against the frozen A arm before keeping it. Preserve all original reference wording and desktop design. No run02 sample or performance pass is available at this checkpoint.
