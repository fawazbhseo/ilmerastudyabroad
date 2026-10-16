<?php
/** Fail-closed editorial eligibility, without modifying production records. */
require_once dirname(__DIR__) . '/includes/place-data.php';
$checks = 0;
$check = static function ($condition) use (&$checks) {
    if (!$condition) throw new RuntimeException('Location publication gate failed at ' . ($checks + 1));
    $checks++;
};
foreach (glob(dirname(__DIR__) . '/places/*.php') as $file) {
    $place = ilmera_place_load(basename($file, '.php'));
    $check(ilmera_place_indexable($place));
}
$base = ilmera_place_load('karnataka');
foreach (['intro_answer', 'heading', 'meta_description', 'page_title'] as $field) {
    $copy = $base;
    $copy[$field] .= ' changed';
    $check(!ilmera_place_indexable($copy));
}
$copy = $base;
$copy['sections'] = [];
$check(!ilmera_place_indexable($copy));
$copy = $base;
$copy['faqs'][0]['answer'] .= ' changed';
$check(!ilmera_place_indexable($copy));
$copy = $base;
$copy['local_facts_used'] = true;
$check(!ilmera_place_indexable($copy));
$copy = $base;
$copy['status'] = 'draft';
$check(!ilmera_place_indexable($copy));
echo json_encode(['passed' => $checks]) . PHP_EOL;
