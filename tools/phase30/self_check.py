#!/usr/bin/env python3
"""Generate fixed-path temporary checker; random key lives only in PHP constant/docs."""
import calendar,datetime,hashlib,json,pathlib,re,secrets
R=pathlib.Path(__file__).resolve().parents[2];p=R/'deploy-check.php'
old=p.read_text() if p.exists() else '';match=re.search(r"const ILMERA_DEPLOY_CHECK_KEY = '([a-f0-9]{64})';",old);key=match[1] if match else secrets.token_hex(32)
m=json.loads((R/'reports/phase-27-payload-manifest.json').read_text());files=[]
for row in m['files']:
 path=row['path']
 if path=='deploy-check.php':continue
 critical=path.startswith(('assets/','includes/','data/','destinations/','places/')) or path.endswith('.json')
 if pathlib.Path(path).name=='.htaccess':critical=False
 b=(R/path).read_bytes();files.append((path,hashlib.sha256(b).hexdigest(),critical))
assert len(files)==130
expiry=calendar.timegm(datetime.datetime(2026,11,16).timetuple())
code="""<?php
// TEMPORARY owner upload check. Delete this file immediately after one use.
const ILMERA_DEPLOY_CHECK_KEY = 'KEY';
// Valid through 2026-11-15 UTC; fails closed from 2026-11-16 00:00:00 UTC.
const ILMERA_DEPLOY_CHECK_EXPIRES_AT = EXPIRY;
header('X-Robots-Tag: noindex, nofollow, nosnippet');
header('Cache-Control: no-store, max-age=0');
header('Pragma: no-cache');
header('Expires: 0');
header('Referrer-Policy: no-referrer');
header('X-Content-Type-Options: nosniff');
header(\"Content-Security-Policy: default-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'\");
$query = $_SERVER['QUERY_STRING'] ?? '';
$key = $_GET['key'] ?? null;
if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'GET'
    || time() >= ILMERA_DEPLOY_CHECK_EXPIRES_AT
    || count($_GET) !== 1 || !is_string($key)
    || !preg_match('/\\Akey=[a-f0-9]{64}\\z/D', $query)
    || !hash_equals(ILMERA_DEPLOY_CHECK_KEY, $key)) {
    http_response_code(404);
    header('Content-Type: text/plain; charset=UTF-8');
    echo 'Not found';
    exit;
}
// Exact fixed allowlist. No filesystem discovery, directory listing or file input.
// .htaccess entries are exists-only and are NEVER opened or hashed.
$files = [
FILES
];
$rows = [];
$problems = [];
foreach ($files as $relative => $check) {
    $file = __DIR__ . '/' . $relative;
    $exists = @is_file($file) && !@is_link($file);
    $critical = $check[1] && basename($relative) !== '.htaccess';
    $readable = $exists && @is_readable($file);
    $size = $critical && $readable ? @filesize($file) : null;
    $hash = $critical && $readable ? @hash_file('sha256', $file) : false;
    $matches = $critical && $readable && is_string($hash) && hash_equals($check[0], $hash);
    if (!$exists) $problems[] = [$relative, 'MISSING'];
    elseif ($critical && !$readable) $problems[] = [$relative, 'UNREADABLE'];
    elseif ($critical && !$matches) $problems[] = [$relative, 'HASH MISMATCH'];
    $rows[] = [$relative, $exists, $critical, $readable, $size, $matches];
}
// Self-hashing would create a circular manifest. The temporary file checks only
// its own existence; its actual ZIP/manifest hash is verified by offline tooling.
$selfExists = @is_file(__DIR__ . '/deploy-check.php') && !@is_link(__DIR__ . '/deploy-check.php');
if (!$selfExists) $problems[] = ['deploy-check.php', 'MISSING'];
$rows[] = ['deploy-check.php (temporary; delete after use)', $selfExists, false, false, null, false];
$escape = static function ($value) { return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); };
header('Content-Type: text/html; charset=UTF-8');
echo '<!doctype html><html lang="en"><meta charset="UTF-8"><meta name="robots" content="noindex,nofollow,nosnippet"><title>Temporary upload check</title><body>';
echo '<h1>' . ($problems ? count($problems) . ' PROBLEMS FOUND' : 'ALL FILES OK') . '</h1>';
echo '<p>Temporary check. Delete deploy-check.php after sending the result.</p><table><tr><th>PHP version</th><td>' . $escape(PHP_VERSION) . '</td></tr></table>';
echo '<h2>FAIL</h2>';
if (!$problems) echo '<p>None.</p>';
else { echo '<ul>'; foreach ($problems as $problem) echo '<li>' . $escape($problem[0]) . ': ' . $escape($problem[1]) . '</li>'; echo '</ul>'; }
echo '<table border="1"><tr><th>Fixed payload path</th><th>Exists</th><th>Readable (critical)</th><th>Bytes (critical)</th><th>SHA-256 matches (critical)</th></tr>';
foreach ($rows as $row) {
    echo '<tr><td>' . $escape($row[0]) . '</td><td>' . ($row[1] ? 'YES' : 'MISSING') . '</td>';
    echo '<td>' . ($row[2] ? ($row[3] ? 'YES' : 'NO') : '-') . '</td>';
    echo '<td>' . ($row[2] ? ($row[4] === null ? '-' : $escape($row[4])) : '-') . '</td>';
    echo '<td>' . ($row[2] ? ($row[5] ? 'MATCH' : 'FAIL') : '-') . '</td></tr>';
}
echo '</table><p>Noncritical files and policies are existence-only. No .htaccess content is read. This is not native hosting, rewrite, cache, CSP, contact or performance certification.</p></body></html>';
""".replace("'KEY'","'"+key+"'",1).replace('EXPIRY',str(expiry),1)
code=code.replace('FILES','\n'.join("    '%s' => ['%s', %s],"%(f,h,'true' if c else 'false') for f,h,c in files),1)
p.write_text(code)
url='https://ilmerastudyabroad.com/deploy-check.php?key='+key
(R/'reports/live-self-check.md').write_text('''# Temporary live upload self-check

Owner-only use after upload. Open:

'''+url+'''

Key: `'''+key+'''`

Valid through **2026-11-15 UTC**, expires **2026-11-16 00:00:00 UTC**. Delete deploy-check.php from public_html immediately after one screenshot/result. The file has no login or secret server information. The random key is a temporary bearer guard, not a password vault; this source repository and its reports must not be treated as secret storage. Never upload this report.

Missing/wrong key, expired time, any extra parameter, duplicate/array/encoded key, path parameter or non-GET method fails closed with a plain404 Not found response. No custom clock or file parameter exists. The checker uses fixed payload-relative paths only, no directory enumeration, content display, .htaccess reads, phpinfo, environment display or writes. Noindex/no-store headers apply even to denied requests.

Critical design/runtime assets/includes/JSON are checked for existence, readability, size and SHA256 against the embedded payload map. All other original130-file entries are existence-only. All8 .htaccess entries are existence-only, never opened. The temporary131st file is existence-only to avoid circular self-hashing; offline ZIP/manifest tooling verifies its actual hash. ALL FILES OK means these scoped checks passed, not native hosting or performance acceptance.

Send back a screenshot of ALL FILES OK or the FAIL list, then delete the PHP file and confirm the URL returns404. Do not include the key in unrelated links or analytics. A host access log can record query strings; deletion and expiry limit exposure.

Native rewrite caveat: unchanged root .htaccess canonicalizes direct .php requests to extensionless URLs before PHP runs. On such a host the initial response can be301, followed by the protected /deploy-check response with the same query. The PHP handler's wrong-key/final response is404. This phase does not change root rewrites or falsely certify native first-hop status. PHP-adapter deny tests do not execute .htaccess.
''')
print('Generated temporary fixed-path self-check; key kept in PHP constant and owner documentation')
