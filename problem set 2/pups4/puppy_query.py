from models import *
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def query_all():
	all_puppies = session.query(Puppy).order_by(Puppy.name)
	for puppy in all_puppies:
		print puppy.name

def puppy_age():
	p_age = session.query(Puppy).\
		filter(Puppy.dateOfBirth.between('2015-05-11', '2015-11-11')).\
		order_by(Puppy.dateOfBirth.desc())
	for age in p_age:
		print age.name, age.dateOfBirth

def puppy_weight():
	weight = session.query(Puppy).filter(Puppy.weight).order_by(Puppy.weight.asc())
	for w in weight:
		print w.name, w.weight

def shelters_where_puppies_are():
	shel = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).order_by(Shelter.name)
	for s, p in shel:
		print s.name, p.name

def count_puppys_in_each_shelter():
	first = session.query(Shelter).filter_by(id = 1).one()
	one = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==1).count()
	print first.name,one
	first.current_occupancy = one
	session.add(first)
	session.commit()

	second = session.query(Shelter).filter_by(id = 2).one()
	two = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==2).count()
	print second.name, two
	second.current_occupancy = two
	session.add(second)
	session.commit()

	third = session.query(Shelter).filter_by(id = 3).one()
	three = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==3).count()
	print third.name, three
	third.current_occupancy = three
	session.add(third)
	session.commit()

	fourth = session.query(Shelter).filter_by(id = 4).one()
	four = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==4).count()
	print fourth.name,four
	fourth.current_occupancy = four
	session.add(fourth)
	session.commit()

	fifth = session.query(Shelter).filter_by(id = 5).one()
	five = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==5).count()
	print fifth.name,five
	fifth.current_occupancy = five
	session.add(fifth)
	session.commit()

def checkPuppyIn(puppy):
	shel = 1
	shelter = session.query(Shelter).filter_by(id = shel).one()
	if shelter.maximum_capacity > shelter.current_occupancy:
		session.add(puppy)
		session.commit()
	elif:
		shel += 1
	else:
		"We need to add more shelters"

def adoptAPuppy():
	


if __name__ == '__main__':
	# query_all()
	# puppy_age()
	# puppy_weight()
	# shelters_where_puppies_are()
	count_puppys_in_each_shelter()
