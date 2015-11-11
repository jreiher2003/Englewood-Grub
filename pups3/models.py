from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	address = Column(String(250))
	city = Column(String(40))
	state = Column(String(20))
	zipCode = Column(String(10))
	website = Column(String)


engine = create_engine("sqlite:///puppyshelter.db")

Base.metadata.create_all(engine)

