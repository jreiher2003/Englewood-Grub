from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine)
session = DBSession()


# 1. Query all of the puppies and return 
# the results in ascending alphabetical order
puppies = session.query(Puppy).order_by(Puppy.name.asc()).all()
for puppy in puppies:
	print puppy.name
	print puppy.dateOfBirth