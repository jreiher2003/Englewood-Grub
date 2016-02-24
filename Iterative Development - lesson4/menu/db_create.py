from app import db
from app.models import Place

def create_places():
	place1 = Place(name='Coffee Cafe')
	db.session.add(place1)
	place2 = Place(name='Jamacian Me Crazy')
	db.session.add(place2)
	place3 = Place(name='Wack Arnolds')
	db.session.add(place3)
	place4 = Place(name='Jack n Crack')
	db.session.add(place4)
	place5 = Place(name='Egg Morning')
	db.session.add(place5)
	db.session.commit()
	print "just created the restaurant table"


if __name__ == '__main__':
	db.drop_all()
	print "Just Dropped all tables"
	db.create_all()
	create_places()
