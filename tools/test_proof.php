<?php
require_once dirname(__DIR__) . '/includes/proof.php';
$data = include dirname(__DIR__) . '/data/proof.php';
foreach (['/about','/contact','/services','/study-in-germany'] as $path) {
    $result = ilmera_proof_blocks($path, $data);
    if ($result !== ['html'=>'','identifiers'=>[],'offers'=>[],'founder_description'=>null]) throw new RuntimeException('Empty slots must render no placeholder or schema');
}
$pending = $data;
$pending['registration_details'] = [['approved'=>false,'label'=>'Fixture only','value'=>'fixture-id']];
if (ilmera_proof_blocks('/about', $pending)['html'] !== '') throw new RuntimeException('Unapproved record rendered');
foreach ([null, [], ['approved'=>true], ['approved'=>true,'source_url'=>'http://example.test','reviewed_on'=>'2026-10-16','label'=>'Fixture','value'=>'fixture-id']] as $record) {
    if (ilmera_proof_approved($record, ['label','value'])) throw new RuntimeException('Incomplete/unsecured proof accepted');
}
echo "PASS empty, pending, incomplete and unsecured proof gates; no student review fixture invented\n";
