#!/usr/bin/env python3
"""Exact source-scope guard for the authorized Phase31 visual edits."""
from __future__ import annotations
import pathlib
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[2]
HOME_OLD=(
    b'/* Phase 25 team-only equal heights */#team .testi-grid{grid-auto-rows:1fr;}'
    b'/* Phase 25 team footprint */#team{min-height:962.1875px;}'
    b'@media(max-width:768px){#team{min-height:clamp(1485px,calc(2013px - 68.75vw),1765.5px);padding-bottom:79.5px!important;}}'
    b'/* End Phase 25 team footprint */'
)
HOME_NEW=HOME_OLD+b'@media(max-width:600px){#team{min-height:auto;}}'
ABOUT_OLD=(
    b'/* Phase 25 team-only equal heights */#team .team-grid{grid-auto-rows:1fr;}'
    b'/* Phase 25 team footprint */#team{min-height:1152.71875px;}'
    b'@media(min-width:701px) and (max-width:1024px){#team{min-height:1292.78125px;}}'
    b'@media(max-width:600px){#team{min-height:2041.96875px;}}'
    b'/* End Phase 25 team footprint */'
)
ABOUT_NEW=ABOUT_OLD.replace(
    b'@media(min-width:701px) and (max-width:1024px){#team{min-height:1292.78125px;}}',
    b'@media(min-width:701px) and (max-width:1024px){#team{min-height:auto;}}',1
).replace(
    b'@media(max-width:600px){#team{min-height:2041.96875px;}}',
    b'@media(max-width:600px){#team{min-height:auto;}}',1
)
TASK2_EXPECTED={'index.php':(HOME_OLD,HOME_NEW),'about.php':(ABOUT_OLD,ABOUT_NEW)}
TASK3_VISUAL_OLD=(
    b'    if (in_array($template, ILMERA_VISUAL_PLAIN_HERO_TEMPLATES, true)) {\n'
    b'        $css .= "\\nbody.p25 :is(.mini-hero,.article-hero,.blog-hero,.legal-hero,.directory-hero,.err-wrap){background:#04060f;}";\n'
    b'    }\n'
)
TASK3_VISUAL_NEW=TASK3_VISUAL_OLD+(b'''    if (in_array($template, ['destination','place','article','blog'], true)) {
        $css .= <<<'CSS'
/* Phase31 Task3 static still; decorative only, scoped to approved template heroes. */
body.p25.p25-destination .article-hero,
body.p25.p25-place .article-hero,
body.p25.p25-article .article-hero,
body.p25.p25-blog .blog-hero {
    background-color:#04060f;
    background-image:linear-gradient(180deg,rgba(4,6,15,.44),rgba(4,6,15,.68)),url('/assets/images/hero-still-1440.webp');
    background-size:cover,cover;
    background-position:center,center;
    background-repeat:no-repeat,no-repeat;
}
@media(max-width:768px) {
body.p25.p25-destination .article-hero,
body.p25.p25-place .article-hero,
body.p25.p25-article .article-hero,
body.p25.p25-blog .blog-hero {
    background-image:linear-gradient(180deg,rgba(4,6,15,.44),rgba(4,6,15,.68)),url('/assets/images/hero-still-720.webp');
}
}
CSS;
    }
''')
TASK3_EXPECTED={'includes/visual-system.php':(TASK3_VISUAL_OLD,TASK3_VISUAL_NEW)}
RUNTIME_ROOTS={'assets','data','includes','destinations','places','blog'}
RUNTIME_FILES={'index.php','services.php','about.php','contact.php','404.php','all-pages.php','privacy-policy.php','terms.php','robots.txt','sitemap.xml','llms.txt','llms-full.txt','favicon.ico','deploy-check.php'}

def runtime_paths_changed(source_head:str,current_head:str)->list[str]:
    if subprocess.run(['git','merge-base','--is-ancestor',source_head,current_head],cwd=ROOT).returncode:
        raise SystemExit('Render source is not an ancestor of verification HEAD')
    names=subprocess.check_output(['git','diff','--name-only',source_head,current_head],cwd=ROOT,text=True).splitlines()
    return [p for p in names if pathlib.PurePosixPath(p).parts[0] in RUNTIME_ROOTS or p in RUNTIME_FILES or pathlib.PurePosixPath(p).name=='.htaccess' or (len(pathlib.PurePosixPath(p).parts)==1 and p.endswith('.php'))]

def git_file(revision:str,path:str)->bytes:
    return subprocess.check_output(['git','show',f'{revision}:{path}'],cwd=ROOT)

def verify_task2_spacing_scope(source_head:str,current_head:str)->list[str]:
    """Allow no runtime diff, exact Task2 spacing, or Task2 plus scoped Task3 still CSS."""
    changed=runtime_paths_changed(source_head,current_head)
    if not changed:return []
    expected=TASK2_EXPECTED
    if set(changed)==set(TASK2_EXPECTED)|set(TASK3_EXPECTED):
        expected={**TASK2_EXPECTED,**TASK3_EXPECTED}
    elif set(changed)!=set(TASK2_EXPECTED):
        raise SystemExit(f'Unexpected production runtime file changes for Phase31 visual scope: {changed}')
    for path,(old,new) in expected.items():
        before=git_file(source_head,path)
        after=git_file(current_head,path)
        if before.count(old)!=1:
            raise SystemExit(f'Expected one frozen Phase31 CSS anchor in {path}, found {before.count(old)}')
        if after!=before.replace(old,new,1):
            raise SystemExit(f'{path} differs outside the authorized Task2/Task3 presentation scope')
    return sorted(changed)
