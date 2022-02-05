import os

from api import app, conf, DBSession
from fastapi.responses import FileResponse

@app.get('/')
async def root():
    return {'name_api': 'CapsApi'}

@app.get('/api/v1/caps/')
async def get_caps():
    ## TODO(anand): Create real table of brands.
    table_brands = {
        1: ("Golden State Warriors", "French Fries Series",),
        2: ("San Francisco Baseball",),
    }

    ## TODO(annad): Change moke object to data from DB.
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

'''
LINK FOR TEST: 
http://192.168.2.136:8000/media/caps/20220203115901001.svg
'''
@app.get('/media/{directory}/{name}')
def get_media_cap(directory, name):
    # TODO(annad): Download all images caps from site.
    image_path = os.path.join(directory, name)
    return FileResponse(os.path.join(conf.STATIC_IMAGE_DIR, image_path))