#!/usr/bin/env python3
"""Replace only original upload section and its appended obsolete upload note."""
import hashlib,json,pathlib,re,subprocess
R=pathlib.Path(__file__).resolve().parents[2];p=R/'reports/post-deploy-checklist.md';old=subprocess.check_output(['git','show','90d5358:reports/post-deploy-checklist.md'],cwd=R)
a=old.index(b'## (b) Upload method');b=old.index(b'## (c) Open on mobile and desktop');tail=b'\nUnzip ilmera-deploy-850d0af.zip locally, preserving its 130-file folder structure.  \nUpload contents with hidden .htaccess files into public_html; exclude the ZIP and releases folder.\n';assert old.endswith(tail)
key=re.search("const ILMERA_DEPLOY_CHECK_KEY = '([a-f0-9]{64})'",(R/'deploy-check.php').read_text())[1];z=json.loads((R/'reports/phase-30-zip-proof.json').read_text());name=pathlib.Path(z['archive']).name;url='https://ilmerastudyabroad.com/deploy-check.php?key='+key
block='''## (b) Upload method

**Current Phase30 ZIP:131 files, including the temporary self-check.130 permanent files remain after deleting it. This section supersedes the older130-file upload wording above and the old ZIP note.** Do not use a PHP-only update or upload the whole repository.

1. **(a) Back up first.** Download the existing public_html contents, including hidden files and hosting/PHP settings, to your computer. Keep the backup outside public_html and confirm how to restore it.
2. **(b) Download** ['''+name+''']('''+z['download_url']+''') from GitHub to your computer. Expected size:690538 bytes.
3. **(c) Extract on Hostinger.** Open hPanel, Websites, this site's Dashboard/Manage, File Manager. Open the domain's public_html folder. Upload the ZIP there, select it and choose Extract. Extract directly into public_html and overwrite existing files. Do not create a ZIP-named subfolder. Enable Show hidden files so .htaccess files are included. Do not upload releases/, reports or tools contents from the repository.
4. **(d) Delete the uploaded ZIP from public_html immediately after extraction.** Keep your backup on your computer, never under web access. Check the folder counts below after deleting the ZIP.
5. **(e) Clear caches.** In hPanel, find this site's Cache Manager, commonly under Performance, and choose Purge all. If Hostinger CDN is enabled, purge its cache too. If a LiteSpeed/LSCache option is enabled, purge that cache; for an installed WordPress LiteSpeed Cache plugin, use LiteSpeed Cache, Toolbox, Purge All. This PHP site need not have WordPress or that plugin: do not install one. Panel labels vary; use panel search or ask Hostinger support. Open a fresh private/incognito window for testing.
6. **(f) Run** [the temporary live self-check]('''+url+''') and send a screenshot of ALL FILES OK or the FAIL list. It checks fixed payload files for you, including the design assets. It expires after15November2026 UTC. Do not add extra URL parameters. This result is not a speed/native-host acceptance.
7. **(g) Delete deploy-check.php from public_html immediately after that one use.** Reopen its link to confirm404. Never leave the temporary file online just because it has a key/expiry.
8. **(h) Continue with all the page, privacy, font, contact and speed checks below.** If anything fails, follow rollback section(j), not speculative file deletion.

**Expected files from this ZIP:** count files, not folders, including hidden files/licences. Existing host extras may make counts larger; compare them with the backup and ask before deleting unrelated hosting files. Overwrite does not remove old unlisted files.

| Folder | Expected files |
|---|---|
'''
for f in ['assets/css','assets/fonts','assets/images','includes','data','destinations','places','blog','.']:block+='| '+('root public_html' if f=='.' else f)+' | '+str(z['folder_counts'][f])+(' before deleting deploy-check.php;45 afterward' if f=='.' else '')+' |\n'
block+='''
reports/ and tools/ each receive ONLY their hidden .htaccess deny file, one file each, no other content. Counts sum131 before deleting the checker,130 afterward. The releases/ folder is never extracted. Font count12 includes9 font binaries,2 licences and1 hidden policy.

**12 important files to spot:** assets/css/visual-system.css; assets/fonts/outfit-latin.woff2; assets/fonts/cormorant-garamond-latin.woff2; includes/visual-system.php; includes/visual-config.php; includes/site-presentation.php; includes/header.php; includes/footer.php; data/seo-map.json; data/answer-map.json; root .htaccess; temporary deploy-check.php. The checker covers the full allowlist and detailed critical hashes; you do not need to compare130 files manually.

'''
new=old[:a]+block.encode()+old[b:-len(tail)];p.write_bytes(new)
# Preserve ALL other checklist sections byte-exact, including historical intro.
assert new.startswith(old[:a]) and new[new.index(b'## (c) Open on mobile and desktop'):]==old[b:-len(tail)]
proof={'passed':True,'only_upload_section_and_appended_old_upload_note_replaced':True,'non_upload_prefix_and_c_through_k_bytes_preserved':True,'original_non_upload_prefix_sha256':hashlib.sha256(old[:a]).hexdigest(),'original_c_through_k_sha256':hashlib.sha256(old[b:-len(tail)]).hexdigest(),'folder_counts':z['folder_counts'],'count_before_temp_delete':131,'after_delete':130,'important_files':12,'old_title_and_intro_retained_as_requested':'New upload section explicitly supersedes historical130-file wording; other steps not rewritten','key_not_serialized_in_proof':True}
(R/'reports/phase-30-upload-sheet-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print('Replaced upload instructions only; non-upload bytes unchanged')
