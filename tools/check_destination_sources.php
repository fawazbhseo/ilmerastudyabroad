<?php
/** Run with PHP CLI; exercises fail-closed source-review eligibility. */
require_once dirname(__DIR__) . '/includes/destination-data.php';
$checks = 0;
$check = static function ($condition) use (&$checks) {
    if (!$condition) throw new RuntimeException('Destination evidence gate failed at check ' . ($checks + 1));
    $checks++;
};
$germany = ilmera_destination_load('germany');
$check(ilmera_destination_indexable($germany));
$copy = $germany;
$copy['status'] = 'draft';
$check(!ilmera_destination_indexable($copy));
foreach (['text', 'source_url', 'source_label', 'checked_on'] as $field) {
    $copy = $germany;
    $copy['costs'][0][$field] .= ' changed';
    $check(!ilmera_destination_indexable($copy));
}
$copy = $germany;
$copy['faqs'][0]['question'] .= ' changed';
$check(!ilmera_destination_indexable($copy));
$copy = $germany;
$copy['intro_answer'] .= ' changed';
$check(!ilmera_destination_indexable($copy));
$copy = $germany;
$copy['faqs'] = [];
$check(!ilmera_destination_indexable($copy));
$copy = $germany;
$copy['publication_review']['original_sources_resolved'] = false;
$check(!ilmera_destination_indexable($copy));
foreach (['czech-republic', 'russia'] as $slug) {
    $copy = ilmera_destination_load($slug);
    $copy['status'] = 'published';
    $check(!ilmera_destination_indexable($copy));
}
$copy = $germany;
$copy['review_notice'] = 'An unreviewed factual statement.';
$check(!ilmera_destination_indexable($copy));
$gcc = ilmera_destination_load('gcc');
$check(ilmera_destination_indexable($gcc));
$gcc['scope_note'] = '';
$check(!ilmera_destination_indexable($gcc));
echo json_encode(['passed' => $checks]) . PHP_EOL;
