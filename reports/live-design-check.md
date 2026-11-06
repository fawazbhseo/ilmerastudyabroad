# Live design check: owner test sheet

Use these checks before changing anything. The likely problem is an incomplete upload, not the new wording. No fix has been applied in this phase.

## 1. Open these five links

| Open this exact URL | Correct result | If it fails, check or re-upload |
|---|---|---|
| https://ilmerastudyabroad.com/assets/css/visual-system.css | CSS code containing `@font-face` and `body.p25`. Readable code in a browser tab is normal. | `public_html/assets/css/visual-system.css` |
| https://ilmerastudyabroad.com/assets/fonts/outfit-latin.woff2 | A font download, or an otherwise blank font tab, not an error page. | `public_html/assets/fonts/outfit-latin.woff2` |
| https://ilmerastudyabroad.com/assets/fonts/cormorant-garamond-latin.woff2 | A font download, or blank font tab, not an error page. | `public_html/assets/fonts/cormorant-garamond-latin.woff2` |
| https://ilmerastudyabroad.com/assets/images/ilmera.logo.png | The ILMERA logo image. | `public_html/assets/images/ilmera.logo.png` |
| https://ilmerastudyabroad.com/study-in-germany | At mobile width: logo/menu at the top, elegant headings, pale reading sections and readable dark text on the gold button. | Check all the above plus `public_html/includes/header.php`. Ask the uploader to compare all 130 payload files, not just changed PHP files. |

**Not Found (404):** usually missing file, wrong folder, wrong filename/case or wrong website root. The folder must be `public_html/assets/`, not `public_html/releases/` or `public_html/ilmera-deploy-850d0af/assets/`.

**Forbidden (403):** ask the host to check permissions and any extra server rule. Do not remove the privacy rules from includes/data/reports/tools.

**Ordinary page text instead of CSS code, or HTML instead of a font/image:** wrong file or an error-page rewrite. Ask support to check the response and file type. Expected types: CSS `text/css`, fonts `font/woff2`, logo `image/png`. CSS displayed as readable plain code is not itself a failure. If Germany displays raw `<?php` code, stop and contact the host: PHP is not executing safely.

## 2. Check the upload, then clear caches

Germany embeds its CSS and fonts when PHP builds the page. Successful links alone do not prove PHP can read them. In File Manager, confirm the exact folders above and `includes/header.php` exist and are readable. Ask support about PHP read errors if needed. Never upload reports/tools contents or the ZIP into the public folder.

In Hostinger hPanel: Websites, this site's Dashboard/Manage, then find **Cache Manager** and choose **Purge all**. If Hostinger CDN is enabled, purge its cache too. Labels vary; use panel search or ask Hostinger support if unavailable. Replacing files without clearing the page cache can leave old embedded styling.

Open a new private/incognito window and reload Germany. Scroll below the dark hero: reading sections should be pale. If it still fails, send screenshots of Germany and all five link results to the uploader/host, with the time tested. Ask them to verify the full payload and PHP error log. Do not send passwords or private documents.
