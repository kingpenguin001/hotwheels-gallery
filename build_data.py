import openpyxl, collections, json, re, os
from PIL import Image, ImageOps, ImageDraw
PREFIX={'HOT WHEELS':'HW','MAJORETTE':'MJ','TEAMSTERZ':'TS','DACTOY':'DC'}
files={re.sub(r'[^A-Z0-9]','',f[:-4].upper()):f for f in os.listdir('drive') if f.lower().endswith('.jpg')}
ws=openpyxl.load_workbook('drive/Ruhaans Car Collection.xlsx').active
c=collections.Counter(); cars=[]
os.makedirs('img/thumb',exist_ok=True); os.makedirs('img/full',exist_ok=True)
for r in ws.iter_rows(min_row=2,max_col=5,values_only=True):
    if not r[1]: continue
    c[r[2]]+=1
    key=f"{PREFIX[r[2]]}{c[r[2]]:03d}"
    src=files.pop(key)
    im=ImageOps.exif_transpose(Image.open('drive/'+src)).convert('RGB')
    g=im.convert('L'); w,h=im.size
    xs=range(0,w,max(1,w//100)); avg=lambda y:sum(g.getpixel((x,y)) for x in xs)/len(xs)
    cut=h
    for y in range(int(h*0.7),h-20):
        if avg(y)>=252 and avg(y+10)>=252 and avg(y+20)>=250: cut=y; break
    if cut<h: im=im.crop((0,0,w,cut))
    print(src,(w,h),'->',im.size)
    a=im.copy(); a.thumbnail((1600,1600)); a.save(f'img/full/{key}.jpg',quality=82,optimize=True,progressive=True)
    b=im.copy(); b.thumbnail((600,600)); b.save(f'img/thumb/{key}.jpg',quality=78,optimize=True,progressive=True)
    q=r[4]; qty=int(re.match(r'\d+',str(q)).group()) if q else 1
    cars.append(dict(id=len(cars)+1,code=key,model=str(r[1]).strip(),brand=r[2].strip(),rating=int(r[3]),qty=qty))
print('unmatched files:',files)
json.dump(cars,open('cars.json','w'),indent=1)
open('cars.js','w').write('window.CARS='+json.dumps(cars,indent=1)+';\n')
