// Local verification adapter, not an Apache rewrite/access-control simulator.
const {PHP}=require('@php-wasm/universal');
const {loadNodeRuntime,useHostFilesystem}=require('@php-wasm/node');
const http=require('http'),fs=require('fs'),path=require('path');
const root=process.cwd(); let php,requests=0,chain=Promise.resolve();
async function reset(){if(php)php.exit();php=new PHP(await loadNodeRuntime('8.5',{emscriptenOptions:{processId:1}}));useHostFilesystem(php);php.chdir(root);requests=0;}
async function serve(req,res){
 const uri=new URL(req.url,'http://adapter').pathname;
 let file=uri==='/'?'index.php':uri==='/blog/'?'blog/index.php':uri.slice(1);
 if(uri==='/sitemap')file='sitemap.php';
 if(!path.extname(file))file+='.php';
 const full=path.resolve(root,file);
 if(!full.startsWith(root+'/')||file.startsWith('.')||/^(includes|data|tools|destinations|places)\//.test(file)){res.writeHead(403);res.end('Forbidden');return;}
 if(!fs.existsSync(full)){res.writeHead(404);res.end('Not found');return;}
 if(!file.endsWith('.php')){const mime={'.png':'image/png','.webp':'image/webp','.ico':'image/x-icon','.xml':'application/xml','.txt':'text/plain','.css':'text/css','.js':'text/javascript'};res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream'});res.end(fs.readFileSync(full));return;}
 if(requests++>70)await reset();
 const out=await php.run({scriptPath:full,relativeUri:req.url,server:{DOCUMENT_ROOT:root,HTTP_HOST:'ilmerastudyabroad.com',SERVER_NAME:'ilmerastudyabroad.com',HTTPS:'on',REQUEST_URI:req.url,SCRIPT_NAME:'/'+file,SCRIPT_FILENAME:full}});
 if(out.exitCode||out.errors)throw new Error(out.errors||'PHP failure');
 res.writeHead(out.httpStatusCode,out.headers);res.end(Buffer.from(out.bytes));
}
(async()=>{await reset();http.createServer((req,res)=>{chain=chain.then(()=>serve(req,res)).catch(e=>{console.error(e);if(!res.headersSent)res.writeHead(500);res.end('Local adapter error');});}).listen(8080,'0.0.0.0',()=>console.log('PHP 8.5 local verification adapter listening on 0.0.0.0:8080'));})();
