# Картинка настоящей работы для карточки пакета: компьютер + телефон на тёмно-синем фоне
import sys
from PIL import Image,ImageDraw,ImageFilter
def rr(im,r):
    m=Image.new('L',im.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,im.size[0]-1,im.size[1]-1),r,fill=255);o=im.convert('RGBA');o.putalpha(m);return o
def shadow(canvas,box,r,blur=28,off=(0,18),alpha=110):
    sh=Image.new('RGBA',canvas.size,(0,0,0,0));d=ImageDraw.Draw(sh)
    d.rounded_rectangle((box[0]+off[0],box[1]+off[1],box[2]+off[0],box[3]+off[1]),r,fill=(5,3,20,alpha))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
def make(desk,phone,out,W=1200,H=750):
    c=Image.new('RGBA',(W,H));px=c.load()
    for y in range(H):
        for x in range(0,W):
            t=(x/W*.6+y/H*.4);px[x,y]=(int(22+(42-22)*t),int(17+(35-17)*t),int(58+(112-58)*t),255)
    # мягкий золотой отблеск
    g=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(g).ellipse((W*.55,-H*.3,W*1.2,H*.6),fill=(229,182,74,70));c.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    d=Image.open(desk).convert('RGB');dw=880;bar=0
    d=d.resize((dw,int(d.size[1]*dw/d.size[0])));dh=min(d.size[1],H-120);d=d.crop((0,0,dw,dh))
    frame=Image.new('RGB',(dw,dh+bar),(240,237,230));frame.paste(d,(0,bar));fd=ImageDraw.Draw(frame)
    for i,col in enumerate([(255,95,87),(254,188,46),(40,200,64)]):fd.ellipse((14+i*20,10,24+i*20,20),fill=col)
    x0,y0=60,60;shadow(c,(x0,y0,x0+dw,y0+dh+bar),18);c.alpha_composite(rr(frame,18),(x0,y0))
    p=Image.open(phone).convert('RGB');pw=250;ph=int(pw*2.0)
    p=p.resize((pw,int(p.size[1]*pw/p.size[0])));p=p.crop((0,0,pw,min(ph,p.size[1])));ph=p.size[1]
    body=Image.new('RGB',(pw+16,ph+16),(12,10,30));body.paste(p,(8,8))
    bx,by=W-pw-16-70,H-ph-16-34;shadow(c,(bx,by,bx+pw+16,by+ph+16),34,alpha=150)
    c.alpha_composite(rr(body,34),(bx,by))
    c.convert('RGB').save(out,quality=86);print(out)
if __name__=='__main__':make(*sys.argv[1:4])
