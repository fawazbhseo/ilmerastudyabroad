#!/usr/bin/env python3
"""Audit first answer vs first prose paragraph after its CTA on all published routes."""
import copy,difflib,hashlib,json,pathlib,re,urllib.request,urllib.parse,xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
R=pathlib.Path(__file__).resolve().parents[2];W=pathlib.Path('/home/user/phase29');D=W/'duplicate-renders';D.mkdir(exist_ok=True)
sm=urllib.request.urlopen('http://127.0.0.1:8090/sitemap.xml').read();routes=[urllib.parse.urlparse(e.text).path for e in ET.fromstring(sm).iter() if e.tag.endswith('loc')];assert len(routes)==len(set(routes))==38
norm=lambda s:' '.join(re.findall(r'\w+',s.casefold()))
def prose(el):
 c=copy.copy(el)
 for a in c.select('.source-citation'):a.decompose()
 return c.get_text(' ',strip=True)
rows=[]
for route in routes:
 b=urllib.request.urlopen('http://127.0.0.1:8090'+route).read();key=route.strip('/').replace('/','_') or 'home';(D/(key+'.html')).write_bytes(b)
 soup=BeautifulSoup(b,'html.parser');ans=soup.select_one('.direct-answer-block .direct-answer');cta=soup.select_one('.direct-answer-block .conversion-cta');entry={'route':route,'url':'https://ilmerastudyabroad.com'+route,'html_sha256':hashlib.sha256(b).hexdigest(),'has_first_answer_block':ans is not None,'has_first_block_cta':cta is not None,'match':False}
 if ans is not None and cta is not None:
  following=cta.find_next('p');following=following if following and following.find_parent('main') else None
  if following:
   a=prose(ans);b=prose(following);na=norm(a);nb=norm(b);ratio=difflib.SequenceMatcher(None,na,nb).ratio();sa=set(na.split());sb=set(nb.split());jac=len(sa&sb)/len(sa|sb) if sa|sb else 0;length=min(len(na),len(nb))/max(len(na),len(nb)) if na and nb else 0
   match=bool(na and nb and (na==nb or ratio>=.90 or (jac>=.85 and length>=.80)))
   template='includes/destination-page.php:130-132' if route.startswith('/study-in-') else 'includes/place-page.php:142-144' if route.startswith('/study-abroad-') else ('blog/index.php' if route=='/blog/' else route.lstrip('/')+'.php')
   entry.update(answer=a,following_paragraph=b,following_raw_html=str(following),normalized_equal=na==nb,character_similarity=round(ratio,6),token_jaccard=round(jac,6),length_ratio=round(length,6),match=match,kind='identical' if na==nb else 'nearly identical' if match else 'different',first_answer_source='includes/site-presentation.php:97-100, data/answer-map.json',cta_source='includes/site-presentation.php:124-128',following_source=template,citations_in_following=[{'text':x.get_text(' ',strip=True),'href':x.get('href')} for x in following.select('.source-citation')])
 rows.append(entry)
matching=[r for r in rows if r['match']];unmatched=[r for r in rows if not r['match']]
output={'source_head':'56914f2 runtime','live_origin_fetched':False,'scope':'All38 published payload sitemap routes, fresh local renders; owner reports Germany live duplicate, other live URLs not independently verified','definition':'First paragraph after first direct-answer-block conversion CTA, excluding source-citation labels, case/punctuation/whitespace normalized. Identical or char similarity>=0.90, or token Jaccard>=0.85 with length ratio>=0.80. This is transparent lexical near-duplication, not a semantic classifier.','published_count':38,'duplicate_count':len(matching),'identical_count':sum(r.get('normalized_equal',False) for r in matching),'near_count':sum(not r.get('normalized_equal',False) for r in matching),'all_routes':rows}
(R/'reports/phase-29-duplicate-paragraphs.json').write_text(json.dumps(output,indent=2)+'\n')
text='''# Phase29 duplicate first-answer paragraphs: report only

All38 published sitemap pages rendered from the unchanged payload. Germany live duplication is owner-reported; this audit confirms the behavior in the deployment payload, not that every other URL is currently deployed. No live host access or copy change.

Definition: compare the first direct-answer paragraph with the first prose paragraph after its first conversion CTA. Strip citation labels only, normalize case/punctuation/whitespace. Exact match, character similarity>=0.90, or token Jaccard>=0.85 with length ratio>=0.80 qualifies. Every comparison, raw following paragraph, score, citation and nonmatch is retained in JSON. This is lexical similarity, not an unsupported semantic-completeness claim.

'''
text+=f'**{len(matching)} matching pages: {output["identical_count"]} identical, {output["near_count"]} nearly identical.**\n\n|Published URL|Match|Character similarity|Following paragraph producer|\n|---|---|---|---|\n'
for row in matching:text+='|'+row['url']+'|'+row['kind']+'|'+str(row['character_similarity'])+'|`'+row['following_source']+'`|\n'
text+='\n## Exact text on every matching page\n\n'
for row in matching:text+='### '+row['route']+'\n\nFirst answer: '+row['answer']+'\n\nAfter CTA: '+row['following_paragraph']+'\n\nFollowing paragraph citations: '+json.dumps(row['citations_in_following'])+'.\n\n'
text+='## Nonmatches / absent answer blocks\n\n'
for row in unmatched:text+='- '+row['url']+': '+('no first answer/CTA block' if not row['has_first_answer_block'] or not row['has_first_block_cta'] else 'different; character similarity '+str(row.get('character_similarity','n/a')))+'.\n'
text+='''
## Producer and smallest safe proposal, NOT APPLIED

includes/site-presentation.php:97-100 inserts data/answer-map.json text without checking whether the original template already opens with the same answer. Lines124-128 insert the CTA immediately after that answer. visual-system.php:40-49 moves the injected introduction into the first reading container while leaving the original paragraph intact. Destinations then print their original intro_answer at includes/destination-page.php:130-132; places at includes/place-page.php:142-144. Article literal introduction paragraphs remain in each source file. This is deterministic source duplication, not a cache or missing-assets consequence.

Smallest safe targeted fix for Germany: in includes/destination-page.php:130-132, skip the existing intro_answer paragraph ONLY when the actually emitted direct-answer block for the current published route already contains the exact same normalized text. Retain the first answer heading/text and CTA. If the original paragraph has a source citation, retain that citation adjacent to the surviving answer; never discard provenance. The same guarded comparison can be applied to place-page.php:142-144 for proven exact matches. Do not blindly delete every intro paragraph or alter answer-map/SEO metadata globally.

For a shared fix across these template families, add one narrow de-duplication pass to site-presentation.php after its CTA insertion, before final visual output: compare actual adjacent original introduction to the emitted answer; suppress only an exact normalized duplicate while carrying over citations/links. Near matches require editorial review to retain unique information; do not auto-delete on the audit's fuzzy threshold. That is a proposal, not a patch. Retest word counts/publication hashes, source citations, content order, FAQ/schema parity and held-page behavior before any future authorized runtime change. This phase leaves every paragraph and all publication/source gates unchanged.
'''
(R/'reports/phase-29-duplicate-paragraphs.md').write_text(text)
print('Published',38,'duplicate matches',len(matching),'exact',output['identical_count'],'near',output['near_count'])
