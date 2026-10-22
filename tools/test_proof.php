<?php
require_once dirname(__DIR__) . '/includes/proof.php';
$data = include dirname(__DIR__) . '/data/proof.php';
$public = ilmera_registration_public($data);
if (!$public || $public['identifier'] !== ['@type'=>'PropertyValue','propertyID'=>'Udyam','value'=>'UDYAM-KR-18-0023330']) throw new RuntimeException('Exact registration missing');
foreach (['/about','/contact','/services','/study-in-germany'] as $path) {
    $result = ilmera_proof_blocks($path, $data);
    if ($result['identifiers'] !== [$public['identifier']] || $result['offers'] || $result['founder_description']) throw new RuntimeException('Unexpected proof schema');
    $visible = in_array($path, ['/about','/contact'], true);
    if (($result['html'] !== '') !== $visible) throw new RuntimeException('Wrong visible registration scope');
    if ($visible && (strpos($result['html'], $public['statement']) === false || strpos(html_entity_decode($result['html'], ENT_QUOTES), $public['caveat']) === false)) throw new RuntimeException('Exact block missing');
    if (preg_match('~2026-10-22|Owner-supplied|source|reviewed_on~', $result['html'])) throw new RuntimeException('Private provenance leaked');
}
foreach (array_keys($data['registration_details'][0]) as $key) {
    $changed = $data;
    unset($changed['registration_details'][0][$key]);
    if (ilmera_registration_public($changed) !== null) throw new RuntimeException('Missing field accepted');
    $changed = $data;
    $changed['registration_details'][0][$key] = 'invalid';
    if (ilmera_registration_public($changed) !== null) throw new RuntimeException('Modified field accepted');
}
foreach (['address','telephone','email','socialCategory','nic','size','date','source_url'] as $key) {
    $changed = $data;
    $changed['registration_details'][0][$key] = 'not-public';
    if (ilmera_registration_public($changed) !== null) throw new RuntimeException('Extra certificate field accepted');
}
$empty = $data; $empty['registration_details'] = [];
if (ilmera_proof_blocks('/about', $empty) !== ['html'=>'','identifiers'=>[],'offers'=>[],'founder_description'=>null]) throw new RuntimeException('Empty slots rendered');
foreach ([null, [], ['approved'=>true], ['approved'=>true,'source_url'=>'http://example.test','reviewed_on'=>'2026-10-16','label'=>'Fixture','value'=>'fixture-id'], $data['registration_details'][0]] as $record) {
    if (ilmera_proof_approved($record, ['label','value'])) throw new RuntimeException('Generic gate weakened');
}
echo "PASS exact private-source registration projection, field mutations, privacy and unchanged generic gates\n";
