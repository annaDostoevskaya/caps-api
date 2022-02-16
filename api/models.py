from api import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql


class CapsBrand(Base):
    __tablename__ = 'cap_brands'
    __tableargs__ = {
        'comment': 'Storage Cap\'s brand.'
                   'It\'s relationshep from Cap.brand, '
                   'where brand is ID in this table.'
    }

    dict_repr = None

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(64))
    description = Column(Text)
    image = Column(String(128))
    # caps = relationship("Cap", back_populates="child")

    def __repr__(self):
        return '<CapsBrand id: {id}, name: {name}>'.format(id=self.id, name=self.name)

    def get_dict_repr(self):
        if self.dict_repr is None:
            self.dict_repr = {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'image': self.image
            }

        return self.dict_repr

    def display(self):
        str_from_dict = ('id: {id}\n'
                         'name: {name}\n'
                         'description: {description}\n'
                         'image: {image}\n'
        ).format_map(
            self.get_dict_repr()
        )

        print(str_from_dict)

class Cap(Base):
    __tablename__ = 'caps'
    __tableargs__ = {
        'comment': 'Storage ONE CAP. Image representation, description, '
                   'price, sell price, date of create and update, '
                   'brand in name and index, size.'
    }
    dict_repr = None # Cache.

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(64))
    image = Column(String(128))
    description = Column(Text)
    price = Column(Float, index=True)
    created = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    updated = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    new_price = Column(Float, index=True)

    # Relastionship with CapBrand table.
    caps_brand_id = Column(Integer, ForeignKey('cap_brands.id'))
    caps_brand = relationship('CapsBrand', backref='parents', lazy='joined')
    # caps_brand = relationship('CapBrand', back_populates='parents')
    size = Column(postgresql.ARRAY(postgresql.INTEGER))

    def __repr__(self):
        return "<Caps id: {id}, name: {name}>".format(id=self.id, name=self.name)

    def get_dict_repr(self):
        if self.dict_repr is None:
            self.dict_repr = {
                "id": self.id,
                "name": self.name,
                "image": self.image,
                "description": self.description,
                "price": self.price,
                "created": self.created,
                "updated": self.updated,
                "new_price": self.new_price,
                "brand": self.caps_brand_id, ## Change from self.brand(!)
                "size": self.size
            }

        return self.dict_repr

    def display(self):
        str_repr_from_dict = ('id: {id};\n'
                              'name: {name};\n'
                              'image: {image};\n'
                              'description: \"{description}\";\n'
                              'price: {price};\n'
                              'created: {created};\n'
                              'updated: {updated};\n'
                              'new_price: {new_price};\n'
                              'brand index: {brand};\n'
                              'size: {size};\n'
        ).format_map(
            self.get_dict_repr()
        )

        print(str_repr_from_dict)