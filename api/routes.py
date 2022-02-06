import os

from api import app, conf, DBSession
from api.models import Cap, CapsBrand
from fastapi.responses import FileResponse

def calc_pointer_id(page, pg_size):
    return ((page - 1) * pg_size) + 1

@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/')
async def get_caps(page=1, pg_size=5):
    ## TODO(annad): Change moke object to data from DB.
    res = {}

    ## TODO(annad): How can this be done correctly?
    pointer_id = calc_pointer_id(page, pg_size)

    with DBSession() as sess:
        caps = sess.query(Cap).filter(Cap.id >= pointer_id, Cap.id < pointer_id + pg_size).all()

    res = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 1,
                "name": "New era",
                "imege": "http://80.87.198.187:8002/media/caps/boston-celtics-basic-green-59fifty-fitted-new-era.png",
                "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap имеет вышитый логотип Warriors на передних панелях, а также надпись World Champs с дополнительными командными нашивками и вышивкой по всей остальной части короны. Дополнительные детали включают цветной логотип NBA команды сзади и серый нижний слой.",
                "price": 23000.0,
                "created": "2022-02-02T11:31:51.079250Z",
                "updated": "2022-02-02T11:31:51.079287Z",
                "brand": 1,
                "size": [
                    2,
                    3,
                    4
                ]
            },
            {
                "id": 2,
                "name": "Nike",
                "imege": "http://80.87.198.187:8002/media/caps/boston-celtics-basic-green-59fifty-fitted-new-era_CPHTCvm.png",
                "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap имеет вышитый логотип Warriors на передних панелях, а также надпись World Champs с дополнительными командными нашивками и вышивкой по всей остальной части короны. Дополнительные детали включают цветной логотип NBA команды сзади и серый нижний слой.",
                "price": 3000.0,
                "created": "2022-02-02T11:32:18.377480Z",
                "updated": "2022-02-02T11:32:18.377523Z",
                "brand": 1,
                "size": [
                    1,
                    2,
                    3
                ]
            }
        ]
    }
    return res

@app.get('/api/v1/brands/{brand_id}')
async def get_brand(brand_id):
    ## TODO(anand): Create real table of brands.
    table_brands = {
        '1': ["Golden State Warriors", "French Fries Series"],
        '2': ["San Francisco Baseball",],
    }
    return table_brands[brand_id]

'''
LINK FOR TEST: 
http://192.168.2.136:8000/media/caps/20220206172612100.jpg
'''
@app.get('/media/{directory}/{name}')
async def get_media_cap(directory, name):
    image_path = os.path.join(directory, name)
    return FileResponse(os.path.join(conf.STATIC_IMAGE_DIR, image_path))