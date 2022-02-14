import os

from api import app, conf, DBSession
from api.models import Cap, CapsBrand
from api.paging import Page

from fastapi.responses import FileResponse, RedirectResponse

'''
from pydantic import BaseModel

class __Data(BaseModel):
    name:   str
    age:    int

_d = __Data(name='Anna', age=20)

@app.post('/posting-data/')
def posting_data(data: __Data):
    print(data)
    return {'Result':'SUCCESS'}
'''

def get_caps_brand_db_request(brand_id: int) -> list[CapsBrand]:
    with DBSession() as sess:
        brand = sess.query(CapsBrand).filter(CapsBrand.id == brand_id).all()
    return brand


def get_caps_db_request(pg: Page) -> list[Cap]:
    with DBSession() as sess:
        caps = sess.query(Cap).filter(Cap.id >= pg.start_id(), Cap.id < pg.end_id()).all()
    return caps


@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/{cap_id}')
async def get_cap_by_id(cap_id: int):
    # NOTE(annad): Mb made specificly request for ONE cap?..
    res = RedirectResponse(url=f'/api/v1/caps/?number_page={cap_id}&pg_size=1')
    return res

@app.get('/api/v1/caps/')
async def get_caps(number_page: int = 1, pg_size: int = 5):
    if (number_page <= 0) or (pg_size <= 0):
        return None

    pg = Page(number_page, pg_size, '?number_page={}&pg_size={}')
    caps: list[Cap] = get_caps_db_request(pg)

    if len(caps) == 0:
        return None

    res = {
        'count': 0,
        'next': '',
        'previous': '',
        'results': []
    }

    res['count'] = len(caps)
    res['next'] = None if res['count'] < pg.size else conf.base_url_generate('/api/' + conf.API_VER + '/caps/') + pg.next().string_format
    res['previous'] = None if pg.number == 1 else conf.base_url_generate('/api/' + conf.API_VER + '/caps/') + pg.previous().string_format


    for cap in caps:
        cap.image = conf.base_url_generate('/' + cap.image)
        res['results'].append(cap.get_dict_repr())

    return res


@app.get('/api/v1/brands/{brand_id}/')
async def get_brand(brand_id: int = 1):
    if brand_id <= 0:
        return None

    brand = get_caps_brand_db_request(brand_id)

    if len(brand) != 1:
        return None

    brand: CapsBrand = brand[0]
    brand.image = conf.base_url_generate('/' + brand.image)
    res = brand.get_dict_repr()

    return res

@app.get('/media/{directory}/{name}/')
async def get_media_cap(directory, name):
    image_path = os.path.join(directory, name)
    return FileResponse(os.path.join(conf.STATIC_IMAGE_DIR, image_path))

# https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#oauth2passwordrequestform
from typing import Optional
from fastapi import Header
@app.get('/api/v1/check-token/')
async def check_token(fuckingshit: Optional[str] = Header(None)):
    return {"Authorization": fuckingshit}