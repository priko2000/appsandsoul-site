import json,re,urllib.parse,sys
sys.path.insert(0,'/home/claude')
from tr import T
src=open('site/index.html',encoding='utf-8').read()
U=json.load(open('ru_strings.json'))
# --- общие правки исходника (русская версия) ---
LANGCSS='''
.langs{display:flex;gap:4px;background:rgba(22,17,58,.06);border-radius:999px;padding:4px;position:relative}
.langs a{display:flex;align-items:center;gap:7px;padding:4px 11px 4px 4px;border-radius:999px;font-family:var(--disp);font-size:12px;font-weight:800;color:var(--mut);line-height:1;transition:background .3s,color .3s,box-shadow .3s}
[dir=rtl] .langs a{padding:4px 4px 4px 11px}
.langs .fl{width:24px;height:24px;border-radius:50%;overflow:hidden;flex:none;position:relative;box-shadow:0 0 0 1.5px rgba(22,17,58,.12),0 2px 6px rgba(22,17,58,.15);transition:transform .45s cubic-bezier(.2,1.6,.4,1),filter .3s;filter:saturate(.55)}
.langs .fl svg{display:block;width:100%;height:100%}
.langs .fl::after{content:"";position:absolute;inset:0;border-radius:50%;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.75) 48%,transparent 62%);transform:translateX(-120%);background-repeat:no-repeat}
.langs a:hover .fl{transform:rotate(-14deg) scale(1.12);filter:none}
.langs a:hover .fl::after{transform:translateX(120%);transition:transform .7s ease}
.langs a:hover{color:var(--ink)}
.langs a.on{background:#fff;color:var(--ink);box-shadow:0 4px 14px rgba(22,17,58,.14)}
.langs a.on .fl{filter:none;animation:flwave 3.2s ease-in-out infinite}
@keyframes flwave{0%,70%,100%{transform:rotate(0)}76%{transform:rotate(-12deg)}84%{transform:rotate(9deg)}92%{transform:rotate(-4deg)}}
@media (max-width:560px){.cnt{display:none}.langs{margin-inline-start:auto;gap:2px;padding:3px}.langs a,[dir=rtl] .langs a{padding:3px}.langs .cd{display:none}.langs .fl{width:26px;height:26px}.nav .in{gap:8px}.cta{padding:9px 12px;font-size:13px}.logo{font-size:15px;gap:6px}}
[dir=rtl] .lbin li::before,[dir=rtl] .sc3 li::before{left:auto;right:0}
[dir=rtl] .st::before{left:auto;right:0}
[dir=rtl] .steps::after{left:auto;right:0;transform-origin:100% 50%}
[dir=rtl] .prog{transform-origin:100% 50%}
[dir=rtl] .x{right:auto;left:16px}
[dir=rtl] .chint{left:auto;right:20px}
[dir=rtl] .mini{right:auto;left:18px}
[dir=rtl] .btn svg,[dir=rtl] .chint svg{transform:scaleX(-1)}
[dir=rtl] .ai .g3{right:auto;left:-200px}
html[lang=he]{--disp:'Heebo',system-ui,sans-serif;--body:'Heebo',system-ui,sans-serif}
html[lang=he] h1,html[lang=he] h2,html[lang=he] h3,html[lang=he] .big3,html[lang=he] .stats b,html[lang=he] .grp-l{letter-spacing:0;font-weight:900}
html[lang=he] .big{font-size:clamp(40px,6.6vw,108px);line-height:1.05}
html[lang=he] body{font-size:18px}
'''
src=src.replace("/* курсор */",LANGCSS+"\n/* курсор */",1)
src=src.replace("family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700&display=swap","family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700&family=Heebo:wght@400;500;700;800;900&display=swap")
src=src.replace('<div class="cnt" id="cnt">','<div class="langs">LANGLINKS</div>\n  <div class="cnt" id="cnt">',1)
src=src.replace('Пример нового дизайна. Иврит и английский будут добавлены.','Пример нового дизайна. Три языка: русский, иврит, английский.')
U=[ ('Пример нового дизайна. Три языка: русский, иврит, английский.' if u=='Пример нового дизайна. Иврит и английский будут добавлены.' else u) for u in U]
FILES={'ru':'ru.html','he':'index.html','en':'en.html'}
FLAG={
'ru':'<svg viewBox="0 0 60 60"><rect width="60" height="20" fill="#fff"/><rect y="20" width="60" height="20" fill="#1C57A5"/><rect y="40" width="60" height="20" fill="#D52B1E"/></svg>',
'he':'<svg viewBox="0 0 60 60"><rect width="60" height="60" fill="#fff"/><rect y="9" width="60" height="7" fill="#0038B8"/><rect y="44" width="60" height="7" fill="#0038B8"/><g fill="none" stroke="#0038B8" stroke-width="2.6" stroke-linejoin="round"><path d="M30 20.5 39 36H21z"/><path d="M30 39.5 21 24h18z"/></g></svg>',
'en':'<svg viewBox="0 0 60 60"><rect width="60" height="60" fill="#012169"/><path d="M0 0 60 60M60 0 0 60" stroke="#fff" stroke-width="12"/><path d="M0 0 60 60M60 0 0 60" stroke="#C8102E" stroke-width="4"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="16"/><path d="M30 0v60M0 30h60" stroke="#C8102E" stroke-width="9"/></svg>'}
NAME={'ru':'Русский','he':'עברית','en':'English'}
CODE={'ru':'RU','he':'עב','en':'EN'}
def links(cur):
    return ''.join('<a href="%s" lang="%s" title="%s"%s><span class="fl">%s</span><span class="cd">%s</span></a>'%(FILES[l],l,NAME[l],' class="on"' if l==cur else '',FLAG[l],CODE[l]) for l in ['ru','he','en'])
ru=src.replace('LANGLINKS',links('ru')).replace('<link rel="canonical" href="https://priko2000.github.io/appsandsoul-site/">','<link rel="canonical" href="https://priko2000.github.io/appsandsoul-site/ru.html">')
open('site/ru.html','w',encoding='utf-8').write(ru)
AI_RU='Здравствуйте! Интересует AI-ассистент'
def build(lang):
    s=src
    k=0 if lang=='he' else 1
    pairs=[]
    for i,u in enumerate(U):
        if i in (0,261,346): continue
        if i not in T: print('нет перевода',i,u);continue
        pairs.append((u,T[i][k]))
    pairs.sort(key=lambda p:-len(p[0]))
    for a,b in pairs: s=s.replace(a,b)
    s=s.replace('<em class="more">История проекта</em>','<em class="more">%s</em>'%T[484][k])
    s=s.replace("var AB='АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ'","var AB='%s'"%('אבגדהוזחטיכלמנסעפצקרשת' if lang=='he' else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    s=s.replace("+'»')","+'%s')"%('״' if lang=='he' else '”'))
    s=s.replace('<html lang="ru">','<html lang="he" dir="rtl">' if lang=='he' else '<html lang="en">')
    enc=urllib.parse.quote(AI_RU)
    s=s.replace(enc,urllib.parse.quote('שלום! מתעניין/ת בעוזר AI' if lang=='he' else 'Hello! I’m interested in an AI assistant'))
    for a,b in [('<b>4 800</b>','<b>4,800</b>'),('<b>109 000+</b>','<b>109,000+</b>'),('1&nbsp;000<small>','1,000<small>'),('5&nbsp;000<small>','5,000<small>'),('<bdi>3&nbsp;000+</bdi>','<bdi>3,000+</bdi>'),('1&nbsp;000</bdi>','1,000</bdi>')]: s=s.replace(a,b)
    # картинки
    imgs=['w_rosa','w_azart','w_azart2','w_assist','w_price','w_tape']
    for n in imgs:
        folder='he' if (lang=='he' or n!='w_price') else 'en'
        s=s.replace('img/%s.jpg'%n,'img/%s/%s.jpg'%(folder,n))
    s=s.replace('img/og_ru.jpg','img/og_%s.jpg'%lang)
    if lang!='he': s=s.replace('<link rel="canonical" href="%s">'%'https://priko2000.github.io/appsandsoul-site/','<link rel="canonical" href="https://priko2000.github.io/appsandsoul-site/%s.html">'%lang)
    s=s.replace('LANGLINKS',links(lang))
    left=re.findall('[А-Яа-яЁё][^<>\'"\\n]{0,40}',re.sub(r'/\*.*?\*/','',s,flags=re.S))
    print(lang,'осталось кириллицы:',len(left),left[:12])
    open('site/'+FILES[lang],'w',encoding='utf-8').write(s)
build('he');build('en')
