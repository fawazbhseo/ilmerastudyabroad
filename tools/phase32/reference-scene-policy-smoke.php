<?php
// Verify output filtering defers all three reference scene dependencies and retains source content.
require_once __DIR__ . '/../../includes/visual-system.php';
$routes = ['/', '/services', '/about', '/contact'];
$results = [];
foreach ($routes as $route) {
    $_SERVER['REQUEST_URI'] = $route;
    $html = '<!doctype html><html><head><style>body{font-family:\'Outfit\',sans-serif}.hero-title{font-family:\'Cormorant Garamond\',serif}</style>';
    foreach ([
        'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js',
    ] as $src) $html .= '<script src="' . $src . '" defer></script>';
    $sceneBlock = $route === '/about'
        ? 'var W=window.innerWidth,H=window.innerHeight;if(window.THREE){var g=new THREE.Group();'
        : 'if(window.THREE){var W=window.innerWidth,H=window.innerHeight;var g=new THREE.Group();';
    $html .= '</head><body><canvas id="space-canvas"></canvas><h1 id="reference-title">Original heading</h1><script>window.addEventListener("DOMContentLoaded",function(){' . $sceneBlock . 'g.add(new THREE.Mesh(new THREE.BoxGeometry(1,1,1)));window.__p32SceneFixture=true;}});</script></body></html>';
    $output = ilmera_visual_scene_policy($html);
    $checks = [
        'font_metric_style_once' => substr_count($output, 'id="p32-reference-font-metric-fallback"') === 1,
        'outfit_metric_fallback_applied' => strpos($output, "font-family:'Outfit', 'Outfit Metric', sans-serif") !== false,
        'cormorant_metric_fallback_applied' => strpos($output, "font-family:'Cormorant Garamond', 'Cormorant Metric', serif") !== false,
        'loader_once' => substr_count($output, 'id="p32-scene-loader"') === 1,
        'fallback_style_once' => substr_count($output, 'id="p32-scene-fallback-style"') === 1,
        'original_external_script_tags_removed' => strpos($output, '<script src="https://cdnjs.cloudflare.com/ajax/libs/') === false,
        'urls_retained_only_in_lazy_loader' => substr_count($output, 'three.min.js') === 1 && substr_count($output, 'gsap.min.js') === 1 && substr_count($output, 'ScrollTrigger.min.js') === 1,
        'scene_init_wrapped' => strpos($output, 'window.__ILMERA_SCENE_INIT=function(){if(window.THREE){') !== false,
        'dimensions_hoisted_for_shared_scope' => strpos($output, 'var W=window.innerWidth,H=window.innerHeight;window.__ILMERA_SCENE_INIT') !== false,
        'heading_preserved' => strpos($output, '<h1 id="reference-title">Original heading</h1>') !== false,
        'original_canvas_preserved' => strpos($output, '<canvas id="space-canvas"></canvas>') !== false,
        'reserved_canvas_style' => strpos($output, '#space-canvas{width:100vw!important;height:100vh!important;}') !== false,
    ];
    if (in_array(false, $checks, true)) {
        fwrite(STDERR, "FAIL {$route}: " . json_encode($checks) . "\n");
        exit(1);
    }
    $results[] = ['route' => $route, 'checks' => $checks, 'status' => 'PASS'];
}
$report = ['phase' => 32, 'status' => 'PASS', 'scenes_enabled' => true, 'routes' => $results];
$json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
file_put_contents(__DIR__ . '/../../reports/phase-32-reference-scene-policy-smoke.json', $json);
echo $json;
