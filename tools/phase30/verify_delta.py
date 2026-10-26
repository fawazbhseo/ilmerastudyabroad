#!/usr/bin/env python3
"""All43 actual before/after renders: exact authorized paragraph/citation delta only."""
import argparse,collections,gzip,hashlib,json,pathlib,re,sys,urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from phase30.duplicates import TARGETS,PATTERN,expected_delta,plain,assert_no_repeated_answer
from check_discovery import routes
from check_phase25 import Words
from check_cycle_consistency import Graphs
p=argparse.ArgumentParser();p.add_argument('--base-url',default='http://127.0.0.1:8080');a=p.parse_args()
before=json.loads(gzip.decompress((ROOT/'reports/phase-30-before-renders.json.gz').read_bytes()));rows=[]
assert set(before)==set(routes(ROOT)) and len(before)==43
for route,record in before.items():
 old=record['html'];new=urllib.request.urlopen(a.base_url+route).read().decode();expected=expected_delta(old,route)
 assert new==expected,(route,'Output differs beyond exact authorized duplicate/citation relocation')
 assert_no_repeated_answer(new,route)
 assert Graphs(new).graphs==Graphs(old).graphs,(route,'schema')
 for pattern in [r'<h[1-6]\b[^>]*>.*?</h[1-6]>',r'<details\b.*?</details>',r'<link[^>]*rel="canonical"[^>]*>',r'<meta[^>]*name="robots"[^>]*>',r'<style\b.*?</style>',r'<script\b.*?</script>']:
  assert re.findall(pattern,new,re.S)==re.findall(pattern,old,re.S),(route,pattern)
 w,v=Words(new),Words(old);assert w.images==v.images
 links=lambda x:collections.Counter(tuple(sorted(k.items())) for k in x.links)
 assert links(w)==links(v),(route,'link lost or changed')
 row={'route':route,'changed':new!=old,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'exact_authorized_output':True,'headings_faq_schema_canonical_status_links_images_styles_scripts_preserved':True}
 if route in TARGETS:
  m=PATTERN.search(old);row.update(removed_text=plain(m[2]),kept_text=plain(m[6]),kept_original_paragraph_html=m[6],kept_citation_links=re.findall(r'<a\b[^>]*>.*?</a>',m[6],re.S),direct_answer_words=len(plain(m[6]).split()),cta_after_cited_answer=True)
  assert 40<=row['direct_answer_words']<=60
 rows.append(row)
assert {r['route'] for r in rows if r['changed']}==TARGETS and len(TARGETS)==23
(ROOT/'reports/phase-30-duplicate-fix.json').write_text(json.dumps({'passed':True,'routes':43,'changed_pages':23,'unchanged_pages':20,'only_public_duplicate_fix_file':'includes/site-presentation.php','method':'Keep original cited paragraph inner HTML in direct-answer slot, keep CTA after it, remove one exact duplicate. Citation moves with kept copy; no link removed. All other rendered bytes identical.','results':rows},indent=2)+'\n')
text='# Phase30 duplicate-answer fix\n\n43 actual before/after renders compared byte-for-byte against the exact authorized transform.23 pages change;20 are byte-identical. Removed only the uncited duplicate; the original cited paragraph content/link is kept in the direct-answer slot, with CTA immediately after. This necessary citation relocation is explicitly allowed, not hidden as an unchanged link order. All link attributes/multiplicity, headings, FAQs, schema, canonicals, status, images, scripts and styles preserved. All retained answers remain40-60 words. No copy rewording or design change.\n\n'
for r in rows:
 if not r['changed']:continue
 text+='## '+r['route']+'\n\nRemoved uncited copy: '+r['removed_text']+'\n\nKept original text: '+r['kept_text']+'\n\nKept original paragraph HTML: `'+r['kept_original_paragraph_html']+'`. Answer words: '+str(r['direct_answer_words'])+'. CTA follows.\n\n'
text+='## Unchanged routes\n\n'+''.join('- '+r['route']+'\n' for r in rows if not r['changed'])
(ROOT/'reports/phase-30-duplicate-fix.md').write_text(text);print('PASS43 exact render deltas,23 citation-preserving fixes,20 unchanged routes')
