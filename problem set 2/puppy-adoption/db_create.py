from app import db 
from app.models import Shelter, Puppy, Profile, Adoptors, AdoptorsPuppies
from db_profile_create import * 

from random import randint
import datetime
import random

db.create_all() 


# Add Shelters
shelter1 = Shelter(name = "Oakland Animal Services", address = "1101 29th Ave", city = "Oakland", state = "California", zipCode = "94601", website = "oaklandanimalservices.org", maximum_capacity=randint(25,40))
db.session.add(shelter1)

shelter2 = Shelter(name = "San Francisco SPCA Mission Adoption Center", address="250 Florida St", city="San Francisco", state="California", zipCode = "94103", website = "sfspca.org", maximum_capacity=randint(25,40))
db.session.add(shelter2)

shelter3 = Shelter(name = "Wonder Dog Rescue", address= "2926 16th Street", city = "San Francisco", state = "California" , zipCode = "94103", website = "http://wonderdogrescue.org", maximum_capacity=randint(25,40))
db.session.add(shelter3)

shelter4 = Shelter(name = "Humane Society of Alameda", address = "PO Box 1571" ,city = "Alameda" ,state = "California", zipCode = "94501", website = "hsalameda.org", maximum_capacity=randint(25,40))
db.session.add(shelter4)

shelter5 = Shelter(name = "Palo Alto Humane Society" ,address = "1149 Chestnut St." ,city = "Menlo Park", state = "California" ,zipCode = "94025", website = "paloaltohumane.org", maximum_capacity=randint(25,40))
db.session.add(shelter5)

db.session.commit()

# #Add Puppies

male_names = ["Bailey", "Max", "Charlie", "Buddy","Rocky","Jake", "Jack", "Toby", "Cody", "Buster", "Duke", "Cooper", "Riley", "Harley", "Bear", "Tucker", "Murphy", "Lucky", "Oliver", "Sam", "Oscar", "Teddy", "Winston", "Sammy", "Rusty", "Shadow", "Gizmo", "Bentley", "Zeus", "Jackson", "Baxter", "Bandit", "Gus", "Samson", "Milo", "Rudy", "Louie", "Hunter", "Casey", "Rocco", "Sparky", "Joey", "Bruno", "Beau", "Dakota", "Maximus", "Romeo", "Boomer", "Luke", "Henry"]

female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby', 'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess','Emma', 'Annie', 'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 'Madison', 'Stella', 'Penny', 'Belle', 'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']

puppy_images = ["https://pixabay.com/static/uploads/photo/2015/11/17/13/13/bulldog-1047518_960_720.jpg", "https://pixabay.com/static/uploads/photo/2015/03/26/09/54/pug-690566__180.jpg","https://pixabay.com/static/uploads/photo/2014/03/05/19/23/dog-280332__180.jpg","https://pixabay.com/static/uploads/photo/2015/02/05/12/09/chihuahua-624924__180.jpg","https://pixabay.com/static/uploads/photo/2016/01/05/17/57/dog-1123026__180.jpg","https://pixabay.com/static/uploads/photo/2014/03/14/20/07/painting-287403__180.jpg","https://pixabay.com/static/uploads/photo/2016/01/05/17/51/dog-1123016__180.jpg","https://pixabay.com/static/uploads/photo/2014/07/05/08/50/puppy-384647__180.jpg","https://pixabay.com/static/uploads/photo/2015/12/23/14/29/puppies-1105730__180.jpg","https://pixabay.com/static/uploads/photo/2015/11/17/12/42/puppy-1047454__180.jpg"]



#This method will make a random age for each puppy between 0-18 months(approx.) old from the day the algorithm was run.
def CreateRandomAge():
	today = datetime.date.today()
	days_old = randint(0,540)
	birthday = today - datetime.timedelta(days = days_old)
	return birthday

#This method will create a random weight between 1.0-40.0 pounds (or whatever unit of measure you prefer)
def CreateRandomWeight():
	return random.uniform(1.0, 40.0)

for i,x in enumerate(male_names):
	new_puppy = Puppy(name = x, gender = "male", dateOfBirth = CreateRandomAge(),picture=random.choice(puppy_images) ,shelter_id=randint(1,5), weight= CreateRandomWeight())
	db.session.add(new_puppy)
	db.session.commit()

for i,x in enumerate(female_names):
	new_puppy = Puppy(name = x, gender = "female", dateOfBirth = CreateRandomAge(),picture=random.choice(puppy_images),shelter_id=randint(1,5), weight= CreateRandomWeight())
	db.session.add(new_puppy)
	db.session.commit()


#######################################################################################
############  Helpful queries  ########################################################
#######################################################################################
# Query all puppies in alphabetical order.
def get_puppies_by_name():
    return db.session.query(Puppy).order_by(Puppy.name).all()

# Query all puppies less than 6 months old and order by birthdate with youngest first. 
def get_baby_puppies():
    sixMonthsAgo = datetime.date.today() - datetime.timedelta(6 *365/12)
    return db.session.query(Puppy).filter(Puppy.dateOfBirth > sixMonthsAgo).order_by(Puppy.dateOfBirth).all()

# Query all puppies and order by ascending weight.
def get_puppies_by_weight():
    return db.session.query(Puppy).order_by(Puppy.weight).all()

# Query all puppies and group by shelter
def get_puppies_by_shelter():
	return db.session.query(Puppy, Shelter).join(Shelter).order_by(Puppy.shelter_id).all()

# Query the current occupancy of a specific shelter. 
def get_shelter_occupancy(shel_id):
	# return Shelter.query.filter(db.and_(Puppy.shelter_id==Shelter.id, Shelter.id == shel_id)).count()
	return db.session.query(Puppy, Shelter).join(Shelter).filter(Shelter.id == shel_id).count()

# Query the capacity for a shelter by it's ID.
def get_shelter_capacity(shel_id):
	return db.session.query(Shelter.maximum_capacity).filter(Shelter.id == shel_id).one()[0]

# A Query that determines which Shelter to place a puppy in.
def add_puppy_to_shelter(puppy_id, shelter_id):
	shelter_id = randint(1,5)
	if (get_shelter_occupancy(shelter_id) <= get_shelter_capacity(shelter_id)):
		sheltered_puppy = session.query(Puppy).filter(Puppy.id == puppy_id).one()
		sheltered_puppy.shelter_id = shelter_id
		session.add(sheltered_puppy)
		session.commit()
		print "Puppy added to shelter."
		return None
	unsheletered_puppy = session.query(Puppy).filter(Puppy.id == puppy_id).one()
	print '%s has been put to sleep. There was no room in the shelter.' % unsheletered_puppy.name
	session.delete(unsheletered_puppy)
	session.commit()
	return None


# A Query that removes a puppy from it's Shelter and adds it to a home.
def adopt_puppies(puppy_id, adopter_list):
	adopted_puppy = session.query(Puppy).filter(Puppy.id == puppy_id).one()
	adopted_puppy.shelter_id = None
	session.add(adopted_puppy)
	
	for adopter in adopter_list:
		new_adoption = AdoptorsPuppies(adoptor_id = adopter, puppy_id = adopted_puppy.id)
		session.add(new_adoption)
		session.commit()
	
	return None


def populate_profile():
	""" function to populate description column of Profile table """
	puppy = db.session.query(Puppy).all()
	for pup in puppy:
		new_profile = Profile(description=descriptions(), specialNeeds=special_needs(), puppy_id=pup.id)
		db.session.add(new_profile)
		db.session.commit()
	print "profile update"
populate_profile()


### update shelter to add the current capacity
def count_pups():
	shelter = db.session.query(Shelter).all()
	for shel in shelter:
		shel.current_capacity = db.session.query(Puppy, Shelter).join(Shelter).filter(Shelter.id == shel.id).count()
		db.session.add(shel)
		db.session.commit()

count_pups()

def add_puppy_to_shelter():
	arr = [1,2,3,4,5]
	while len(arr) > 0:
		shelter_id = random.choice(arr)
		if (get_shelter_occupancy(shelter_id) < get_shelter_capacity(shelter_id)):
			return shelter_id
		else:
			arr.remove(shelter_id)
	

# print add_puppy_to_shelter()
