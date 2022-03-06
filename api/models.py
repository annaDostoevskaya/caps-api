from api import Base, DBEngine

from datetime import datetime
from fastapi.encoders import jsonable_encoder

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

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(64))
    description = Column(Text)
    image = Column(String(128))
    # caps = relationship("Cap", back_populates="child")

    def __repr__(self):
        return '<CapsBrand id: {id}, name: {name}>'.format(id=self.id, name=self.name)

    def get_dict_repr(self):
        return jsonable_encoder(self)

    def display(self):
        print(self.get_dict_repr())


class Cap(Base):
    __tablename__ = 'caps'
    __tableargs__ = {
        'comment': 'Storage ONE CAP. Image representation, description, '
                   'price, sell price, date of create and update, '
                   'brand in name and index, size.'
    }

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(64))
    image = Column(String(128))
    description = Column(Text)
    price = Column(Float, index=True)
    created = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    updated = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    new_price = Column(Float, index=True)

    # Relastionship with CapBrand table.
    # TODO(annad): https://vk.com/wall-201010673_1026
    caps_brand_id = Column(Integer, ForeignKey('cap_brands.id'))
    caps_brand = relationship('CapsBrand', backref='parents', lazy='joined')
    # caps_brand = relationship('CapBrand', back_populates='parents')
    size = Column(postgresql.ARRAY(postgresql.INTEGER))

    def __repr__(self):
        return "<Caps id: {id}, name: {name}>".format(id=self.id, name=self.name)

    def get_dict_repr(self):
        res: dict = jsonable_encoder(self)
        res.pop('caps_brand', None)
        return res

    def display(self):
        print(self.get_dict_repr())


class User(Base):
    __tablename__ = 'User'
    __tableargs = {
        'comment': 'The table stores names, e-mails, vk-id, avatar and tokens of users'
    }
    ## TODO(annad): More fields? datatime creating? or...?
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(64))
    email = Column(String(254), index=True)
    vk_id = Column(Integer, index=True)
    avatar = Column(String(256))
    token = Column(String(256)) ## we are don't storage token, because
                                ## it check in vk_app;

    def __repr__(self):
        return f'<VKUser id: {self.id}, vk-id: {self.vk_id}>'

    def get_dict_repr(self):
        return jsonable_encoder(self)

    def display(self):
        print(self.get_dict_repr())

## NOTE(annad): We must check how work with this.
# Base.metadata.create_all(DBEngine, checkfirst=True)