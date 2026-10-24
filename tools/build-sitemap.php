<?php
/** Regenerate the portable XML snapshot; Apache serves the same data live. */
if (PHP_SAPI !== 'cli') {
    http_response_code(403);
    exit;
}
require_once dirname(__DIR__) . '/includes/sitemap-data.php';
$target = dirname(__DIR__) . '/sitemap.xml';
$xml = ilmera_sitemap_xml();
if (file_put_contents($target, $xml) === false) {
    fwrite(STDERR, "Could not write sitemap snapshot.\n");
    exit(1);
}
echo "Sitemap snapshot generated.\n";
