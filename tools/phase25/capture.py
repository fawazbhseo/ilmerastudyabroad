"""Capture baseline HTTP renders before any public source change."""
import json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from check_discovery import routes,fetch
root=pathlib.Path(__file__).resolve().parents[2];out=pathlib.Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);manifest={}
for i,(route,info) in enumerate(routes(root).items()):
 status,headers,body=fetch('http://127.0.0.1:8080',route);assert status==200,(route,status)
 name=f'{i:02}.html';(out/name).write_bytes(body);manifest[route]={'file':name,'info':info}
(out/'snapshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Captured',len(manifest),'routes')
