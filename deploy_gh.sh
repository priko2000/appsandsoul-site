#!/bin/bash
# Копирует сайт в репозиторий GitHub и отправляет
set -e
R=/home/claude/appsandsoul-site; S=/home/claude/site; B=https://priko2000.github.io/appsandsoul-site
cp $S/index.html $S/ru.html $S/en.html $S/reel.mp4 $R/; cp $S/he_redirect.html $R/he.html; mkdir -p $R/articles; cp -r $S/articles/. $R/articles/
cp $R/img/qr.png /tmp/qr_gh.png; cp -r $S/img/. $R/img/; cp /tmp/qr_gh.png $R/img/qr.png
cd $R
for f in index ru en; do sed -i "s|content=\"img/og_|content=\"$B/img/og_|" $f.html; done
grep -q 'og:url' index.html || sed -i "s|<meta property=\"og:type\"|<meta property=\"og:url\" content=\"$B/\"><meta property=\"og:type\"|" index.html
git add -A
git -c user.name="priko2000" -c user.email="davidmushailov@gmail.com" commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01SmWZkdKbRWLdFK9ywzZ6vc" || echo "нет изменений"
git -c push.negotiate=true push -q origin main 2>&1 | tail -2
git log --oneline | head -1
