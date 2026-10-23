<?php
// Independent processes exercise the single constant in both states.
define('ILMERA_SCENES_ENABLED', ($argv[1] ?? '') === 'on');
define('ILMERA_VISUAL_PILOTS_ENABLED', true);
require_once __DIR__.'/../../includes/visual-system.php';
$source='<html><head><link rel="canonical" href="https://ilmerastudyabroad.com/study-in-germany"><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script></head><body><main><section class="article-hero"><h1>Exact heading</h1><p>Exact words.</p></section></main></body></html>';
$out=ilmera_visual_present($source);
if (ILMERA_SCENES_ENABLED) {
    if (strpos($out,'aria-hidden="true" role="presentation"')===false || strpos($out,'/assets/js/hero-still.js')===false) throw new RuntimeException('Missing decorative still');
} else {
    if (strpos($out,'src="https://cdnjs.cloudflare.com/ajax/libs/three')!==false || strpos($out,'/assets/js/hero-still.js')!==false || strpos($out,'class="p25-hero-scene"')!==false || strpos($out,'id="ilmera-scenes-off"')===false) throw new RuntimeException('Global off failed');
}
if (strpos($out,'<h1>Exact heading</h1><p>Exact words.</p>')===false) throw new RuntimeException('Scene changed content');
echo 'PASS scene '.(ILMERA_SCENES_ENABLED?'ON':'OFF')." decorative/static/content-preserving\n";
