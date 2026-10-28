// Isolated local audit server. PHP runs inside PHP-WASM; no native hosting rules.
const { PHP } = require('@php-wasm/universal');
const { loadNodeRuntime } = require('@php-wasm/node');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { execFileSync } = require('node:child_process');

const ROOT = path.resolve(__dirname, '../..');
const SOURCE_ROOT = path.resolve(process.env.PHASE31_SOURCE_ROOT || ROOT);
const EVIDENCE = process.env.PHASE31_EVIDENCE || '/home/user/phase31';
const PORT = Number(process.env.PORT || 8080);
const OUT = path.join(EVIDENCE, 'render-before');
fs.mkdirSync(OUT, { recursive: true });
let php;
const pages = new Map();
let sitemap = '';
let chain = Promise.resolve();

function mime(file) {
  return ({
    '.css':'text/css; charset=utf-8', '.js':'text/javascript; charset=utf-8',
    '.png':'image/png', '.webp':'image/webp', '.jpg':'image/jpeg', '.jpeg':'image/jpeg',
    '.svg':'image/svg+xml', '.ico':'image/x-icon', '.woff2':'font/woff2',
    '.txt':'text/plain; charset=utf-8', '.xml':'application/xml; charset=utf-8',
    '.json':'application/json; charset=utf-8', '.html':'text/html; charset=utf-8'
  })[path.extname(file).toLowerCase()] || 'application/octet-stream';
}
function routeFile(url) {
  if (url === '/') return 'index.php';
  if (url === '/blog/') return 'blog/index.php';
  if (url === '/sitemap.xml') return 'sitemap.php';
  return url.replace(/^\//, '') + '.php';
}
function phpServer(url, file) {
  return {
    DOCUMENT_ROOT:'/site', HTTP_HOST:'ilmerastudyabroad.com', SERVER_NAME:'ilmerastudyabroad.com', HTTPS:'on',
    REQUEST_URI:url, SCRIPT_NAME:'/' + file, SCRIPT_FILENAME:'/site/' + file,
    REQUEST_METHOD:'GET', SERVER_PORT:'443', SERVER_PROTOCOL:'HTTP/1.1'
  };
}
async function main() {
  const packageDir = path.resolve(process.env.PHASE31_RUNTIME || '/home/user/phase31/runtime/node_modules');
  const wasmDir = path.join(packageDir, '@php-wasm/node-8-5', 'asyncify');
  php = new PHP(await loadNodeRuntime('8.5', {
    emscriptenOptions: {
      processId: 1,
      locateFile: file => path.isAbsolute(file) ? file : path.join(wasmDir, file)
    }
  }));
  php.mkdirTree('/site');
  const walk = dir => fs.readdirSync(dir,{withFileTypes:true}).flatMap(entry=>{
    const full=path.join(dir,entry.name);
    if(entry.isDirectory())return walk(full);
    return entry.isFile()?[path.relative(SOURCE_ROOT,full).split(path.sep).join('/')]:[];
  });
  const tracked = SOURCE_ROOT===ROOT
    ? execFileSync('git', ['ls-files', '-z'], { cwd:ROOT, encoding:'buffer' }).toString().split('\0').filter(Boolean)
    : walk(SOURCE_ROOT);
  const runtimePath = p => /\.php$/i.test(p) || /^(?:assets|data|includes|destinations|places|blog)\//.test(p) || /^phase14-[a-z-]+\.json$/.test(p) || /^(?:index|llms(?:-full)?\.txt|favicon\.ico)$/.test(p);
  for (const rel of tracked.filter(runtimePath)) {
    const source = path.join(SOURCE_ROOT, rel);
    if (!fs.existsSync(source) || !fs.statSync(source).isFile()) continue;
    const target = '/site/' + rel;
    php.mkdirTree(path.posix.dirname(target));
    php.writeFile(target, fs.readFileSync(source));
  }
  php.chdir('/site');
  const sitemapOut = await php.run({
    scriptPath:'/site/sitemap.php', relativeUri:'/sitemap.xml', server:phpServer('/sitemap.xml','sitemap.php')
  });
  if (sitemapOut.exitCode || sitemapOut.errors) throw new Error('Sitemap PHP failed: ' + sitemapOut.errors);
  sitemap = Buffer.from(sitemapOut.bytes).toString('utf8');
  fs.writeFileSync(path.join(EVIDENCE,'sitemap.xml'), sitemap);
  const routeBaseline = JSON.parse(fs.readFileSync(path.join(ROOT, 'reports/phase-25-baseline-renders.json'), 'utf8'));
  const routes = Object.keys(routeBaseline.routes || {}).sort();
  if (routes.length !== 43 || new Set(routes).size !== 43) throw new Error(`Expected exactly 43 routes in the frozen baseline inventory, got ${routes.length}`);
  const sitemapRoutes = [...sitemap.matchAll(/<loc>https:\/\/ilmerastudyabroad\.com([^<]*)<\/loc>/g)].map(m => decodeURIComponent(m[1]));
  if (sitemapRoutes.length !== 38 || new Set(sitemapRoutes).size !== 38) throw new Error(`Expected 38 current sitemap routes, got ${sitemapRoutes.length}`);
  const renders = [];
  for (const url of routes) {
    const file = routeFile(url);
    if (!php.fileExists('/site/' + file)) throw new Error(`Missing PHP route target ${file} for ${url}`);
    const out = await php.run({ scriptPath:'/site/' + file, relativeUri:url, server:phpServer(url,file) });
    if (out.exitCode || out.errors) throw new Error(`PHP render failed ${url}: ${out.errors}`);
    const body = Buffer.from(out.bytes);
    const name = url === '/' ? 'home' : url.replace(/^\//,'').replace(/\/$/,'').replace(/[^A-Za-z0-9._-]+/g,'_');
    const fileOut = path.join(OUT, name + '.html');
    fs.writeFileSync(fileOut, body);
    pages.set(url, body);
    renders.push({ url, file, status:out.httpStatusCode, bytes:body.length, evidence:path.basename(fileOut) });
  }
  const routeIndex = JSON.stringify({ source_head:execFileSync('git',['rev-parse','HEAD'],{cwd:ROOT,encoding:'utf8'}).trim(), routes:renders },null,2)+'\n';
  fs.writeFileSync(path.join(EVIDENCE,'routes.json'), routeIndex);
  fs.writeFileSync(path.join(OUT,'routes.json'), routeIndex);
  const server = http.createServer((req,res) => {
    let pathname;
    try { pathname = decodeURIComponent(new URL(req.url,'http://local').pathname); }
    catch { res.writeHead(400); return res.end('Bad request'); }
    if (pathname === '/sitemap.xml') {
      const b=Buffer.from(sitemap); res.writeHead(200,{'Content-Type':mime('sitemap.xml'),'Content-Length':b.length,'Cache-Control':'no-store'}); return res.end(req.method==='HEAD'?undefined:b);
    }
    if (pages.has(pathname)) {
      const b=pages.get(pathname); res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Content-Length':b.length,'Cache-Control':'no-store'}); return res.end(req.method==='HEAD'?undefined:b);
    }
    const rel=pathname.replace(/^\//,'');
    const full=path.resolve(SOURCE_ROOT,rel);
    const privatePath=/^(?:reports|tools|includes|data|destinations|places)(?:\/|$)/i.test(rel);
    if (!full.startsWith(SOURCE_ROOT + path.sep) || /(?:^|\/)\.(?:git|svn|htaccess|htpasswd)(?:\/|$)/i.test(rel) || privatePath || /\.(?:php|md|py|cjs|csv|zip|json)$/i.test(rel)) {
      res.writeHead(404,{'Cache-Control':'no-store'}); return res.end('Not found');
    }
    if (!fs.existsSync(full) || !fs.statSync(full).isFile()) { res.writeHead(404,{'Cache-Control':'no-store'}); return res.end('Not found'); }
    const b=fs.readFileSync(full); res.writeHead(200,{'Content-Type':mime(full),'Content-Length':b.length,'Cache-Control':'no-store'}); res.end(req.method==='HEAD'?undefined:b);
  });
  server.listen(PORT,'0.0.0.0',()=>console.log(`Phase31 isolated PHP-WASM audit adapter on 0.0.0.0:${PORT}; ${routes.length} rendered routes; native .htaccess not executed`));
}
main().catch(e=>{console.error(e.stack||e);process.exit(1);});
