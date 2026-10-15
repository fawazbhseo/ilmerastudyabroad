<?php
$blr = 'https://consbangalore.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/study-in-italy/';
$blrLabel = 'Consulate General of Italy in Bengaluru: Study in Italy';
$d = '2026-10-15';

return [
    'slug' => 'italy',
    'name' => 'Italy',
    'status' => 'draft',
    'intro_answer' => 'Indian students who want to study in Italy first apply for admission to the Italian institution, then complete pre-enrolment on the Universitaly portal, then apply for a study visa by appointment at a VFS centre. Each institution sets its own admission requirements, deadlines and tuition fees.',
    'intro_answer_source_url' => $blr,
    'intro_answer_source_label' => $blrLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'ILMERA helps identify scholarships, government grants, and stipend programmes suited to a student\'s profile, most notably Italy\'s DSU (Diritto allo Studio Universitario) scholarship.',
    'summary_provenance' => 'git:7dfac93:llms-full.txt section 3.4',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['consbangalore.esteri.it'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [],
    'scholarships' => [],
    'visa_steps' => [
        ['text' => 'The consulate lists three mandatory steps: apply for admission on the chosen institution website within its deadline, apply online for pre-enrolment on the Universitaly portal within the deadlines, and once pre-enrolled apply for the visa.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['text' => 'A D visa is needed if the course lasts more than 90 days, and a C visa if it lasts less than 90 days.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['text' => 'Visa applications are submitted only by prior appointment at a VFS centre. The consulate names Bangalore, Chennai and Hyderabad.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['text' => 'All students must attend a mandatory video interview when they submit the visa application.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['text' => 'Under Italian law, processing of a D visa application can take up to 90 days from the day the consulate receives it. If the consulate asks for extra documents, the total time is likely to be longer.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
    ],
    'intakes' => [],
    'documents' => [
        ['text' => 'The consulate publishes an official study visa checklist for 2025-2026 and recommends submitting every listed document at the start, to avoid delay. Check the consulate page for the checklist that applies to your intake.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['text' => 'If the Italian institution requires a Declaration of Value (DOV) and the previous studies were completed in an Indian state under the Bengaluru consulate, the consulate publishes a separate DOV checklist.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [],
    'faqs' => [
        ['question' => 'Do Indian students need Universitaly pre-enrolment to study in Italy?', 'answer' => 'Yes. The consulate lists pre-enrolment on the Universitaly portal, within the deadlines, as a mandatory step after applying for admission and before applying for the visa.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['question' => 'Which Italian study visa do Indian students need?', 'answer' => 'A D visa for courses lasting more than 90 days and a C visa for courses lasting less than 90 days.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['question' => 'Is there an interview for the Italian study visa?', 'answer' => 'Yes. All students must attend a mandatory video interview when they submit the application at the VFS centre.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
        ['question' => 'How can students avoid fake emails about the Italian study visa?', 'answer' => 'The Consulate General of Italy in Bengaluru states that its official visa email is bangalore.visa@esteri.it, and it warns students to ignore messages from other addresses that claim to come from the consulate and never to share personal or financial information with them.', 'source_url' => $blr, 'source_label' => $blrLabel, 'checked_on' => $d],
    ],
];
