"""Lossless browser-evidence packaging, not generated website imagery."""
from pathlib import Path
from PIL import Image
import json
root=Path(__file__).resolve().parents[3];source=Path('/home/user/phase25-evidence/s2/contact');out=root/'reports/screenshots/phase-25-stage-2';rows=[]
items=[('services','Services reference','Original hero; original light/dark reference rhythm; original CTA; full reference footer. Unchanged reference, not subject to rebuilt accent limit.'),('germany','Germany','Plain navy hero (measured lighter tier); light intro/reading/FAQ; no dark accent; CTA within light content; full reference footer.'),('mysuru','Mysuru','Gradient hero; light intro/reading/FAQ; no dark accent; CTA within light content; full reference footer.'),('article','Article','Gradient hero; light intro/longform/disclosures; no dark accent; CTA within light content; full reference footer.'),('blog','Blog index','Gradient hero; light post index; one dark CTA/accent; full reference footer.'),('privacy','Privacy','Gradient hero; light legal reading area; no dark accent or new CTA; full reference footer.'),('all-pages','All pages','Gradient hero; light intro/directory; no dark accent or new CTA; full reference footer.'),('404','404','Gradient hero; light recovery/navigation area; no dark accent; recovery CTA; abbreviated footer with original contents.')]
md=['# Phase25 owner contact sheet','','Final Stage2 branch captures at1280 and360. Browser motion is frozen only for evidence; source pages are not rewritten. Fonts/images fully loaded. Images are full-page viewport-tile captures, losslessly packaged as WebP (PNG when beyond the WebP dimension limit), not generated website assets. Raw-branch URLs track this session branch.','', '**Release status: NOT READY.** RuleC, immutable-reference accessibility/performance, literal404 footer and tiny destination header auto-margin deviation remain documented in the release check.','']
for name,title,roles in items:
 md+=['## '+title,'']
 for width in [1280,360]:
  src=source/f'review-{name}-{width}.png';im=Image.open(src).convert('RGB');ext='png' if max(im.size)>16383 else 'webp';dest=out/f'review-{name}-{width}.{ext}';
  if ext=='webp':im.save(dest,'WEBP',lossless=True,method=6)
  else:im.save(dest,'PNG',optimize=True,compress_level=9)
  assert Image.open(dest).convert('RGB').tobytes()==im.tobytes()
  url=f'https://raw.githubusercontent.com/fawazbhseo/ilmerastudyabroad/refs/heads/arena/48320ee5-ilmerastudyabroad/reports/screenshots/phase-25-stage-2/{dest.name}'
  md+=[f'### {width}px','',f'![{title} at {width}px]({url})','',roles,''];rows.append({'name':name,'width':width,'file':dest.relative_to(root).as_posix(),'pixels':im.size,'lossless':True,'bytes':dest.stat().st_size})
(root/'reports/phase-25-contact-sheet.md').write_text('\n'.join(md)+'\n');(root/'reports/phase-25-stage-2-contact-assets.json').write_text(json.dumps(rows,indent=2)+'\n')
# Refresh the measured-fallback pilot evidence without lossy recompression.
for p in out.glob('after-germany-*.png'):
 im=Image.open(p).convert('RGB');im.save(p,optimize=True,compress_level=9)
print('PASS16 lossless full-page review images; Germany pilot3 widths refreshed')
