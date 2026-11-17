(()=>{
const $=id=>document.getElementById(id),app=$("app");
let sek=30,hedef="",box=$("matn"),inp=$("in"),spans=[],boshi=null,tim=null,tugadi=true,jami=0,xato=0,seriya=[];
const togriSoni=()=>{let c=0;for(let i=0;i<inp.value.length;i++)if(inp.value[i]===hedef[i])c++;return c};
function chiz(matn){const f=document.createDocumentFragment();[...matn].forEach(ch=>{const s=document.createElement("span");s.textContent=ch;f.appendChild(s);spans.push(s)});box.appendChild(f)}
function yangila(){const v=inp.value;spans.forEach((s,i)=>{s.className=i<v.length?(v[i]===hedef[i]?"ok":"bad"):(i===v.length?"cur":"")});
 const c=spans[v.length];if(c&&c.offsetTop>40)box.scrollTop=c.offsetTop-40}
async function yukla(){const r=await fetch(app.dataset.matn);const d=await r.json();hedef=d.matn;spans=[];box.textContent="";chiz(hedef);yangila()}
function stat(){const t=boshi?Math.min((Date.now()-boshi)/1000,sek):0,c=togriSoni();
 $("t").textContent=Math.max(0,Math.ceil(sek-t));$("w").textContent=t>1?Math.round(c/5/(t/60)):0;
 $("a").textContent=(jami?Math.round(c/jami*100):100)+"%";$("x").textContent=jami-c;return {t,c}}
function tik(){const {t}=stat();if(t>=sek)tugat();else if(Math.floor(t)>seriya.length){const c=togriSoni(),w=c/5/(Math.floor(t)/60);seriya.push({w,a:jami?c/jami*100:100})}}
async function tugat(){if(tugadi)return;tugadi=true;clearInterval(tim);inp.disabled=true;$("boshla").disabled=false;
 const c=togriSoni(),acc=jami?c/jami*100:0,w=c/5/(sek/60);
 const R={wpm:w,cpm:c/(sek/60),acc,x:jami-c,c,sek,rek:null,old:null,saved:false};
 if(app.dataset.auth==="1"){try{const r=await fetch(app.dataset.url,{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":cookie("csrftoken")},
  body:JSON.stringify({vaqt:sek,togri:c,jami,seriya:seriya.map(p=>p.w)})});if(r.ok){const d=await r.json();R.rek=d.rekord_qiymat;R.old=d.oldingi_ortacha;R.yangi=d.rekord;R.saved=true}}catch(e){}}
 korsat(R)}
function cookie(n){return (document.cookie.split("; ").find(x=>x.startsWith(n+"="))||"").split("=")[1]||""}
function korsat(R){$("rw").textContent=Math.round(R.wpm);$("ra").textContent=Math.round(R.acc)+"%";$("rc").textContent=Math.round(R.cpm);$("rx").textContent=R.x;
 $("rt").textContent=R.c;$("rv").textContent=R.sek+" soniya";$("rr").textContent=R.saved?R.rek:"—";$("sana").textContent=new Date().toLocaleString("uz-UZ");
 const rk=$("rek");rk.hidden=!R.yangi;rk.textContent="Yangi shaxsiy rekord!";
 $("solish").textContent=!R.saved?"Natija saqlanmadi. Saqlash uchun tizimga kiring.":R.old===null?"Bu sizning birinchi mashqingiz.":
  "Oldingi o‘rtacha natijangiz: "+R.old+" WPM. Farq: "+(Math.round(R.wpm)-R.old>=0?"+":"")+(Math.round(R.wpm)-R.old)+" WPM.";
 grafik($("g1"),seriya.map(p=>p.w));grafik($("g2"),seriya.map(p=>p.a),100);$("modal").hidden=false}
function grafik(svg,v,max){svg.innerHTML="";if(v.length<2)return;const m=max||Math.max(...v,10),n=v.length-1;
 const p=v.map((y,i)=>(10+i/n*280).toFixed(1)+","+(80-Math.min(y,m)/m*70).toFixed(1)).join(" ");
 svg.innerHTML='<polyline fill="none" stroke="#25845A" stroke-width="2" points="'+p+'"/>'}
async function boshla(){clearInterval(tim);tugadi=false;boshi=null;jami=0;seriya=[];inp.value="";inp.disabled=false;$("modal").hidden=true;
 $("boshla").disabled=true;await yukla();stat();inp.focus()}
inp.addEventListener("paste",e=>e.preventDefault());
inp.addEventListener("input",()=>{if(tugadi)return;const v=inp.value,prev=inp._p||0;
 if(v.length>prev)for(let i=prev;i<v.length;i++)jami++;inp._p=v.length;
 if(!boshi){boshi=Date.now();tim=setInterval(tik,200)}
 if(v.length>hedef.length-60)fetch(app.dataset.matn).then(r=>r.json()).then(d=>{hedef+=" "+d.matn;chiz(" "+d.matn);yangila()});
 yangila();stat()});
document.querySelectorAll("#vaqt button").forEach(b=>b.onclick=()=>{if(!tugadi&&boshi)return;sek=+b.dataset.s;document.querySelectorAll("#vaqt button").forEach(x=>x.classList.toggle("on",x===b));$("t").textContent=sek});
$("boshla").onclick=()=>{inp._p=0;boshla()};$("qayta").onclick=()=>{inp._p=0;boshla()};
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!tugadi){clearInterval(tim);tugadi=true;inp.disabled=true;$("boshla").disabled=false}});
yukla();
})();
