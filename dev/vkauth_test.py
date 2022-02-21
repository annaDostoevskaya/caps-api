from api import app
import httpx
import json

from fastapi.responses import RedirectResponse
from api import conf


@app.get('/CLIENT_gen_token')
async def gen_token():
    vk_access_email = 1 << 22
    vk_access_token_forever = 1 << 16
    return RedirectResponse(f'https://oauth.vk.com/authorize?client_id={conf.VKAPP_ID}&'
                            f'display=page&redirect_uri={conf.base_url_generate(conf.VKREDIRECT_URL)}&'
                            f'scope={vk_access_email+vk_access_token_forever}&'
                            f'response_type=code')


@app.get('/CLIENT_users_get')
async def users_get():
    access_token = '0'
    user_id = '0'

    client = httpx.AsyncClient()
    req = await client.get(f'https://api.vk.com/method/users.get?user_id={user_id}&'
                           f'access_token={access_token}&'
                           f'fields=uid&'
                           f'v=5.131')

    jreq = json.loads(req.text)
    return jreq