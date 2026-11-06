/* Static decorative canvas, never a WebGL scene or LCP image. No animation loop. */
(function(){
  'use strict';
  var canvas=document.querySelector('.p25-hero-scene');
  if(!canvas||navigator.connection&&navigator.connection.saveData)return;
  var image=null,loaded=false,started=false,scheduled=false;
  function draw(){
    if(document.hidden||!loaded)return;
    var box=canvas.getBoundingClientRect(),ratio=Math.min(window.devicePixelRatio||1,2);
    if(!box.width||!box.height)return;
    canvas.width=Math.round(box.width*ratio);canvas.height=Math.round(box.height*ratio);
    var context=canvas.getContext('2d');if(!context)return;
    var scale=Math.max(canvas.width/image.naturalWidth,canvas.height/image.naturalHeight);
    var w=image.naturalWidth*scale,h=image.naturalHeight*scale;
    context.drawImage(image,(canvas.width-w)/2,(canvas.height-h)/2,w,h);
  }
  function start(){
    scheduled=false;if(document.hidden||started)return;started=true;
    image=new Image();image.decoding='async';
    image.onload=function(){loaded=true;draw();};
    image.srcset='/assets/images/hero-still-720.webp 720w, /assets/images/hero-still-1440.webp 1440w';
    image.sizes='100vw';image.src='/assets/images/hero-still-720.webp';
  }
  function schedule(){
    if(document.hidden||started||scheduled)return;scheduled=true;
    // Two content frames precede decoding. Save-Data makes no image request.
    requestAnimationFrame(function(){requestAnimationFrame(function(){
      if('requestIdleCallback' in window)requestIdleCallback(start,{timeout:1500});else setTimeout(start,0);
    });});
  }
  document.addEventListener('visibilitychange',function(){if(!document.hidden){if(loaded)draw();else{scheduled=false;schedule();}}});
  if('ResizeObserver' in window)new ResizeObserver(draw).observe(canvas.parentElement);
  // Reduced-motion has nothing to stop: stills, no parallax, no recurring RAF.
  schedule();
})();
