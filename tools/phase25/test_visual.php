<?php
// Test the opt-in generator without enabling any live/default route.
define('ILMERA_VISUAL_PILOTS_ENABLED', true);
require_once __DIR__ . '/../../includes/visual-system.php';
function need($condition, $label) { if (!$condition) throw new RuntimeException($label); }
foreach (['/study-in-germany','/study-abroad-counselling-mysuru','/blog/how-to-choose-study-abroad-consultant-karnataka','/blog/'] as $route) {
    $s = '<html><head><link rel="canonical" href="https://ilmerastudyabroad.com'.$route.'"></head><body><main>Exact words</main></body></html>';
    $v = ilmera_visual_present($s);
    need(strpos($v, 'class="p25 p25-') !== false, 'Missing pilot class');
    need(strpos($v, 'id="ilmera-visual-system"') !== false, 'Missing shared CSS');
    need(strpos($v, '<main>Exact words</main>') !== false, 'Content changed');
    need(strpos($v, '<link rel="stylesheet"') === false, 'Added render-blocking stylesheet');
}
foreach (['/','/services','/about','/contact','/privacy-policy','/terms','/404','/all-pages','/study-in-italy','/study-in-russia','/study-abroad-counselling-bengaluru'] as $route) {
    $s='<head><link rel="canonical" href="https://ilmerastudyabroad.com'.$route.'"></head><body>Exact</body>';
    need(ilmera_visual_present($s) === $s, 'Non-pilot changed: '.$route);
}
foreach (['outfit-latin.woff2','cormorant-garamond-latin.woff2'] as $f) {
    $bytes=file_get_contents(__DIR__.'/../../assets/fonts/'.$f);
    need(substr($bytes,0,4)==='wOF2', 'Invalid local font');
}
echo "PASS four opt-ins, eleven exclusions, inline CSS, preserved words, valid two-family fonts\n";
