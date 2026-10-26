"""Exact authorized duplicate delta plus independent repeated-answer build guard."""
import difflib,html,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
TARGETS={r['route'] for r in json.loads((ROOT/'reports/phase-29-duplicate-paragraphs.json').read_text())['all_routes'] if r['match']}
# Both actual rendered light-section layout and the immutable predesign layout.
PATTERN=re.compile(r'(<p class="direct-answer">)(.*?)(</p>)(<p class="conversion-cta">.*?</p>)(</div>\s*(?:</section>\s*<section class="s-wrap article-body">\s*<div class="container">\s*)?)<p>(.*?)</p>',re.S)
def plain(value):
 value=re.sub(r'<a\b[^>]*class="source-citation"[^>]*>.*?</a>','',value,flags=re.S)
 return ' '.join(html.unescape(re.sub('<[^>]+>','',value)).split())
def expected_delta(text,route):
 if route not in TARGETS:return text
 def replace(m):
  assert plain(m[2])==plain(m[6]),(route,'authorized original pair differs')
  return m[1]+m[6]+m[3]+m[4]+m[5]
 out,n=PATTERN.subn(replace,text,count=1)
 assert n==1,(route,'authorized duplicate pair not found')
 return out

def assert_no_repeated_answer(text,route):
 # Inspect the first real paragraph after the answer block/CTA, not arbitrary FAQs.
 for m in PATTERN.finditer(text):
  a,b=plain(m[2]),plain(m[6]);ratio=difflib.SequenceMatcher(None,a.casefold(),b.casefold()).ratio()
  assert a!=b and ratio<.90,(route,'Repeated first answer after CTA',a,b)
