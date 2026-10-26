// Read-only diagnostic adapter. Native Apache/LiteSpeed policy is NOT executed.
const {PHP}=require('@php-wasm/universal'),{loadNodeRuntime}=require('@php-wasm/node');
const fs=require('fs'),path=require('path'),http=require('http');
const W='/home/user/phase29',root=W+'/payload',port=Number(process.env.PORT||8090);let chain=Promise.resolve();
fs.mkdirSync(W+'/renders',{recursive:true});fs.mkdirSync(W+'/diagnostics',{recursive:true});
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);}
const payload=walk(root),changed=new Set(JSON.parse(fs.readFileSync(W+'/changed-php.json')));
async function render(kind,file,uri){
 const version=kind.startsWith('php-')?kind.slice(4):'8.5';const php=new PHP(await loadNodeRuntime(version,{emscriptenOptions:{processId:1}}));
 const source=['cached-phase13','changed-php-over-phase13'].includes(kind)?W+'/phase13':root,sub=kind==='subfolder'?'/preview':'';
 php.mkdirTree('/site'+sub);
 for(const f of (source===root?payload:walk(source))){let rel=path.relative(source,f);
  if(kind==='changed-php-over-phase13'&&rel.startsWith('assets/'))continue;
  if(kind==='disk-css-missing'&&rel==='assets/css/visual-system.css')continue;
  if(kind==='disk-fonts-missing'&&rel.startsWith('assets/fonts/'))continue;
  if(kind.startsWith('no-assets')&&rel.startsWith('assets/'))continue;
  if(kind==='changed-php-only'&&!(rel.endsWith('.php')&&changed.has(rel)))continue;
  if(kind==='config-missing'&&rel==='includes/visual-config.php')continue;
  if(['header-missing','no-assets-header-missing'].includes(kind)&&rel==='includes/header.php')continue;
  if(kind==='visual-missing'&&rel==='includes/visual-system.php')continue;
  const target='/site'+sub+'/'+rel;php.mkdirTree(path.posix.dirname(target));php.writeFile(target,fs.readFileSync(f));
 }
 if(kind==='changed-php-over-phase13')for(const f of payload){const rel=path.relative(root,f);if(rel.endsWith('.php')&&changed.has(rel)){const target='/site/'+rel;php.mkdirTree(path.posix.dirname(target));php.writeFile(target,fs.readFileSync(f));}}
 php.chdir('/site'+sub);
 const definitions=kind==='scenes-off'?"define('ILMERA_SCENES_ENABLED',false);":kind==='groups-disabled'?"define('ILMERA_VISUAL_TEMPLATE_GROUPS',[]);":'';
 // A development adapter throwing on every warning would conceal production-style
 // warning-only empty CSS/font reads. Capture all warnings, suppress display only.
 const code="<?php ini_set('display_errors','0');error_reporting(E_ALL);"+definitions+"register_shutdown_function(static function(){file_put_contents('/trace.json',json_encode(get_included_files()));});require '/site"+sub+'/'+file+"';";
 let out;try{out=await php.run({code,relativeUri:uri,server:{DOCUMENT_ROOT:'/site',HTTP_HOST:'ilmerastudyabroad.com',SERVER_NAME:'ilmerastudyabroad.com',HTTPS:'on',REQUEST_URI:uri,SCRIPT_NAME:sub+'/'+file,SCRIPT_FILENAME:'/site'+sub+'/'+file}});}catch(e){if(!e.response){php.exit();throw e;}out=e.response;}
 const diag={case:kind,route:uri,php:version,exitCode:out.exitCode,status:out.httpStatusCode,errors:out.errors,includes:php.fileExists('/trace.json')?JSON.parse(php.readFileAsText('/trace.json')):[],native_acl_test:false};
 fs.writeFileSync(W+'/diagnostics/'+kind+'-'+file.replaceAll('/','_')+'.json',JSON.stringify(diag,null,2));
 const html=Buffer.from(out.bytes);php.exit();fs.writeFileSync(W+'/renders/'+kind+'-'+file.replaceAll('/','_')+'.html',html);return {html,status:out.exitCode?500:out.httpStatusCode};
}
async function serve(q,r){let kind=q.headers['x-phase29-case']||'normal';let uri=new URL(q.url,'http://proof').pathname;
 if(!/^[a-z0-9.-]+$/.test(kind)){r.writeHead(400);r.end();return;}
 const sub=kind==='subfolder';if(sub&&!uri.startsWith('/preview/')){r.writeHead(404);r.end('Subfolder fault: asset not in domain root');return;}
 let name=(sub?uri.slice('/preview'.length):uri).slice(1);if(name===''||name==='blog/')name=name===''?'index.php':'blog/index.php';if(!path.extname(name))name+='.php';
 if(name.includes('..')||/^\.?\/?(?:includes|data|destinations|places|reports|tools)\//.test(name)||path.basename(name).startsWith('.')||/^phase.*\.json$/.test(name)){r.writeHead(403);r.end('Forbidden');return;}
 if(kind==='http-css-404'&&name==='assets/css/visual-system.css'){r.writeHead(404);r.end('Not found');return;}
 if(kind==='http-css-403'&&name==='assets/css/visual-system.css'){r.writeHead(403);r.end('Forbidden');return;}
 if(kind==='http-fonts-404'&&name.startsWith('assets/fonts/')){r.writeHead(404);r.end('Not found');return;}
 if(kind.startsWith('no-assets')&&name.startsWith('assets/')){r.writeHead(404);r.end('Not found');return;}
 if(!fs.existsSync(root+'/'+name)){r.writeHead(404);r.end('Not found');return;}
 if(!name.endsWith('.php')){let mime={'.woff2':'font/woff2','.css':'text/css','.png':'image/png','.webp':'image/webp','.ico':'image/x-icon','.txt':'text/plain','.xml':'application/xml','.html':'text/html'}[path.extname(name)]||'application/octet-stream';r.writeHead(200,{'Content-Type':mime});r.end(q.method==='HEAD'?undefined:fs.readFileSync(root+'/'+name));return;}
 let out=kind==='cached-predesign'?{html:fs.readFileSync(W+'/cached-predesign.html'),status:200}:await render(kind,name,uri);
 r.writeHead(out.status,{'Content-Type':'text/html; charset=UTF-8','Cache-Control':'no-store'});r.end(q.method==='HEAD'?undefined:out.html);
}
http.createServer((q,r)=>{chain=chain.then(()=>serve(q,r)).catch(e=>{console.error(e);if(!r.headersSent)r.writeHead(500);r.end('Diagnostic adapter failure');});}).listen(port,'0.0.0.0',()=>console.log('Phase29 diagnostic adapter 0.0.0.0:'+port+'; clean ZIP only; no native rule engine'));
