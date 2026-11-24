import sys,asyncio
from playwright.async_api import async_playwright
# usage: shot.py file.html out_prefix [w h ...]
async def main():
    f=sys.argv[1]; out=sys.argv[2]; sizes=[(390,844),(1024,1366),(3440,1440)]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w,h in sizes:
            pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
            await pg.goto('file://'+f); await pg.wait_for_timeout(1500)
            H=await pg.evaluate('document.documentElement.scrollHeight')
            secs=await pg.evaluate('''[...document.querySelectorAll("main > section, main > div, footer")].filter(e=>e.offsetHeight>0).map(e=>[(e.id||e.className).slice(0,25),Math.round(e.getBoundingClientRect().top+scrollY),e.offsetHeight])''')
            print(w,'height',H); print(secs)
            await pg.screenshot(path=f'{out}_{w}.png')
            await pg.close()
        await b.close()
asyncio.run(main())
