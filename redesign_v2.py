# -*- coding: utf-8 -*-
# Редизайн по одобренному плану (24.11). Применяется к копии backups/v1/index.ru.bak -> site/index.ru.bak
import re
SRC='/home/claude/backups/v1/index.ru.bak'; OUT='/home/claude/site/index.ru.bak'
s=open(SRC,encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt,('найдено %d раз: %r'%(n,a[:90]))
    s=s.replace(a,b)
def cut(start,end_marker,new=''):
    """заменить кусок от start (включительно) до end_marker (не включая)"""
    global s
    i=s.index(start); j=s.index(end_marker,i)
    assert s.count(start)==1
    s=s[:i]+new+s[j:]

WA_ICON='<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'

# ---------- 1. первый экран ----------
rep('<span class="flip" id="flip1" aria-hidden="true"></span>','<span class="v2rot" id="flip1" aria-hidden="true"></span>')
rep('<a class="btn mag" href="https://wa.me/972587800228" target="_blank" rel="noopener">Расскажите о вашем деле <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8h10M9 4l4 4-4 4"/></svg></a><a class="btn ghost mag" href="#works">Смотреть работы</a><button type="button" class="btn ghost mag vbtn" id="vOpen"><svg viewBox="0 0 16 16" fill="currentColor"><path d="M4 2.5v11l9-5.5z"/></svg>Ролик · 17 секунд</button></div>',
    '<a class="btn mag" href="https://wa.me/972587800228" target="_blank" rel="noopener">'+WA_ICON+'Написать в WhatsApp</a><a class="btn ghost mag" href="#works">Смотреть работы</a></div>\n  <button type="button" class="v2vid" id="vOpen"><svg viewBox="0 0 16 16" width="12" height="12" fill="currentColor" aria-hidden="true"><path d="M4 2.5v11l9-5.5z"/></svg>Ролик · 17 секунд</button>')
# спокойная смена слов вместо табло
rep("new Flip(document.getElementById('flip1'),['САЙТЫ','МАГАЗИНЫ','ПРИЛОЖЕНИЯ','КАТАЛОГИ']);",
"""function V2Rot(n0,words){if(!n0)return;var sp=words.map(function(w){var e=document.createElement('span');e.textContent=w;n0.appendChild(e);return e;}),k=0;sp[0].classList.add('on');function fit(){n0.style.width=sp[k].offsetWidth+'px';}fit();addEventListener('resize',fit);if(document.fonts)document.fonts.ready.then(fit);
  if(reduce)return;var vis=true;if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;}).observe(n0);
  setInterval(function(){if(document.hidden||!vis)return;sp[k].classList.remove('on');k=(k+1)%sp.length;sp[k].classList.add('on');fit();},2800);}
(function(){var b=document.getElementById('a11b'),bu=document.getElementById('burg'),pn=document.getElementById('a11p');if(!b||!bu||!pn)return;var mq=matchMedia('(max-width:700px)');
  function m(){if(mq.matches){if(b.parentNode!==bu.parentNode)bu.parentNode.insertBefore(b,bu);b.classList.add('v2inhd');}else{if(b.nextElementSibling!==pn)pn.parentNode.insertBefore(b,pn);b.classList.remove('v2inhd');}}
  m();if(mq.addEventListener)mq.addEventListener('change',m);})();
V2Rot(document.getElementById('flip1'),['САЙТЫ','МАГАЗИНЫ','ПРИЛОЖЕНИЯ','КАТАЛОГИ']);""")

# ---------- 2. убрать «Пока вы спите…» ----------
cut('<section class="fillx" aria-label="Главная мысль">','\n\n<!-- 02 для кого -->')

# ---------- 3. пакеты + настоящие работы ----------
rep('<div class="pkim"><img src="img/pk1.jpg" alt="" loading="lazy"></div>',
    '<div class="pkim v2work"><img src="img/ru/pw1.jpg" alt="" loading="lazy"></div><p class="v2ex">Пример: сайт студии Apps &amp; Soul — тот, что вы сейчас смотрите.</p>')
rep('<div class="pkim"><img src="img/pk2.jpg" alt="" loading="lazy"></div>',
    '<div class="pkim v2work"><img src="img/pw2.jpg" alt="" loading="lazy"></div><p class="v2ex">Пример: магазин деликатесов, около 900 товаров. Устроен как большой супермаркет: отдел, группа, полка.</p>')
rep('<div class="pkim"><img src="img/pk3.jpg" alt="" loading="lazy"></div>',
    '<div class="pkim v2work"><img src="img/pw3.jpg" alt="" loading="lazy"></div><p class="v2ex">Пример: три магазина одного владельца, почти 4 800 товаров прямо из кассы.</p>')
cut('<!-- масштаб -->','<div class="revx"')

# ---------- 8. плашка скидки ----------
rep('<p class="pnote"><b>Первым трём клиентам — скидка 30%</b>',
    '<p class="pnote v2seats"><span class="v2badge"><i></i>Осталось 3 места</span><b>Первым трём клиентам — скидка 30%</b>')

# ---------- 4. «два пути» -> одна строка ----------
cut('<div class="appw" id="app2">','\n  <h3 class="addh">Можно добавить к любому пакету</h3>',
    '<p class="v2app">Нужно приложение? Чем отличаются пути и что выбрать — в статье: <a href="articles/ru/site-or-app.html">Сайт, приложение на экране или приложение в App Store?</a></p>\n')
rep('Это не одно и то же: разница описана в блоке «Приложение для вашего бизнеса».','Это не одно и то же: разница описана в статье «Сайт, приложение на экране или приложение в App Store?».')

# ---------- 5. «Как мы работаем» — одна полоса ----------
rep("if(steps&&!off()){steps.classList.add('plx','done','on');pl=[].slice.call(steps.querySelectorAll('.st'));\n  pl.forEach(function(st,i){st.style.setProperty('--i',i);st.style.setProperty('--c',COL[i%COL.length]);if(i===COL.length-1)st.classList.add('dk');});}",
    "if(steps){steps.classList.add('done','on');}")

# ---------- 6. истории проектов за одну кнопку (на всех экранах) ----------
rep("  .chips.fold button:nth-of-type(n+7){display:none}\n  .chips .allb{background:var(--ink)!important;color:#fff;border-color:var(--ink)!important}\n","")

# ---------- 7. бесплатный разбор — сразу после работ ----------
i=s.index('  <div class="adt" id="rev">'); j=s.index('\n</div></section>',i)
adt=s[i:j]; s=s[:i].rstrip(' \n')+'\n'+s[j:]
rep('<!-- свои инструменты -->','<!-- бесплатный разбор -->\n<section class="sec v2audit"><div class="wrap">\n'+adt+'\n</div></section>\n\n<!-- свои инструменты -->')

# ---------- 9. меню ----------
rep('<nav><a href="#services">Услуги</a><a href="#works">Работы</a><a href="#admin">Панель</a><a href="#ai">AI</a><a href="#try">Попробовать</a><a href="#process">Как работаем</a><a href="#about">Обо мне</a><a href="#faq">Вопросы</a><a href="articles/ru/index.html" class="navart">Статьи</a></nav>',
    '<nav><a href="#services">Услуги</a><a href="#works">Работы</a><a href="#process">Как работаем</a><a href="#about">Обо мне</a><a href="articles/ru/index.html" class="navart">Статьи</a></nav>')
rep('aria-label="Поиск (Ctrl+K)" title="Поиск (Ctrl+K)"','aria-label="Поиск по сайту" title="Поиск по сайту"')
rep('<kbd>Ctrl K</kbd></button>','</button>')
rep('  <div class="cnt" id="cnt"><b>01</b> / 12</div>\n','')
rep("cnt.innerHTML='<b>'+c+'</b> / '+TOT;}","if(cnt)cnt.innerHTML='<b>'+c+'</b> / '+TOT;}")

# ---------- 11. цвета: боковые точки разделов ----------
rep("var SPAL=['#5B3DF5','#FF7A1A','#26C281','#E5484D','#2F80ED','#C7A56A','#D63AF9','#00A3A3','#F5A300','#5B3DF5','#E5484D','#26C281'];",
    "var SPAL=['#16113A','#B8892E','#16113A','#B8892E','#16113A','#B8892E','#16113A','#B8892E','#16113A','#B8892E','#16113A','#B8892E'];")

# ---------- 25.11: ширина блоков на 3440 и скорость ----------
# шрифты: не задерживают показ страницы; почерк Playpen (только «Обо мне») грузится, когда до блока доходит прокрутка
rep('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700&family=Heebo:wght@400;500;700;800;900&family=Playpen+Sans:wght@600;800&family=Playpen+Sans+Hebrew:wght@600;800&display=swap">',
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700&family=Heebo:wght@400;500;700;800;900&display=swap" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700&family=Heebo:wght@400;500;700;800;900&display=swap"></noscript>')
rep("V2Rot(document.getElementById('flip1')",
"""(function(){var ab=document.getElementById('about'),done=false;function ld(){if(done)return;done=true;var l=document.createElement('link');l.rel='stylesheet';l.href='https://fonts.googleapis.com/css2?family=Playpen+Sans:wght@600;800&family=Playpen+Sans+Hebrew:wght@600;800&display=swap';document.head.appendChild(l);}
  if(!ab||!('IntersectionObserver' in window)){ld();return;}new IntersectionObserver(function(es,o){if(es[0].isIntersecting){ld();o.disconnect();}},{rootMargin:'1200px 0px'}).observe(ab);})();
V2Rot(document.getElementById('flip1')""")
# картинки пакетов: маленькая версия для телефона
for n in ['ru/pw1','pw2','pw3']:
    rep('<img src="img/%s.jpg" alt="" loading="lazy">'%n,'<img src="img/%s.jpg" srcset="img/%s_s.jpg 640w, img/%s.jpg 1200w" sizes="(max-width:700px) 82vw, (max-width:1400px) 32vw, 600px" width="1200" height="750" alt="" loading="lazy" decoding="async">'%(n,n,n))
# карточки «Для кого»: на телефоне картинка 104px
rep("""fi.innerHTML='<img src="img/f'+(i+1)+'.jpg" alt="" loading="lazy">';""",
    """fi.innerHTML='<img src="img/f'+(i+1)+'.jpg" srcset="img/f'+(i+1)+'_s.jpg 220w, img/f'+(i+1)+'.jpg 400w" sizes="(max-width:600px) 104px, 400px" width="400" height="400" alt="" loading="lazy" decoding="async">';""")

# ---------- 25.11 (2): повтор заголовков, подвал, доступность, «Азарт» на телефоне ----------
# 2. в блоке помощников свой заголовок вместо второго «Попробуйте сами»
rep('<div class="aichat"><div><h3>Попробуйте сами</h3>','<div class="aichat"><div><h3>Спросите ассистента</h3>')
# 3. подвал: та же спокойная смена слов, что на первом экране
rep('<h2 class="big">Сделаем ваш<br><span class="flip" id="flip2"></span></h2>','<h2 class="big">Сделаем ваш<br><span class="v2rot v2rotd" id="flip2"></span></h2>')
rep("new Flip(document.getElementById('flip2'),['САЙТ','МАГАЗИН','КАТАЛОГ']);","V2Rot(document.getElementById('flip2'),['САЙТ','МАГАЗИН','КАТАЛОГ']);")
# 5. доступность
rep('<div class="doing" aria-label="Делаю сайты, магазины, приложения и каталоги под ключ"><span aria-hidden="true">Делаю</span>',
    '<div class="doing"><span class="vh">Делаю сайты, магазины, приложения и каталоги под ключ</span><span aria-hidden="true">Делаю</span>')
rep('<div class="trytabs" role="tablist"><button type="button" class="on" data-t="build">Конструктор</button><button type="button" data-t="loss">Калькулятор</button><button type="button" data-t="game">Игра</button></div>',
    '<div class="trytabs" role="tablist"><button type="button" role="tab" aria-selected="true" aria-controls="build" class="on" data-t="build">Конструктор</button><button type="button" role="tab" aria-selected="false" aria-controls="loss" data-t="loss">Калькулятор</button><button type="button" role="tab" aria-selected="false" aria-controls="game" data-t="game">Игра</button></div>')
rep("tb.forEach(function(x){x.classList.toggle('on',x===b);});","tb.forEach(function(x){x.classList.toggle('on',x===b);x.setAttribute('aria-selected',x===b?'true':'false');});")
for pid in ['build','loss','game']:
    rep('<section class="sec t0 trypane" id="%s"'%pid,'<section class="sec t0 trypane" role="tabpanel" id="%s"'%pid)
rep("d.setAttribute('aria-label','История проекта: '+w[1]);","")
rep('<img src="img/w_rosa.jpg" alt="" loading="eager">','<img src="img/w_rosa.jpg" alt="Интернет-магазин с витриной как в супермаркете" loading="eager">')

# ---------- новые стили (в самом конце, чтобы перекрывать старые) ----------
CSS=r'''
/* ===== редизайн v2 (24.11) ===== */
:root{--navy:#16113A;--gold:#C9A04A;--gold2:#E5C77A}
/* 1. спокойная смена слов */
.v2rot{display:inline-grid;vertical-align:baseline;color:var(--navy);position:relative;transition:width .7s cubic-bezier(.2,.8,.2,1)}
.v2rot>span{grid-area:1/1;opacity:0;transform:translateY(.32em);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1);justify-self:start;white-space:nowrap;background:linear-gradient(var(--gold),var(--gold)) 0 92%/100% .12em no-repeat;padding-bottom:.06em}
.v2rot>span.on{opacity:1;transform:none}
html:not([lang=he]) .v2rot>span{text-transform:lowercase}
.hero .acts .btn svg{flex:none}
.v2vid{display:inline-flex;align-items:center;gap:8px;margin-top:16px;font-size:14px;font-weight:600;color:var(--mut);text-decoration:underline;text-underline-offset:3px;align-self:flex-start}
.v2vid:hover{color:var(--ink)}
html.hin .hero>.v2vid{animation:hin 1.15s cubic-bezier(.16,1,.3,1) .85s backwards}
.glow{background:conic-gradient(from var(--a,0deg),#E5C77A,#2A2370,#C9A04A,#5A4FB0,#E5C77A);opacity:.32}
/* 3. пакеты с настоящими работами */
.pkg .pkim.v2work{aspect-ratio:16/10;background:var(--navy)}
.pkg .pkim.v2work img{object-fit:cover;object-position:center}
.v2ex{font-size:14px!important;line-height:1.45;margin:-6px 0 12px!important;color:var(--mut)}
.pkg.mid .v2ex{color:rgba(255,255,255,.72)!important}
.pkg.mid{background:linear-gradient(160deg,#241C5C,#16113A);box-shadow:0 30px 60px rgba(22,17,58,.28)}
.pkg.mid .pn,.pkg.mid .psz{color:var(--gold2)}.pkg.mid li::before{color:var(--gold2)}
.pkg .psz{color:var(--navy)}.pkg li::before{background:#F3EEDF;color:#8A6A22}
.pkg.mid .pbtn{background:var(--gold2)}
/* 8. плашка «Осталось 3 места» */
.pnote.v2seats{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;background:var(--navy);color:rgba(255,255,255,.78);border-radius:22px;padding:18px 22px;font-size:15px;margin:22px 0 30px}
.pnote.v2seats b{color:#fff}
.pnote.v2seats .lk{color:var(--gold2)}
.v2badge{display:inline-flex;align-items:center;gap:8px;background:var(--gold2);color:var(--navy);font-family:var(--disp);font-weight:800;font-size:14px;padding:8px 14px;border-radius:999px;white-space:nowrap}
.v2badge i{width:8px;height:8px;border-radius:50%;background:#C0392B;box-shadow:0 0 0 3px rgba(192,57,43,.25);animation:bl 2s infinite}
/* 4. строка про приложение */
.v2app{margin:0 0 clamp(30px,4vw,50px);padding:16px 20px;border-radius:18px;background:#fff;box-shadow:0 0 0 1px var(--line);font-size:16px;color:var(--mut)}
.v2app a{color:var(--navy);font-weight:700;text-decoration:underline;text-decoration-color:var(--gold);text-underline-offset:4px}
/* 5. шаги — одна полоса */
#process .steps{padding-top:30px}
#process .sti{aspect-ratio:4/3;border-radius:16px;margin-bottom:12px}
#process .st b{font-size:17px}
#process .st span{font-size:14px}
#process .steps.on .st::before{background:var(--gold)}
@media (max-width:1100px){#process .steps{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;margin-inline:calc(var(--pad)*-1);padding:6px var(--pad) 14px;scrollbar-width:none}
#process .steps::-webkit-scrollbar{display:none}
#process .st{flex:0 0 min(42%,300px);scroll-snap-align:start}
#process .st::before{display:none}}
@media (max-width:600px){#process .st{flex-basis:62%}}
/* 6. истории за одной кнопкой */
.chips.fold button:not(.allb){display:none}
.chips .allb{background:var(--navy)!important;color:#fff;border-color:var(--navy)!important}
/* 7. блок бесплатного разбора */
.v2audit{padding-top:0!important}
.v2audit .adt{margin-top:0;background:linear-gradient(135deg,#F3E6C4,#E5C77A)}
/* 9. меню: лупа без надписи */
.sbtn{padding:9px;border-radius:50%}
.nav nav{gap:26px}
@media (max-width:1180px){.sbtn{margin-inline-start:auto}}
/* 10. широкий экран 3440 */
@media (min-width:2200px){#works .wrap,#admin .wrap,#tools .wrap{max-width:calc(var(--max) + var(--pad)*2)}}
@media (min-width:2000px){:root{--max:min(2000px,64vw)}body{font-size:18px}.pkgs{gap:26px}}
@media (min-width:2800px){:root{--max:2080px}}
/* 11. приглушённые цвета */
.ai{background:linear-gradient(140deg,#1E1750,#16113A 60%,#2A2266)!important}
.ai .aic{background:rgba(255,255,255,.06);border-color:rgba(229,199,122,.22)}
.gc:nth-child(n){background:var(--navy)}
.gc b{color:var(--gold2)}
.end{background:linear-gradient(90deg,rgba(22,17,58,.96) 0%,rgba(22,17,58,.85) 42%,rgba(22,17,58,.15) 72%),#16113A url(img/foot.jpg) right bottom/cover no-repeat!important}
@media (max-width:900px){.end{background:linear-gradient(180deg,rgba(22,17,58,.92),rgba(22,17,58,.82)),#16113A url(img/foot.jpg) 78% bottom/cover no-repeat!important}}
.end .flip span{background:#2A2266}
.end .btn{background:var(--gold2)}
.side::after{background:linear-gradient(180deg,var(--gold),var(--gold2))!important;box-shadow:none}
.fc:nth-child(n){background:#fff}.fc:nth-child(even){background:#FBF7EE}
.fc .k,.fc:nth-child(n) .k{background:var(--navy);color:var(--gold2)!important}
.bld{background:#F3EEDF}.bchips button.on{background:var(--navy)}
/* 2. вкладки «Попробуйте сами»: подзаголовок вкладки скромный, без второго большого заголовка */
section#try.sec{padding-bottom:0!important}section.trypane.sec{padding-top:44px!important}
.trypane .head{display:block;margin-bottom:22px}
.trypane .head h2.scr{font-size:clamp(22px,2vw,30px)!important;letter-spacing:-.02em;margin:0 0 8px}
.trypane .head p{max-width:760px;margin:0}
/* 3. подвал */
.v2rotd{color:var(--gold2)}
.v2rotd>span{background:linear-gradient(var(--gold2),var(--gold2)) 0 94%/100% .08em no-repeat}
/* 5. контраст */
.msg em{color:#666!important}
.s-wa{background:#0E7A40!important}
/* «Азарт» на телефоне: картинка сразу, без длинной прокрутки */
@media (max-width:700px){.revx{height:auto!important}.revx .rst{position:static!important;height:auto!important;padding:20px 0 10px}
.revx .rfr{clip-path:none!important;--cp:1!important;max-height:none}}
/* 12. телефон: кнопка доступности переезжает в верхнюю полосу (рядом с меню) */
.a11b.v2inhd{position:static;inset:auto;width:38px;height:38px;flex:none;box-shadow:0 4px 12px rgba(31,91,255,.3);transform:none}
.a11b.v2inhd svg{width:19px;height:19px}
@media (max-width:700px){.a11p,[dir=rtl] .a11p{top:74px;bottom:auto;left:auto;right:12px;inset-inline-start:auto;inset-inline-end:auto}
[dir=rtl] .a11p{right:auto;left:12px}}
'''
rep('</style>',CSS+'</style>')
open(OUT,'w',encoding='utf-8').write(s)
print('готово',len(s))
