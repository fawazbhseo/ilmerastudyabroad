#!/usr/bin/env node
// Task4-only equal-delivery A/B fixture host. Not a production router or deployment server.
const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const ROOT=path.resolve(__dirname,'../..');
const EVIDENCE=path.resolve(process.env.PHASE31_AB_EVIDENCE||'/home/user/phase31/task4');
const PORT=Number(process.env.PORT||8082);
const fixturePath=path.join(EVIDENCE,'fixtures.json'),selectionPath=path.join(EVIDENCE,'selected.json');
if(!fs.existsSync(fixturePath)||!fs.existsSync(selectionPath))throw Error('Task4 fixtures and selected.json must be frozen before server startup');
const fixtures=JSON.parse(fs.readFileSync(fixturePath,'utf8'));
const pages=new Set(Object.keys(fixtures));
function send(res,status,headers,body=''){res.writeHead(status,headers);res.end(body);}
function mime(file){return({'.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.png':'image/png','.webp':'image/webp','.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml','.ico':'image/x-icon','.woff2':'font/woff2','.txt':'text/plain; charset=utf-8','.xml':'application/xml; charset=utf-8'})[path.extname(file).toLowerCase()]||'application/octet-stream';}
const server=http.createServer((req,res)=>{
 let pathname;try{pathname=decodeURIComponent(new URL(req.url,'http://fixture').pathname);}catch{return send(res,400,{'Cache-Control':'no-store'},'Bad request');}
 if(pathname.startsWith('/assets/')){
  const full=path.resolve(ROOT,'.'+pathname);
  if(!full.startsWith(path.join(ROOT,'assets')+path.sep)||!fs.existsSync(full)||!fs.statSync(full).isFile())return send(res,404,{'Cache-Control':'no-store'});
  const body=fs.readFileSync(full);return send(res,200,{'Content-Type':mime(full),'Content-Length':body.length,'Cache-Control':'no-store'},req.method==='HEAD'?'':body);
 }
 if(!pages.has(pathname))return send(res,404,{'Cache-Control':'no-store'});
 let selected;try{selected=JSON.parse(fs.readFileSync(selectionPath,'utf8'));}catch(e){console.error('Invalid A/B selection',e.message);return send(res,500,{'Cache-Control':'no-store'});}
 if(selected.route!==pathname||!['A','B'].includes(selected.variant))return send(res,404,{'Cache-Control':'no-store'});
 const body=Buffer.from(fixtures[pathname][selected.variant]);
 return send(res,200,{'Content-Type':'text/html; charset=utf-8','Content-Length':body.length,'Cache-Control':'no-store'},req.method==='HEAD'?'':body);
});
server.listen(PORT,'0.0.0.0',()=>console.log(`Task4 isolated A/B fixtures on 0.0.0.0:${PORT}; ${pages.size} routes; no public app or live data`));
