# uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models
from uvicorn import run

from dev import dbutils

if __name__ == '__main__':
    # dbutils.fill_db_cap_from_dict({
    #     "name": "French Fries Series",
    #     "image": "media/caps/20220203115901001.svg",
    #     "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap "
    #                    "имеет вышитый логотип Warriors на передних панелях, "
    #                    "а также надпись World Champs с дополнительными командными "
    #                    "нашивками и вышивкой по всей остальной части короны. "
    #                    "Дополнительные детали включают цветной логотип "
    #                    "NBA команды сзади и серый нижний слой.",
    #     "price": 4500.0,
    #     "new_price": 0.0,
    #     "brand": 1,
    #     "size": [1, 2, 0, 0]
    # })



    run(app, host='192.168.2.136', port=8000)

