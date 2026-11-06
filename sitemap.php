<?php
require_once __DIR__ . '/includes/sitemap-data.php';
header('Content-Type: application/xml; charset=UTF-8');
echo ilmera_sitemap_xml();
