# Temporary live upload self-check

Owner-only use after upload. Open:

https://ilmerastudyabroad.com/deploy-check.php?key=596b2f06f047c76730364c34857c6b47d03b019b21f8818960752a42fe104d9f

Key: `596b2f06f047c76730364c34857c6b47d03b019b21f8818960752a42fe104d9f`

Valid through **2026-11-15 UTC**, expires **2026-11-16 00:00:00 UTC**. Delete deploy-check.php from public_html immediately after one screenshot/result. The file has no login or secret server information. The random key is a temporary bearer guard, not a password vault; this source repository and its reports must not be treated as secret storage. Never upload this report.

Missing/wrong key, expired time, any extra parameter, duplicate/array/encoded key, path parameter or non-GET method fails closed with a plain404 Not found response. No custom clock or file parameter exists. The checker uses fixed payload-relative paths only, no directory enumeration, content display, .htaccess reads, phpinfo, environment display or writes. Noindex/no-store headers apply even to denied requests.

Critical design/runtime assets/includes/JSON are checked for existence, readability, size and SHA256 against the embedded payload map. All other original130-file entries are existence-only. All8 .htaccess entries are existence-only, never opened. The temporary131st file is existence-only to avoid circular self-hashing; offline ZIP/manifest tooling verifies its actual hash. ALL FILES OK means these scoped checks passed, not native hosting or performance acceptance.

Send back a screenshot of ALL FILES OK or the FAIL list, then delete the PHP file and confirm the URL returns404. Do not include the key in unrelated links or analytics. A host access log can record query strings; deletion and expiry limit exposure.

Native rewrite caveat: unchanged root .htaccess canonicalizes direct .php requests to extensionless URLs before PHP runs. On such a host the initial response can be301, followed by the protected /deploy-check response with the same query. The PHP handler's wrong-key/final response is404. This phase does not change root rewrites or falsely certify native first-hop status. PHP-adapter deny tests do not execute .htaccess.
