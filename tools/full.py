import sys,asyncio
from playwright.async_api import async_playwright
from PIL import Image
async def main():
    f,out,w=sys.argv[1],sys.argv[2],int(sys.argv[3]); h=int(sys.argv[4]) if len(sys.argv)>4 else 900
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.goto('file://'+f); await pg.wait_for_timeout(1200)
        H=await pg.evaluate('document.documentElement.scrollHeight')
        # scroll through to trigger lazy/observers
        for y in range(0,H,h): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(120)
        await pg.evaluate('scrollTo(0,0)'); await pg.wait_for_timeout(500)
        await pg.screenshot(path='/tmp/_full.png',full_page=True)
        await b.close()
    im=Image.open('/tmp/_full.png'); print('H',im.size)
    n=int(sys.argv[5]) if len(sys.argv)>5 else 4; step=-(-im.size[1]//n)
    for i in range(n):
        c=im.crop((0,i*step,im.size[0],min(im.size[1],(i+1)*step)))
        c.thumbnail((1000,4000)); c.save(f'{out}_{i}.png')
asyncio.run(main())
