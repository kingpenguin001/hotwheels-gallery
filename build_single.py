import json,base64,io
from PIL import Image
cars=json.load(open('site/cars.json'))
def b64(path,size,q):
    im=Image.open(path);im.thumbnail((size,size));buf=io.BytesIO();im.save(buf,'JPEG',quality=q,optimize=True,progressive=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
imgs={c['code']:{'t':b64(f"site/img/thumb/{c['code']}.jpg",480,72),'f':b64(f"site/img/full/{c['code']}.jpg",1200,78)} for c in cars}
html=open('site/index.html').read()
inline='<script>window.CARS='+json.dumps(cars)+';window.IMAGES='+json.dumps(imgs)+';</script>'
html=html.replace('<script src="cars.js"></script>',inline)
open('ruhaans-car-collection.html','w').write(html)
