import os

from api import app, conf, DBSession
from api.models import Cap, CapsBrand
from fastapi.responses import FileResponse

def calc_pointer_id(page: int, pg_size: int):
    return ((page - 1) * pg_size) + 1

@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/')
async def get_caps(page=1, pg_size=5):
    ## TODO(annad): Perform code refactoring

    page = int(page)
    pg_size = int(pg_size)
    res = {}

    ## TODO(annad): How can this be done correctly?
    pointer_id = calc_pointer_id(page, pg_size)

    with DBSession() as sess:
        caps = sess.query(Cap).filter(Cap.id >= pointer_id, Cap.id < pointer_id + pg_size).all()

    res['count'] = len(caps)

    if res['count'] < pg_size:
        res['next'] = None
    else:
        res['next'] = 'http://192.168.2.136:8000' + '/api/v1/caps/' + \
                      '?page={page}&pg_size={pg_size}'.format(page=page+1, pg_size=pg_size)

    if page == 1:
        res['previous'] = None
    else:
        res['previous'] = 'http://192.168.2.136:8000' + '/api/v1/caps/' + \
                          '?page={page}&pg_size={pg_size}'.format(page=page-1, pg_size=pg_size)

    res['results'] = []
    for cap in caps:
        cap.image = 'http://192.168.2.136:8000/' + cap.image
        res['results'].append(cap.get_dict_repr())

    return res

@app.get('/api/v1/brands/{brand_id}')
async def get_brand(brand_id):
    ## TODO(annad): Perform code refactoring
    brand_id = int(brand_id)

    with DBSession() as sess:
        brand = sess.query(CapsBrand).filter(CapsBrand.id == brand_id).all()

    if len(brand) != 1:
        return None

    brand: CapsBrand = brand[0]
    res = brand.get_dict_repr()
    res['image'] = 'http://192.168.2.136:8000/' + res['image']

    return res

'''
LINK FOR TEST: 
http://192.168.2.136:8000/media/caps/20220206172612100.jpg
'''
@app.get('/media/{directory}/{name}')
async def get_media_cap(directory, name):
    image_path = os.path.join(directory, name)
    return FileResponse(os.path.join(conf.STATIC_IMAGE_DIR, image_path))