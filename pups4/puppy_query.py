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
	one = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==1).count()
	print one
	two = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==2).count()
	print two
	three = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==3).count()
	print three
	four = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==4).count()
	print four
	five = session.query(Shelter,Puppy).filter(Shelter.id==Puppy.shelter_id).filter(Shelter.id==5).count()
	print five

if __name__ == '__main__':
	# query_all()
	# puppy_age()
	# puppy_weight()
	# shelters_where_puppies_are()
	count_puppys_in_each_shelter()
