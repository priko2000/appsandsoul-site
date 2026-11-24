#!/bin/bash
set -e
cd /home/claude
cp site/index.ru.bak site/index.html
python3 build.py | grep -v 'осталось кириллицы' || true
python3 build_articles.py
