from os import path

from api.models import  Cap, CapsBrand
from api import DBSession, Base, DBEngine


def fill_db_caps_brand_from_dict(dict_repr_caps_brand: dict):
    Base.metadata.create_all(DBEngine, checkfirst=True)

    cb: CapsBrand = CapsBrand()
    cb.name =           dict_repr_caps_brand['name']
    cb.description =    dict_repr_caps_brand['description']
    cb.image =          dict_repr_caps_brand['image']

    with DBSession() as sess:
        sess.add(cb)
        sess.commit()
        sess.close()


def fill_db_cap_from_dict(dict_repr_cap: dict):
    Base.metadata.create_all(DBEngine, checkfirst=True)

    assert (len(dict_repr_cap['size']) == 4), 'len(size) my be 4'

    c: Cap = Cap()

    with DBSession() as sess:
        cb: CapsBrand = sess.query(CapsBrand).filter_by(id=dict_repr_cap['brand']).all()[0]

        c.name =            dict_repr_cap['name']
        c.image =           dict_repr_cap['image']
        c.description =     dict_repr_cap['description']
        c.price =           dict_repr_cap['price']
        c.new_price =       dict_repr_cap['new_price']
        c.caps_brand_id =   cb.id
        c.size_1 =          dict_repr_cap['size'][0]
        c.size_2 =          dict_repr_cap['size'][1]
        c.size_3 =          dict_repr_cap['size'][2]
        c.size_4 =          dict_repr_cap['size'][3]

        sess.add(c)
        sess.commit()
        sess.close()


def print_all_database_cap_table():
    assert path.isfile('app.db')

    with DBSession() as sess:
        all_caps = sess.query(Cap).filter_by().all()
        sess.close()

    for cap in all_caps:
        cap.display()
        print(cap.caps_brand)