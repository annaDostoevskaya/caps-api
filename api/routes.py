import os

from api import app, conf, DBSession
from api.models import Cap, CapsBrand, User
from api.paging import Page

from fastapi.responses import FileResponse, RedirectResponse

import httpx
import json

# TODO(annad): All the same, it is worth making requests in a separate file
async def get_caps_brand_db_request(brand_id: int) -> list[CapsBrand]:
    with DBSession() as sess:
        brand = sess.query(CapsBrand).filter(CapsBrand.id == brand_id).all()
    return brand


async def get_caps_db_request(pg: Page) -> list[Cap]:
    with DBSession() as sess:
        caps = sess.query(Cap).filter(Cap.id >= pg.start_id(), Cap.id < pg.end_id()).all()
    return caps

async def get_user_db_request(user_id: int) -> list[User]:
    with DBSession() as sess:
        users = sess.query(User).filter(User.id == user_id).all()
    return users

async def post_user_db_request(user: User):
    with DBSession() as sess:
        sess.add(user)
        sess.commit()



@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')

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

async def add_to_database(user_id, email, access_token):
    client = httpx.AsyncClient()
    req = await client.get(f'https://api.vk.com/method/users.get?user_id={user_id}&'
                           f'access_token={access_token}&'
                           f'fields=uid,photo_max_orig&'
                           f'v=5.131')
    jreq: dict = json.loads(req.text)
    if jreq.setdefault('error', 0):
        return jreq

    u = User()
    u.name = jreq['response'][0]['first_name'] + ' ' + jreq['response'][0]['last_name']
    u.email = email
    u.vk_id = jreq['response'][0]['id']
    u.avatar = jreq['response'][0]['photo_max_orig']
    u.token = access_token

    await post_user_db_request(u)

    return u


## http://192.168.2.136:8080/CLIENT_gen_token
@app.get('/vkauth')
async def vkauth(code: str = None, error: str = None):
    client = httpx.AsyncClient()
    req = await client.get(f'https://oauth.vk.com/access_token?client_id={conf.VKAPP_ID}&'
                           f'client_secret={conf.VKAPP_SERCRET_KEY}&'
                           f'code={code}&'
                           f'redirect_uri={conf.base_url_generate(conf.VKREDIRECT_URL)}')
    req.raise_for_status()      # NOTE(annad): I still doubt it's possible.

    jreq: dict = json.loads(req.text)
    if jreq.setdefault('error', 0):
        return jreq

    access_token = jreq['access_token']
    user_id      = jreq['user_id']
    email        = jreq['email']
    res = await add_to_database(user_id, email, access_token)

    return res


@app.get('/get_vk_user/{user_id}')
async def get_vk_user(user_id: int):
    '''
    TODO(annad): REMOVE! NO DEPLOY IT!
    TODO(annad): REMOVE! NO DEPLOY IT!
    TODO(annad): REMOVE! NO DEPLOY IT!
    WARNING!!! WE SHOULD NOT TRANSFER THE TOKEN IN THIS WAY!
    THIS COMPLETES THE SAFETY OF USERS. THE FUNCTION IS
    WRITTEN EXCLUSIVELY FOR THE MODE OF
    DEBUGING AND CHECKING THE PERFORMANCE OF THE DATABASE!!!
    '''
    if user_id <= 0:
        return None

    users = await get_user_db_request(user_id)

    if len(users) != 1:
        return None

    user: User = users[0]
    res = user.get_dict_repr()

    return res