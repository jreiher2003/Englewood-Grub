from db_model import *
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def all_puppies():
	all_pups = session.query(Puppy).order_by("puppy.name asc").all()
	for pup in all_pups:
		print pup.name

def puppyLess6mo():
	young_pups = session.query(Puppy).filter(
		Puppy.dateOfBirth.between('2015-03-25','2015-09-26')).order_by('puppy.dateOfBirth desc')
	for pup in young_pups:
		print pup.name, pup.dateOfBirth	

def puppyWeight():
	pupWeight = session.query(Puppy).order_by('puppy.weight asc')
	for pup in pupWeight:
		print pup.name, pup.weight

def puppy_by_shelter():
	pupshelter = session.query(Shelter,Puppy).filter(
		Shelter.id==Puppy.shelter_id).order_by('shelter.name desc').all()
	for shel, pup in pupshelter:
		print shel.name, pup.name


if __name__ == '__main__':
	# all_puppies()
	# puppyLess6mo()
	# puppyWeight()
	puppy_by_shelter()