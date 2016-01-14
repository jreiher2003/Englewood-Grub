import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, Date
from sqlalchemy.orm import relationship, backref 
from sqlalchemy import create_engine 

Base = declarative_base() 

class Shelter(Base):
	__tablename__ = 'shelter'
	id = Column(Integer, Sequence('shelter_id_seq'), primary_key=True)
	name = Column(String(80), nullable=False)
	address = Column(String(256))
	city = Column(String(80))
	state = Column(String(40))
	zipCode = Column(String(10))
	website = Column(String)

	def __repr__(self):
		return "<Shelter(name='%s', address='%s', city='%s', state='%s', email='%s', id='%s')>" \
		% (self.name, self.address, self.city, self.state, self.email, self.id)

class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	gender = Column(String(10), nullable=False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	weight = Column(Integer)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship("Shelter", backref=backref('puppy', order_by=id))

	def __repr__(self):
		return "<Puppy(name='%s', dob='%s',breed='%s',gender='%s',weight='%s',shelter_id='%s',shelter='%s')>"\
				% (name,dob,breed,gender,weight,shelter_id,shelter)

class Profile(Base):
	__tablename__ = 'profile'
	id = Column(Integer, primary_key=True)
	photo = Column(String)
	description = Column(String(300))
	specialNeeds = Column(String(300))
	puppy_id = Column(Integer, ForeignKey('puppy.id'))



engine = create_engine('sqlite:///puppyshelter.db', echo=True)
Base.metadata.create_all(engine)