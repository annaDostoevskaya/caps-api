from api.models import  Cap
from api import DBSession


def fill_db_cap_from_dict(dict_repr_cap: dict):
    assert (len(dict_repr_cap['size']) == 4), 'len(size) my be 4'

    c = Cap()

    c.name =        dict_repr_cap['name']
    c.image =       dict_repr_cap['image']
    c.description = dict_repr_cap['description']
    c.price =       dict_repr_cap['price']
    c.new_price =   dict_repr_cap['new_price']
    c.brand =       dict_repr_cap['brand']
    c.size_1 =      dict_repr_cap['size'][0]
    c.size_2 =      dict_repr_cap['size'][1]
    c.size_3 =      dict_repr_cap['size'][2]
    c.size_4 =      dict_repr_cap['size'][3]

    with DBSession() as sess:
        sess.add(c)
        sess.commit()
        sess.close()


def print_all_database_cap_table():
    with DBSession() as sess:
        all_caps = sess.query(Cap).filter_by().all()
        sess.close()

    for cap in all_caps:
        cap.display()