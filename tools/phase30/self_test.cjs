// Tests the PHP handler and fail-closed guards, not native .htaccess redirects.
const fs=require('fs'),path=require('path'),{PHP}=require('@php-wasm/universal'),{loadNodeRuntime}=require('@php-wasm/node');
(async()=>{const root=path.resolve(__dirname,'../..'),source=fs.readFileSync(root+'/deploy-check.php','utf8'),key=source.match(/const ILMERA_DEPLOY_CHECK_KEY = '([a-f0-9]{64})';/)[1],m=JSON.parse(fs.readFileSync(root+'/reports/phase-27-payload-manifest.json'));
const php=new PHP(await loadNodeRuntime('8.5',{emscriptenOptions:{processId:1}}));php.mkdirTree('/site');
for(const row of m.files){if(row.path==='deploy-check.php')continue;const f='/site/'+row.path;php.mkdirTree(path.posix.dirname(f));php.writeFile(f,fs.readFileSync(root+'/'+row.path));}php.writeFile('/site/deploy-check.php',source);php.chdir('/site');let cases=[];
async function run(label,query,expected,method='GET'){
 const out=await php.run({method,scriptPath:'/site/deploy-check.php',relativeUri:'/deploy-check.php'+(query?'?'+query:''),server:{QUERY_STRING:query,REQUEST_METHOD:method,HTTP_HOST:'ilmerastudyabroad.com',HTTPS:'on'}});
 if(out.errors||out.exitCode)throw Error(out.errors||'PHP failure');
 if(out.httpStatusCode!==expected)throw Error(label+' status '+out.httpStatusCode);
 const h=Object.fromEntries(Object.entries(out.headers).map(([k,v])=>[k.toLowerCase(),String(v)]));if(!h['x-robots-tag']?.includes('noindex')||!h['cache-control']?.includes('no-store'))throw Error(label+' missing headers');
 if(expected===404&&out.text!=='Not found')throw Error(label+' information leak');
 if(out.text.includes('/site/')||out.text.includes(key)||out.text.includes('ILMERA_DEPLOY_CHECK_KEY'))throw Error(label+' secret/server path exposed');
 cases.push({case:label,status:out.httpStatusCode,plain_404:expected===404,noindex:true,no_store:true});return out.text;
}
await run('missing key','',404);await run('wrong key','key='+'0'.repeat(64),404);await run('traversal in key','key=../../etc/passwd',404);await run('extra file parameter','key='+key+'&file=../../etc/passwd',404);await run('arbitrary extra parameter','key='+key+'&x=1',404);await run('duplicate key','key='+key+'&key='+key,404);await run('array key','key[]='+key,404);await run('encoded parameter','%6bey='+key,404);await run('post method','key='+key,404,'POST');
php.writeFile('/site/deploy-check.php',source.replace(/const ILMERA_DEPLOY_CHECK_EXPIRES_AT = \d+;/,'const ILMERA_DEPLOY_CHECK_EXPIRES_AT = 0;'));await run('expired copied fixture','key='+key,404);php.writeFile('/site/deploy-check.php',source);
let good=await run('correct key clean payload','key='+key,200);if(!good.includes('ALL FILES OK')||!good.includes('<h2>FAIL</h2><p>None.</p>'))throw Error('Clean payload not OK');
// Changing policy contents must not invoke hashing or count as a hash mismatch.
php.writeFile('/site/.htaccess','DO NOT READ POLICY CONTENT');good=await run('policy exists-only contents changed','key='+key,200);if(!good.includes('ALL FILES OK')||good.includes('DO NOT READ'))throw Error('Policy content read or displayed');
const css=fs.readFileSync(root+'/assets/css/visual-system.css');php.unlink('/site/assets/css/visual-system.css');let missing=await run('missing critical CSS','key='+key,200);if(!missing.includes('1 PROBLEMS FOUND')||!missing.includes('assets/css/visual-system.css: MISSING'))throw Error('Missing CSS not listed');php.writeFile('/site/assets/css/visual-system.css','bad');let bad=await run('mismatched critical CSS','key='+key,200);if(!bad.includes('HASH MISMATCH'))throw Error('Mismatch not detected');php.writeFile('/site/assets/css/visual-system.css',css);
// No runtime file parameter, directory API, environment dump, writes or content display.
for(const forbidden of ['phpinfo(', 'getenv(', 'scandir(', 'glob(', 'opendir(', 'readdir(', 'file_put_contents(', 'fopen(', 'readfile(', 'file_get_contents('])if(source.includes(forbidden))throw Error('Forbidden API '+forbidden);
php.exit();fs.writeFileSync(root+'/reports/phase-30-self-check-tests.json',JSON.stringify({passed:true,cases,random_key_bits:256,expiry:'2026-11-16T00:00:00Z',valid_through:'2026-11-15 UTC',native_engine:false,key_not_serialized_in_test_evidence:true,manifest_self_hash_exception:'Temporary checker existence-only; offline manifest hashes actual file',critical_payload_fixed_path_tests:true},null,2)+'\n');console.log('PASS self-check '+cases.length+' authorization/expiry/manifest tests; no key in evidence');})();
