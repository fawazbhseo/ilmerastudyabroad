<?php
require_once __DIR__ . '/../includes/site-presentation.php';
function demand($condition, $label) { if (!$condition) { fwrite(STDERR, "FAIL $label\n"); exit(1); } }
$map = ['/a'=>['kind'=>'place'], '/b'=>['kind'=>'place'], '/article'=>['kind'=>'article']];
demand(ilmera_related_place_list_schema('<h2>No list</h2>', $map) === '', 'No visible list emits nothing');
$visible = '<h2>Related place guides</h2><ul><li><a href="/a">A &amp; area</a></li><li><a href="/held">Held</a></li><li><a href="/article">Article</a></li><li><a href="/a">Duplicate</a></li><li><a href="/b">B</a></li></ul>';
$markup = ilmera_related_place_list_schema($visible, $map);
preg_match('~<script type="application/ld\+json">(.*?)</script>~s', $markup, $match);
$graph = json_decode($match[1], true);
demand($graph['@type'] === 'ItemList' && $graph['numberOfItems'] === 2, 'Published place entries only, deduplicated');
demand($graph['itemListOrder'] === 'https://schema.org/ItemListUnordered', 'Not a ranking');
demand($graph['itemListElement'][0]['item']['name'] === 'A & area', 'Visible decoded label parity');
demand($graph['itemListElement'][1]['position'] === 2, 'Contiguous positions');
demand($graph['itemListElement'][1]['item']['url'] === 'https://ilmerastudyabroad.com/b', 'Canonical URL');
demand(ilmera_related_place_list_schema('<h2>Related place guides</h2><ul><a href="/held">Held</a></ul>', $map) === '', 'Empty qualified list emits nothing');
echo "PASS 7 related-guide ItemList boundaries\n";
