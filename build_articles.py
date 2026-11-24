import os, json, sys
sys.path.insert(0, '/home/claude')
from articles_src import A
for _m in ['art_start','art_shop','art_tech_law','art_promo']:
    A.update(__import__(_m).A)

BASE = 'https://priko2000.github.io/appsandsoul-site/'
OUT = '/home/claude/site/articles'
SECTIONS = [
 ('start', {'ru':'С чего начать','he':'איך מתחילים','en':'Getting started'}, ['seven-questions','prepare-materials','domain-hosting','choose-developer','stages-contract','own-site-or-builder']),
 ('shop', {'ru':'Магазин','he':'חנות אונליין','en':'Online store'}, ['shop-checklist','whatsapp-and-site','big-catalog','delivery','online-payment','promotions']),
 ('tech', {'ru':'Приложения и технологии','he':'אפליקציות וטכנולוגיה','en':'Apps and technology'}, ['site-or-app','notifications','ai-assistant','admin-panel']),
 ('law', {'ru':'Закон и безопасность','he':'חוק ואבטחה','en':'Law and security'}, ['accessibility-law','privacy-13','ownership']),
 ('promo', {'ru':'Продвижение','he':'קידום','en':'Getting found'}, ['google-start','no-visitors','reviews']),
 ('after', {'ru':'После запуска','he':'אחרי ההשקה','en':'After launch'}, ['support']),
]
ORDER = [a for _,_,l in SECTIONS for a in l]
SEC_OF = {a:(k,n) for k,n,l in SECTIONS for a in l}
SCOL = {'start':'#5B3DF5','shop':'#26C281','tech':'#FF7A1A','law':'#E5484D','promo':'#2F80ED','after':'#C7A56A'}
import re as _re
def rtime(lang, slug):
    d=A[slug][lang]; w=len(_re.sub('<[^>]+>',' ',d['lead']+' '+d['body']).split())
    m=max(2,round(w/150)); return {'ru':'%d мин чтения','he':'%d דקות קריאה','en':'%d min read'}[lang]%m
HOME = {'he': '../../', 'ru': '../../ru.html', 'en': '../../en.html'}
UI = {
 'ru': dict(home='Главная', arts='Статьи', more='Другие статьи', cta_t='Обсудим ваш проект?', cta_p='Напишите в WhatsApp: отвечаю в течение 2 часов в рабочее время. Или закажите бесплатный разбор вашего сайта.', wa='Написать в WhatsApp', rev='Бесплатный разбор сайта', wamsg='Здравствуйте, Давид! Я прочитал статью на сайте и хочу обсудить проект.', foot='© Apps & Soul · студия Давида Мушаилова', by='Мушаилов Давид, основатель Apps & Soul', back='← Все статьи', read='Читать'),
 'he': dict(home='ראשי', arts='מאמרים', more='מאמרים נוספים', cta_t='נדבר על הפרויקט שלכם?', cta_p='כתבו בוואטסאפ: אני עונה תוך שעתיים בשעות העבודה. או הזמינו בדיקה חינם לאתר שלכם.', wa='לכתוב בוואטסאפ', rev='בדיקה חינם לאתר', wamsg='שלום דוד! קראתי מאמר באתר ורוצה לדבר על פרויקט.', foot='© Apps & Soul · הסטודיו של דוד מושאילוב', by='מושאילוב דוד, מייסד Apps & Soul', back='כל המאמרים →', read='לקריאה'),
 'en': dict(home='Home', arts='Articles', more='More articles', cta_t='Shall we talk about your project?', cta_p='Message me on WhatsApp: I reply within 2 hours during working hours. Or ask for a free review of your website.', wa='Message on WhatsApp', rev='Free website review', wamsg='Hello David! I read an article on your site and would like to discuss a project.', foot='© Apps & Soul · David Mushailov’s studio', by='David Mushailov, founder of Apps & Soul', back='← All articles', read='Read'),
}
NAME = {'ru': 'Русский', 'he': 'עברית', 'en': 'English'}
CODE = {'ru': 'RU', 'he': 'עב', 'en': 'EN'}
from urllib.parse import quote

CSS = '''
:root{--bg:#F6F3EC;--ink:#111;--mut:#6A655C;--line:rgba(17,17,17,.12);--y:#FFC700;--vi:#5B3DF5;--mi:#26C281;--disp:'Unbounded',system-ui,sans-serif;--body:'Manrope',system-ui,sans-serif}
html[lang=he]{--disp:'Heebo',system-ui,sans-serif;--body:'Heebo',system-ui,sans-serif}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:18px;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:inherit}
.top{position:sticky;top:0;z-index:5;background:rgba(246,243,236,.9);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .in{max-width:1100px;margin:0 auto;padding:12px clamp(16px,4vw,40px);display:flex;align-items:center;gap:14px}
.logo{display:flex;align-items:center;gap:8px;text-decoration:none;font-family:'Unbounded',system-ui,sans-serif;font-weight:800;font-size:17px;direction:ltr}
.logo em{font-style:normal;color:#C7A56A}
.langs{margin-inline-start:auto;display:flex;gap:4px;background:rgba(22,17,58,.06);border-radius:999px;padding:4px}
.langs a{padding:6px 12px;border-radius:999px;font-weight:800;font-size:13px;text-decoration:none;color:var(--mut)}
.langs a.on{background:#fff;color:var(--ink);box-shadow:0 4px 14px rgba(22,17,58,.14)}
.wa1{background:var(--ink);color:#fff;text-decoration:none;border-radius:999px;padding:9px 16px;font-weight:800;font-size:14px;white-space:nowrap}
main{max-width:760px;margin:0 auto;padding:clamp(24px,5vw,56px) clamp(18px,4vw,40px) 40px}
.crumbs{font-size:14px;color:var(--mut);margin-bottom:18px}
.crumbs a{text-decoration:none;color:var(--vi);font-weight:700}
h1{font-family:var(--disp);font-size:clamp(30px,4.4vw,50px);line-height:1.12;margin:0 0 18px;letter-spacing:-.01em}
html[lang=he] h1,html[lang=he] h2{font-weight:900;letter-spacing:0}
.lead{font-size:clamp(19px,1.7vw,22px);line-height:1.6;color:#2b2925;margin:0 0 14px}
.by{font-size:14px;color:var(--mut);padding-bottom:22px;border-bottom:1px solid var(--line);margin-bottom:10px}
h2{font-family:var(--disp);font-size:clamp(22px,2.3vw,28px);line-height:1.25;margin:38px 0 10px}
p{margin:0 0 16px}
ul,ol{margin:0 0 18px;padding-inline-start:24px}
li{margin:0 0 10px}
li::marker{color:var(--vi);font-weight:800}
ol.chk{list-style:none;padding:0;counter-reset:c;margin-top:26px}
ol.chk li{counter-increment:c;position:relative;background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px 18px 16px 66px;margin-bottom:12px}
[dir=rtl] ol.chk li{padding:16px 66px 16px 18px}
ol.chk li::before{content:counter(c);position:absolute;inset-inline-start:16px;top:15px;width:36px;height:36px;border-radius:50%;background:var(--y);display:grid;place-items:center;font-family:'Unbounded',system-ui,sans-serif;font-weight:800;font-size:14px}
.cta{margin:46px 0 10px;background:var(--y);border-radius:26px;padding:clamp(22px,4vw,38px)}
.cta h2{margin:0 0 10px}
.cta .b{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.cta a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:800;border-radius:14px;padding:14px 20px}
.cta .p1{background:var(--ink);color:#fff}.cta .p2{background:#fff;color:var(--ink)}
.more{max-width:1100px;margin:0 auto;padding:10px clamp(18px,4vw,40px) 60px}
.more h3{font-family:var(--disp);font-size:22px;margin:0 0 16px}
.ag{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.ac{display:flex;flex-direction:column;gap:8px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px;text-decoration:none;position:relative;overflow:hidden;transition:transform .25s,box-shadow .25s}
.ac::before{content:"";position:absolute;inset:0 0 auto 0;height:5px;background:var(--vi)}
.ac.c2::before{background:var(--mi)}.ac.c3::before{background:var(--y)}
.ac:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(17,17,17,.12)}
.ac b{font-family:var(--disp);font-size:18px;line-height:1.25}
.ac span{color:var(--mut);font-size:15px;line-height:1.5}
.ac.on{outline:2px solid var(--vi)}
footer{border-top:1px solid var(--line);text-align:center;font-size:14px;color:var(--mut);padding:24px}
@media (max-width:820px){.ag{grid-template-columns:1fr}}
@media (max-width:560px){.wa1{display:none}.logo{font-size:15px}body{font-size:17px}}
'''


CSS += '''
.ac::before{background:var(--sc,var(--vi))!important}
.ac small{font-size:12px;font-weight:800;color:var(--sc,var(--vi));text-transform:uppercase;letter-spacing:.04em}
html[lang=he] .ac small{text-transform:none;letter-spacing:0}
.ac em{font-style:normal;font-size:13px;color:var(--mut);margin-top:auto}
.kick{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:14px;font-size:14px}
.kick a{background:var(--sc);color:#fff;text-decoration:none;border-radius:999px;padding:5px 12px;font-weight:800}
.kick span{color:var(--mut)}
.note{font-size:14px;color:var(--mut);border-inline-start:3px solid var(--line);padding-inline-start:12px;margin-top:24px}
.allb{display:inline-flex;margin-top:18px;background:var(--ink);color:#fff;text-decoration:none;border-radius:14px;padding:13px 20px;font-weight:800}
.hub{max-width:1180px;margin:0 auto;padding:clamp(28px,5vw,64px) clamp(18px,4vw,40px) 30px}
.hub h1{font-size:clamp(34px,5vw,64px);max-width:16ch}
.hub .lead{max-width:60ch}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:26px 0 10px;position:sticky;top:58px;z-index:3;background:rgba(246,243,236,.92);backdrop-filter:blur(8px);padding:10px 0}
.chips a{text-decoration:none;border:1.5px solid var(--sc);color:var(--ink);border-radius:999px;padding:8px 14px;font-weight:800;font-size:14px;display:flex;gap:8px;align-items:center}
.chips a i{font-style:normal;background:var(--sc);color:#fff;border-radius:999px;font-size:12px;padding:1px 8px}
.chips a:hover{background:var(--sc);color:#fff}
.hsec{padding-top:34px;scroll-margin-top:120px}
.hsec h2{display:flex;align-items:center;gap:12px;margin:0 0 16px}
.hsec h2::before{content:"";width:14px;height:14px;border-radius:4px;background:var(--sc);flex:none}
.hsec .ag{grid-template-columns:repeat(3,minmax(0,1fr))}
@media (min-width:1700px){.hub{max-width:1560px}.hub .ag{grid-template-columns:repeat(4,minmax(0,1fr))}.more{max-width:1300px}}
@media (max-width:820px){.hsec .ag{grid-template-columns:1fr}.chips{position:static;margin-top:18px}}
'''
UI['ru'].update(hub_t='Статьи для владельцев бизнеса', hub_l='Коротко и честно о том, что стоит знать до заказа сайта, магазина или приложения, и о том, что делать после запуска. Всё по темам.', all='Все статьи', same='Ещё в разделе', n='статьи')
UI['he'].update(hub_t='מאמרים לבעלי עסקים', hub_l='בקצרה ובכנות: מה כדאי לדעת לפני שמזמינים אתר, חנות או אפליקציה, ומה עושים אחרי ההשקה. הכול לפי נושאים.', all='כל המאמרים', same='עוד בנושא', n='מאמרים')
UI['en'].update(hub_t='Articles for business owners', hub_l='Short and honest: what is worth knowing before you order a website, store or app, and what to do after launch. Everything by topic.', all='All articles', same='More in this topic', n='articles')


FLAG = {
'ru':'<svg viewBox="0 0 60 60"><rect width="60" height="20" fill="#fff"/><rect y="20" width="60" height="20" fill="#1C57A5"/><rect y="40" width="60" height="20" fill="#D52B1E"/></svg>',
'he':'<svg viewBox="0 0 60 60"><rect width="60" height="60" fill="#fff"/><rect y="9" width="60" height="7" fill="#0038B8"/><rect y="44" width="60" height="7" fill="#0038B8"/><g fill="none" stroke="#0038B8" stroke-width="2.6" stroke-linejoin="round"><path d="M30 20.5 39 36H21z"/><path d="M30 39.5 21 24h18z"/></g></svg>',
'en':'<svg viewBox="0 0 60 60"><rect width="60" height="60" fill="#012169"/><path d="M0 0 60 60M60 0 0 60" stroke="#fff" stroke-width="12"/><path d="M0 0 60 60M60 0 0 60" stroke="#C8102E" stroke-width="4"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="16"/><path d="M30 0v60M0 30h60" stroke="#C8102E" stroke-width="9"/></svg>'}
LANGCSS2 = """.langs{display:flex;gap:4px;background:rgba(22,17,58,.06);border-radius:999px;padding:4px;position:relative}
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
.top .langs{margin-inline-start:auto}
.langs a{text-decoration:none}
@media (max-width:560px){.langs{gap:2px;padding:3px}.langs a,[dir=rtl] .langs a{padding:3px}.langs .cd{display:none}.langs .fl{width:26px;height:26px}}
"""
ICO = {
 'start':'<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
 'shop':'<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
 'tech':'<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
 'law':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
 'promo':'<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
 'after':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.93 4.93 4.24 4.24M14.83 9.17l4.24-4.24M14.83 14.83l4.24 4.24M9.17 14.83l-4.24 4.24"/>',
 'seven-questions':'<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
 'prepare-materials':'<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
 'domain-hosting':'<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 'choose-developer':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',
 'stages-contract':'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
 'own-site-or-builder':'<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/>',
 'shop-checklist':'<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
 'whatsapp-and-site':'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 'big-catalog':'<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M8 7v10M12 7v10M16 7v10"/>',
 'delivery':'<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
 'online-payment':'<rect width="20" height="14" x="2" y="5" rx="2"/><path d="M2 10h20"/>',
 'promotions':'<path d="M19 5 5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'site-or-app':'<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
 'notifications':'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
 'ai-assistant':'<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/><path d="M19 3v4M17 5h4"/>',
 'admin-panel':'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
 'accessibility-law':'<circle cx="12" cy="4.5" r="1.8"/><path d="M5 8.5l7 1.5 7-1.5M12 10v5m0 0l-3.5 6M12 15l3.5 6"/>',
 'privacy-13':'<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'ownership':'<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
 'google-start':'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 'no-visitors':'<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
 'reviews':'<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
 'support':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.93 4.93 4.24 4.24M14.83 9.17l4.24-4.24M14.83 14.83l4.24 4.24M9.17 14.83l-4.24 4.24"/>',
}
def ico(k, sz=24):
    return '<svg viewBox="0 0 24 24" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (sz, sz, ICO[k])
def cnt(lang, n):
    if lang == 'ru':
        w = 'статья' if n % 10 == 1 and n % 100 != 11 else ('статьи' if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else 'статей')
        return '%d %s' % (n, w)
    if lang == 'he':
        return 'מאמר אחד' if n == 1 else '%d מאמרים' % n
    return '1 article' if n == 1 else '%d articles' % n
SDESC = {
 'start':{'ru':'Что решить и подготовить до заказа: вопросы, материалы, договор, выбор разработчика.','he':'מה להחליט ולהכין לפני ההזמנה: שאלות, חומרים, חוזה, בחירת מפתח.','en':'What to decide and prepare before ordering: questions, materials, contract, choosing a developer.'},
 'shop':{'ru':'Как устроить продажи онлайн: каталог, заказы, доставка, оплата и акции.','he':'איך לבנות מכירות אונליין: קטלוג, הזמנות, משלוחים, תשלום ומבצעים.','en':'How to set up online sales: catalogue, orders, delivery, payment and promotions.'},
 'tech':{'ru':'Сайт, приложение, уведомления, AI и панель управления: что чем отличается.','he':'אתר, אפליקציה, התראות, AI ופאנל ניהול: מה ההבדל ביניהם.','en':'Website, app, notifications, AI and a management panel: how they differ.'},
 'law':{'ru':'Доступность, приватность и владение сайтом: что важно знать по закону.','he':'נגישות, פרטיות ובעלות על האתר: מה חשוב לדעת לפי החוק.','en':'Accessibility, privacy and owning your site: what matters legally.'},
 'promo':{'ru':'Как вас находят: Google, посетители и отзывы.','he':'איך מוצאים אתכם: גוגל, גולשים וביקורות.','en':'How people find you: Google, visitors and reviews.'},
 'after':{'ru':'Что происходит с сайтом после запуска и как он растёт.','he':'מה קורה עם האתר אחרי ההשקה ואיך הוא גדל.','en':'What happens to your site after launch and how it grows.'},
}
CSS += LANGCSS2 + """
.ac{background:linear-gradient(180deg,color-mix(in srgb,var(--sc) 7%,#fff) 0,#fff 120px)!important;border-color:color-mix(in srgb,var(--sc) 22%,transparent)!important;padding:20px 22px 18px!important}
.ac::before{height:4px!important}
.ai{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.ai i{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:color-mix(in srgb,var(--sc) 14%,#fff);color:var(--sc);transition:transform .35s cubic-bezier(.2,1.6,.4,1),background .25s,color .25s}
.ac:hover .ai i{transform:rotate(-8deg) scale(1.08);background:var(--sc);color:#fff}
.ai u{text-decoration:none;font-family:'Unbounded',system-ui,sans-serif;font-weight:800;font-size:13px;color:color-mix(in srgb,var(--sc) 70%,#111)}
.ac em{display:flex;justify-content:space-between;align-items:center;gap:8px}
.ac em b{font-family:inherit;font-size:16px;color:var(--sc);transition:transform .25s}
[dir=rtl] .ac em b{transform:scaleX(-1)}
.ac:hover em b{transform:translateX(4px)}
[dir=rtl] .ac:hover em b{transform:scaleX(-1) translateX(4px)}
.hero{position:relative;border-radius:32px;padding:clamp(26px,4vw,56px);background:#fff;border:1px solid var(--line);overflow:hidden;margin-bottom:8px}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 92% 12%,#5B3DF526,transparent 34%),radial-gradient(circle at 70% 95%,#26C28126,transparent 32%),radial-gradient(circle at 8% 90%,#FF7A1A20,transparent 30%),radial-gradient(circle at 30% 0%,#2F80ED1c,transparent 30%);pointer-events:none}
[dir=rtl] .hero::before{transform:scaleX(-1)}
.hero>*{position:relative}
.hero h1{margin-top:6px}
.tiles{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.tiles a{width:56px;height:56px;border-radius:16px;display:grid;place-items:center;background:var(--sc);color:#fff;box-shadow:0 8px 20px color-mix(in srgb,var(--sc) 35%,transparent);transition:transform .3s cubic-bezier(.2,1.6,.4,1)}
.tiles a:nth-child(odd){transform:rotate(-6deg)}.tiles a:nth-child(even){transform:rotate(5deg)}
.tiles a:hover{transform:rotate(0) translateY(-4px) scale(1.06)}
.chips a svg{color:var(--sc)}
.chips a:hover svg{color:#fff}
.shead{display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center;background:color-mix(in srgb,var(--sc) 8%,#fff);border:1px solid color-mix(in srgb,var(--sc) 20%,transparent);border-radius:24px;padding:18px 22px;margin-bottom:16px}
.shead>i{width:60px;height:60px;border-radius:18px;background:var(--sc);color:#fff;display:grid;place-items:center;box-shadow:0 10px 24px color-mix(in srgb,var(--sc) 35%,transparent)}
.hsec .shead h2{margin:0;font-size:clamp(22px,2vw,30px);display:block}
.hsec .shead h2::before{display:none}
.shead p{margin:4px 0 0;color:var(--mut);font-size:16px;line-height:1.5}
.shead b{font-family:'Unbounded',system-ui,sans-serif;font-size:13px;background:#fff;color:var(--sc);border-radius:999px;padding:6px 12px;white-space:nowrap}
html[lang=he] .shead b{font-family:'Heebo',system-ui,sans-serif;font-size:15px}
.hsec{padding-top:40px}
.ahead{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.ahead>i{width:58px;height:58px;border-radius:18px;background:var(--sc);color:#fff;display:grid;place-items:center;box-shadow:0 10px 24px color-mix(in srgb,var(--sc) 35%,transparent);flex:none}
.ahead .kick{margin:0}
.kick a{display:inline-flex;align-items:center;gap:6px}
main article h2{position:relative;padding-inline-start:16px}
main article h2::before{content:"";position:absolute;inset-inline-start:0;top:.25em;bottom:.25em;width:5px;border-radius:3px;background:var(--sc)}
main article li::marker{color:var(--sc)}
main .lead{border-inline-start:4px solid color-mix(in srgb,var(--sc) 40%,transparent);padding-inline-start:16px}
.cta{background:linear-gradient(135deg,var(--y),#FFDD55)}
@media (max-width:700px){.shead{grid-template-columns:auto 1fr}.shead b{grid-column:2;justify-self:start}.shead>i{width:48px;height:48px;border-radius:14px}}
"""
LOGO = '<img src="../../img/mark.svg" width="28" height="28" alt="">'

def card(lang, slug, cur=None):
    d = A[slug][lang]; k, n = SEC_OF[slug]
    lead = d['lead'].split('. ')[0].rstrip('.') + '.'
    num = '%02d' % (ORDER.index(slug) + 1)
    return '<a class="ac%s" style="--sc:%s" href="%s.html"><span class="ai"><i>%s</i><u>%s</u></span><small>%s</small><b>%s</b><span>%s</span><em>%s<b>→</b></em></a>' % (' on' if slug == cur else '', SCOL[k], slug, ico(slug, 22), num, n[lang], d['title'], lead, rtime(lang, slug))

def shell(lang, title, desc, url, alts, langs_html, body, ogtype='article', ld=None):
    u = UI[lang]; rtl = ' dir="rtl"' if lang == 'he' else ''
    fonts = 'family=Heebo:wght@400;500;700;800;900&family=Unbounded:wght@800' if lang == 'he' else 'family=Unbounded:wght@500;700;800&family=Manrope:wght@400;500;600;700;800'
    wa = 'https://wa.me/972587800228?text=' + quote(u['wamsg'])
    ldtag = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False) if ld else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="../../img/mark.svg" type="image/svg+xml">
<meta name="robots" content="noindex, nofollow"><!-- СНЯТЬ ПЕРЕД ЗАПУСКОМ на appsandsoul.com -->
<title>{title} — Apps &amp; Soul</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">{alts}
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="Apps &amp; Soul"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{BASE}img/og_{lang}.jpg"><meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>{CSS}</style>
{ldtag}
</head>
<body>
<header class="top"><div class="in"><a class="logo" href="{HOME[lang]}">{LOGO}Apps <em>&amp;</em> Soul</a><nav class="langs" aria-label="Language">{langs_html}</nav><a class="wa1" href="{wa}" target="_blank" rel="noopener">{u['wa']}</a></div></header>
{body}
<footer>{u['foot']}</footer>
</body>
</html>
'''

def alts_for(fname):
    a = ''.join('<link rel="alternate" hreflang="%s" href="%sarticles/%s/%s">' % (l, BASE, l, fname) for l in ['he', 'ru', 'en'])
    return a + '<link rel="alternate" hreflang="x-default" href="%sarticles/he/%s">' % (BASE, fname)

def langs_for(lang, fname):
    return ''.join('<a href="../%s/%s" lang="%s" title="%s"%s><span class="fl">%s</span><span class="cd">%s</span></a>' % (l, fname or 'index.html', l, NAME[l], ' class="on"' if l == lang else '', FLAG[l], CODE[l]) for l in ['ru', 'he', 'en'])

def page(lang, slug):
    d = A[slug][lang]; u = UI[lang]; k, n = SEC_OF[slug]
    url = BASE + 'articles/%s/%s.html' % (lang, slug)
    wa = 'https://wa.me/972587800228?text=' + quote(u['wamsg'])
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": d['title'], "description": d['lead'], "inLanguage": lang,
          "articleSection": n[lang], "author": {"@type": "Person", "name": "David Mushailov"}, "publisher": {"@type": "Organization", "name": "Apps & Soul"},
          "datePublished": "2026-11-24", "dateModified": "2026-11-24", "mainEntityOfPage": url, "image": BASE + 'img/og_%s.jpg' % lang}
    sec = [a for kk, _, l in SECTIONS if kk == k for a in l if a != slug]
    others = [a for a in ORDER if a not in sec and a != slug]
    more = (sec + others)[:3]
    body = f'''<main style="--sc:{SCOL[k]}">
<div class="crumbs"><a href="{HOME[lang]}">{u['home']}</a> › <a href="index.html">{u['arts']}</a> › <a href="index.html#{k}">{n[lang]}</a></div>
<article>
<div class="ahead"><i>{ico(slug, 28)}</i><div class="kick"><a href="index.html#{k}">{ico(k, 15)}{n[lang]}</a><span>{rtime(lang, slug)}</span></div></div>
<h1>{d['title']}</h1>
<p class="lead">{d['lead']}</p>
<div class="by">{u['by']}</div>
{d['body']}
</article>
<div class="cta"><h2>{u['cta_t']}</h2><p>{u['cta_p']}</p><div class="b"><a class="p1" href="{wa}" target="_blank" rel="noopener">{u['wa']}</a><a class="p2" href="{HOME[lang]}#rev">{u['rev']}</a></div></div>
</main>
<section class="more"><h3>{u['same'] if sec else u['more']}</h3><div class="ag">{''.join(card(lang, a) for a in more)}</div><a class="allb" href="index.html">{u['all']} · {len(ORDER)}</a></section>'''
    return shell(lang, d['title'], d['lead'], url, alts_for(slug + '.html'), langs_for(lang, slug + '.html'), body, 'article', ld)

def hub(lang):
    u = UI[lang]; url = BASE + 'articles/%s/' % lang
    chips = ''.join('<a style="--sc:%s" href="#%s">%s%s <i>%d</i></a>' % (SCOL[k], k, ico(k, 16), n[lang], len(l)) for k, n, l in SECTIONS)
    tiles = ''.join('<a style="--sc:%s" href="#%s" title="%s">%s</a>' % (SCOL[k], k, n[lang], ico(k, 26)) for k, n, l in SECTIONS)
    secs = ''.join('<section class="hsec" id="%s" style="--sc:%s"><div class="shead"><i>%s</i><div><h2>%s</h2><p>%s</p></div><b>%s</b></div><div class="ag">%s</div></section>' % (k, SCOL[k], ico(k, 30), n[lang], SDESC[k][lang], cnt(lang, len(l)), ''.join(card(lang, a) for a in l)) for k, n, l in SECTIONS)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": u['hub_t'], "inLanguage": lang, "url": url,
          "hasPart": [{"@type": "Article", "headline": A[a][lang]['title'], "url": BASE + 'articles/%s/%s.html' % (lang, a)} for a in ORDER]}
    body = f'''<div class="hub">
<div class="crumbs"><a href="{HOME[lang]}">{u['home']}</a> › {u['arts']}</div>
<div class="hero hasimg"><div class="htxt"><h1>{u['hub_t']}</h1>
<p class="lead">{u['hub_l']} {len(ORDER)} {u['n']}.</p>
<div class="tiles">{tiles}</div></div>
<nav class="chips">{chips}</nav>
{secs}
</div>'''
    return shell(lang, u['hub_t'], u['hub_l'], url, alts_for(''), langs_for(lang, ''), body, 'website', ld)


from art_live import LIVE, PICK, TIPS, LIVECSS
def cov(k, cls):
    f = '/home/claude/site/img/art/%s.jpg' % k
    pos = {'promo': '50% 16%', 'after': '50% 48%'}.get(k)
    st = ' style="object-position:%s"' % pos if pos else ''
    return '<img class="%s" src="../../img/art/%s.jpg" alt="" loading="lazy"%s>' % (cls, k, st) if os.path.exists(f) else ''
CSS += LIVECSS
WASVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.2-1.2-.2-.2-.5-.3z"/></svg>'
SRCH = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
BULB = '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2z"/></svg>'

_card_old = card
def card(lang, slug, cur=None):
    h = _card_old(lang, slug, cur)
    plain = _re.sub('<[^>]+>', ' ', A[slug][lang]['title'] + ' ' + A[slug][lang]['lead'] + ' ' + A[slug][lang]['body'] + ' ' + SEC_OF[slug][1][lang]).lower()
    plain = ' '.join(plain.split()).replace('"', '')
    h = h.replace('<a class="ac', '<a data-s="%s" data-k="%s" class="ac' % (slug, plain), 1)
    return h.replace('<em>', '<em><span class="rdl">%s ✓</span>' % LIVE[lang]['rdl'], 1)

def total_min(lang):
    return sum(int(_re.match(r'\d+', rtime(lang, a)).group()) for a in ORDER)

def hub(lang):
    u = UI[lang]; L = LIVE[lang]; url = BASE + 'articles/%s/' % lang
    wa = 'https://wa.me/972587800228?text=' + quote(u['wamsg'])
    chips = ''.join('<a style="--sc:%s" href="#%s">%s%s <i>%d</i></a>' % (SCOL[k], k, ico(k, 16), n[lang], len(l)) for k, n, l in SECTIONS)
    tiles = ''.join('<a style="--sc:%s" href="#%s" title="%s">%s</a>' % (SCOL[k], k, n[lang], ico(k, 26)) for k, n, l in SECTIONS)
    secs = ''.join('<section class="hsec" id="%s" style="--sc:%s">' % (k, SCOL[k]) + cov(k, 'scov rv') + '<div class="shead rv"><i>%s</i><div><h2>%s</h2><p>%s</p></div><b>%s</b></div><div class="ag">%s</div></section>' % (ico(k, 30), n[lang], SDESC[k][lang], cnt(lang, len(l)), ''.join(card(lang, a).replace('class="ac', 'class="rv ac', 1) for a in l)) for k, n, l in SECTIONS)
    q1 = ''.join('<button type="button" data-v="%d">%s</button>' % (i, o) for i, o in enumerate(L['q1o']))
    q2 = ''.join('<button type="button" data-v="%d">%s</button>' % (i, o) for i, o in enumerate(L['q2o']))
    picks = ''.join('<div class="pres" data-p="%s"><h3>%s</h3><div class="ag">%s</div></div>' % (key, L['pk_r'], ''.join(card(lang, a) for a in v)) for key, v in PICK.items())
    tips = json.dumps([[t[lang], s, A[s][lang]['title']] for s, t in TIPS], ensure_ascii=False).replace('</', '<\\/')
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": u['hub_t'], "inLanguage": lang, "url": url,
          "hasPart": [{"@type": "Article", "headline": A[a][lang]['title'], "url": BASE + 'articles/%s/%s.html' % (lang, a)} for a in ORDER]}
    body = f'''<div class="hub">
<div class="crumbs"><a href="{HOME[lang]}">{u['home']}</a> › {u['arts']}</div>
<div class="hero hasimg"><div class="htxt"><h1>{u['hub_t']}</h1>
<p class="lead">{u['hub_l']}</p>
<div class="stats"><div><b data-c="{len(ORDER)}">0</b><span>{L['st_a']}</span></div><div><b data-c="{len(SECTIONS)}">0</b><span>{L['st_t']}</span></div><div><b data-c="{total_min(lang)}">0</b><span>{L['st_m']}</span></div></div>
<div class="tiles">{tiles}</div></div>
<img class="himg" src="../../img/art/articles_hero.jpg" alt="" width="1536" height="1024"></div>
<div class="tools2">
<div class="pick" id="pick"><h2>{L['pk_t']}</h2><p>{L['pk_p']}</p>
<div class="pq" id="pq1"><b>{L['q1']}</b><div class="ops">{q1}</div></div>
<div class="pq" id="pq2"><b>{L['q2']}</b><div class="ops">{q2}</div></div>
{picks}<button type="button" class="pagain" id="pagain" hidden>{L['pk_again']}</button></div>
<div class="side2">
<label class="sbox">{SRCH}<input id="asrch" type="search" placeholder="{L['srch']}" aria-label="{L['srch']}"></label>
<div class="rdbar" id="rdbar"><div><span>{L['rd']} <b id="rdn">0</b> {L['of']} {len(ORDER)}</span><span id="rdp">0%</span></div><i><u id="rdu"></u></i></div>
<a class="tipc" id="tipc" href="#"><small>{BULB}{L['tip']}</small><p id="tipt"></p><em id="tipm">{L['tipm']}</em></a>
</div></div>
<nav class="chips">{chips}</nav>
{secs}
<div class="nf" id="nf"><a href="{wa}" target="_blank" rel="noopener">{L['none']}</a></div>
<div class="endc rv"><div><h2>{L['end_t']}</h2><p>{L['end_p']}</p></div><a href="{wa}" target="_blank" rel="noopener">{WASVG}{L['end_b']}</a></div>
</div>
<script>
(function(){{
var R=[];try{{R=JSON.parse(localStorage.getItem('as_read')||'[]');}}catch(e){{}}
var cards=document.querySelectorAll('.ac[data-s]');
cards.forEach(function(c){{if(R.indexOf(c.getAttribute('data-s'))>=0)c.classList.add('rd');}});
var uniq=R.filter(function(x,i){{return R.indexOf(x)===i;}}).length,T={len(ORDER)};
document.getElementById('rdn').textContent=uniq;var pc=Math.round(uniq/T*100);document.getElementById('rdp').textContent=pc+'%';
setTimeout(function(){{document.getElementById('rdu').style.width=pc+'%';}},300);
var TIPS={tips},d=new Date(),day=Math.floor((d-new Date(d.getFullYear(),0,0))/864e5),tp=TIPS[day%TIPS.length];
document.getElementById('tipt').textContent=tp[0];document.getElementById('tipc').href=tp[1]+'.html';document.getElementById('tipm').textContent+=': '+tp[2];
var red=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.stats b').forEach(function(b){{var n=+b.getAttribute('data-c');if(red){{b.textContent=n;return;}}var t0=null;function st(t){{if(!t0)t0=t;var p=Math.min(1,(t-t0)/1200);b.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(st);}}requestAnimationFrame(st);}});
if('IntersectionObserver' in window&&!red){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{var el=e.target,sib=[].indexOf.call(el.parentNode.children,el);el.style.transitionDelay=Math.min(sib,6)*70+'ms';el.classList.add('in');io.unobserve(el);}}}});}},{{rootMargin:'0px 0px -8% 0px'}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el);}});}}else document.querySelectorAll('.rv').forEach(function(el){{el.classList.add('in');}});
var a1=null,a2=null;function pk(){{document.querySelectorAll('.pres').forEach(function(p){{p.classList.toggle('on',p.getAttribute('data-p')===a1+'-'+a2);}});document.getElementById('pagain').hidden=!(a1!==null&&a2!==null);}}
[['pq1',function(v){{a1=v;}}],['pq2',function(v){{a2=v;}}]].forEach(function(x){{var box=document.getElementById(x[0]);box.querySelectorAll('button').forEach(function(b){{b.addEventListener('click',function(){{box.querySelectorAll('button').forEach(function(o){{o.classList.remove('on');}});b.classList.add('on');x[1](b.getAttribute('data-v'));pk();}});}});}});
document.getElementById('pagain').addEventListener('click',function(){{a1=a2=null;document.querySelectorAll('.pq button').forEach(function(o){{o.classList.remove('on');}});pk();}});
var inp=document.getElementById('asrch'),nf=document.getElementById('nf');
inp.addEventListener('input',function(){{var v=inp.value.trim().toLowerCase(),any=false;document.querySelectorAll('.hsec').forEach(function(s){{var vis=0;s.querySelectorAll('.ac').forEach(function(c){{var ok=!v||c.getAttribute('data-k').indexOf(v)>=0;c.style.display=ok?'':'none';if(ok){{vis++;c.classList.add('in');}}}});s.style.display=vis?'':'none';if(vis)any=true;}});nf.style.display=any?'none':'block';}});
}})();
</script>'''
    return shell(lang, u['hub_t'], u['hub_l'], url, alts_for(''), langs_for(lang, ''), body, 'website', ld)

def page(lang, slug):
    d = A[slug][lang]; u = UI[lang]; L = LIVE[lang]; k, n = SEC_OF[slug]
    url = BASE + 'articles/%s/%s.html' % (lang, slug)
    wa = 'https://wa.me/972587800228?text=' + quote(u['wamsg'])
    share = 'https://wa.me/?text=' + quote(L['share_msg'] + d['title'] + ' ' + url)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": d['title'], "description": d['lead'], "inLanguage": lang,
          "articleSection": n[lang], "author": {"@type": "Person", "name": "David Mushailov"}, "publisher": {"@type": "Organization", "name": "Apps & Soul"},
          "datePublished": "2026-11-24", "dateModified": "2026-11-24", "mainEntityOfPage": url, "image": BASE + 'img/og_%s.jpg' % lang}
    body_html = d['body']; toc = []
    def addid(m):
        i = len(toc) + 1; toc.append(_re.sub('<[^>]+>', '', m.group(1))); return '<h2 id="p%d">%s</h2>' % (i, m.group(1))
    body_html = _re.sub(r'<h2>(.*?)</h2>', addid, body_html)
    tochtml = ''.join('<a href="#p%d">%s</a>' % (i + 1, t) for i, t in enumerate(toc))
    sec = [a for kk, _, l in SECTIONS if kk == k for a in l if a != slug]
    others = [a for a in ORDER if a not in sec and a != slug]
    more = (sec + others)[:3]
    body = f'''<div class="rprog" style="--sc:{SCOL[k]}"><i id="rpi"></i></div>
<div class="wrapa" style="--sc:{SCOL[k]}">
<main>
<div class="crumbs"><a href="{HOME[lang]}">{u['home']}</a> › <a href="index.html">{u['arts']}</a> › <a href="index.html#{k}">{n[lang]}</a></div>
<article>
{cov(k, 'acov')}<div class="ahead"><i>{ico(slug, 28)}</i><div class="kick"><a href="index.html#{k}">{ico(k, 15)}{n[lang]}</a><span>{rtime(lang, slug)}</span><a class="shr" href="{share}" target="_blank" rel="noopener">{WASVG}{L['share']}</a></div></div>
<h1>{d['title']}</h1>
<p class="lead">{d['lead']}</p>
<div class="by">{u['by']}</div>
{body_html}
</article>
<div class="cta"><h2>{u['cta_t']}</h2><p>{u['cta_p']}</p><div class="b"><a class="p1" href="{wa}" target="_blank" rel="noopener">{u['wa']}</a><a class="p2" href="{HOME[lang]}#rev">{u['rev']}</a><a class="p3" href="{share}" target="_blank" rel="noopener">{WASVG}{L['share']}</a></div></div>
</main>
<aside class="toc" aria-label="{L['toc']}"><b>{L['toc']}</b>{tochtml}</aside>
</div>
<section class="more"><h3>{u['same'] if sec else u['more']}</h3><div class="ag">{''.join(card(lang, a) for a in more)}</div><a class="allb" href="index.html">{u['all']} · {len(ORDER)}</a></section>
<script>
(function(){{
try{{var R=JSON.parse(localStorage.getItem('as_read')||'[]');if(R.indexOf('{slug}')<0){{R.push('{slug}');localStorage.setItem('as_read',JSON.stringify(R));}}document.querySelectorAll('.ac[data-s]').forEach(function(c){{if(R.indexOf(c.getAttribute('data-s'))>=0)c.classList.add('rd');}});}}catch(e){{}}
var bar=document.getElementById('rpi'),art=document.querySelector('article'),links=[].slice.call(document.querySelectorAll('.toc a')),hs=links.map(function(a){{return document.getElementById(a.getAttribute('href').slice(1));}});
function on(){{var r=art.getBoundingClientRect(),h=innerHeight,p=Math.min(1,Math.max(0,(h*0.35-r.top)/(r.height-h*0.5)));bar.style.transform='scaleX('+p.toFixed(4)+')';
var cur=-1;hs.forEach(function(x,i){{if(x&&x.getBoundingClientRect().top<h*0.35)cur=i;}});links.forEach(function(a,i){{a.classList.toggle('on',i===cur);}});}}
addEventListener('scroll',on,{{passive:true}});addEventListener('resize',on);on();
}})();
</script>'''
    return shell(lang, d['title'], d['lead'], url, alts_for(slug + '.html'), langs_for(lang, slug + '.html'), body, 'article', ld)

for lang in ['he', 'ru', 'en']:
    os.makedirs(f'{OUT}/{lang}', exist_ok=True)
    for slug in ORDER:
        open(f'{OUT}/{lang}/{slug}.html', 'w', encoding='utf-8').write(page(lang, slug))
    open(f'{OUT}/{lang}/index.html', 'w', encoding='utf-8').write(hub(lang))
print('ok', sum(len(os.listdir(f'{OUT}/{l}')) for l in ['he', 'ru', 'en']))

# --- статьи в поиске главной (Ctrl K) ---
import re as _re2
MAINF = {'he': 'index.html', 'ru': 'ru.html', 'en': 'en.html'}
ARTN = {'ru': 'Статьи', 'he': 'מאמרים', 'en': 'Articles'}
for lang, fn in MAINF.items():
    fp = '/home/claude/site/' + fn
    m = open(fp, encoding='utf-8').read()
    data = [[A[a][lang]['title'], A[a][lang]['lead'], 'articles/%s/%s.html' % (lang, a), SEC_OF[a][1][lang] + ' ' + _re2.sub('<[^>]+>', ' ', A[a][lang]['body'])[:600]] for a in ORDER]
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    m2 = _re2.sub(r"var ART=\[.*?\]/\*ARTDATA\*/,ARTN='[^']*'/\*ARTN\*/", lambda _: "var ART=%s/*ARTDATA*/,ARTN='%s'/*ARTN*/" % (js, ARTN[lang]), m, flags=_re2.S)
    assert m2 != m or 'ARTDATA' in m, fn
    open(fp, 'w', encoding='utf-8').write(m2)
print('main search patched')
