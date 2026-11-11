import csv,os
from PIL import Image,ImageOps,ImageDraw,ImageFont,ImageFilter
F='/home/claude/fonts/';INK=(14,42,71);SUN2=(255,176,32)
logo=Image.open('/home/claude/urbook-social/tools/urbook-logo.png').convert('RGB')
logo=logo.crop((150,250,930,830))  # mark + wordmark, trims navy margin
def badge(h):
  w=int(h*logo.width/logo.height);l=logo.resize((w,h),Image.LANCZOS)
  m=Image.new('L',(w,h),0);ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),radius=int(h*.16),fill=255)
  return l,m
def fit_font(text,path,maxw,start,minsz):
  s=start
  while s>minsz:
    f=ImageFont.truetype(path,s)
    if f.getlength(text)<=maxw: return f
    s-=2
  return ImageFont.truetype(path,minsz)
def make(src,title,sub,W,H,out,brand=True):
  im=ImageOps.fit(ImageOps.exif_transpose(Image.open(src)).convert('RGB'),(W,H),Image.LANCZOS)
  if brand:
    g=Image.new('L',(1,H));gh=int(H*(.55 if H<W else .45))
    for y in range(H):
      t=max(0,(y-(H-gh))/gh);g.putpixel((0,y),int(235*min(1,t**1.3*1.15)))
    ov=Image.new('RGB',(W,H),INK);im=Image.composite(ov,im,g.resize((W,H)))
    d=ImageDraw.Draw(im);pad=int(W*.05)
    bh=int(H*(.17 if H<W else .1));l,m=badge(bh)
    sh=Image.new('L',(l.width+40,l.height+40),0);ImageDraw.Draw(sh).rounded_rectangle((20,20,20+l.width,20+l.height),radius=int(bh*.16),fill=120);sh=sh.filter(ImageFilter.GaussianBlur(10))
    im.paste((0,0,0),(pad-20,pad-14),sh);im.paste(l,(pad,pad),m)
    tf=fit_font(title,F+'Baloo2-800.ttf',W-2*pad,int(H*(.12 if H<W else .085)),30)
    sf=fit_font(sub,F+'DMSans-700.ttf',W-2*pad,int(H*(.055 if H<W else .04)),20)
    y_sub=H-pad-sf.size; y_t=y_sub-int(tf.size*1.12)
    d.text((pad,y_t),title,font=tf,fill='white');d.text((pad,y_sub),sub,font=sf,fill=SUN2)
  im.save(out,quality=88,optimize=True)
os.makedirs('branded',exist_ok=True);os.makedirs('clean',exist_ok=True)
for slug,media,t,s in csv.reader(open('list.tsv'),delimiter='\t'):
  for nm,(W,H) in {'landscape':(1200,628),'square':(1200,1200)}.items():
    make(f'src/{slug}.jpg',t,s,W,H,f'branded/{slug}_{nm}.jpg')
    make(f'src/{slug}.jpg',t,s,W,H,f'clean/{slug}_{nm}.jpg',brand=False)
