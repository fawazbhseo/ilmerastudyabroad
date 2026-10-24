// Isolated local proof only. Never parses native .htaccess or contacts production.
const {PHP}=require('@php-wasm/universal'),{loadNodeRuntime}=require('@php-wasm/node');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(process.argv[2]),port=Number(process.argv[3]||8084);let php,count=0,chain=Promise.resolve();
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(dir,d.name)):[path.join(dir,d.name)]);}
async function reset(){
 if(php)php.exit();php=new PHP(await loadNodeRuntime('8.5',{emscriptenOptions:{processId:1}}));
 php.mkdirTree('/site');
 for(const f of walk(root)){if(fs.lstatSync(f).isSymbolicLink())throw Error('No symlink allowed');const target='/site/'+path.relative(root,f);php.mkdirTree(path.posix.dirname(target));php.writeFile(target,fs.readFileSync(f));}
 php.chdir('/site');count=0;
 // No useHostFilesystem: original checkout is inaccessible from the PHP VM.
 const probe=await php.run({code:'<?php echo file_exists("/home/user/ilmerastudyabroad/index.php") ? "LEAK" : "ISOLATED";'});
 if(probe.text!=='ISOLATED')throw Error('PHP filesystem isolation failure');
}
async function serve(req,res){
 const uri=decodeURIComponent(new URL(req.url,'http://proof').pathname);
 if(/(?:^|\/)\.git(?:\/|$)/i.test(uri)||/(?:\.(?:md|py|cjs|log|bak|csv)$|^phase.*\.json$|^\.)/i.test(path.basename(uri))||/^\/(?:includes|data|tools|reports|destinations|places)(?:\/|$)/.test(uri)){res.writeHead(403);res.end(req.method==='HEAD'?undefined:'Forbidden');return;}
 let file=uri==='/'?'index.php':uri==='/blog/'?'blog/index.php':uri.slice(1);
 if(uri==='/sitemap.xml'||uri==='/sitemap'||uri==='/sitemap.php')file='sitemap.php';
 if(!path.extname(file))file+='.php';
 const full=path.resolve(root,file);
 if(!full.startsWith(root+'/')||!fs.existsSync(full)||!fs.statSync(full).isFile()){res.writeHead(404);res.end('Not found');return;}
 if(!file.endsWith('.php')){const mime={'.png':'image/png','.webp':'image/webp','.woff2':'font/woff2','.ico':'image/x-icon','.xml':'application/xml','.txt':'text/plain','.css':'text/css','.js':'text/javascript','.html':'text/html'};res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream'});res.end(req.method==='HEAD'?undefined:fs.readFileSync(full));return;}
 if(count++>70)await reset();
 const out=await php.run({scriptPath:'/site/'+file,relativeUri:req.url,server:{DOCUMENT_ROOT:'/site',HTTP_HOST:'ilmerastudyabroad.com',SERVER_NAME:'ilmerastudyabroad.com',HTTPS:'on',REQUEST_URI:req.url,SCRIPT_NAME:'/'+file,SCRIPT_FILENAME:'/site/'+file}});
 if(out.exitCode||out.errors)throw Error(out.errors||'PHP failure');
 res.writeHead(out.httpStatusCode,out.headers);res.end(req.method==='HEAD'?undefined:Buffer.from(out.bytes));
}
(async()=>{await reset();http.createServer((q,r)=>{chain=chain.then(()=>serve(q,r)).catch(e=>{console.error(e);if(!r.headersSent)r.writeHead(500);r.end('Local proof error');});}).listen(port,'0.0.0.0',()=>console.log('Isolated payload PHP8.5 on 0.0.0.0:'+port+'; no host filesystem mount'));})().catch(e=>{console.error(e);process.exit(1)});
