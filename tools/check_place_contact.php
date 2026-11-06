<?php
/** Contact facts must remain existing sitewide details, never city offices. */
$root = dirname(__DIR__);
$contact = file_get_contents($root . '/contact.php');
$template = file_get_contents($root . '/includes/place-page.php');
foreach (['WhatsApp', 'video'] as $channel) {
    if (stripos($contact, $channel) === false) throw new RuntimeException('Contact channel is not established');
}
preg_match_all("/'telephone' => '(\\+[0-9]+)'/", $template, $phones);
if (count($phones[1]) !== 1) throw new RuntimeException('Unexpected location contact schema');
foreach ($phones[1] as $phone) {
    if (strpos($contact, '"telephone": "' . $phone . '"') === false) throw new RuntimeException('New contact number');
}
if (strpos($template, "'@type' => 'LocalBusiness'") !== false || strpos($template, 'streetAddress') !== false) throw new RuntimeException('Unverified local business presence');
foreach (glob($root . '/places/*.php') as $file) {
    $data = include $file;
    if ($data['local_facts_used'] !== false || $data['local_fact_sources'] !== []) throw new RuntimeException('Local facts need an opened-source review');
}
echo "PASS existing contact channels, shared phone and no local office schema\n";
