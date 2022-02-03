# uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models, Base, DBEngine
from uvicorn import run

# TODO(annad): write utils for fill database.
'''
# for fill db.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from api import DBSession
from api.models import Cap

Base.metadata.create_all(DBEngine)

s: Session  = DBSession()
c = Cap()
c.name = "Golden State Warriors Icon 59FIFTY Fitted Cap"
c.image = "http://192.168.2.136:8000/media/caps/cap2.png"
c.description = "Кепка Golden State Warriors Icon 59FIFTY Fitted Cap " \
                "имеет вышитый логотип Warriors на передних панелях, " \
                "а также надпись World Champs с дополнительными командными " \
                "нашивками и вышивкой по всей остальной части короны. " \
                "Дополнительные детали включают цветной логотип NBA команды " \
                "сзади и серый нижний слой."
c.price = 2500.0
c.new_price = 0.0
c.brand = 1
c.size = [1, 2, 3, 4, ]

s.add(c)
s.commit()
s.close()
'''

'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from api import DBSession
from api.models import Cap

Base.metadata.create_all(DBEngine)
s: Session  = DBSession()
get = s.query(Cap).filter_by(name="Golden State Warriors Icon 59FIFTY Fitted Cap").all()
s.close()
print("\n\n\n")
print(get)
print("\n\n\n")
'''

if __name__ == '__main__':
    run(app, host='192.168.2.136', port=8000)
