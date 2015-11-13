from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
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

class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	gender = Column(String(6), nullable = False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	weight = Column(Integer)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	profile = relationship("Profile", uselist=False, backref="puppy")
	adopter_id = relationship("Adopter", secondary='puppy_adopter_link', backref="puppy")

engine = create_engine("sqlite:///puppyshelter.db")

Base.metadata.create_all(engine)
