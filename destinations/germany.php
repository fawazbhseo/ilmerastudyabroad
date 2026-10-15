<?php
$daad = 'https://www.daad.de/en/studying-in-germany/living-in-germany/finances/';
$daadLabel = 'DAAD: Costs of education and living in Germany';
$d = '2026-10-15';

return [
    'slug' => 'germany',
    'name' => 'Germany',
    'status' => 'draft',
    'intro_answer' => 'Most state-funded universities in Germany charge no tuition fees for most degree courses, but every student pays a semester contribution of about 100 to 350 euros. Baden-Württemberg charges non-EU students 1,500 euros per semester, and private institutions charge more. Check each university for its exact fees.',
    'intro_answer_source_url' => $daad,
    'intro_answer_source_label' => $daadLabel,
    'intro_answer_checked_on' => $d,
    'ilmera_summary' => 'ILMERA confirms the rule for each university before applying.',
    'summary_provenance' => 'git:7dfac93:llms-full.txt section 4.1',
    'facts_last_checked' => $d,
    'official_source_hosts' => ['daad.de'],
    'who_its_for' => [],
    'english_requirements' => [],
    'costs' => [
        ['text' => 'There are generally no fees for courses at most state-funded higher education institutions in Germany. Private institutions may charge substantial fees for their degree programmes.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['text' => 'The state of Baden-Württemberg charges non-EU citizens tuition fees of 1,500 euros per semester for its degree programmes.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['text' => 'DAAD states that from the winter semester 2024/2025 the Technical University of Munich also charges tuition fees to international students from outside the EU and EEA: 2,000 or 3,000 euros per semester for bachelor programmes and 4,000 or 6,000 euros for master programmes. Check the university page for current amounts.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['text' => 'Every student pays a semester contribution of between 100 and 350 euros. It is separate from tuition fees, is paid at enrolment and before each new semester, and at many institutions also includes a public transport pass.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
    ],
    'scholarships' => [],
    'visa_steps' => [],
    'intakes' => [],
    'documents' => [
        ['text' => 'Students from outside the EU or EEA must present proof of financial resources already when they apply for a study visa. Check the exact amount and accepted forms of proof with the German mission or DAAD before applying.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
    ],
    'work_and_stay' => [
        ['text' => 'International students do not have unlimited permission to work in Germany. Check the current rules before planning to earn money during study.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
    ],
    'faqs' => [
        ['question' => 'Is tuition free in Germany for Indian students?', 'answer' => 'At most state-funded universities there are generally no fees for courses, but every student pays a semester contribution of 100 to 350 euros. Baden-Württemberg charges non-EU students 1,500 euros per semester, the Technical University of Munich charges non-EU students from winter 2024/2025, and private institutions charge more.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['question' => 'What is the semester contribution in Germany?', 'answer' => 'It is a payment of 100 to 350 euros that every student makes at enrolment and before each new semester. It is separate from tuition fees and at many institutions includes a public transport pass.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['question' => 'Do students from India need to show money for a German study visa?', 'answer' => 'Yes. Students from outside the EU or EEA must present proof of financial resources when they apply for a study visa.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
        ['question' => 'Can international students work in Germany while studying?', 'answer' => 'Only within limits. International students do not have unlimited permission to work, so the current rules should be checked first.', 'source_url' => $daad, 'source_label' => $daadLabel, 'checked_on' => $d],
    ],
];
