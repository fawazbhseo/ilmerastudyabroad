<?php
require_once __DIR__ . '/service-scope.php';
/** One reviewed identity, independent of page-specific SEO descriptions. */
function ilmera_entity_data()
{
    return json_decode(file_get_contents(dirname(__DIR__) . '/data/entity.json'), true);
}

function ilmera_entity_graph($path)
{
    $data = ilmera_entity_data();
    $graph = [
        '@type'=>'Organization', '@id'=>'https://ilmerastudyabroad.com/#organization',
        'name'=>$data['name'], 'url'=>$data['url'], 'logo'=>$data['logo'],
        'description'=>$data['description'], 'areaServed'=>$data['areaServed'],
        'sameAs'=>$data['sameAs'], 'telephone'=>'+919019557427',
        'email'=>'info@ilmerastudyabroad.com', 'knowsAbout'=>$data['services'],
        'founder'=>['@id'=>'https://ilmerastudyabroad.com/#jabir']
    ];
    $proof = ilmera_proof_blocks($path);
    if ($proof['identifiers']) $graph['identifier'] = $proof['identifiers'];
    if ($proof['offers']) $graph['makesOffer'] = $proof['offers'];
    return $graph;
}

function ilmera_entity_visible()
{
    $data = ilmera_entity_data();
    $html = '<section class="entity-glance" style="max-width:760px;margin:32px auto;padding:24px;"><h2>ILMERA at a glance</h2><p>' . ilmera_presentation_escape($data['description']) . '</p><ul>';
    foreach ($data['services'] as $service) $html .= '<li>' . ilmera_presentation_escape($service) . '</li>';
    return $html . '</ul><p>' . ilmera_presentation_escape($data['countries_note']) . '</p></section>';
}

function ilmera_entity_markup($path)
{
    $founder = ['@type'=>'Person','@id'=>'https://ilmerastudyabroad.com/#jabir','name'=>'Jabir KJ','jobTitle'=>'Founder','worksFor'=>['@id'=>'https://ilmerastudyabroad.com/#organization']];
    $founder['description'] = ilmera_scope_data()['founder_bio'];
    $proof = ilmera_proof_blocks($path);
    if ($proof['founder_description']) $founder['description'] = $proof['founder_description'];
    return '<script type="application/ld+json">' . json_encode(['@context'=>'https://schema.org','@graph'=>[ilmera_entity_graph($path), $founder]], JSON_UNESCAPED_SLASHES|JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT) . '</script>';
}
