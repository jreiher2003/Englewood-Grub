import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship 
from sqlalchemy import create_engine 

Base = declarative_base()

class Shelter(Base):
	"""This is for puppy shelter infomation acrossed the US"""

	__tablename__ = 'shelter'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String(40))
	zipCode = Column(String(10))
	website = Column(String)

class Puppy(Base):
	"""names of puppys in by shelter location"""
	__tablename__ = "puppy"

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	gender = Column(String(16), nullable=False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	weight = Column(Numeric(10))

class Adoption(Base):
	""" people who will adopt """
	__tablename__ = "adopt"
	id = Column(Integer,primary_key=True)
	name = Column(String(250), nullable=False)

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)