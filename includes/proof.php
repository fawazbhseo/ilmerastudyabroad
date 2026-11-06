<?php
/** Fail-closed owner proof. Empty/unapproved/incomplete records render nothing. */
function ilmera_proof_approved($record, $fields, $consent = false)
{
    if (!is_array($record) || ($record['approved'] ?? false) !== true) return false;
    if ($consent && ($record['consent'] ?? false) !== true) return false;
    foreach (array_merge($fields, ['source_url', 'reviewed_on']) as $field) {
        if (!isset($record[$field]) || !is_scalar($record[$field]) || trim((string)$record[$field]) === '') return false;
    }
    if (!preg_match('~^https://[^\s]+$~D', $record['source_url']) || !preg_match('~^\d{4}-\d{2}-\d{2}$~D', $record['reviewed_on'])) return false;
    $text = json_encode($record, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if (preg_match('~\b(?:free|best|top|leading|office|offices)\b|tuition[- ]?free|no\.?\s*1|\x{2014}~iu', $text)) return false;
    $names = file(dirname(__DIR__) . '/tools/blocked-names.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($names as $name) {
        if ($name[0] !== '#' && preg_match('~(?<!\w)' . preg_quote($name, '~') . '(?!\w)~iu', $text)) return false;
    }
    return true;
}

/** Private owner provenance: only this exact record, no extra certificate fields. */
function ilmera_registration_public($data = null)
{
    if ($data === null) $data = include dirname(__DIR__) . '/data/proof.php';
    $expected = [
        'label' => 'Udyam registration',
        'value' => 'UDYAM-KR-18-0023330',
        'approved' => true,
        'source' => 'Owner-supplied Udyam certificate',
        'reviewed_on' => '2026-10-22',
    ];
    if (($data['registration_details'] ?? null) !== [$expected]) return null;
    return [
        'statement' => 'ILMERA Study Abroad is registered under Udyam (MSME), registration number '.$expected['value'].'.',
        'caveat' => "Udyam registration is a business registration. It does not mean any authority has approved or endorsed ILMERA's services.",
        'identifier' => ['@type'=>'PropertyValue', 'propertyID'=>'Udyam', 'value'=>$expected['value']],
    ];
}

function ilmera_proof_blocks($path, $data = null)
{
    if ($data === null) $data = include dirname(__DIR__) . '/data/proof.php';
    $result = ['html'=>'', 'identifiers'=>[], 'offers'=>[], 'founder_description'=>null];
    $blocks = [];
    $escape = static function($value) { return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); };
    if ($path === '/about') {
        foreach ($data['testimonials'] ?? [] as $record) {
            if (!ilmera_proof_approved($record, ['display_name','text'], true)) continue;
            $blocks[] = '<blockquote><p>'.$escape($record['text']).'</p><cite>'.$escape($record['display_name']).'</cite></blockquote>';
        }
        $record = $data['placement_count'] ?? null;
        if (ilmera_proof_approved($record, ['value','definition','period']) && is_int($record['value']) && $record['value'] >= 0) {
            $blocks[] = '<p>'.$escape($record['definition']).': '.$escape($record['value']).' ('.$escape($record['period']).').</p>';
        }
        foreach ($data['founder_bios'] ?? [] as $record) {
            if (($record['name'] ?? '') !== 'Jabir KJ' || !ilmera_proof_approved($record, ['name','bio'], true)) continue;
            $blocks[] = '<h3>'.$escape($record['name']).'</h3><p>'.$escape($record['bio']).'</p>';
            $result['founder_description'] = $record['bio'];
        }
    }
    $registration = ilmera_registration_public($data);
    if ($registration !== null) {
        // One canonical Organization identifier, independent of the current page.
        $result['identifiers'][] = $registration['identifier'];
        if (in_array($path, ['/about','/contact'], true)) {
            $blocks[] = '<p>'.$escape($registration['statement']).'</p><p>'.$escape($registration['caveat']).'</p>';
        }
    }
    if (in_array($path, ['/services','/contact'], true)) {
        $entity = json_decode(file_get_contents(dirname(__DIR__).'/data/entity.json'), true);
        foreach ($data['fee_information'] ?? [] as $record) {
            if (!ilmera_proof_approved($record, ['service','scope','price','currency','refund_terms']) || !in_array($record['service'], $entity['services'], true)) continue;
            if (!is_numeric($record['price']) || (float)$record['price'] < 0 || !preg_match('~^[A-Z]{3}$~D', $record['currency'])) continue;
            $blocks[] = '<h3>'.$escape($record['service']).'</h3><p>'.$escape($record['scope']).': '.$escape($record['currency']).' '.$escape($record['price']).'. '.$escape($record['refund_terms']).'</p>';
            $result['offers'][] = ['@type'=>'Offer','price'=>(string)$record['price'],'priceCurrency'=>$record['currency'],'description'=>$record['scope'].' '.$record['refund_terms'],'itemOffered'=>['@type'=>'Service','name'=>$record['service']]];
        }
    }
    if ($blocks) $result['html'] = '<section class="owner-proof" style="max-width:760px;margin:32px auto;padding:24px;"><h2>Published service information</h2>'.implode('', $blocks).'</section>';
    return $result;
}
