import os

from api import app, conf
from api.models import CapsBrand
from fastapi.responses import FileResponse

from api.auxil_func.get_caps import *
from api.auxil_func.get_brand import *

@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/')
async def get_caps(page: int = 1, pg_size: int = 5):
    if (page <= 0) or (pg_size <= 0):
        return None

    pointer_id = calc_pointer_id_in_db(page, pg_size) ## NOTE(annad): How can this be done correctly?
    caps = get_caps_db_request(pointer_id, pg_size)

    if len(caps) == 0:
        return None

    res = {
        'count': '',
        'next': '',
        'previous': '',
        'results': []
    }

    res['count'] = len(caps)
    res['next'] = None if res['count'] < pg_size else conf.base_url_generate('/api/' + conf.API_VER + '/caps/') + \
                                                      '?page={page}&pg_size={pg_size}'.format(page=page+1, pg_size=pg_size)
    res['previous'] = None if page == 1 else conf.base_url_generate('/api/' + conf.API_VER + '/caps/') + \
                                             '?page={page}&pg_size={pg_size}'.format(page=page-1, pg_size=pg_size)

    for cap in caps:
        cap.image = conf.base_url_generate('/' + cap.image)
        res['results'].append(cap.get_dict_repr())

    return res


@app.get('/api/v1/brands/{brand_id}')
async def get_brand(brand_id: int = 1):
    if brand_id <= 0:
        return None

    brand = get_caps_brand_db_request(brand_id)

    if len(brand) != 1:
        return None

    brand: CapsBrand = brand[0]
    res = brand.get_dict_repr()
    res['image'] = conf.base_url_generate('/' + res['image'])

    return res

@app.get('/media/{directory}/{name}')
async def get_media_cap(directory, name):
    image_path = os.path.join(directory, name)
    return FileResponse(os.path.join(conf.STATIC_IMAGE_DIR, image_path))