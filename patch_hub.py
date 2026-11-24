import re
s = open('/home/claude/build_articles.py').read()
b = open('/home/claude/build.py').read()
lang_css = re.search(r"LANGCSS='''(.*?)'''", b, re.S).group(1)
lang_css = '\n'.join(l for l in lang_css.split('\n') if l.startswith('.langs') or l.startswith('[dir=rtl] .langs') or l.startswith('@keyframes flwave'))
flag = re.search(r"(FLAG=\{.*?'\})\n", b, re.S).group(1)
NEW = '\n' + flag.replace('FLAG=', 'FLAG = ') + '\nLANGCSS2 = """' + lang_css + '''
.top .langs{margin-inline-start:auto}
.langs a{text-decoration:none}
@media (max-width:560px){.langs{gap:2px;padding:3px}.langs a,[dir=rtl] .langs a{padding:3px}.langs .cd{display:none}.langs .fl{width:26px;height:26px}}
"""
''' + open('/home/claude/patch_icons.txt').read() + '\n'
anchor = "LOGO = '<img src"
assert anchor in s
s = s.replace(anchor, NEW + anchor, 1)

def rep(a, b_):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b_)

rep("""    return ''.join('<a href="../%s/%s" lang="%s" title="%s"%s>%s</a>' % (l, fname, l, NAME[l], ' class="on"' if l == lang else '', CODE[l]) for l in ['ru', 'he', 'en'])""",
    """    return ''.join('<a href="../%s/%s" lang="%s" title="%s"%s><span class="fl">%s</span><span class="cd">%s</span></a>' % (l, fname or 'index.html', l, NAME[l], ' class="on"' if l == lang else '', FLAG[l], CODE[l]) for l in ['ru', 'he', 'en'])""")
rep("""    return '<a class="ac%s" style="--sc:%s" href="%s.html"><small>%s</small><b>%s</b><span>%s</span><em>%s</em></a>' % (' on' if slug == cur else '', SCOL[k], slug, n[lang], d['title'], lead, rtime(lang, slug))""",
    """    num = '%02d' % (ORDER.index(slug) + 1)
    return '<a class="ac%s" style="--sc:%s" href="%s.html"><span class="ai"><i>%s</i><u>%s</u></span><small>%s</small><b>%s</b><span>%s</span><em>%s<b>→</b></em></a>' % (' on' if slug == cur else '', SCOL[k], slug, ico(slug, 22), num, n[lang], d['title'], lead, rtime(lang, slug))""")
rep("""<div class="kick"><a href="index.html#{k}">{n[lang]}</a><span>{rtime(lang, slug)}</span></div>""",
    """<div class="ahead"><i>{ico(slug, 28)}</i><div class="kick"><a href="index.html#{k}">{ico(k, 15)}{n[lang]}</a><span>{rtime(lang, slug)}</span></div></div>""")
rep("""    chips = ''.join('<a style="--sc:%s" href="#%s">%s <i>%d</i></a>' % (SCOL[k], k, n[lang], len(l)) for k, n, l in SECTIONS)
    secs = ''.join('<section class="hsec" id="%s" style="--sc:%s"><h2>%s</h2><div class="ag">%s</div></section>' % (k, SCOL[k], n[lang], ''.join(card(lang, a) for a in l)) for k, n, l in SECTIONS)""",
    """    chips = ''.join('<a style="--sc:%s" href="#%s">%s%s <i>%d</i></a>' % (SCOL[k], k, ico(k, 16), n[lang], len(l)) for k, n, l in SECTIONS)
    tiles = ''.join('<a style="--sc:%s" href="#%s" title="%s">%s</a>' % (SCOL[k], k, n[lang], ico(k, 26)) for k, n, l in SECTIONS)
    secs = ''.join('<section class="hsec" id="%s" style="--sc:%s"><div class="shead"><i>%s</i><div><h2>%s</h2><p>%s</p></div><b>%s</b></div><div class="ag">%s</div></section>' % (k, SCOL[k], ico(k, 30), n[lang], SDESC[k][lang], cnt(lang, len(l)), ''.join(card(lang, a) for a in l)) for k, n, l in SECTIONS)""")
rep("""<h1>{u['hub_t']}</h1>
<p class="lead">{u['hub_l']} {len(ORDER)} {u['n']}.</p>
<nav class="chips">{chips}</nav>""", """<div class="hero"><h1>{u['hub_t']}</h1>
<p class="lead">{u['hub_l']} {len(ORDER)} {u['n']}.</p>
<div class="tiles">{tiles}</div></div>
<nav class="chips">{chips}</nav>""")
open('/home/claude/build_articles.py', 'w').write(s)
print('patched')
