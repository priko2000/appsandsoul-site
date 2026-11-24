import asyncio,sys
sys.path.insert(0,'/home/claude/tools')
from comp import make
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for lang,f in [('ru','ru.html'),('he','index.html'),('en','en.html')]:
            for name,vp,sc in [('d',{'width':1400,'height':921},1),('m',{'width':390,'height':780},540/390)]:
                pg=await b.new_page(viewport=vp,device_scale_factor=sc)
                await pg.goto('file:///home/claude/site/'+f);await pg.wait_for_timeout(2500)
                await pg.evaluate("document.querySelectorAll('.qr,.a11b,.side').forEach(e=>e.style.display='none')")
                await pg.screenshot(path=f'/tmp/pw_{lang}_{name}.png');await pg.close()
            out='/home/claude/site/img/%s/pw1.jpg'%lang
            make(f'/tmp/pw_{lang}_d.png',f'/tmp/pw_{lang}_m.png',out)
        await b.close()
asyncio.run(main())
