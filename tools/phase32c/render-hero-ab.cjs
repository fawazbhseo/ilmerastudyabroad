#!/usr/bin/env node
'use strict';

// Render only the two frozen Task 3 routes from one isolated PHP-WASM source tree.
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const {PHP}=require('@php-wasm/universal');
const {loadNodeRuntime}=require('@php-wasm/node');

const ROUTES=[
  '/study-abroad-counselling-mysuru',
  '/blog/how-to-choose-study-abroad-consultant-karnataka',
];
const ARM=process.env.PHASE32C_HERO_ARM;
const SOURCE_ROOT=path.resolve(process.env.PHASE32C_HERO_SOURCE_ROOT||'');
const SOURCE_COMMIT=process.env.PHASE32C_HERO_SOURCE_COMMIT||'';
const EVIDENCE=path.resolve(process.env.PHASE32C_HERO_EVIDENCE||'/home/user/phase32c-runtime/hero-ab');
const RUNTIME=process.env.PHASE31_RUNTIME||'/home/user/phase32c-runtime/node_modules';
const OUT=path.join(EVIDENCE,'renders',ARM||'missing');
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');

function routeFile(url){
  if(url==='/blog/')return 'blog/index.php';
  return url.replace(/^\//,'')+'.php';
}
function serverVars(url,file){
  return{
    DOCUMENT_ROOT:'/site',HTTP_HOST:'ilmerastudyabroad.com',SERVER_NAME:'ilmerastudyabroad.com',HTTPS:'on',
    REQUEST_URI:url,SCRIPT_NAME:'/'+file,SCRIPT_FILENAME:'/site/'+file,
    REQUEST_METHOD:'GET',SERVER_PORT:'443',SERVER_PROTOCOL:'HTTP/1.1',
  };
}
function runtimePath(rel){
  return /\.php$/i.test(rel)||/^(?:assets|data|includes|destinations|places|blog)\//.test(rel)||/^(?:index|llms(?:-full)?\.txt|favicon\.ico)$/.test(rel);
}
function walk(dir,root){
  return fs.readdirSync(dir,{withFileTypes:true}).flatMap(entry=>{
    const full=path.join(dir,entry.name);
    if(entry.isDirectory())return walk(full,root);
    if(entry.isFile())return[path.relative(root,full).split(path.sep).join('/')];
    return[];
  });
}
async function main(){
  if(!['A','B-still','B-plain'].includes(ARM))throw new Error('Set PHASE32C_HERO_ARM to A, B-still or B-plain');
  if(!SOURCE_COMMIT||!fs.existsSync(SOURCE_ROOT))throw new Error('A source commit and extracted source tree are required');
  const wasmDir=path.join(RUNTIME,'@php-wasm/node-8-5','asyncify');
  const php=new PHP(await loadNodeRuntime('8.5',{emscriptenOptions:{processId:1,locateFile:file=>path.isAbsolute(file)?file:path.join(wasmDir,file)}}));
  php.mkdirTree('/site');
  const files=walk(SOURCE_ROOT,SOURCE_ROOT).filter(runtimePath);
  for(const rel of files){
    const source=path.join(SOURCE_ROOT,rel);
    if(!fs.existsSync(source)||!fs.statSync(source).isFile())continue;
    const target='/site/'+rel;
    php.mkdirTree(path.posix.dirname(target));
    php.writeFile(target,fs.readFileSync(source));
  }
  php.chdir('/site');
  fs.mkdirSync(OUT,{recursive:true});
  const rows=[];
  for(const route of ROUTES){
    const file=routeFile(route);
    if(!php.fileExists('/site/'+file))throw new Error(`Missing route file ${file} for ${route}`);
    const result=await php.run({scriptPath:'/site/'+file,relativeUri:route,server:serverVars(route,file)});
    if(result.exitCode||result.errors)throw new Error(`PHP-WASM failed for ${route}: ${String(result.errors||result.exitCode)}`);
    if(result.httpStatusCode!==200)throw new Error(`Expected HTTP 200 for ${route}, received ${result.httpStatusCode}`);
    const body=Buffer.from(result.bytes);
    if(!body.length)throw new Error(`Empty PHP-WASM output for ${route}`);
    const name=route.replace(/^\//,'').replace(/[^A-Za-z0-9._-]+/g,'_')+'.html';
    const fileOut=path.join(OUT,name);
    fs.writeFileSync(fileOut,body);
    rows.push({route,status:result.httpStatusCode,bytes:body.length,sha256:sha(body),file:path.relative(EVIDENCE,fileOut).split(path.sep).join('/')});
    console.log(`RENDERED ${ARM} ${route} ${body.length} bytes`);
  }
  const report={arm:ARM,sourceCommit:SOURCE_COMMIT,sourceRoot:SOURCE_ROOT,phpWasm:'8.5.8',routeCount:rows.length,routes:rows};
  fs.writeFileSync(path.join(OUT,'routes.json'),JSON.stringify(report,null,2)+'\n');
  console.log(`RENDER COMPLETE ${ARM} ${rows.length} routes`);
}
main().then(()=>process.exit(0)).catch(error=>{console.error(error.stack||error);process.exit(1);});
