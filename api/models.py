from api import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text, Date, DateTime, ARRAY
from sqlalchemy.ext.declarative import declarative_base


class Cap(Base):
    __tablename__ = 'caps'
    __tableargs__ = {
        'comment': '''  Storage ONE CAP. Image representation, description, 
price, sell price, date of create and update, brand in name and index, size.'''
    }

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String(32))
    image = Column(Text)
    description = Column(Text)
    price = Column(Float, index=True)
    created = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    updated = Column(DateTime(timezone=True), index=True, default=datetime.utcnow)
    new_price = Column(Float, index=True)
    brand = Column(Integer, index=True)
    size_1 = Column(Integer)
    size_2 = Column(Integer)
    size_3 = Column(Integer)
    size_4 = Column(Integer)

    def __repr__(self):
        return "<Caps id: {id}, name: {name}>".format(id = self.id, name=self.name)