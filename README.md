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
