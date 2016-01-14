from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine)
session = DBSession()


# 1. Query all of the puppies and return 
# the results in ascending alphabetical order
def allPuppies():
	puppies = session.query(Puppy).order_by(Puppy.name.asc()).all()
	for puppy in puppies:
		print puppy.name
		print puppy.dateOfBirth

def youngPups():
	puppies = session.query(Puppy).order_by(Puppy.dateOfBirth.desc()).all()
	for puppy in puppies:
		before6mo = datetime.date(2015,03,05)
		if puppy.dateOfBirth >= before6mo:
			print puppy.name
			print puppy.dateOfBirth
			print "\n"

def pupsWeight():
	puppies = session.query(Puppy).order_by(Puppy.weight.asc()).all()
	for puppy in puppies:
		print puppy.name
		print puppy.weight
		print "\n"

def pupsShelter():
	# puppies = session.query(Shelter).order_by(Puppy.shelter_id).all()
	# for pup in puppies:
	# 	print pup.shelter.name
	# 	print pup.name
	# 	print "\n"
	q = session.query(Shelter).join(Puppy, Shelter.id == Puppy.shelter_id).order_by(Shelter.name)
	print q


if __name__ == '__main__':
	# allPuppies()
	# youngPups()
	# pupsWeight()
	pupsShelter()