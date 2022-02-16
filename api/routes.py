import os

from api import app, conf, DBSession
from api.models import Cap, CapsBrand
from api.paging import Page

from fastapi.responses import FileResponse, RedirectResponse

import httpx
import json

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

async def get_caps_brand_db_request(brand_id: int) -> list[CapsBrand]:
    with DBSession() as sess:
        brand = sess.query(CapsBrand).filter(CapsBrand.id == brand_id).all()
    return brand


async def get_caps_db_request(pg: Page) -> list[Cap]:
    with DBSession() as sess:
        caps = sess.query(Cap).filter(Cap.id >= pg.start_id(), Cap.id < pg.end_id()).all()
    return caps


## TODO(annad): Host it on HEROKU and check!
# @app.get('/favicon.ico', include_in_schema=False)
# async def favicon():
#     return FileResponse('favicon.ico')

@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/{cap_id}')
async def get_cap_by_id(cap_id: int):
    # TODO(annad): Rewrite!
    # NOTE(annad): Mb made specificly request for ONE cap?..
    res = RedirectResponse(url=f'/api/v1/caps/?number_page={cap_id}&pg_size=1')
    return res

@app.get('/api/v1/caps/')
async def get_caps(number_page: int = 1, pg_size: int = 5):
    if (number_page <= 0) or (pg_size <= 0):
        return None

    pg = Page(number_page, pg_size, '?number_page={}&pg_size={}')
    caps: list[Cap] = await get_caps_db_request(pg)

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
        cap.image = conf.base_url_generate('/' + conf.IMAGE_DIR + cap.image)
        res['results'].append(cap.get_dict_repr())

    return res

## TODO(annad): Add method for get more brands. Analog @app.get('/api/v1/caps/')!
@app.get('/api/v1/brands/{brand_id}/')
async def get_brand(brand_id: int = 1):
    if brand_id <= 0:
        return None

    brand = await get_caps_brand_db_request(brand_id)

    if len(brand) != 1:
        return None

    brand: CapsBrand = brand[0]
    brand.image = conf.base_url_generate('/' + conf.IMAGE_DIR + brand.image)
    res = brand.get_dict_repr()

    return res

@app.get('/media/{file_path:path}')
async def get_media_cap(file_path):
    return FileResponse(os.path.join(conf.IMAGE_DIR, file_path))

## TODO(annad): Move to dev/
@app.get('/CLIENT_gen_token')
async def gen_token():
    vk_access_email = 1 << 22
    return RedirectResponse(f'https://oauth.vk.com/authorize?client_id={conf.VKAPP_ID}&'
                            f'display=page&redirect_uri={conf.base_url_generate(conf.VKREDIRECT_URL)}&'
                            f'scope={vk_access_email}&'
                            f'response_type=code')

## TODO(annad): Move to dev/
@app.get('/CLIENT_users_get')
async def users_get():
    access_token = '0'
    user_id = '0'

    client = httpx.AsyncClient()
    req = await client.get(f'https://api.vk.com/method/users.get?user_id={user_id}&'
                           f'access_token={access_token}&'
                           f'fields=uid&'
                           f'v=5.131')

    if req.status_code != 200: ## TODO(annad): Write normal check of status_code and request.
        return req.status_code

    jreq = json.loads(req.text)
    return jreq

@app.get('/vkauth')
async def vkauth(code: str = None, error: str = None):
    ## TODO(annad): Refactoring!
    client = httpx.AsyncClient()

    if code is None:
        return {'error_code': error}

    req = await client.get(f'https://oauth.vk.com/access_token?client_id={conf.VKAPP_ID}&'
                           f'client_secret={conf.VKAPP_SERCRET_KEY}&'
                           f'code={code}&'
                           f'redirect_uri={conf.base_url_generate(conf.VKREDIRECT_URL)}')

    if req.status_code != 200: ## TODO(annad): Write normal check of status_code and request.
        return req.status_code

    ## TODO(annad): Add DATABASE table.
    jreq = json.loads(req.text)
    access_token = jreq['access_token']
    user_id      = jreq['user_id']
    email        = jreq['email']

    if access_token is None:
        return {'error_token': error} ## TODO(annad): More information Errors feedback.
    else:
        return {
            'user_id': user_id,
            'email': email,
            'access_token': access_token
        }