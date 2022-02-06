## NOTE(annad): This file only exists because I don't have a ready-made backend in order to populate the database
## through the admin panel for example. Maybe later I will write it.
## But right now I'm working on API, so it's not possible.

from os import path

from api.models import  Cap, CapsBrand
from api import DBSession, Base, DBEngine

from dev import db_dict_repr

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

    assert (len(dict_repr_cap['size']) == 4), 'len(size) must be 4'

    c: Cap = Cap()

    with DBSession() as sess:
        cbs: CapsBrand = sess.query(CapsBrand).filter_by(id=dict_repr_cap['caps_brand_id']).all()
        assert len(cbs) == 1, 'This brand_index is not in the database.'
        cb = cbs[0]

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
    assert path.isfile('app.db'), 'Database not found'

    with DBSession() as sess:
        all_caps = sess.query(Cap).filter_by().all()
        sess.close()

    for cap in all_caps:
        cap.display()

def print_all_database_caps_brand_table():
    assert path.isfile('app.db')

    with DBSession() as sess:
        all_caps_brands = sess.query(CapsBrand).filter_by().all()
        sess.close()

    for caps_brand in all_caps_brands:
        caps_brand.display()


def fill():
    assert (not path.isfile('app.db')), 'Database found. Database must be empty. Delete the database'

    ## Cap's Brands Table Fill.
    fill_db_caps_brand_from_dict(db_dict_repr.cap_brand_id_1)
    fill_db_caps_brand_from_dict(db_dict_repr.cap_brand_id_2)
    fill_db_caps_brand_from_dict(db_dict_repr.cap_brand_id_3)
    fill_db_caps_brand_from_dict(db_dict_repr.cap_brand_id_4)
    fill_db_caps_brand_from_dict(db_dict_repr.cap_brand_id_5)

    ## Caps Table Fill.
    fill_db_cap_from_dict(db_dict_repr.cap_id_1)
    fill_db_cap_from_dict(db_dict_repr.cap_id_2)
    fill_db_cap_from_dict(db_dict_repr.cap_id_3)
    fill_db_cap_from_dict(db_dict_repr.cap_id_4)
    fill_db_cap_from_dict(db_dict_repr.cap_id_5)
    fill_db_cap_from_dict(db_dict_repr.cap_id_6)
    fill_db_cap_from_dict(db_dict_repr.cap_id_7)
    fill_db_cap_from_dict(db_dict_repr.cap_id_8)
    fill_db_cap_from_dict(db_dict_repr.cap_id_9)
    fill_db_cap_from_dict(db_dict_repr.cap_id_10)
