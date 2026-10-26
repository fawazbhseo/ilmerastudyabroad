# Phase29 server rules: static analysis only

No Apache, LiteSpeed, apachectl, Docker or native rule simulator is installed. The local PHP adapter deliberately does NOT execute .htaccess. Native behavior is **UNVERIFIED**. The JSON ledger preserves every line/hash of all8 payload rule files and explicit path evaluations. These evaluations are source reasoning, not a claimed Apache simulator run. Unknown owner/global/parent/Hostinger/CDN rules are not available here.

| Payload rule file | Effect on CSS/fonts |
|---|---|
| .htaccess | Inherited by assets. No deny for css, woff2, png or webp. FilesMatch lines19-21 blocks md/py/cjs/log/bak/csv, root review JSON names and basename-leading dotfiles, not visual-system.css or ordinary font names. Git403 at line23 only /.git. |
| assets/.htaccess | **Absent**, not a missing ninth payload file. No assets-wide deny shipped. |
| assets/fonts/.htaccess | Lines2-4 mod_mime AddType font/woff2; lines5-9 optional mod_headers immutable cache for woff2. No deny/rewrite. If module unavailable, that override is skipped, not an access denial. CSS directory is not beneath this rule. |
| data/.htaccess | Require all denied, scoped to data subtree HTTP access; no effect on /assets. |
| includes/.htaccess | Same scoped HTTP deny. PHP require/file_get_contents still uses filesystem permissions, not HTTP ACL. |
| destinations/.htaccess | Same scoped HTTP deny, no assets impact. |
| places/.htaccess | Same scoped HTTP deny, no assets impact. |
| reports/.htaccess | Same scoped HTTP deny, no assets impact. |
| tools/.htaccess | Same scoped HTTP deny, no assets impact. |

The excluded releases/.htaccess protects only releases and cannot block /assets.

## Root rewrite walk-through

- .htaccess:5-7 canonicalizes/generated sitemap only.
- Lines10-11 redirect a directly requested .php URL to its extensionless counterpart. A .css or .woff2 request does not match the THE_REQUEST condition.
- Lines14-16 internally rewrite only if the requested path is not a directory AND the adjacent requested-name.php exists. There is **no universal unknown-file-to-PHP/front-controller rule** and no tracked ErrorDocument directive. Missing CSS normally remains404; missing font normally remains404. A host-level fallback or ErrorDocument may supply an HTML error response, but is not proved here.
- All tested CSS/font paths have no .php neighbor. A stale host-only file such as visual-system.css.php could change that conditional outcome; none exists in this payload. Existing real CSS/font files should be served directly under the normal MIME map.
- No rule sets CSS Content-Type. Expected text/css relies on normal native mod_mime/host configuration. A200 text/html error document or text/plain CSS MIME indicates host mapping/rewrite behavior or wrong file content, not a shipped CSS deny. Opening a stylesheet as readable code in a browser tab is normal; do not confuse that with PHP source exposure.
- No tracked CSP directive exists. A host/CDN Content-Security-Policy blocking inline style or data: fonts can independently break injection or font decoding. Germany needs inline styles plus font-src allowance for data:; font endpoints succeeding alone do not establish CSP compatibility.

## Why an HTTP rule cannot alone explain Germany's missing overlay

The stylesheet and destination variable fonts are server-side disk reads. An HTTP403 on their URLs does not deny PHP filesystem reads. HTTP font blocking affects static-font templates, not Germany's embedded faces. If CSS URL fails, first locate the file under the correct public_html path and check readable filesystem permissions, then inspect HTML for the actual inline style/data faces. A native filesystem read denial, missing file or incomplete upload differs from a URL ACL denial. Do not remove privacy denies in includes/data/destinations/places to repair styling.

## Minimal conditional remediation, not applied

1. If files are absent: re-upload assets/css/visual-system.css and assets/fonts/ at exact paths, preserving all payload assets; clear HTML cache.
2. If files exist but a host-wide assets deny is proven: have owner/host identify and narrow that external rule, not remove the shipped private-directory denies. No shipped deny adjustment is supported by evidence.
3. If a host catch-all rewrites existing static files: host should exempt existing files/directories before that catch-all, e.g. RewriteCond %{REQUEST_FILENAME} !-f and !-d. Do not add this speculatively to the current rules; the offending catch-all is not in this repo.
4. If CSS is served with a wrong MIME: host should correct CSS mapping to text/css; fonts to font/woff2. If CSP blocks inline design/data fonts, owner must inspect actual response policy and approve a narrow policy solution. No live-header or security-policy change is made here.
