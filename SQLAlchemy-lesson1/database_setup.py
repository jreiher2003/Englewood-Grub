import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship 

from sqlalchemy import create_engine

Base = declarative_base()

#### class code goes between configuration code ####
class Place(Base):
	__tablename__ = 'place'
	name = Column(String(80), nullable=False)
	location = Column(String(250))
	category = Column(String(100))
	id =  Column(Integer, primary_key=True)

class MenuItem(Base):
	__tablename__ = 'menu_item'
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	section = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	place_id = Column(Integer, ForeignKey('place.id'))
	place = relationship(Place)


##### insert at end of file ########
engine = create_engine('sqlite:///grub.db')

Base.metadata.create_all(engine)
