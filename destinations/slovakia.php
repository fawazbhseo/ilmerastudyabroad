<?php
$eu = 'https://education.ec.europa.eu/study-in-europe/country-profiles/slovakia';
$euLabel = 'Study in Europe (European Commission): Slovakia country profile';
$iom = 'https://www.mic.iom.sk/en/news/894-studying-at-a-university-in-slovakia.html';
$iomLabel = 'IOM Migration Information Centre Slovakia: Studying at a university in Slovakia';
$visa = 'https://www.mzv.sk/en/web/dilli-en/services/national-visa';
$visaLabel = 'Embassy of the Slovak Republic in New Delhi: National visa';
$contact = 'https://mzv.sk/en/web/dilli-en/contact-us';
$contactLabel = 'Embassy of the Slovak Republic in New Delhi: Contact and appointments';
$d = '2026-10-15';

return [
    'slug' => 'slovakia',
    'name' => 'Slovakia',
    'status' => 'draft',
    'intro_answer' => 'Studying in the Slovak language can be free of charge for full-time students. Programmes taught in English or other foreign languages are charged tuition, and the European Commission study portal gives a range of roughly 750 to 11,000 euros a year. Students apply directly to the university or faculty.',
    'intro_answer_source_url' => $eu,
    'intro_answer_source_label' => $euLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'Standard admissions and visa support.',
    'summary_provenance' => 'git:7dfac93:llms-full.txt section 4.7',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['education.ec.europa.eu', 'mzv.sk', 'mic.iom.sk'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [
        ['text' => 'Programmes taught in foreign languages such as English carry tuition. The European Commission study portal gives an approximate range of 750 to 11,000 euros a year, with some programmes cheaper depending on the institution, and notes that studies in Slovak can be free of charge.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
        ['text' => 'At public universities the fee rules are the same for Slovak citizens and foreigners. Full-time study in Slovak is free except in cases set by law, such as exceeding the standard length of study, and full-time study in another language is charged each year regardless of nationality. Private universities set their own fees.', 'source_url' => $iom, 'source_label' => $iomLabel, 'checked_on' => $d],
        ['text' => 'The study portal estimates a total yearly budget of around 7,000 to 15,000 euros, including tuition and living costs.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
    ],
    'scholarships' => [
        ['text' => 'The National Scholarship Programme of the Slovak Republic supports study, research and teaching stays and is open to international students, PhD candidates and researchers. Check the programme page for current eligibility and deadlines.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
    ],
    'visa_steps' => [
        ['text' => 'Applications for a Slovak national visa are submitted at a diplomatic mission of the Slovak Republic. Indian applicants use the Embassy in New Delhi.', 'source_url' => $visa, 'source_label' => $visaLabel, 'checked_on' => $d],
        ['text' => 'The New Delhi embassy states that appointments for national D visas for purposes other than low-skilled employment are arranged by email to cons.delhi@mzv.sk. Check the embassy page for the current booking method before applying.', 'source_url' => $contact, 'source_label' => $contactLabel, 'checked_on' => $d],
    ],
    'intakes' => [],
    'documents' => [
        ['text' => 'The embassy basic document list for a national visa includes an application form, proof of accommodation in Slovakia, and proof of sufficient means of subsistence for the stay. Check the embassy page for the list that applies to study.', 'source_url' => $visa, 'source_label' => $visaLabel, 'checked_on' => $d],
        ['text' => 'Original documents are needed for the temporary residence application submitted with the national D visa application, and they must be no older than 90 days on the day of submission.', 'source_url' => $contact, 'source_label' => $contactLabel, 'checked_on' => $d],
        ['text' => 'A student with temporary residence for study should have health insurance covering the whole stay in Slovakia.', 'source_url' => $iom, 'source_label' => $iomLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [],
    'faqs' => [
        ['question' => 'Is study in Slovakia free for Indian students?', 'answer' => 'Full-time study in the Slovak language at public universities is free for both Slovaks and foreigners, except in cases set by law. Programmes taught in English or other languages are charged for every student regardless of nationality.', 'source_url' => $iom, 'source_label' => $iomLabel, 'checked_on' => $d],
        ['question' => 'Where do Indian students apply for a Slovak national visa?', 'answer' => 'At the Embassy of the Slovak Republic in New Delhi. Check the embassy page for the current appointment method.', 'source_url' => $visa, 'source_label' => $visaLabel, 'checked_on' => $d],
        ['question' => 'Do students apply directly to Slovak universities?', 'answer' => 'Yes. The European Commission study portal says students apply directly to the chosen faculty or university.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
        ['question' => 'Do international students need health insurance in Slovakia?', 'answer' => 'A student with temporary residence for study should have health insurance that covers the whole stay in Slovakia.', 'source_url' => $iom, 'source_label' => $iomLabel, 'checked_on' => $d],
    ],
];
