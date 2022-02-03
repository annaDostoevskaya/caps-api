from api import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text, Date, DateTime
from sqlalchemy.types import ARRAY
from sqlalchemy.ext.declarative import declarative_base


class Cap(Base):
    __tablename__ = 'caps'
    __tableargs__ = {
        'comment': 'Storage ONE CAP. Image representation, description, '
                   'price, sell price, date of create and update, '
                   'brand in name and index, size.'
    }
    dict_repr = None # Cache.

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(32))
    image = Column(Text)
    description = Column(Text)
    price = Column(Float, index=True)
    created = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    updated = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    new_price = Column(Float, index=True)
    brand = Column(Integer, index=True)

    # TODO(annad): find method use array in SQLite.
    # Plugins? Or...
    size_1 = Column(Integer, default=0)
    size_2 = Column(Integer, default=0)
    size_3 = Column(Integer, default=0)
    size_4 = Column(Integer, default=0)

    def __repr__(self):
        return "<Caps id: {id}, name: {name}>".format(id = self.id, name=self.name)

    def get_dict_repr(self):
        if not (self.dict_repr is None):
            return self.dict_repr
        else:
            self.dict_repr = {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
            "price": self.price,
            "created": self.created,
            "updated": self.updated,
            "new_price": self.new_price,
            "brand": self.brand,
            "size_1": self.size_1,
            "size_2": self.size_2,
            "size_3": self.size_3,
            "size_4": self.size_4,
        }
            return self.dict_repr

    def display(self):
        str_repr_from_dict = ('id: {id};\nname: {name};\nimage: {image};\ndescription: \"{description}\";\n'
                              'price: {price};\ncreated: {created};\nupdated: {updated};\nnew_price: {new_price};\nbrand index: {brand};\n'
                              'size: {size_1}, {size_2}, {size_3}, {size_4};\n').format_map(self.get_dict_repr())
        print(str_repr_from_dict)