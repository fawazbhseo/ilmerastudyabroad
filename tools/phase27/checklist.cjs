// Offline printable two-page rendering of the owner Markdown, not a website file.
const fs=require('fs'),path=require('path'),{marked}=require('marked'),{chromium}=require('playwright'),packed=require('@sparticuz/chromium');
(async()=>{const root=path.resolve(__dirname,'../..'),md=fs.readFileSync(path.join(root,'reports/post-deploy-checklist.md'),'utf8');
const content=marked.parse(md.replace('<!-- PAGE BREAK -->','<div class="break"></div>'));
const b=await chromium.launch({executablePath:await packed.executablePath(),args:packed.args.filter(a=>!['--single-process','--in-process-gpu'].includes(a)),headless:true});
const p=await b.newPage();await p.route('**/*',r=>r.abort());
await p.setContent('<!doctype html><meta charset="utf-8"><style>@page{size:A4;margin:9mm 10mm}body{font-family:Arial,sans-serif;font-size:9.2pt;line-height:1.1;color:#111}h1{font-size:14pt;margin:0 0 5pt}h2{font-size:10.2pt;margin:6pt 0 2pt}p{margin:3pt 0}ul{padding-left:13pt;margin:3pt 0}li{margin:2pt 0}table{width:100%;border-collapse:collapse;margin:3pt 0;font-size:8.5pt}td,th{border:0.4pt solid #bbb;padding:2pt 3pt;text-align:left}a{color:#123f6c;text-decoration:none}tr{break-inside:avoid}.break{break-before:page}code{font-size:8pt}</style>'+content);
await p.pdf({path:path.join(root,'reports/post-deploy-checklist.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();console.log('Printed owner checklist PDF from Markdown, no external requests');})().catch(e=>{console.error(e);process.exit(1)});
