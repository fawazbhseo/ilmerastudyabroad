# Phase 15 handoff

Reviewed on 16 October 2026 against site commit `3321580` on `arena/48320ee5-ilmerastudyabroad`.

This is a report only. No site file, publication status, sitemap, `llms.txt` or `llms-full.txt` was changed. The only added repository file is `reports/phase-15-handoff.md`. This report also replaces the PR description. Nothing was merged or deployed.

The site is not ready for an unconditional release sign-off. The stored publication checks pass, but this fresh review found draft links in `llms.txt`, existing prohibited wording in both LLM files, university names on published pages, a broken Latvia citation, an unavailable Dubai citation with a working official document, and one unsupported Qatar sentence. Business assertions and the 8,000-euro partner claim are not government-verified facts.

## 1. Page status, discovery and sitemap

The original 29 targets are 9 destinations, 17 locations and 3 articles. Of those, 27 are published and 2 are draft destinations. APS and DSU are two additional withheld articles, not part of the original 29. The table therefore has 31 entries: 27 published and 4 draft. The sitemap has 37 indexable HTML pages because it also includes 10 other published pages listed below.

“Published” is the current repository state, not a new approval in this report. “Indexable” means the rendered HTML and response do not tell crawlers to exclude that page. It does not mean a search engine has indexed it. All 31 URLs returned HTTP 200 in the fresh PHP adapter check. Apache behavior is still untested.

**F** means the shared footer on every one of the 41 editorial routes: all 37 sitemap pages and the 4 draft URLs in this table. For each published target, that is 40 other incoming pages plus a self-link in its own footer. The 404 utility page has a different footer and is not in F. This is the complete set of incoming HTML source pages found for each of the 27 published targets. Footer source: `includes/footer.php:61-88`.

**L** means the additional incoming text link from `llms.txt`; that file is public and was checked separately. “None stored” means the existing automatic publication gate passes. Fresh source and owner issues are still listed, rather than concealed by that result.

| Page | URL | Final status | Indexable | Sitemap | Linked from where | Gates failed or fresh gaps | Owner input needed |
|---|---|---|---|---|---|---|---|
| Germany | https://ilmerastudyabroad.com/study-in-germany | published | Yes | Yes | F | None stored; owner assertions unverified. | Shared business details and this destination service statement. |
| Italy | https://ilmerastudyabroad.com/study-in-italy | published | Yes | Yes | F | None stored; DSU help is an owner statement, not an award entitlement. | Actual scholarship service and partner/award evidence where claimed elsewhere. |
| Slovakia | https://ilmerastudyabroad.com/study-in-slovakia | published | Yes | Yes | F | None stored; owner assertions unverified. | Shared business details and this destination service statement. |
| UK | https://ilmerastudyabroad.com/study-in-uk | published | Yes | Yes | F | None stored; owner assertions unverified. | Shared business details and this destination service statement. |
| Czech Republic | https://ilmerastudyabroad.com/study-in-czech-republic | draft | No | No | No incoming HTML or LLM URL link found | 4 categories, below 5; no opened approved tuition replacement; archived instructions are not current. | Approved evidence or instructions for a later review; no status change now. |
| Lithuania | https://ilmerastudyabroad.com/study-in-lithuania | published | Yes | Yes | F | None stored; owner assertions unverified. | Shared business details and this destination service statement. |
| Latvia | https://ilmerastudyabroad.com/study-in-latvia | published | Yes | Yes | F | None stored; owner assertions unverified. | Shared business details and this destination service statement. |
| GCC | https://ilmerastudyabroad.com/study-in-gcc | published | Yes | Yes | F | None stored; Dubai citation failed; Qatar no-steps clause unsupported (section 6). | Actual service countries, scope and authority; common business details. |
| Russia | https://ilmerastudyabroad.com/study-in-russia | draft | No | No | No incoming HTML or LLM URL link found | 0 categories; no verified current notice or 5 categories; cited notice unavailable. | A usable current approved notice or evidence for a later review. |
| Karnataka | https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Kodagu | https://ilmerastudyabroad.com/study-abroad-consultants-in-kodagu | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Madikeri | https://ilmerastudyabroad.com/study-abroad-counselling-madikeri | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Virajpet | https://ilmerastudyabroad.com/study-abroad-counselling-virajpet | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Kushalnagar | https://ilmerastudyabroad.com/study-abroad-counselling-kushalnagar | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Somwarpet | https://ilmerastudyabroad.com/study-abroad-counselling-somwarpet | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Gonikoppal | https://ilmerastudyabroad.com/study-abroad-counselling-gonikoppal | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Ponnampet | https://ilmerastudyabroad.com/study-abroad-counselling-ponnampet | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Siddapura | https://ilmerastudyabroad.com/study-abroad-counselling-siddapura | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Mysuru | https://ilmerastudyabroad.com/study-abroad-counselling-mysuru | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Bengaluru | https://ilmerastudyabroad.com/study-abroad-counselling-bengaluru | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Mangaluru | https://ilmerastudyabroad.com/study-abroad-counselling-mangaluru | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Udupi and Manipal | https://ilmerastudyabroad.com/study-abroad-counselling-udupi-manipal | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Hassan | https://ilmerastudyabroad.com/study-abroad-counselling-hassan | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Chikkamagaluru | https://ilmerastudyabroad.com/study-abroad-counselling-chikkamagaluru | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Shivamogga | https://ilmerastudyabroad.com/study-abroad-counselling-shivamogga | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Belagavi | https://ilmerastudyabroad.com/study-abroad-counselling-belagavi | published | Yes | Yes | F | None stored; owner assertions unverified. | Confirm service area and Shared owner claims. |
| Costs article | https://ilmerastudyabroad.com/blog/cost-of-studying-abroad-for-indian-students | published | Yes | Yes | F | None stored; owner assertions unverified. | Authorship, CMO role and actual review; common business details. |
| Documents article | https://ilmerastudyabroad.com/blog/documents-needed-to-study-abroad-from-india | published | Yes | Yes | F | None stored; Latvia source URL is a missing page; working official alternative opened. | Authorship, CMO role and actual review; common business details. |
| Scholarships article | https://ilmerastudyabroad.com/blog/scholarships-for-indian-students-study-abroad | published | Yes | Yes | F | None stored; owner assertions unverified. | Authorship, CMO role and actual review; common business details. |
| Additional APS article | https://ilmerastudyabroad.com/blog/study-in-germany-free-aps-certificate | draft | No | No | L at `llms.txt:129` | Draft; APS source host not approved; no released APS review entry. | Whether to approve the APS host in a future authorized review. |
| Additional DSU article | https://ilmerastudyabroad.com/blog/italy-dsu-scholarship-eligibility | draft | No | No | L at `llms.txt:130` | Draft; no approved current DSU call or verified amount/partner entitlement. | Current award call and documentary partner authority. |

### Additional links outside the shared footer

These lists identify the exact source pages, using the page names in the table above. Home, Services, Contact, All pages and Blog index mean `/`, `/services`, `/contact`, `/all-pages` and `/blog/`. Backlogs article and Coorg article mean the two legacy article URLs in the sitemap list. APS and DSU mean the additional draft URLs above. Draft pages can link out to published pages without those published pages linking back to the drafts.

- **Germany**: Home, All pages, Costs article, Documents article, Scholarships article, Services, GCC, Italy, Latvia, Lithuania, Slovakia, UK.

- **Italy**: Home, All pages, Costs article, Documents article, Scholarships article, Services, GCC, Germany, Latvia, Lithuania, Slovakia, UK.

- **Slovakia**: Home, All pages, Services, GCC, Germany, Italy, Latvia, Lithuania, UK.

- **UK**: Home, All pages, Services, GCC, Germany, Italy, Latvia, Lithuania, Slovakia.

- **Lithuania**: Home, All pages, Services, GCC, Germany, Italy, Latvia, Slovakia, UK.

- **Latvia**: Home, All pages, Services, GCC, Germany, Italy, Lithuania, Slovakia, UK.

- **GCC**: Home, All pages, Services, Germany, Italy, Latvia, Lithuania, Slovakia, UK.

- **Karnataka**: Home, All pages, Contact, Services, Kodagu, Belagavi, Bengaluru, Chikkamagaluru, Gonikoppal, Hassan, Kushalnagar, Madikeri, Mangaluru, Mysuru, Ponnampet, Shivamogga, Siddapura, Somwarpet, Udupi and Manipal, Virajpet.

- **Kodagu**: Home, All pages, Contact, Services, Karnataka, Gonikoppal, Kushalnagar, Madikeri, Ponnampet, Siddapura, Somwarpet, Virajpet.

- **Madikeri**: Home, All pages, Contact, Services, Kodagu, Somwarpet.

- **Virajpet**: Home, All pages, Contact, Services, Kodagu, Gonikoppal, Ponnampet, Siddapura.

- **Kushalnagar**: Home, All pages, Contact, Services, Kodagu, Madikeri, Siddapura, Somwarpet.

- **Somwarpet**: Home, All pages, Contact, Services, Kodagu, Kushalnagar, Madikeri.

- **Gonikoppal**: Home, All pages, Contact, Services, Kodagu, Ponnampet, Virajpet.

- **Ponnampet**: Home, All pages, Contact, Services, Kodagu, Gonikoppal, Virajpet.

- **Siddapura**: Home, All pages, Contact, Services, Kodagu, Kushalnagar.

- **Mysuru**: Home, All pages, Contact, Services.

- **Bengaluru**: Home, All pages, Contact, Services.

- **Mangaluru**: Home, All pages, Contact, Services.

- **Udupi and Manipal**: Home, All pages, Contact, Services, Karnataka, Belagavi, Shivamogga.

- **Hassan**: Home, All pages, Contact, Services.

- **Chikkamagaluru**: Home, All pages, Contact, Services.

- **Shivamogga**: Home, All pages, Contact, Services, Karnataka, Belagavi, Udupi and Manipal.

- **Belagavi**: Home, All pages, Contact, Services, Karnataka, Shivamogga, Udupi and Manipal.

- **Costs article**: Home, All pages, Blog index, Documents article, DSU article, Scholarships article, Coorg article, Backlogs article, APS article, Services.

- **Documents article**: Home, All pages, Blog index, Costs article, Coorg article, Backlogs article, Services.

- **Scholarships article**: Home, All pages, Blog index, Services.

### All 37 sitemap URLs

Fresh `/sitemap.xml` output matched the unchanged `sitemap.xml` file byte for byte. Every URL below returned an indexable page with exactly its own canonical URL. No draft or 404 URL appears. The 10 outside the original 27 published targets are Home, Services, About, Contact, Blog index, Privacy policy, Terms, All pages, Backlogs article and Coorg article.

1. https://ilmerastudyabroad.com/

2. https://ilmerastudyabroad.com/services

3. https://ilmerastudyabroad.com/about

4. https://ilmerastudyabroad.com/contact

5. https://ilmerastudyabroad.com/blog/

6. https://ilmerastudyabroad.com/privacy-policy

7. https://ilmerastudyabroad.com/terms

8. https://ilmerastudyabroad.com/all-pages

9. https://ilmerastudyabroad.com/blog/study-abroad-with-academic-backlogs

10. https://ilmerastudyabroad.com/blog/study-abroad-counselling-from-coorg

11. https://ilmerastudyabroad.com/blog/cost-of-studying-abroad-for-indian-students

12. https://ilmerastudyabroad.com/blog/documents-needed-to-study-abroad-from-india

13. https://ilmerastudyabroad.com/blog/scholarships-for-indian-students-study-abroad

14. https://ilmerastudyabroad.com/study-in-germany

15. https://ilmerastudyabroad.com/study-in-italy

16. https://ilmerastudyabroad.com/study-in-uk

17. https://ilmerastudyabroad.com/study-in-lithuania

18. https://ilmerastudyabroad.com/study-in-latvia

19. https://ilmerastudyabroad.com/study-in-slovakia

20. https://ilmerastudyabroad.com/study-in-gcc

21. https://ilmerastudyabroad.com/study-abroad-counselling-belagavi

22. https://ilmerastudyabroad.com/study-abroad-counselling-bengaluru

23. https://ilmerastudyabroad.com/study-abroad-counselling-chikkamagaluru

24. https://ilmerastudyabroad.com/study-abroad-counselling-gonikoppal

25. https://ilmerastudyabroad.com/study-abroad-counselling-hassan

26. https://ilmerastudyabroad.com/study-abroad-consultants-in-karnataka

27. https://ilmerastudyabroad.com/study-abroad-consultants-in-kodagu

28. https://ilmerastudyabroad.com/study-abroad-counselling-kushalnagar

29. https://ilmerastudyabroad.com/study-abroad-counselling-madikeri

30. https://ilmerastudyabroad.com/study-abroad-counselling-mangaluru

31. https://ilmerastudyabroad.com/study-abroad-counselling-mysuru

32. https://ilmerastudyabroad.com/study-abroad-counselling-ponnampet

33. https://ilmerastudyabroad.com/study-abroad-counselling-shivamogga

34. https://ilmerastudyabroad.com/study-abroad-counselling-siddapura

35. https://ilmerastudyabroad.com/study-abroad-counselling-somwarpet

36. https://ilmerastudyabroad.com/study-abroad-counselling-udupi-manipal

37. https://ilmerastudyabroad.com/study-abroad-counselling-virajpet

## 2. Exact APS and DSU repository state

Both articles are reachable, but neither is indexable. Therefore neither is the particular “reachable and indexable” error. They are not private: noindex is a crawler instruction, not access control. The remaining incoming links in the public LLM file are a real discovery failure.

| Check | APS | DSU |
|---|---|---|
| Status switch | `includes/posts.php:6-16`, draft at line 14 | `includes/posts.php:17-27`, draft at line 25 |
| Visitor URL | `/blog/study-in-germany-free-aps-certificate` | `/blog/italy-dsu-scholarship-eligibility` |
| Fresh HTTP result | 200, full article readable | 200, full article readable |
| Crawler instructions | HTTP `X-Robots-Tag: noindex, follow`, robots meta `noindex, follow`, googlebot meta `noindex, follow` | Same three noindex instructions |
| Canonical | Its own full clean URL | Its own full clean URL |
| Sitemap | Absent | Absent |
| Incoming HTML links | None in all 42 checked routes, including article lists, related cards, footer and directory | None in all 42 checked routes |
| Remaining public incoming link | `llms.txt:129`, still titled “Study in Germany for Free from India: APS Certificate Guide” | `llms.txt:130`, still titled “Italy DSU Scholarship: Who Qualifies” |
| `llms-full.txt` URL link | None found | None found |
| What the visitor sees | Germany Tuition and APS: Check the Applicable Route; tuition exceptions, APS explanation, sources, author card, review notice and counselling offer | Italy Scholarship Planning: Verification Needed; prominent draft notice, conditional owner amount and a statement that eligibility, dates and partner authority are unconfirmed |

APS body and notice: `blog/study-in-germany-free-aps-certificate.php:129-148`; its counselling offer is at line 168. The notice says the APS host is outside the approved list and that the draft is not a released checklist. DSU body and notice: `blog/italy-dsu-scholarship-eligibility.php:126-142`. Its exact conditional amount remains at line 134 and its metadata excerpt at `includes/posts.php:20`.

Literal APS/DSU slugs also remain in internal related-post arrays and link maps, such as `includes/posts.php:15,26,37,48,59,70,81` and `includes/links.php:117,144`. Those references are not rendered incoming links: the publication filters suppress the draft destinations of those links. Neither the HTML checks nor that filtering covers `llms.txt`.

## 3. Italy scholarship wording and every 8,000-euro occurrence

### What the Italy destination page actually says

The current scholarship-related sentence in the visible “ILMERA overview” is:

> ILMERA helps identify scholarships, government grants, and stipend programmes suited to a student's profile, most notably Italy's DSU (Diritto allo Studio Universitario) scholarship.

Source: `destinations/italy.php:10`, rendered by `includes/destination-page.php:127-130`. This is an owner/business service statement. It is not an official DSU eligibility or amount statement. The scholarship fact list is empty at `destinations/italy.php:26`.

There is **no 8,000-euro sentence on `/study-in-italy`**, either in its visible body or metadata/schema. The exact description used by its normal description meta, Open Graph description and WebPage schema is:

> Indian students who want to study in Italy first apply for admission to the Italian institution, then complete pre-enrolment on the Universitaly portal, then apply for a study visa by appointment at a VFS centre. Each institution sets its own admission requirements, deadlines and tuition fees.

Source: `destinations/italy.php:6`; selection and output: `includes/destination-page.php:17,21,36,44`. There is no Twitter description in this template. Service schema has no scholarship amount or description. The four FAQ schema answers concern Universitaly, visa duration, interview and the consulate's official email; none contains a scholarship amount.

### Exact amount sentence elsewhere

Every monetary match below uses this same owner-supplied sentence, either alone or after a tuition paragraph:

> Tuition can be fully or largely covered at our partner universities through scholarships of up to 8,000 euros, subject to eligibility.

The conditional phrase does not verify the amount, identify a current award call, prove a partner agreement or establish any individual entitlement. The Italian consulate page opened in this pass does not supply that proof. Withholding the DSU article has **not** removed the claim from other published pages.

| File and line | Where it appears | Current availability |
|---|---|---|
| `about.php:671` | Visible tuition/scholarship paragraph | Published |
| `contact.php:168,171` | Two FAQ schema answers | Published |
| `contact.php:515,539` | Matching visible FAQ answers | Published |
| `index.php:172,174,178` | Three FAQ schema answers | Published |
| `index.php:510` | Visible guidance paragraph using the `testi-text` CSS class, not proof of a student testimonial | Published |
| `index.php:557` | Visible study route card | Published |
| `index.php:590,594,602` | Three visible FAQ answers | Published |
| `services.php:141,142` | Two FAQ schema answers | Published |
| `services.php:439` | Visible Italy section | Published |
| `services.php:711` | Visible scholarship guidance card | Published |
| `services.php:760,764` | Visible FAQ answers | Published |
| `blog/italy-dsu-scholarship-eligibility.php:134` | Visible owner conditional statement with draft warning | Publicly reachable draft |
| `includes/posts.php:20` | DSU excerpt used in draft description, social metadata and BlogPosting description | Draft metadata, not a published article card |

That is 21 source-line occurrences: 19 in published page files, one in the reachable DSU body, and one shared DSU metadata definition. Generated copies of a metadata definition are not extra source lines. The scan covered visitor-facing PHP/HTML/TXT source, decoded rendered text, metadata and schema, including both public LLM files, for `8,000`, `8000`, `8.000`, `8 000` and “eight thousand”. No additional monetary variant was found. CSS `z-index:8000` is not an award amount. Internal historical reports and review logs are not visitor copy and are not counted as extra site claims.

## 4. GCC scope and country sources

The exact visible scope note is:

> Coverage: UAE, Qatar, Saudi Arabia and a dated Bahrain registration notice. This is not a complete six-country GCC guide. Oman and Kuwait are excluded because no usable, opened evidence was confirmed for them in this review.

Source: `destinations/gcc.php:209`; renderer: `includes/destination-page.php:121-122`.

| Country | Actual published scope | Official source opened in this pass |
|---|---|---|
| UAE | Admissions checks, language, budget, scholarships as opportunities, visa sponsorship, documents, insurance, intakes, work and selected post-study guidance | Indian Consulate Dubai 2026 advisory document, AE below. The site's AE-X landing citation failed with HTTP 500; direct official document opened successfully. |
| Qatar | Student-visa applicability, living-cost comparison and embassy registration advice | Embassy of India, Doha advisory, QA below. It also contains application/document information, so the site's “does not list the steps” clause is not verified. |
| Saudi Arabia | Admission/document caution, no work on a student visa and embassy registration | Embassy of India, Riyadh student information page, SA below. |
| Bahrain | Only a registration request dated 31 May 2022, not current visa, scholarship, tuition or admission guidance | Embassy of India Bahrain press release PDF, BH below. |
| Oman | Excluded | No usable opened evidence supports published Oman guidance in this page. |
| Kuwait | Excluded | No usable opened evidence supports published Kuwait guidance in this page. |

Government source coverage is not proof that ILMERA is authorized by any institution or performs each service. The broader owner summary “Admissions guidance and student visa processing for GCC destinations.” at `destinations/gcc.php:10` needs the owner's actual service scope. All source URLs and the affected lines are recorded in section 6.

## 5. Office, address, phone and in-person implications for all 17 locations

### Shared lines on every location page

All 17 use the same template and footer. No local street address, city-specific phone, LocalBusiness office or in-person appointment is offered in their rendered content or Service schema. They do imply an ILMERA counselling service for the named audience. That service-area statement requires owner confirmation and must not be described as government-verified local presence.

| Exact source | Statement or implication | Assessment |
|---|---|---|
| `includes/place-page.php:17-20` | Fallback heading says consultancy/counselling “for” the named students; each current page supplies its own heading/title/description | Audience and service positioning, not a street office |
| `includes/place-page.php:34` | Service provider ILMERA, `areaServed` equal to the page's place name, phone `+919019557427` | Shared organization contact and service area; no address in Service or provider |
| `includes/place-page.php:176-179` | “ILMERA is based in Coorg, Kodagu, with no physical office. Contact is by phone, WhatsApp or video call. Admissions, awards and visas are decided by the relevant bodies, not guaranteed by counselling.” followed by “Discuss this plan” contact link | Explicitly denies a physical office; base and channels are owner statements |
| `includes/header.php:65,67,76` | Contact links in both menus and “Book Consultation” | Booking a discussion, not evidence of a local appointment facility |
| `includes/footer.php:42` | “Your Gateway to Global Education. Based in Coorg, Kodagu, Karnataka.” | Base is owner-supplied; no street address |
| `includes/footer.php:47,98` | WhatsApp target `https://wa.me/421944485186` | Existing shared +421 number, not a local branch number |
| `includes/footer.php:95` | `+91 90195 57427`, `tel:+919019557427` | Existing shared primary phone, also used in Service schema |
| `includes/footer.php:96` | `+91 94810 84038`, `tel:+919481084038` | Existing shared second phone, not a town-specific phone |
| `includes/footer.php:97` | `info@ilmerastudyabroad.com` | Shared email |
| `includes/footer.php:99` | “Book no-charge Consultation”, links to `/contact` | Owner's charging/booking statement, not an in-person promise |

No phone call, WhatsApp exchange, business registration check or site visit was performed. Reusing an existing contact is not proof that it still belongs to or is answered by ILMERA.

### Page-by-page location findings

**Shared** below means every line in the preceding table, applying to that row in full. The file-specific lines below include negative office disclaimers and issuing-office references, not just positive claims. An issuing office mentioned as a generic document issuer is not an ILMERA office. No local geographic, college, bank, loan, transport or visa-appointment fact is asserted in these 17 planning guides.

| Location | Current page purpose | Office, address, phone and in-person result | Additional exact file lines |
|---|---|---|---|
| Karnataka | Turning a longlist into a defensible shortlist | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Kodagu | Coordinating the family decision | Shared; no local office/address/phone or in-person offer. | `places/kodagu.php:47`: existing phone, WhatsApp and video arrangements; says not to assume a local office meeting. |
| Madikeri | Explaining the academic timeline | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Virajpet | Preparing the application handover | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Kushalnagar | Reading a conditional offer | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Somwarpet | Presenting a backlog record accurately | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Gonikoppal | Organising household evidence | Shared; no local office/address/phone or in-person offer. | `places/gonikoppal.php:43`: explicitly does not identify an issuing office or local attestation route. |
| Ponnampet | Writing an authentic study statement | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Siddapura | Sharing documents deliberately | Shared; no local office/address/phone or in-person offer. | `places/siddapura.php:43`: phone, WhatsApp and video are existing contact options, not a security certification; line 49: no local storage facility, office or special system access offered. |
| Mysuru | Checking names and academic records | Shared; no local office/address/phone or in-person offer. | `places/mysuru.php:40`: no issuing office or processing-time estimate is named. |
| Bengaluru | Changing academic direction | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Mangaluru | Clarifying sponsor support | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Udupi and Manipal | Comparing the learning experience | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Hassan | Testing the budget boundary | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Chikkamagaluru | Planning language evidence | Shared; no local office/address/phone or in-person offer. | None beyond Shared; no additional office/contact assertion in the data file. |
| Shivamogga | Building a dependency calendar | Shared; no local office/address/phone or in-person offer. | `places/shivamogga.php:42`: no courier time, appointment city or issuing-office turnaround asserted. |
| Belagavi | Agreeing the counselling brief | Shared; no local office/address/phone or in-person offer. | `places/belagavi.php:48`: audience only; explicitly no local office, college connection or appointment facility. |

The Karnataka introduction also says “ILMERA discussions can start from your academic record and priorities” at `places/karnataka.php:8`. This is a business service statement, not a sourced local fact. The location title, heading and description fields describe the guide's subject; they are not proof of local premises. The same schema/no-office/contact statements above are the only business-presence claims on the other location pages.

## 6. Fresh official source review and unverified published statements

### What was checked, and what was not certified

The following official source text was opened during this Phase 15 pass on 16 October 2026, not accepted from a search snippet or a Phase 14 “verified” flag. Relevant source sections were compared with the current intro, factual rows, article paragraphs and FAQ answers. Official-source confirmation is limited to the stated country, route, dates and conditions. DAAD and European Commission study portals are education sources already allowed by the existing rules; they are not ILMERA business evidence.

Advice such as “confirm your selected programme”, “keep a budget worksheet” and “do not count an unconfirmed award” is editorial guidance, not a claimed government rule or proof that ILMERA performs a service. The 17 location guides deliberately give this type of planning advice, not local administrative facts. None has an official local source to claim as opened or verified.

A stored gate still passes when its old journal says a line was checked. That does not mean a link opened today, or that every owner summary was checked. In particular, GCC's 9 stored categories and the Documents article's stored approval were not changed despite the fresh findings below.

### Official sources opened now

Source codes below are used in the page evidence table. Redirects and failed paths are explicit. AE document sections 1-13 needed for retained claims were read; no claim is based on an unread footer or search excerpt.

| Code | Exact source URL | Result and limits |
|---|---|---|
| DE-F | https://www.daad.de/en/studying-in-germany/living-in-germany/finances/ | Opened. Tuition exceptions, semester contribution, living estimates, funding proof and limited work. The 992-euro figure is expressly January 2025, not a verified 2026 amount. |
| DE-V | https://www.daad.de/en/studying-in-germany/living-in-germany/visa/ | Opened. Student/prospective-student distinction and usual visa documents; no APS host approval. |
| DE-S | https://www.daad.de/en/studying-in-germany/scholarships/ | Opened. Funding organizations and scholarship search; no applicant-specific award guarantee. |
| IT | https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/ | Opened. Institution requirements/fees, admission, Universitaly, visa duration, VFS, interview, processing, DOV and email warning. Linked checklist labelled 2025-2026. No DSU amount or partner proof. |
| SK-E | https://education.ec.europa.eu/study-in-europe/country-profiles/slovakia | Opened. Language-dependent tuition, budget estimates, direct admission, scholarship overview and non-EU admission/funds/insurance requirements. |
| SK-V | https://www.mzv.sk/en/web/dilli-en/services/national-visa | Opened through redirect to SK-V2. General national-visa and category-dependent documents. The study appointment link is labelled 2024/2025, not a new intake booking window. |
| SK-V2 | https://www.mzv.sk/en/web/dilli-en/visa-and-services/national-visa | Opened relevant general/document sections. Form, travel document, photograph, purpose and health insurance, with additional category requirements. |
| SK-C | https://www.mzv.sk/en/web/dilli-en/contact-us | Opened. New Delhi mission contact and prior-appointment visa hours, not an employment booking route for students. |
| UK-V | https://www.gov.uk/student-visa | Opened. Age 16+, licensed sponsor, funds, English and parental permission at 16-17. |
| UK-F | https://www.gov.uk/guidance/financial-evidence-for-student-and-child-student-route-applicants | Opened both content chunks. CAS fees, monthly 1,171/1,529 pounds for up to nine months, exemptions, account/28-day/31-day rules, funding sources and sponsor-letter contents. |
| UK-E | https://www.gov.uk/student-visa/knowledge-of-english | Opened. Qualifying evidence, Ecctis and degree-level provider assessment equivalent to B2; not a universal test waiver. |
| LT-E | https://education.ec.europa.eu/study-in-europe/country-profiles/lithuania | Opened. Starting tuition averages 1,300/2,300/8,400 euros, 500-800 monthly living estimate, English programme count and health insurance. |
| LT-V | https://migracija.lrv.lt/en/structure-and-contacts/information-for-visitors/services-for-persons-abroad/temporary-residence-permit-and-national-visa-services/republic-of-india/ | Opened. New Delhi/Mumbai TRP service points, 110-euro provider fee separate from state fee, MIGRIS booking after Submitted to external service provider status. |
| LV-E | https://education.ec.europa.eu/fi/country-profiles/latvia | Opened after redirect to https://education.ec.europa.eu/fi/study-in-europe/country-profiles/latvia. Relevant living-cost, tuition and insurance sections read. |
| LV-S | https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students | Opened. 90-day study visa, subsequent residence permit, Hello Verify and VFS/interview instructions. |
| LV-I | https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/students/indian-nationals | Opened. Working Indian-national student page, including application, accommodation, insurance and submission steps. |
| LV-X | https://www2.mfa.gov.lv/en/newdelhi/consular-section/applying-for-a-long-stay-visa/indian-nationals | FAILED substantive page check: the response was a missing-page message, not student guidance. Not evidence. LV-I is the working alternative, not this path. |
| AE-X | https://www.cgidubai.gov.in/page/student-advisory/ | FAILED with HTTP 500 in this pass. Do not label this cited landing URL as successfully reopened. |
| AE | https://www.cgidubai.gov.in/content/Student-Advisory-2026.doc | Opened directly, relevant chunks 0-3. UAE accreditation, agreements, money, sponsorship, documents, insurance, language/intakes, work, post-study and attestation advice. This confirms retained UAE wording independently of the failed landing URL. |
| QA | https://indianembassyqatar.gov.in/education_Advisory_students | Opened. Visa applicability, application/document information, costs and embassy registration. Contradicts the no-steps implication, not the visa-applicability clause. |
| SA | https://eoiriyadh.gov.in/page/useful-information-for-indian-students-in-saudi-arabia | Opened at its www/trailing-slash URL. Admission/document caution, student-visa work prohibition and registration advice. No GCC-wide work rule inferred. |
| BH | https://www.eoibahrain.gov.in/pdf/Press%20Release-Student%20Global%20portal.pdf | Opened. Registration request explicitly dated 31 May 2022. Not a current immigration or scholarship source. |
| CZ | https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/long_term_visa_and_long_term_residence.html | Opened both chunks. Originals/copies as specified, Czech translation conditions, Indian apostille and insurance. Used by the published Documents article, not evidence that the withheld Czech destination passed its tuition gate. |

APS background was also reopened at https://aps-india.de/ and describes its academic verification procedure, but the host remains outside the approved destination source list. Opening it did not approve it. A Russia candidate at https://www.education.gov.in/sites/upload_files/mhrd/files/Scholarships_Russia_Federation_AY_2026_27.pdf returned an actual “Page Not Found” page, not a usable award notice. These do not release either held page. The Czech tuition/booking blockers in section 1 remain the stored blockers; this pass did not claim a new approved tuition source or new booking-window verification.

### All 27 published targets: official evidence and owner limits

Destination references below identify every retained factual intro, row and FAQ-answer source line, grouped by official source code. A group containing advice is confirmed only to the extent the source actually supplies the factual part. FAQ answers are also generated into schema by `includes/destination-page.php:24-27`. All seven destination pages additionally carry the shared owner statement at `includes/destination-page.php:168` about the Coorg base, no physical office, and phone/WhatsApp/video counselling, plus shared footer owner claims listed below. Their Service schema at `includes/destination-page.php:22` describes ILMERA's counselling service, not government accreditation.

| Published destination | Source codes and exact factual lines; failed paths are flagged below | Owner-only or unverified lines |
|---|---|---|
| Germany | DE-F: `destinations/germany.php:6,20,26,32,38,56,64,73,80,87,94`; DE-V: `destinations/germany.php:47` | `destinations/germany.php:10`: “ILMERA confirms the rule for each university before applying.” No external proof of this business practice. Shared owner lines also apply. |
| Italy | IT: `destinations/italy.php:6,20,29,35,41,47,53,62,68,78,85,92,99` | `destinations/italy.php:10`: “ILMERA helps identify scholarships, government grants, and stipend programmes suited to a student's profile, most notably Italy's DSU (Diritto allo Studio Universitario) scholarship.” DSU help/availability for a profile is not verified award or partner evidence. Shared owner lines also apply. |
| Slovakia | SK-E: `destinations/slovakia.php:6,21,27,35,64,74,88,95`; SK-V: `destinations/slovakia.php:43,81`; SK-C: `destinations/slovakia.php:49`; SK-V2: `destinations/slovakia.php:58` | `destinations/slovakia.php:10`: “Standard admissions and visa support.” No external proof of this business practice. Shared owner lines also apply. |
| UK | UK-F: `destinations/uk.php:6,34,40,51,57,63,69,79,86,93,100`; UK-V: `destinations/uk.php:18`; UK-E: `destinations/uk.php:26` | `destinations/uk.php:10`: “Rules can change; ILMERA advises students to confirm current rules at the time of application.” Editorial caution plus an assertion about ILMERA advice, not an applicant decision. Shared owner lines also apply. |
| Lithuania | LT-E: `destinations/lithuania.php:6,21,45,62,69`; LT-V: `destinations/lithuania.php:30,36,55` | `destinations/lithuania.php:10`: “English requirements vary by university and programme.” General caution to confirm programme-specific English evidence, not proof of a no-test route. Shared owner lines also apply. |
| Latvia | LV-I: `destinations/latvia.php:6,30,48,57,63,93`; LV-E: `destinations/latvia.php:21,69,100`; LV-S: `destinations/latvia.php:36,42,79,86` | `destinations/latvia.php:10`: “ILMERA counsellors review a student's academic transcripts, standardized test scores (if any), budget, preferred field of study, and career goals.” No external proof of this business practice. Shared owner lines also apply. |
| GCC | AE-X: `destinations/gcc.php:6,23,31,37,51,59,65,71,85,93,99,105,119,125,140,147,154,161,168`; QA: `destinations/gcc.php:43,77,175,189`; SA: `destinations/gcc.php:111,131,182,196`; BH: `destinations/gcc.php:203` | `destinations/gcc.php:10`: “Admissions guidance and student visa processing for GCC destinations.” Actual service-country scope is unverified. Also see unsupported Qatar clause at line 77 and failed AE-X citations below. Shared owner lines also apply. |

The retained government/education claims in those groups match the reopened source text, except the Qatar no-steps clause below. That does not turn the unsourced owner-summary fields into verified facts. The direct AE document supports UAE wording, but does not repair its failed citation on the site.

| Published location | Official sources opened for local claims | Advice and owner limits |
|---|---|---|
| Karnataka | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/karnataka.php:8,17,21,37,43,49`. Shared owner lines in section 5. ILMERA discussion offer at line 8. |
| Kodagu | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/kodagu.php:8,17,21,41,47,53`. Shared owner lines in section 5. `places/kodagu.php:47`: existing phone, WhatsApp and video arrangements; says not to assume a local office meeting. |
| Madikeri | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/madikeri.php:8,17,21,37,43,49`. Shared owner lines in section 5. |
| Virajpet | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/virajpet.php:8,17,21,37,43,49`. Shared owner lines in section 5. |
| Kushalnagar | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/kushalnagar.php:8,17,21,37,43,49`. Shared owner lines in section 5. |
| Somwarpet | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/somwarpet.php:8,17,21,37,43,49`. Shared owner lines in section 5. |
| Gonikoppal | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/gonikoppal.php:8,17,21,37,43,49`. Shared owner lines in section 5. `places/gonikoppal.php:43`: explicitly does not identify an issuing office or local attestation route. |
| Ponnampet | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/ponnampet.php:8,17,21,37,43,49`. Shared owner lines in section 5. |
| Siddapura | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/siddapura.php:8,17,21,37,43,49`. Shared owner lines in section 5. `places/siddapura.php:43`: phone, WhatsApp and video are existing contact options, not a security certification; line 49: no local storage facility, office or special system access offered. |
| Mysuru | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/mysuru.php:8,17,21,34,40,46`. Shared owner lines in section 5. `places/mysuru.php:40`: no issuing office or processing-time estimate is named. |
| Bengaluru | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/bengaluru.php:8,17,21,34,40,46`. Shared owner lines in section 5. |
| Mangaluru | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/mangaluru.php:8,17,21,34,40,46`. Shared owner lines in section 5. |
| Udupi and Manipal | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/udupi-manipal.php:8,17,21,36,42,48`. Shared owner lines in section 5. |
| Hassan | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/hassan.php:8,17,21,34,40,46`. Shared owner lines in section 5. |
| Chikkamagaluru | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/chikkamagaluru.php:8,17,21,34,40,46`. Shared owner lines in section 5. |
| Shivamogga | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/shivamogga.php:8,17,21,36,42,48`. Shared owner lines in section 5. `places/shivamogga.php:42`: no courier time, appointment city or issuing-office turnaround asserted. |
| Belagavi | None; planning advice only. | Editorial intro, paragraphs and FAQ answers: `places/belagavi.php:8,17,21,36,42,48`. Shared owner lines in section 5. `places/belagavi.php:48`: audience only; explicitly no local office, college connection or appointment facility. |

For the three published articles below, factual paragraphs and FAQ answers were compared again with the reopened sources, including the date and exception limits. Their planning paragraphs are advice, not externally verified business practices. Each also has owner-dependent attribution and common footer claims.

| Published article | Opened official sources and exact factual lines | Advice and owner-dependent attribution |
|---|---|---|
| Costs article | DE-F: `blog/cost-of-studying-abroad-for-indian-students.php:49,150,151`; IT: `blog/cost-of-studying-abroad-for-indian-students.php:153`; SK-E: `blog/cost-of-studying-abroad-for-indian-students.php:154`; LT-E: `blog/cost-of-studying-abroad-for-indian-students.php:156`; LV-E: `blog/cost-of-studying-abroad-for-indian-students.php:157`; UK-F: `blog/cost-of-studying-abroad-for-indian-students.php:53,159`; AE-X: `blog/cost-of-studying-abroad-for-indian-students.php:161`; FAQ answers `blog/cost-of-studying-abroad-for-indian-students.php:49,53` draw on the same official background and planning cautions. | Planning/intro advice `blog/cost-of-studying-abroad-for-indian-students.php:147,163`. Owner attribution, role, location and review display `blog/cost-of-studying-abroad-for-indian-students.php:16,19,20,62,63,143,169,181,183,184`; review dates also in `includes/posts.php`. Shared footer applies. |
| Documents article | DE-V: `blog/documents-needed-to-study-abroad-from-india.php:152`; IT: `blog/documents-needed-to-study-abroad-from-india.php:53,153`; UK-F: `blog/documents-needed-to-study-abroad-from-india.php:155`; UK-E: `blog/documents-needed-to-study-abroad-from-india.php:49,156`; CZ: `blog/documents-needed-to-study-abroad-from-india.php:158`; SK-V2: `blog/documents-needed-to-study-abroad-from-india.php:159`; LT-V: `blog/documents-needed-to-study-abroad-from-india.php:161`; LV-X: `blog/documents-needed-to-study-abroad-from-india.php:162`; FAQ answers `blog/documents-needed-to-study-abroad-from-india.php:49,53` draw on the same official background and planning cautions. | Planning/intro advice `blog/documents-needed-to-study-abroad-from-india.php:149,164`. Owner attribution, role, location and review display `blog/documents-needed-to-study-abroad-from-india.php:16,19,20,62,63,145,170,183,185,186`; review dates also in `includes/posts.php`. Shared footer applies. |
| Scholarships article | DE-S: `blog/scholarships-for-indian-students-study-abroad.php:49,149`; DE-F: `blog/scholarships-for-indian-students-study-abroad.php:150,151`; SK-E: `blog/scholarships-for-indian-students-study-abroad.php:49,153`; UK-F: `blog/scholarships-for-indian-students-study-abroad.php:53,155`; IT: `blog/scholarships-for-indian-students-study-abroad.php:157`; FAQ answers `blog/scholarships-for-indian-students-study-abroad.php:49,53` draw on the same official background and planning cautions. | Planning/intro advice `blog/scholarships-for-indian-students-study-abroad.php:146,159`. Owner attribution, role, location and review display `blog/scholarships-for-indian-students-study-abroad.php:16,19,20,62,63,142,165,175,177,178`; review dates also in `includes/posts.php`. Shared footer applies. |

### Every fresh failed-source dependency and unsupported clause

1. **Documents article, Latvia citation**: `blog/documents-needed-to-study-abroad-from-india.php:72` in BlogPosting citations and line 179 in the visible source list point to failed LV-X. The dependent factual paragraph is line 162. LV-X cannot verify that paragraph as cited. Its Hello Verify/VFS and document content is independently supported by opened LV-I and LV-S. This is a broken citation, not proof that the content is false. The Latvia destination itself cites the working nested student path; it is not affected by this shorter-path failure.
2. **GCC UAE landing citation**: AE-X returned HTTP 500. Every dependent text/source line is listed next. The direct AE document was read and supports those UAE facts, so do not call the content wholly unverified or call the failed landing URL successfully opened.

- GCC dependent factual/FAQ text: `destinations/gcc.php:6,23,31,37,51,59,65,71,85,93,99,105,119,125,140,147,154,161,168`.

- GCC source URL definitions: `destinations/gcc.php:7,24,32,38,52,60,66,72,86,94,100,106,120,126,141,148,155,162,169`. Intro also supplies the page description and WebPage schema through `includes/destination-page.php:17,21,36,44`; FAQ answers supply FAQ schema through lines 24-27.

- Costs article dependent UAE paragraph: `blog/cost-of-studying-abroad-for-indian-students.php:161`; failed URL in schema at line 71 and visible source list at line 177.
3. **GCC Qatar clause not verified**: `destinations/gcc.php:77` says, “In Qatar, international students who do not hold a valid Qatar residence permit, excluding GCC citizens, must apply for a student visa. The embassy page does not list the steps, so confirm them with the institution.” The first sentence matches QA. The claim “The embassy page does not list the steps” does not: QA includes online application information, typical supporting documents and directions to check institutional requirements. The negative claim about the source is unsupported and should not retain an all-lines-verified label in a future authorized content pass. No correction was made here.

### Owner statements shared across the 27 targets

These are published business assertions that no opened official study/visa source can verify. Listing them once with their full scope avoids falsely counting the same footer 27 times as independently checked evidence.

- All 27: base at Coorg/Kodagu/Karnataka, `includes/footer.php:42`; social-account identity links at lines 44-47; phone numbers, email, WhatsApp and no-charge consultation at lines 95-99; ILMERA GROUP ownership/copyright branding at line 103; team review and “Content updated: October 2026” at line 104. The exact contact values are in section 5.
- All 17 locations: Service availability/area served and primary phone, `includes/place-page.php:34`; base, no physical office and phone/WhatsApp/video at line 178. Additional Karnataka, Kodagu and Siddapura assertions are listed above. No office was independently inspected.
- All 7 published destinations: Service description `includes/destination-page.php:22`; each owner overview at `destinations/<country>.php:10`, quoted above; base/no physical office/contact channels at `includes/destination-page.php:168`. The metadata and source renderer do not make those owner fields official evidence.
- All 3 target articles: Fawaz BH authorship, CMO role, Coorg location and review attribution at the exact article lines in the table, plus their `includes/posts.php:50-81` titles/excerpts/date fields. Displaying a review date proves what the page displays, not that the named person personally reviewed it. The factual comparison in this report is separate.

There is no current award-call or partner document for the 8,000-euro assertion. Every published occurrence is listed in section 3. Those are owner-only claims, not officially verified scholarship facts. No claim of admission, visa or award authority follows from counselling.

### Wider published material that must not be mistaken for this target review

The 10 other sitemap pages and both public LLM files were included in discovery and wording checks. That is not a fresh line-by-line verification of all their country, eligibility, career or business assertions. In particular:

- The About founder/student/financial-consultant/first-hand experience claims remain owner-dependent at `about.php:195,201,325,595,696,733`. A named institution is not proof of enrollment, expertise or a partnership.
- The UK prestige/global-recognition/career statement at `services.php:489` was not supported by the reopened Student visa funding/English pages; those are immigration sources, not a ranking or employment guarantee.
- Both LLM files retain wider country/eligibility and business claims outside the current source-reviewed target copy, including the prohibited wording listed in section 7. Their frozen status does not make those claims verified, current or publication-approved.
- `includes/posts.php:12,23,34,45` retains 2025 original publication dates for APS, DSU and the two legacy published articles. The owner says the consultancy was founded in 2026. That history needs an owner explanation, not an invented date correction. The two 2025 legacy articles remain published.

The report therefore does not claim that every line of all public site material has been independently verified. Within the 27 targets, the source-group tables cover all retained official factual claims; all owner-dependent lines and the fresh unsupported clause are separated above. The old journal flags were left untouched, not endorsed wholesale.

## 7. Deploy checklist

Fresh checks: 42 rendered routes, 41 editorial self-canonicals, 37 indexable HTML pages, 4 draft noindex pages and the noindex 404 utility. Every rendered JSON-LD block parsed. Location Service schema has the existing primary phone and no address. The unchanged static sitemap matched generated XML. `tools/check_publication_review.py --base-url http://127.0.0.1:8080` passed its repository checks; it checks stored review records, not current external-page accessibility or the strict LLM wording requirements below.

| Check | PASS / FAIL | Exact result |
|---|---|---|
| Sitemap contains only indexable pages | PASS in PHP adapter | Exactly the 37 URLs in section 1; all drafts and 404 excluded. |
| All sitemap URLs are self-canonical | PASS in PHP adapter | Each has exactly its own clean full URL, including `/blog/` with its trailing slash. |
| No published target has noindex | PASS in PHP adapter | All 27 targets and all 37 published editorial pages allow indexing. The noindex 404 utility is not counted as a published content page. |
| No draft is linked anywhere public | FAIL | No incoming HTML or schema link was found, but `llms.txt:129,130` still links APS and DSU. Both text files were served publicly with HTTP 200. |
| No “free” or “tuition-free” anywhere published | FAIL | No occurrence in the 37 published HTML pages' visible copy, metadata or schema. Both public LLM files still contain the words at the exact lines below. A previous “no new wording” pass is not this test. |
| No university names anywhere published | FAIL | About contains University of Rome Tor Vergata; Services contains Oxford, Cambridge, Imperial and UCL; `llms.txt` additionally lists Imperial College London and University of Manchester. Exact lines below. |
| No em dashes anywhere published | PASS for checked public text | No U+2014 character in all 42 rendered HTML responses, including metadata/schema, or either public LLM file. Report also contains no em dash. |
| Robots points to the sitemap | PASS for file and served content | `robots.txt` ends with `Sitemap: https://ilmerastudyabroad.com/sitemap.xml`. This is not a draft-blocking rule. |
| Every current official citation can be reopened as cited | FAIL | LV-X missing page and AE-X HTTP 500; working official alternatives were read but not substituted. |
| All retained factual statements match reopened sources | FAIL | Qatar no-steps clause at `destinations/gcc.php:77`; owner assertions and the amount are not official facts. |
| Apache routing, redirects and production headers tested | FAIL, not tested here | No native Apache in this workspace; the PHP adapter does not execute `.htaccess`. Tests required below. |

### Exact prohibited-wording and university-name evidence

These are existing failures, not changes introduced or fixed by this report. The frozen LLM files remain byte-identical to the site snapshot used at the start of this phase.

- `llms.txt:3,28,34,42,44,53,94,97,99,102,129,139,155,163,164,185,191,194,200`: existing “free”/“tuition-free” wording, including headings, education claims and consultation descriptions.

- `llms-full.txt:56,57,69,76,79,107,108,111,138`: existing “free”/“tuition-free” wording, including headings, education claims and consultation descriptions.

- `about.php:195,201,325`: University of Rome Tor Vergata in Person/FAQ schema; `about.php:595,696,733`: the same name in visible history, biography and FAQ copy.
- `services.php:489`: Oxford, Cambridge, Imperial and UCL in visible UK copy.
- `llms.txt:58`: Oxford, Cambridge, Imperial College London, University of Manchester and UCL.

Generic words such as “university”, “institution” and “university offer letter” are not named universities. The retained APS URL slug contains “free”, but that page is draft, its slug is frozen, and it is not the reason the published-HTML wording check passes or fails. The public LLM wording still fails even without counting that slug.

### Apache checks still required before deployment

1. Enable the intended Apache configuration and PHP handler; verify `mod_rewrite`, allowed `.htaccess` overrides and the actual directory root. `.htaccess:1-2` enables rewriting and sets `DirectoryIndex index.php index.html`. Confirm `/` and `/blog/` resolve correctly without duplicate index URLs.
2. Test `.htaccess:5-7`: `/sitemap` and `/sitemap.php` must redirect once to `/sitemap.xml`, preserve intended query behavior, and return the generated XML without a loop. `[END]` requires Apache 2.4. Verify XML status, content type and the same 37 URLs on staging.
3. Test `.htaccess:10-11`: direct `.php` requests must redirect to the intended clean URL with correct status, path and query preservation. Include ordinary pages, all article routes and destination/location wrappers. Check that internal rewrites do not cause visible redirects or loops.
4. Test `.htaccess:14-16`: clean file routes must resolve to their PHP file, directories must remain directories, `/blog/` must keep its declared canonical, and unknown paths must return a genuine 404. The adapter served `/404` itself with HTTP 200 and noindex; that is not proof of a production 404 response. This file contains no `ErrorDocument` rule, so do not assume the branded page is the server's error handler.
5. Test direct access to all four withheld clean URLs and `.php` aliases. Their crawler instructions must survive redirects and the production PHP handler. They currently remain readable; noindex does not make them private. Test direct `/destinations/`, `/places/`, `/includes/`, report and review-data paths against the intended hosting access policy; `robots.txt` is not access control and this `.htaccess` does not establish such protection.
6. Check the real HTTPS host/canonical-host redirect policy, response headers, robots, external assets, form/contact delivery and phone/WhatsApp destinations on staging. The current `.htaccess` has no explicit HTTP-to-HTTPS or www-to-apex rule. A proxy or host setting might provide it, but that was not demonstrated here.

The long-running sandbox PHP adapter exhausted its WASM memory during the first read attempt. It was restarted without changing a site file, then the complete fresh route and publication checks passed. That sandbox restart is not evidence of a production Apache fix. No production deployment, native Apache check, contact delivery test or live search-engine inspection was performed.

**Release recommendation: FAIL for an unconditional deploy approval.** The report records the current published state, not an instruction to alter it. The public LLM contradictions, name/wording restrictions, citation failures, Qatar clause, owner evidence and Apache tests need an explicitly authorized follow-up. No site corrections, status changes, sitemap changes or LLM edits were made in Phase 15.

## 8. Questions only the owner can answer

- For the Italy, Home, About, Services, Contact and DSU pages, which current award call and signed partner authority support the “up to 8,000 euros” claim for the programmes actually offered?
- For all 17 location pages, is the stated service area accurate and is ILMERA still based in Coorg, Kodagu with no physical office and counselling by phone, WhatsApp and video call?
- For the shared footer on all target pages, are both Indian phone numbers, the +421 WhatsApp number, the email and the no-charge consultation offer current and authorized?
- For Germany, Latvia, Slovakia and GCC, what admissions, scholarship and visa-document services does ILMERA actually provide, in which countries, and under what authority and charging terms?
- For the three target articles, did Fawaz BH author or approve the content and the displayed review date, and is CMO still the correct role?
- For the APS article, do you authorize the APS India host to be considered in a future source-policy review?
- For About, what current evidence supports the founder's student status, financial-consultant role and claimed first-hand application experience?
- For the two published legacy articles and the held APS/DSU articles, what explains the 2025 publication dates when the consultancy was founded in 2026?
- For `llms.txt` and `llms-full.txt`, do you authorize a separate future update to remove draft links and reconcile the old claims with the approved published copy?
