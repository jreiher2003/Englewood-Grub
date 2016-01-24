from app import db 
from app.models import Shelter, Puppy, Profile, Adoptors, AdoptorsPuppies

from random import randint
import datetime
import random

# db.create_all() 


# # Add Shelters
# shelter1 = Shelter(name = "Oakland Animal Services", address = "1101 29th Ave", city = "Oakland", state = "California", zipCode = "94601", website = "oaklandanimalservices.org", maximum_capacity=40)
# db.session.add(shelter1)

# shelter2 = Shelter(name = "San Francisco SPCA Mission Adoption Center", address="250 Florida St", city="San Francisco", state="California", zipCode = "94103", website = "sfspca.org", maximum_capacity=40)
# db.session.add(shelter2)

# shelter3 = Shelter(name = "Wonder Dog Rescue", address= "2926 16th Street", city = "San Francisco", state = "California" , zipCode = "94103", website = "http://wonderdogrescue.org", maximum_capacity=40)
# db.session.add(shelter3)

# shelter4 = Shelter(name = "Humane Society of Alameda", address = "PO Box 1571" ,city = "Alameda" ,state = "California", zipCode = "94501", website = "hsalameda.org", maximum_capacity=40)
# db.session.add(shelter4)

# shelter5 = Shelter(name = "Palo Alto Humane Society" ,address = "1149 Chestnut St." ,city = "Menlo Park", state = "California" ,zipCode = "94025", website = "paloaltohumane.org", maximum_capacity=40)
# db.session.add(shelter5)

# # db.session.commit()

# # #Add Puppies

# male_names = ["Bailey", "Max", "Charlie", "Buddy","Rocky","Jake", "Jack", "Toby", "Cody", "Buster", "Duke", "Cooper", "Riley", "Harley", "Bear", "Tucker", "Murphy", "Lucky", "Oliver", "Sam", "Oscar", "Teddy", "Winston", "Sammy", "Rusty", "Shadow", "Gizmo", "Bentley", "Zeus", "Jackson", "Baxter", "Bandit", "Gus", "Samson", "Milo", "Rudy", "Louie", "Hunter", "Casey", "Rocco", "Sparky", "Joey", "Bruno", "Beau", "Dakota", "Maximus", "Romeo", "Boomer", "Luke", "Henry"]

# female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby', 'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess','Emma', 'Annie', 'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 'Madison', 'Stella', 'Penny', 'Belle', 'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']

# puppy_images = ["http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct", "http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct","http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct","http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct","http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg","http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct","http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct","http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct","http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct","http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"]

# #This method will make a random age for each puppy between 0-18 months(approx.) old from the day the algorithm was run.
# def CreateRandomAge():
# 	today = datetime.date.today()
# 	days_old = randint(0,540)
# 	birthday = today - datetime.timedelta(days = days_old)
# 	return birthday

# #This method will create a random weight between 1.0-40.0 pounds (or whatever unit of measure you prefer)
# def CreateRandomWeight():
# 	return random.uniform(1.0, 40.0)

# for i,x in enumerate(male_names):
# 	new_puppy = Puppy(name = x, gender = "male", dateOfBirth = CreateRandomAge(),picture=random.choice(puppy_images) ,shelter_id=randint(1,5), weight= CreateRandomWeight())
# 	db.session.add(new_puppy)
# 	db.session.commit()

# for i,x in enumerate(female_names):
# 	new_puppy = Puppy(name = x, gender = "female", dateOfBirth = CreateRandomAge(),picture=random.choice(puppy_images),shelter_id=randint(1,5), weight= CreateRandomWeight())
# 	db.session.add(new_puppy)
# 	db.session.commit()

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
	return db.session.query(Shelter.maximum_capacity).filter(Shelter.id == shel_id).all()
	

# A Query that determines which Shelter to place a puppy in.
def add_puppy_to_shelter(puppy_id, shelter_id):
	if (get_shelter_occupancy(shelter_id) >= get_shelter_capacity(shelter_id)):
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


