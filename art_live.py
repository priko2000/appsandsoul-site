# Живые элементы страницы статей и самих статей (вставляется в build_articles.py)
LIVE = {
 'ru': dict(st_a='статьи', st_t='тем', st_m='минут чтения', pk_t='С чего мне начать?', pk_p='Два вопроса — и мы подберём три статьи именно для вас.',
   q1='Что у вас?', q1o=['Магазин', 'Услуги или мастерская', 'Пока только идея'], q2='Сайт уже есть?', q2o=['Да', 'Ещё нет'], pk_r='Начните с этих статей:', pk_again='Выбрать заново',
   srch='Поиск по статьям: доставка, Google, договор…', none='Ничего не нашлось. Спросите в WhatsApp →', rd='Вы прочитали', of='из', rdl='Прочитано',
   tip='Совет дня', tipm='Подробнее в статье', end_t='Не нашли ответ?', end_p='Задайте вопрос в WhatsApp — отвечаю в течение 2 часов в рабочее время.', end_b='Спросить в WhatsApp',
   toc='В этой статье', share='Отправить статью в WhatsApp', share_msg='Полезная статья: '),
 'he': dict(st_a='מאמרים', st_t='נושאים', st_m='דקות קריאה', pk_t='מאיפה להתחיל?', pk_p='שתי שאלות — ונמצא לכם שלושה מאמרים שמתאימים בדיוק לכם.',
   q1='מה יש לכם?', q1o=['חנות', 'שירותים או סדנה', 'בינתיים רק רעיון'], q2='כבר יש אתר?', q2o=['כן', 'עדיין לא'], pk_r='התחילו מהמאמרים האלה:', pk_again='לבחור מחדש',
   srch='חיפוש במאמרים: משלוחים, גוגל, חוזה…', none='לא נמצא כלום. שאלו בוואטסאפ ←', rd='קראתם', of='מתוך', rdl='נקרא',
   tip='הטיפ היומי', tipm='עוד במאמר', end_t='לא מצאתם תשובה?', end_p='שאלו בוואטסאפ — אני עונה תוך שעתיים בשעות העבודה.', end_b='לשאול בוואטסאפ',
   toc='במאמר הזה', share='לשלוח את המאמר בוואטסאפ', share_msg='מאמר שימושי: '),
 'en': dict(st_a='articles', st_t='topics', st_m='minutes of reading', pk_t='Where should I start?', pk_p='Two questions, and we will pick three articles just for you.',
   q1='What do you have?', q1o=['A store', 'Services or a workshop', 'Just an idea so far'], q2='Do you already have a website?', q2o=['Yes', 'Not yet'], pk_r='Start with these articles:', pk_again='Choose again',
   srch='Search articles: delivery, Google, contract…', none='Nothing found. Ask on WhatsApp →', rd='You have read', of='of', rdl='Read',
   tip='Tip of the day', tipm='More in the article', end_t='Didn’t find your answer?', end_p='Ask on WhatsApp — I reply within 2 hours during working hours.', end_b='Ask on WhatsApp',
   toc='In this article', share='Send this article on WhatsApp', share_msg='A useful article: '),
}
# подбор: [что у вас][сайт есть?] -> три статьи
PICK = {
 '0-0': ['shop-checklist', 'no-visitors', 'online-payment'],
 '0-1': ['seven-questions', 'whatsapp-and-site', 'own-site-or-builder'],
 '1-0': ['no-visitors', 'reviews', 'accessibility-law'],
 '1-1': ['seven-questions', 'site-or-app', 'google-start'],
 '2-0': ['own-site-or-builder', 'google-start', 'ownership'],
 '2-1': ['seven-questions', 'prepare-materials', 'choose-developer'],
}
TIPS = [
 ('domain-hosting', {'ru': 'Проверьте, на кого оформлен ваш домен. Он должен принадлежать вам, а не разработчику.', 'he': 'בדקו על שם מי רשום הדומיין שלכם. הוא צריך להיות שלכם, ולא של המפתח.', 'en': 'Check whose name your domain is registered in. It should be yours, not the developer’s.'}),
 ('delivery', {'ru': 'Показывайте стоимость доставки до корзины, а не на последнем шаге: так меньше брошенных заказов.', 'he': 'הציגו את מחיר המשלוח לפני העגלה, ולא בשלב האחרון: כך פחות הזמנות ננטשות.', 'en': 'Show the delivery cost before the cart, not at the last step: fewer abandoned orders.'}),
 ('reviews', {'ru': 'Просите отзыв в момент, когда клиент доволен больше всего — сразу после доставки.', 'he': 'בקשו ביקורת ברגע שהלקוח הכי מרוצה — מיד אחרי המשלוח.', 'en': 'Ask for a review when the customer is happiest — right after delivery.'}),
 ('privacy-13', {'ru': 'Рядом с каждой формой на сайте напишите, зачем вы собираете данные и кто их получит.', 'he': 'ליד כל טופס באתר כתבו למה אתם אוספים את המידע ומי יקבל אותו.', 'en': 'Next to every form on your site, say why you collect the data and who receives it.'}),
 ('shop-checklist', {'ru': 'Откройте свой сайт на телефоне и попробуйте заказать что-то за минуту. Где споткнулись — там и теряете клиентов.', 'he': 'פתחו את האתר בטלפון ונסו להזמין משהו בתוך דקה. איפה שנתקעתם — שם אתם מאבדים לקוחות.', 'en': 'Open your site on a phone and try to order something in a minute. Where you stumble is where you lose customers.'}),
 ('whatsapp-and-site', {'ru': 'Кнопка WhatsApp должна быть видна на каждой странице, а не только в контактах.', 'he': 'כפתור וואטסאפ צריך להיות גלוי בכל עמוד, ולא רק בעמוד צור קשר.', 'en': 'The WhatsApp button should be visible on every page, not only on the contact page.'}),
 ('google-start', {'ru': 'Карточка в Google Картах бесплатна и для местного бизнеса часто важнее самого сайта.', 'he': 'כרטיס בגוגל מפות הוא חינם, ולעסק מקומי לעיתים קרובות חשוב יותר מהאתר עצמו.', 'en': 'A Google Maps listing is free, and for a local business it often matters more than the site itself.'}),
 ('ownership', {'ru': 'Задайте себе вопрос: смогу ли я передать сайт другому разработчику за один день?', 'he': 'שאלו את עצמכם: האם אוכל להעביר את האתר למפתח אחר ביום אחד?', 'en': 'Ask yourself: could I hand the site to another developer in one day?'}),
 ('promotions', {'ru': '«Бесплатная доставка от суммы» — одна из самых сильных акций: клиент сам добирает корзину.', 'he': '„משלוח חינם מעל סכום” — אחד המבצעים החזקים ביותר: הלקוח משלים את העגלה בעצמו.', 'en': '“Free delivery over an amount” is one of the strongest promotions: customers fill up the cart themselves.'}),
 ('notifications', {'ru': 'Одно полезное сообщение в неделю лучше ежедневного шума. Пишите только тем, кто разрешил.', 'he': 'הודעה מועילה אחת בשבוע עדיפה על רעש יומי. כתבו רק למי שאישר.', 'en': 'One useful message a week beats daily noise. Write only to those who agreed.'}),
 ('prepare-materials', {'ru': 'Соберите все товары в одну таблицу: одна строка — один товар. Это ускоряет запуск сильнее всего.', 'he': 'רכזו את כל המוצרים בטבלה אחת: שורה אחת — מוצר אחד. זה מאיץ את ההשקה יותר מכל דבר אחר.', 'en': 'Put all products in one spreadsheet: one row per product. Nothing speeds up a launch more.'}),
 ('accessibility-law', {'ru': 'Кнопка-виджет доступности сама по себе не делает сайт доступным: важно, как он сделан в коде.', 'he': 'כפתור תוסף נגישות לבדו לא הופך אתר לנגיש: חשוב איך הוא בנוי בקוד.', 'en': 'An accessibility widget alone does not make a site accessible: what matters is how it is built in code.'}),
]

LIVECSS = """
.stats{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:20px}
.stats div{display:flex;align-items:baseline;gap:8px}
.stats b{font-family:'Unbounded',system-ui,sans-serif;font-size:clamp(28px,3vw,44px);line-height:1;color:var(--ink)}
.stats span{color:var(--mut);font-weight:700}
.tools2{display:grid;grid-template-columns:1.25fr 1fr;gap:16px;margin:18px 0 6px;align-items:start}
.pick{background:linear-gradient(135deg,#16113A,#2A1F6E);color:#fff;border-radius:26px;padding:clamp(20px,2.4vw,30px);position:relative;overflow:hidden}
.pick::after{content:"";position:absolute;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle,#FFC70055,transparent 70%);inset-inline-end:-60px;top:-80px;pointer-events:none}
.pick h2{color:#fff;margin:0 0 6px;font-size:clamp(22px,2vw,28px)}
.pick>p{margin:0 0 16px;color:#cfc9f0}
.pq{margin:0 0 12px}
.pq b{display:block;font-size:15px;margin-bottom:8px;color:#fff}
.pq .ops{display:flex;flex-wrap:wrap;gap:8px}
.pq button{font:inherit;font-weight:700;font-size:15px;border:1.5px solid rgba(255,255,255,.35);background:transparent;color:#fff;border-radius:999px;padding:9px 16px;cursor:pointer;transition:background .2s,color .2s,border-color .2s}
.pq button:hover{border-color:#fff}
.pq button.on{background:#FFC700;color:#16113A;border-color:#FFC700}
.pres{display:none;margin-top:8px}
.pres.on{display:block;animation:fadeup .45s ease both}
.pres h3{font-size:16px;margin:0 0 10px;color:#FFC700}
.pres .ag{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.pres .ac{padding:14px!important;color:var(--ink)}
.pres .ac b{font-size:15px!important}
.pres .ac>span:not(.ai),.pres .ac small{display:none}
.pres .ai i{width:36px;height:36px}
.pagain{margin-top:10px;background:none;border:0;color:#cfc9f0;font:inherit;text-decoration:underline;cursor:pointer;padding:0}
.side2{display:flex;flex-direction:column;gap:16px}
.sbox{position:relative}
.sbox input{width:100%;box-sizing:border-box;font:inherit;font-size:17px;padding:17px 20px;padding-inline-start:52px;border-radius:18px;border:2px solid var(--line);background:#fff;outline:none;transition:border-color .2s,box-shadow .2s}
.sbox input:focus{border-color:var(--vi);box-shadow:0 0 0 5px #5B3DF51f}
.sbox svg{position:absolute;inset-inline-start:18px;top:50%;transform:translateY(-50%);color:var(--mut)}
.rdbar{background:#fff;border:1px solid var(--line);border-radius:18px;padding:14px 18px}
.rdbar div{display:flex;justify-content:space-between;font-weight:700;font-size:15px;margin-bottom:8px}
.rdbar i{display:block;height:8px;border-radius:99px;background:#eee;overflow:hidden}
.rdbar i u{display:block;height:100%;width:0;background:linear-gradient(90deg,#5B3DF5,#26C281,#FFC700);border-radius:99px;transition:width .8s cubic-bezier(.2,.8,.2,1)}
.tipc{display:block;text-decoration:none;color:var(--ink);background:#FFF6D6;border:1px solid #FFE38A;border-radius:18px;padding:16px 18px;transition:transform .2s}
.tipc:hover{transform:translateY(-2px)}
.tipc small{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:13px;color:#9A6B00}
.tipc p{margin:6px 0 6px;font-weight:600;line-height:1.5}
.tipc em{font-style:normal;font-size:14px;color:var(--vi);font-weight:800}
.ac.rd .ai u::after{content:" ✓";color:#26C281}
.ac.rd{opacity:.82}
.ac .rdl{display:none;font-size:12px;font-weight:800;color:#1a9a62;background:#e6f8ef;border-radius:99px;padding:2px 8px}
.ac.rd .rdl{display:inline-block}
.nf{display:none;padding:26px;text-align:center;background:#fff;border:1px dashed var(--line);border-radius:20px;margin-top:20px}
.nf a{color:var(--vi);font-weight:800;text-decoration:none}
.endc{margin:56px 0 10px;background:linear-gradient(135deg,#16113A,#3A2A9A);color:#fff;border-radius:30px;padding:clamp(26px,4vw,48px);display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px}
.endc h2{color:#fff;margin:0 0 6px}
.endc p{margin:0;color:#d6d0f5}
.endc a{background:#25D366;color:#fff;text-decoration:none;font-weight:800;border-radius:16px;padding:16px 24px;display:inline-flex;gap:10px;align-items:center}
.rv{opacity:0;transform:translateY(22px);transition:opacity .6s ease,transform .6s cubic-bezier(.2,.8,.2,1)}
.rv.in{opacity:1;transform:none}
@keyframes fadeup{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}}
@media (max-width:980px){.tools2{grid-template-columns:1fr}.pres .ag{grid-template-columns:1fr}}
.rprog{position:fixed;top:0;left:0;right:0;height:4px;z-index:9;pointer-events:none}
.rprog i{display:block;height:100%;width:100%;background:var(--sc);transform-origin:0 50%;transform:scaleX(0)}
[dir=rtl] .rprog i{transform-origin:100% 50%}
.wrapa{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,760px) minmax(0,1fr);gap:40px;max-width:1700px;margin:0 auto}
.wrapa>main{grid-column:2;max-width:none;width:100%;padding-inline:0}
.toc{grid-column:3;align-self:start;position:sticky;top:96px;margin-top:150px;max-width:300px}
.toc b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin-bottom:10px}
html[lang=he] .toc b{text-transform:none;letter-spacing:0;font-size:15px}
.toc a{display:block;text-decoration:none;color:var(--mut);font-size:15px;line-height:1.35;padding:7px 12px;border-inline-start:3px solid var(--line);transition:color .2s,border-color .2s}
.toc a:hover,.toc a.on{color:var(--ink);border-color:var(--sc);font-weight:700}
.tocl{grid-column:1}
@media (max-width:1399px){.wrapa{display:block}.toc{display:none}.wrapa>main{max-width:760px;margin:0 auto;padding-inline:clamp(18px,4vw,40px)}}
.shr{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:800;font-size:14px;color:#128C4A;background:#E7F8EE;border-radius:999px;padding:6px 12px}
.shr:hover{background:#25D366;color:#fff}
.cta .p3{background:#25D366;color:#fff}
"""

LIVECSS += """
.scov{display:block;width:100%;aspect-ratio:2.6;object-fit:cover;object-position:50% 35%;border-radius:20px;margin:0 0 14px;box-shadow:0 14px 34px rgba(17,17,17,.12)}
.acov{display:block;width:100%;aspect-ratio:2.4;object-fit:cover;object-position:50% 38%;border-radius:22px;margin:0 0 22px}
"""
LIVECSS += """
.kick a.shr{background:#E7F8EE;color:#128C4A}
.kick a.shr:hover{background:#25D366;color:#fff}
"""
LIVECSS += """
.hero.hasimg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:10px;align-items:center}
.hero .himg{width:100%;height:auto;display:block;-webkit-mask-image:radial-gradient(ellipse 58% 56% at 50% 50%,#000 55%,transparent 100%);mask-image:radial-gradient(ellipse 58% 56% at 50% 50%,#000 55%,transparent 100%);transition:transform .4s ease-out}
@media (max-width:900px){.hero.hasimg{grid-template-columns:1fr}.hero .himg{max-width:560px;margin:0 auto}}
"""
