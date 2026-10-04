const screens=[...document.querySelectorAll('.screen')];
const counter=document.getElementById('current');
let step=0;
function go(n){
 const old=screens[step]; old.classList.add('exit');
 setTimeout(()=>{old.classList.remove('active','exit');step=n;screens[step].classList.add('active');counter.textContent=String(step+1).padStart(2,'0');window.scrollTo({top:0,behavior:'smooth'});},360);
}
document.querySelectorAll('.next').forEach(b=>b.addEventListener('click',()=>{if(step<screens.length-1)go(step+1)}));
document.getElementById('restart').addEventListener('click',()=>go(0));
document.getElementById('showContact').addEventListener('click',e=>{document.getElementById('contactBox').classList.add('show');e.currentTarget.style.display='none'});
document.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key==='ArrowRight')&&step<3)go(step+1)});
