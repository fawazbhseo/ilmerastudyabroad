<?php
// Prove the existing global scene switch excludes animated scenes and Phase32 still requests.
define('ILMERA_SCENES_ENABLED', false);
require_once __DIR__ . '/../../includes/visual-system.php';
$fixtures = [
    '/study-in-germany' => ['destination', 'article-hero'],
    '/study-abroad-counselling-mysuru' => ['place', 'article-hero'],
    '/blog/how-to-choose-study-abroad-consultant-karnataka' => ['article', 'article-hero'],
    '/blog/' => ['blog', 'blog-hero'],
];
$results = [];
foreach ($fixtures as $path => [$template, $heroClass]) {
    $_SERVER['REQUEST_URI'] = $path;
    $html = '<!doctype html><html><head><link rel="canonical" href="https://ilmerastudyabroad.com' . $path . '"></head><body><section class="' . $heroClass . '"><h1>Original heading</h1></section><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r1/three.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script></body></html>';
    $output = ilmera_visual_present(ilmera_visual_scene_policy($html));
    $checks = [
        'scene_off_marker' => strpos($output, 'id="ilmera-scenes-off"') !== false,
        'scene_script_removed' => strpos($output, 'three.min.js') === false,
        'non_scene_gsap_preserved' => strpos($output, 'gsap.min.js') !== false && strpos($output, 'ScrollTrigger.min.js') !== false,
        'still_canvas_absent' => strpos($output, '<canvas class="p32-hero-still"') === false,
        'still_assets_absent' => strpos($output, 'hero-still-640.webp') === false && strpos($output, 'hero-still-1440.webp') === false,
        'still_loader_absent' => strpos($output, "var canvas=document.querySelector('.p32-hero-still')") === false,
        'heading_preserved' => strpos($output, '<h1>Original heading</h1>') !== false,
    ];
    if (in_array(false, $checks, true)) {
        fwrite(STDERR, "FAIL {$path}: " . json_encode($checks) . "\n");
        exit(1);
    }
    $results[] = ['route' => $path, 'template' => $template, 'checks' => $checks, 'status' => 'PASS'];
}
$referenceRoutes = ['/' => 'home', '/services' => 'services', '/about' => 'about', '/contact' => 'contact'];
foreach ($referenceRoutes as $path => $template) {
    $_SERVER['REQUEST_URI'] = $path;
    $html = '<!doctype html><html><head>';
    foreach ([
        'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js',
    ] as $src) $html .= '<script src="' . $src . '"></script>';
    $html .= '</head><body><canvas id="space-canvas"></canvas><h1>Original heading</h1><script>if(window.THREE){var W=window.innerWidth,H=window.innerHeight;window.__p32SceneFixture=true;}</script></body></html>';
    $output = ilmera_visual_scene_policy($html);
    $checks = [
        'scene_off_marker' => strpos($output, 'id="ilmera-scenes-off"') !== false,
        'all_scene_dependencies_removed' => strpos($output, 'three.min.js') === false && strpos($output, 'gsap.min.js') === false && strpos($output, 'ScrollTrigger.min.js') === false,
        'deferred_loader_absent' => strpos($output, 'id="p32-scene-loader"') === false,
        'off_palette_preserved' => strpos($output, '#space-canvas,#vignette') !== false && strpos($output, 'background:#04060f') !== false,
        'fallback_dimensions_initialized' => strpos($output, 'var W=window.innerWidth,H=window.innerHeight;if(window.THREE){') !== false,
        'heading_preserved' => strpos($output, '<h1>Original heading</h1>') !== false,
        'canvas_preserved' => strpos($output, '<canvas id="space-canvas"></canvas>') !== false,
    ];
    if (in_array(false, $checks, true)) {
        fwrite(STDERR, "FAIL {$path}: " . json_encode($checks) . "\n");
        exit(1);
    }
    $results[] = ['route' => $path, 'template' => $template, 'checks' => $checks, 'status' => 'PASS'];
}
$report = ['phase' => 32, 'status' => 'PASS', 'scenes_enabled' => false, 'routes' => $results];
$json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
file_put_contents(__DIR__ . '/../../reports/phase-32-scene-switch-smoke.json', $json);
echo $json;
