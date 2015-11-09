from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Place, MenuItem 

engine = create_engine('sqlite:///grub.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

myFirstSpot = Place(name="Pizza Palace")
session.add(myFirstSpot)
session.commit()
allPlaces = session.query(Place).all()

for place in allPlaces:
	print place.name