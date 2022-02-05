# uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models
from uvicorn import run

from dev import dbutils

if __name__ == '__main__':
    dbutils.fill_db_caps_brand_from_dict({
        'name': 'Andy Capp\'s',
        'description': 'Andy Capp\'s is an American brand of flavored '
                       'corn and potato snack made to look like French fries. '
                       'The product was created in 1971 by '
                       'Goodmark Foods, Inc., which licensed the name and '
                       'likeness of the comic strip character Andy Capp from '
                       'Publishers-Hall Syndicate. Until recent years the strip '
                       'was featured on the back of packages. '
                       'In 1998 Goodmark Foods was acquired by ConAgra Foods, '
                       'which manufactures and distributes the product to this day.',
        'image': 'media/caps_brands/20220206121512100.png'
    })

    dbutils.fill_db_cap_from_dict({
        "name": "French Fries Series",
        "image": "media/caps/20220203115901001.svg",
        "description": "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap "
                       "имеет вышитый логотип Warriors на передних панелях, "
                       "а также надпись World Champs с дополнительными командными "
                       "нашивками и вышивкой по всей остальной части короны. "
                       "Дополнительные детали включают цветной логотип "
                       "NBA команды сзади и серый нижний слой.",
        "price": 4500.0,
        "new_price": 0.0,
        "brand": 1,
        "size": [1, 2, 0, 0]
    })

    dbutils.print_all_database_cap_table()

    # run(app, host='192.168.2.136', port=8000)

