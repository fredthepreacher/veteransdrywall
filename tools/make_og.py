"""Regenerates assets/images/og/veteran-drywall-og-v11.jpg (1200x630 social preview)."""
from PIL import Image, ImageDraw, ImageFont
W,H=1200,630
bg=Image.new('RGB',(W,H),(10,21,40))
crew=Image.open('assets/images/webp/veteran-drywall-crew-mobile-900x1200.webp').convert('RGB')
ph_w=560; c=crew.resize((ph_w,int(ph_w*crew.height/crew.width)))
top=min(int(c.height*0.06), c.height-H); c=c.crop((0,top,ph_w,top+H))
bg.paste(c,(W-ph_w,0))
fw=110
g=Image.linear_gradient('L').rotate(90,expand=True).resize((fw,H))
region=bg.crop((W-ph_w,0,W-ph_w+fw,H)); navy=Image.new('RGB',(fw,H),(10,21,40))
bg.paste(Image.composite(region,navy,g),(W-ph_w,0))
d=ImageDraw.Draw(bg)
F='/usr/share/fonts/truetype/google-fonts/'
bold=lambda s: ImageFont.truetype(F+'Poppins-Bold.ttf',s); med=lambda s: ImageFont.truetype(F+'Poppins-Medium.ttf',s)
gold=(242,178,51)
logo=Image.open('assets/images/veteran-drywall-horizontal-logo.webp').convert('RGBA')
lw=400; logo=logo.resize((lw,int(lw*logo.height/logo.width)))
plate=Image.new('RGBA',(lw+24,logo.height+20),(255,252,246,255)); plate.paste(logo,(12,10),logo)
mask=Image.new('L',plate.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,*plate.size),16,fill=255)
bg.paste(plate,(52,44),mask)
y=44+plate.size[1]+30
d.text((54,y),'USMC VETERAN OWNED · NORTH PORT, FL',font=med(19),fill=gold); y+=38
d.text((52,y),'Drywall repair that',font=bold(52),fill=(255,255,255)); y+=64
d.text((52,y),'disappears.',font=bold(52),fill=gold); y+=74
d.text((54,y),'Texture matching · Water & storm damage',font=med(20),fill=(220,215,205)); y+=31
d.text((54,y),'Ceilings · Popcorn removal · Remodels',font=med(20),fill=(220,215,205)); y+=48
d.rounded_rectangle((52,y,52+300,y+56),28,fill=gold); d.text((74,y+9),'(941) 527-5924',font=bold(27),fill=(10,21,40))
d.text((52+318,y+15),'FL Lic. SCC131152687',font=med(18),fill=(200,196,188))
bg.save('assets/images/og/veteran-drywall-og-v11.jpg',quality=86,optimize=True,progressive=True)
