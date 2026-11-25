# Исходники сайта Apps & Soul (ветка source)

Ветка `main` — готовый сайт (GitHub Pages). Здесь — исходники, из которых он собирается.

## Как восстановить рабочую папку
```
mkdir -p /home/claude && cd /home/claude
git clone https://github.com/priko2000/appsandsoul-site.git
git -C appsandsoul-site worktree add /tmp/src source
cp /tmp/src/*.py /tmp/src/*.sh /tmp/src/ru_strings.json .
mkdir -p site && cp /tmp/src/site/* site/
cp -r appsandsoul-site/img site/img          # картинки берутся из main
cp appsandsoul-site/reel.mp4 site/
chmod +x make_site.sh deploy_gh.sh
./make_site.sh                                # собирает site/index.html (иврит), ru.html, en.html, articles/
./deploy_gh.sh "описание изменения"           # выкладывает в main
```

## Где что
- `site/index.ru.bak` — главный исходник страницы (русский). Правки делать здесь.
- `ru_strings.json` + `tr.py` — переводы на иврит и английский (build.py подставляет).
- `articles_src.py`, `art_*.py` — 23 статьи на трёх языках; `build_articles.py` собирает хаб и статьи.
- Коммит `dcdf3ad` в main — копия сайта до редизайна (24.11.2026), к нему можно вернуться.

## Редизайн v2 (24.11.2026)
- `redesign_v2.py` — все правки плана одним скриптом: берёт копию `backups/v1/index.ru.bak` (= исходник до редизайна, он же `site/index.ru.bak` из коммита до этого) и пишет новый `site/index.ru.bak`. Новые служебные классы — с приставкой `v2`.
- Картинки пакетов: `img/pw2.jpg`, `img/pw3.jpg` (+ `img/he/…`), `img/{ru,he,en}/pw1.jpg` — собираются `tools/comp.py` и `tools/pw1.py`.
- Точка возврата: коммит `dcdf3ad` в main.

## Состояние на 25.11.2026 (после части 2)
- Редизайн по плану из 12 пунктов выполнен и выложен (иврит, русский, английский).
- Дополнительно: ширина блоков на 3440, ускорение (шрифты не блокируют показ, лёгкие картинки), доступность 100/100, один заголовок «Попробуйте сами», спокойная смена слов в подвале, «Азарт» на телефоне без длинной прокрутки.
- Карточка «Визитка»: образец винодельни `demo/v4_winery.html` → картинка `img/pw1_visitka.jpg` (+ `_s`).
- Все правки главной страницы — в `redesign_v2.py` (применяется к `backups/v1/index.ru.bak`), затем `./make_site.sh`, затем `./deploy_gh.sh "описание"`.
- Новые строки переводов дописываются в конец `ru_strings.json` и `tr.py` (T.update).
