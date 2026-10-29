<?php
// Prove the existing global scene switch excludes both animated scenes and Phase32 still requests.
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
    $html = '<!doctype html><html><head><link rel="canonical" href="https://ilmerastudyabroad.com' . $path . '"></head><body><section class="' . $heroClass . '"><h1>Original heading</h1></section><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r1/three.min.js"></script></body></html>';
    $output = ilmera_visual_present(ilmera_visual_scene_policy($html));
    $checks = [
        'scene_off_marker' => strpos($output, 'id="ilmera-scenes-off"') !== false,
        'scene_script_removed' => strpos($output, 'three.min.js') === false,
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
$report = ['phase' => 32, 'status' => 'PASS', 'scenes_enabled' => false, 'routes' => $results];
$json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
file_put_contents(__DIR__ . '/../../reports/phase-32-scene-switch-smoke.json', $json);
echo $json;
