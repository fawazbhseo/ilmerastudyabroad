"""Keep original two variable families/weights, subset only unused glyphs.

Reproducible from npm inputs named in README; OFL notices retained. All text from
four immutable pilot baselines (including footer) supplies Unicode coverage.
"""
import hashlib,json,os,pathlib,sys
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
root=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(root/'tools'))
from check_phase25 import Words,PILOTS
original=json.loads((root/'reports/phase-25-baseline-renders.json').read_text());text=' '.join(' '.join(Words(original['routes'][r]['html']).words) for r in PILOTS);characters=set(map(ord,text));rows=[]
for family,file in [('outfit','outfit-latin.woff2'),('cormorant-garamond','cormorant-garamond-latin.woff2')]:
 source=pathlib.Path(os.environ['NODE_PATH'].split(':')[0])/'@fontsource-variable'/family/'files'/(family+'-latin-wght-normal.woff2')
 font=TTFont(source,recalcTimestamp=False)
 if family=='cormorant-garamond':instantiateVariableFont(font,{'wght':700},inplace=True)
 available=set(font.getBestCmap());options=subset.Options();options.flavor='woff2';options.recalc_timestamp=False
 sub=subset.Subsetter(options);sub.populate(unicodes=characters);sub.subset(font);out=root/'assets/fonts'/file;font.save(out)
 rows.append({'family':family,'weight_strategy':'original Outfit variable axis; Cormorant fixed at its only pilot role weight 700','file':str(out.relative_to(root)),'bytes':out.stat().st_size,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'subset_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'coverage':'All characters present in original Latin font and used by the four immutable pilot renders; reference family and included-glyph metrics retained. Emoji/non-Latin glyphs absent from the original font retain normal system fallback.','missing_required_source_glyphs':sorted((characters&available)-set(font.getBestCmap()))});assert not rows[-1]['missing_required_source_glyphs']
(root/'reports/phase-25-font-assets.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
