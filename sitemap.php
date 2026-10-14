<?php
/**
 * sitemap.php
 *
 * The canonical, always-up-to-date sitemap is the static /sitemap.xml file
 * (referenced in robots.txt and submitted to search consoles). This file
 * exists so that /sitemap.php also resolves to something useful instead of
 * a 404, but it deliberately does not generate a second, independently
 * maintained copy of the URL list: two sitemaps with the same content would
 * be redundant and risk drifting out of sync with each other.
 *
 * It permanently redirects to /sitemap.xml.
 */
header('HTTP/1.1 301 Moved Permanently');
header('Location: https://ilmerastudyabroad.com/sitemap.xml');
exit;
