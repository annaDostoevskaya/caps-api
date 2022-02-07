from api import DBSession
from api.models import CapsBrand

def get_caps_brand_db_request(brand_id: int) -> list[CapsBrand]:
    with DBSession() as sess:
        brand = sess.query(CapsBrand).filter(CapsBrand.id == brand_id).all()
    return brand