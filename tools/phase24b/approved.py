"""Exact authorized source transformations, used independently by current checks."""
import json,re,subprocess
from team_bio_policy import ZAHEER,FAWAZ,FAWAZ_SAME_AS
BASELINE='0c5c437b901aacbff12e0a66df1d8e098627f334'
DENY=b'# Internal owner evidence and verification artifacts, not website content.\r\nRequire all denied\r\n'
ROOT_DENY=b'\r\n# Phase 24b: internal notes, scripts and audit data are not public website files.\r\n<FilesMatch "(?i)(?:\\.(?:md|py|cjs|log|bak)$|^phase.*\\.json$)">\r\n    Require all denied\r\n</FilesMatch>\r\n'
def old(root,file):return subprocess.check_output(['git','show',BASELINE+':'+file],cwd=root)
def expected_source(root,file,stage=5):
 data=old(root,file)
 if file=='data/team.json':
  obj=json.loads(data);obj['reviewed_on']='2026-10-23';obj['basis']='Owner-approved Phase 24b bios; Jabir unchanged. First-party portfolio supports Fawaz credentials and SEO start.'
  obj['members'][1]['description']=FAWAZ;obj['members'][1]['sameAs']=FAWAZ_SAME_AS;obj['members'][2]['description']=ZAHEER
  return (json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()
 if file in ['about.php','index.php']:
  text=data.decode();previous=json.loads(old(root,'data/team.json'))['members'];text=text.replace(previous[2]['description'],ZAHEER)
  if file=='about.php':
   text=re.sub(r'(<p class="team-bio">)(.*?)(</p>)',lambda m:m[1]+FAWAZ+m[3] if 'Fawaz BH' in m[2] else m[0],text,flags=re.S)
   text=re.sub(r'("description": ")Fawaz BH[^"\r\n]*(")',lambda m:m[1]+FAWAZ+m[2],text)
   text=re.sub(r'("text": ")Fawaz BH[^"\r\n]*(")',lambda m:m[1]+FAWAZ+m[2],text)
   text=re.sub(r'(<summary>Who is Fawaz BH\?</summary><div><p>).*?(</p>)',lambda m:m[1]+FAWAZ+m[2],text,flags=re.S)
   # Legacy detailed credential nodes are replaced by the approved description,
   # avoiding additional institution-name contexts beyond the two exact bios.
   text=re.sub(r'      "hasCredential": \[.*?      \],\r\n','',text,count=1,flags=re.S)
   start=text.index('      "@id": "https://ilmerastudyabroad.com/#fawaz"');end=text.index('      "@id": "https://ilmerastudyabroad.com/#zaheer"',start)
   block=text[start:end];block=re.sub(r'"sameAs": \[.*?\]', '"sameAs": '+json.dumps(FAWAZ_SAME_AS),block,count=1,flags=re.S);text=text[:start]+block+text[end:]
  else:
   text=text.replace("Drives ILMERA's digital presence and helps students find clear, honest information about their study-abroad options.",FAWAZ)
   text=text.replace('"sameAs": ["https://fawazbhseo.in"]','"sameAs": '+json.dumps(FAWAZ_SAME_AS))
   for name,bio in [('Fawaz BH',FAWAZ),('Zaheer KJ',ZAHEER)]:text=text.replace('"name": "'+name+'",','"name": "'+name+'", "description": '+json.dumps(bio)+',')
  return text.encode()
 if stage>=2 and file.startswith('blog/') and file.endswith('.php'):
  return re.sub(rb'(<img\b[^>]*\bsrc=")(https://ilmerastudyabroad.com)?/assets/images/fawazbh\.webp(")',lambda m:m[1]+(m[2] or b'')+b'/assets/images/fawazbh-192.webp'+m[3],data)
 if stage>=2 and file=='includes/site-presentation.php':
  return data.replace(b"$imagePath === '/assets/images/fawazbh.webp'",b"in_array($imagePath, ['/assets/images/fawazbh.webp','/assets/images/fawazbh-192.webp'], true)")
 if stage>=3 and file=='.htaccess':return data+ROOT_DENY
 return data
