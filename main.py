# uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models, Base, DBEngine
from uvicorn import run

from dev import dbutils

# from api import DBSession
# from api.models import Cap
#
# s: Session  = DBSession()
# get = s.query(Cap).filter_by().all()
# s.close()


if __name__ == '__main__':

    Base.metadata.create_all(DBEngine)

    dbutils.fill_db_cap_from_dict({
            "name": "San Francisco Baseball",
            "image": "media/caps/cap4.png",
            "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted"
                           " Cap имеет вышитый логотип Warriors на передних панелях, "
                           "а также надпись World Champs с дополнительными командными "
                           "нашивками и вышивкой по всей остальной части короны. "
                           "Дополнительные детали включают цветной логотип NBA "
                           "команды сзади и серый нижний слой.",
            "price": 3800.0,
            "new_price": 0.0,
            "brand": 2,
            "size" : [0, 1, 2, 3]})

    dbutils.fill_db_cap_from_dict({
            "name": "Golden State Warriors Icon 59FIFTY Fitted Cap",
            "image": "media/caps/cap2.png",
            "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap "
                           "имеет вышитый логотип Warriors на передних панелях, "
                           "а также надпись World Champs с дополнительными командными "
                           "нашивками и вышивкой по всей остальной части короны. "
                           "Дополнительные детали включают цветной логотип NBA "
                           "команды сзади и серый нижний слой.",
            "price": 2500.0,
            "new_price": 0.0,
            "brand": 1,
            "size": [1, 2, 3, 4]})

    dbutils.fill_db_cap_from_dict({
            "name": "French Fries Series",
            "image": "media/caps/cap1.png",
            "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted "
                           "Cap имеет вышитый логотип Warriors на передних панелях, "
                           "а также надпись World Champs с дополнительными командными "
                           "нашивками и вышивкой по всей остальной части короны. "
                           "Дополнительные детали включают цветной логотип NBA "
                           "команды сзади и серый нижний слой.",
            "price": 4500.0,
            "new_price": 0.0,
            "brand": 1,
            "size": [1, 2, 0, 0]})

    # for i in get:
    #     i.display()

    # run(app, host='192.168.2.136', port=8000)
