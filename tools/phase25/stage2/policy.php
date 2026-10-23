<?php
$inline = ($argv[1] ?? '') === 'inline';
define('ILMERA_SCENES_ENABLED', ($argv[1] ?? '') !== 'off');
if ($inline) {
    define('ILMERA_VISUAL_INLINE_FONT_TEMPLATES', ['destination','place','article','blog','legal','directory','error']);
    define('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES', ['destination','place','article','blog','legal','directory','error']);
}
require_once __DIR__.'/../../../includes/visual-system.php';
$rows = json_decode(file_get_contents(__DIR__.'/../../../reports/phase-25-baseline-renders.json'),true)['routes'];
foreach ($rows as $path=>$row) {
    $_SERVER['REQUEST_URI']=$path;
    $out=ilmera_visual_present($row['html']);
    if (ilmera_visual_present($out)!==$out) throw new RuntimeException('Presentation not idempotent');
    $reference=in_array($path,['/','/services','/about','/contact'],true);
    if ($reference && $out!==$row['html']) throw new RuntimeException('Reference changed');
    if (!$reference && strpos($out,'class="p25 p25-')===false) throw new RuntimeException('Missing shared role');
    if (strpos($out,'/assets/js/hero-still.js')!==false || strpos($out,'/assets/images/hero-still-')!==false) throw new RuntimeException('Still referenced');
    if (!$reference && (strpos($out,'setTimeout(show,3000)')===false || strpos($out,'Promise.all([document.fonts.load')===false)) throw new RuntimeException('Missing text-paint failsafe');
    if ($inline && !$reference && (substr_count($out,'data:font/woff2;base64,')!==2 || strpos($out,'/assets/fonts/')!==false || strpos($out,"\nbody.p25 :is(.mini-hero")===false)) throw new RuntimeException('Template fallback fixture failed');
    if (!ILMERA_SCENES_ENABLED && strpos(ilmera_visual_scene_policy($out),'id="ilmera-scenes-off"')===false) throw new RuntimeException('Global off missing');
}
define('ILMERA_VISUAL_REQUEST_TEMPLATE', 'error');
$_SERVER['REQUEST_URI']='/missing-route';
if (strpos(ilmera_visual_present($rows['/404']['html']), 'class="p25 p25-utility"')===false) throw new RuntimeException('ErrorDocument context lost');
echo "PASS43 template/reference/failsafe/still/global-switch policy fixtures\n";
