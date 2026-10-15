<?php
$mig = 'https://migracija.lrv.lt/en/structure-and-contacts/information-for-visitors/services-for-persons-abroad/temporary-residence-permit-and-national-visa-services/republic-of-india/';
$migLabel = 'Migration Department of Lithuania: Services for persons abroad, Republic of India';
$eu = 'https://education.ec.europa.eu/study-in-europe/country-profiles/lithuania';
$euLabel = 'Study in Europe (European Commission): Lithuania country profile';
$vt = 'https://vilniustech.lt/en/international-students/immigration-regulations/immigration-regulations-full-time/';
$vtLabel = 'VILNIUS TECH: Immigration regulations for full-time students';
$d = '2026-10-15';

return [
    'slug' => 'lithuania',
    'name' => 'Lithuania',
    'status' => 'draft',
    'intro_answer' => 'Tuition fees vary by university and programme, and the European Commission study portal puts the average at from 1,300 euros a year for bachelor programmes, from 2,300 for master programmes and from 8,400 for doctoral programmes. More than 500 programmes are taught in English. Check each university for exact fees.',
    'intro_answer_source_url' => $eu,
    'intro_answer_source_label' => $euLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'English requirements vary by university and programme.',
    'summary_provenance' => 'git:7dfac93:services.php #lithuania',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['migracija.lrv.lt', 'education.ec.europa.eu', 'vilniustech.lt'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [
        ['text' => 'The European Commission study portal gives average tuition of from 1,300 euros a year for bachelor programmes, from 2,300 for master programmes and from 8,400 for doctoral programmes, and estimates living costs at 500 to 800 euros a month. Fees vary by institution and programme.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
    ],
    'scholarships' => [],
    'visa_steps' => [
        ['text' => 'University guidance states that since 1 July 2023 Lithuania no longer issues national D visas to full-time students at registered higher education institutions. Full-time students apply for a temporary residence permit instead, through the Lithuanian migration system at migracija.lt.', 'source_url' => $vt, 'source_label' => $vtLabel, 'checked_on' => $d],
        ['text' => 'For Indian applicants, the Migration Department lists VFS Global centres in New Delhi and Mumbai for temporary residence permits. Appointments are booked only through the Lithuanian migration information system MIGRIS, after the application is submitted.', 'source_url' => $mig, 'source_label' => $migLabel, 'checked_on' => $d],
        ['text' => 'The external service provider applies a customer service fee of 110 euros. The state fee for processing the application is listed separately by the Migration Department.', 'source_url' => $mig, 'source_label' => $migLabel, 'checked_on' => $d],
    ],
    'intakes' => [],
    'documents' => [
        ['text' => 'Health insurance is mandatory for international students, and non-EU students must obtain private insurance or register with the Lithuanian health system.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
        ['text' => 'Proof of sufficient funds for subsistence is required with the residence permit application, and university guidance says the funds can be in the student or a parent bank account. The amount changes, so check the current figure with the Migration Department.', 'source_url' => $vt, 'source_label' => $vtLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [],
    'faqs' => [
        ['question' => 'Do Indian students need a national visa to study in Lithuania?', 'answer' => 'According to university guidance, since 1 July 2023 full-time students at registered Lithuanian higher education institutions apply for a temporary residence permit instead of a national D visa. Check the Migration Department page for India for the current process.', 'source_url' => $vt, 'source_label' => $vtLabel, 'checked_on' => $d],
        ['question' => 'Where do Indian students submit the Lithuanian residence permit application?', 'answer' => 'Applications go through the Lithuanian migration system MIGRIS, and the Migration Department lists VFS Global centres in New Delhi and Mumbai as the service points for Indian applicants.', 'source_url' => $mig, 'source_label' => $migLabel, 'checked_on' => $d],
        ['question' => 'How much is tuition in Lithuania?', 'answer' => 'Fees vary by university and programme. The European Commission study portal gives averages from 1,300 euros a year for bachelor, 2,300 for master and 8,400 for doctoral programmes.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
        ['question' => 'Is health insurance required for students in Lithuania?', 'answer' => 'Yes. Health insurance is mandatory, and non-EU students must obtain private insurance or register with the Lithuanian health system.', 'source_url' => $eu, 'source_label' => $euLabel, 'checked_on' => $d],
    ],
];
