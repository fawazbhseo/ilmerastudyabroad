<?php
$portal = 'https://www.studyin.cz/plan-your-studies/tuition-fees/';
$portalLabel = 'Study in Czechia: Tuition fees (official study portal)';
$delhiMain = 'https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/long_term_visa_and_long_term_residence.html';
$delhiMainLabel = 'Embassy of the Czech Republic in New Delhi: Long-term visa and residence permit application';
$delhiBook = 'https://mzv.gov.cz/newdelhi/en/ko/visa_information/long_term_visa_long_term_residence/booking_appointments_for_submission_of.html';
$delhiBookLabel = 'Embassy of the Czech Republic in New Delhi: Booking appointments for study applications (India)';
$delhiReq = 'https://mzv.gov.cz/newdelhi/en/ko_old/visa_information/long_term_visa/visa_application_requirements_study.html';
$delhiReqLabel = 'Embassy of the Czech Republic in New Delhi: Visa application requirements for study';
$ipc = 'https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/long-term-visa/long-term-visa-for-the-purpose-of-studies';
$ipcLabel = 'Ministry of the Interior (ipc.gov.cz): Long-term visa for the purpose of studies';
$funds = 'https://mv.gov.cz/mvcren/article/proof-of-funds-for-the-purposes-of-a-long-term-visa.aspx';
$fundsLabel = 'Ministry of the Interior: Proof of funds for a long-term visa';
$d = '2026-10-15';

return [
    'slug' => 'czech-republic',
    'name' => 'Czech Republic',
    'status' => 'draft',
    'intro_answer' => 'Public universities in the Czech Republic teach programmes in Czech free of tuition fees for students of every nationality. Programmes taught in English or other languages are charged by each university, and the national study portal gives a range of 0 to 22,350 USD a year. Check each university for exact fees.',
    'intro_answer_source_url' => $portal,
    'intro_answer_source_label' => $portalLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'Exact costs vary by university, city and programme, so check the official university page for current fees.',
    'summary_provenance' => 'git:7dfac93:services.php #czech-republic',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['studyin.cz', 'mzv.gov.cz', 'ipc.gov.cz', 'mv.gov.cz'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [
        ['text' => 'Czech-language programmes at public and state universities carry no tuition fees for students of any nationality. Some charges can still apply, including fees for admission processing, for studying beyond the set time limit, and for studying in a foreign language.', 'source_url' => $portal, 'source_label' => $portalLabel, 'checked_on' => $d],
        ['text' => 'Private institutions set their own fees, and programmes taught in a foreign language are priced by each university. The national study portal states a range of 0 to 22,350 USD a year depending on the institution and programme.', 'source_url' => $portal, 'source_label' => $portalLabel, 'checked_on' => $d],
    ],
    'scholarships' => [],
    'visa_steps' => [
        ['text' => 'Indian applicants for a long-term visa or long-term residence permit for study submit the application in person at the Czech Embassy in New Delhi, and an appointment must be booked beforehand.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
        ['text' => 'Appointments for Indian study applicants are given through registration windows announced by the embassy. A missed or late appointment is cancelled, so a new one must be arranged. Check the embassy page for the current dates.', 'source_url' => $delhiBook, 'source_label' => $delhiBookLabel, 'checked_on' => $d],
        ['text' => 'The Ministry of the Interior decides study visa and study residence permit applications within 60 days.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
        ['text' => 'A long-term visa, including extensions, can be valid for a maximum of 1 year in total. A longer stay needs a long-term residence permit, which can also be applied for directly at the embassy.', 'source_url' => $ipc, 'source_label' => $ipcLabel, 'checked_on' => $d],
    ],
    'intakes' => [],
    'documents' => [
        ['text' => 'A valid passport that is not older than 10 years, has at least 2 free pages, and stays valid for at least 3 months beyond the visa.', 'source_url' => $delhiReq, 'source_label' => $delhiReqLabel, 'checked_on' => $d],
        ['text' => 'The embassy requirements list an original enrolment letter from the university, described as issued in Czech, and a police clearance certificate. Indian documents need an apostille stamp.', 'source_url' => $delhiReq, 'source_label' => $delhiReqLabel, 'checked_on' => $d],
        ['text' => 'All documents submitted with the application must be in Czech, although bank account statements may be accepted without a translation.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
        ['text' => 'Comprehensive medical insurance covering the whole permitted stay must be shown.', 'source_url' => $ipc, 'source_label' => $ipcLabel, 'checked_on' => $d],
        ['text' => 'Proof of funds is calculated as a multiple of the existential minimum set by Czech rules. For study permits, a pledge from a public body or legal entity, or a document showing that the school covers all costs, can be accepted instead. Check the current amount on the source page.', 'source_url' => $funds, 'source_label' => $fundsLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [],
    'faqs' => [
        ['question' => 'Is tuition free in the Czech Republic for Indian students?', 'answer' => 'Only for programmes taught in Czech at public and state universities. Programmes taught in English or other languages are priced by each university, and other fees such as admission processing can apply.', 'source_url' => $portal, 'source_label' => $portalLabel, 'checked_on' => $d],
        ['question' => 'Where do Indian students apply for a Czech study visa?', 'answer' => 'In person at the Czech Embassy in New Delhi, after booking an appointment through the embassy process.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
        ['question' => 'How long does a Czech study visa take?', 'answer' => 'The Ministry of the Interior decides study visa and study residence permit applications within 60 days.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
        ['question' => 'Do documents need to be translated into Czech?', 'answer' => 'Yes. Documents submitted with the application must be in Czech, although bank statements may be accepted without a translation.', 'source_url' => $delhiMain, 'source_label' => $delhiMainLabel, 'checked_on' => $d],
    ],
];
