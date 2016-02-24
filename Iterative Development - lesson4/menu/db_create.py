from app import db
from app.models import Place

def create_places():
	place1 = Place(name='Coffee Cafe')
	db.session.add(place1)
	db.session.commit()
	print "just created the restaurant table"


if __name__ == '__main__':
	# db.drop_all()
	# print "Just Dropped all tables"
	db.create_all()
	create_places()
