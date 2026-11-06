// Reproducible offline stand-ins, NOT actual CDN/network evidence.
const fs=require('fs'),path=require('path');
const nm=process.env.NODE_PATH.split(':')[0];
function fonts(){let css='';for(const [pkg,weights,styles] of [['outfit',[100,300,400,500,600,700],['normal']],['cormorant-garamond',[300,400,600,700],['normal','italic']]])for(const weight of weights)for(const style of styles){const file=`${pkg}-latin-${weight}-${style}.woff2`;if(fs.existsSync(path.join(nm,'@fontsource',pkg,'files',file)))css+=`@font-face{font-family:'${pkg==='outfit'?'Outfit':'Cormorant Garamond'}';font-weight:${weight};font-style:${style};font-display:swap;src:url('https://fonts.gstatic.com/phase25/${pkg}/${file}') format('woff2');}\n`;}return css;}
async function resources(route){const u=new URL(route.request().url());
 if(['127.0.0.1','localhost'].includes(u.hostname))return route.continue();
 if(u.hostname==='ilmerastudyabroad.com'&&u.pathname.startsWith('/assets/')){const f=path.resolve(process.cwd(),'.'+u.pathname);return route.fulfill({status:200,body:fs.readFileSync(f),contentType:u.pathname.endsWith('.webp')?'image/webp':'image/png'});}
 if(u.hostname==='fonts.googleapis.com')return route.fulfill({status:200,body:fonts(),contentType:'text/css'});
 if(u.hostname==='fonts.gstatic.com'&&u.pathname.startsWith('/phase25/')){const [pkg,file]=u.pathname.split('/').slice(2);return route.fulfill({status:200,body:fs.readFileSync(path.join(nm,'@fontsource',pkg,'files',file)),contentType:'font/woff2',headers:{'Access-Control-Allow-Origin':'*'}});}
 const scripts={'/ajax/libs/three.js/r128/three.min.js':'three/build/three.min.js','/ajax/libs/gsap/3.12.2/gsap.min.js':'gsap/dist/gsap.min.js','/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js':'gsap/dist/ScrollTrigger.min.js'};
 if(u.hostname==='cdnjs.cloudflare.com'&&scripts[u.pathname])return route.fulfill({status:200,body:fs.readFileSync(path.join(nm,scripts[u.pathname])),contentType:'text/javascript'});
 return route.abort();
}
module.exports={resources,fonts};
