from random import randint
import datetime
import random

puppy_images = ["https://pixabay.com/static/uploads/photo/2015/11/17/13/13/bulldog-1047518_960_720.jpg", "https://pixabay.com/static/uploads/photo/2015/03/26/09/54/pug-690566__180.jpg","https://pixabay.com/static/uploads/photo/2014/03/05/19/23/dog-280332__180.jpg","https://pixabay.com/static/uploads/photo/2015/02/05/12/09/chihuahua-624924__180.jpg","https://pixabay.com/static/uploads/photo/2016/01/05/17/57/dog-1123026__180.jpg","https://pixabay.com/static/uploads/photo/2014/03/14/20/07/painting-287403__180.jpg","https://pixabay.com/static/uploads/photo/2016/01/05/17/51/dog-1123016__180.jpg","https://pixabay.com/static/uploads/photo/2014/07/05/08/50/puppy-384647__180.jpg","https://pixabay.com/static/uploads/photo/2015/12/23/14/29/puppies-1105730__180.jpg","https://pixabay.com/static/uploads/photo/2015/11/17/12/42/puppy-1047454__180.jpg"]


breed = ["Bulldog", "Collie", "Boston Terrier", "Chihuahua", "German Shepherd", "Greyhound", "Labrador Retriever",
		"Maltese", "Schnauzer", "Pug", "Saint Bernard", "Shih-Tzu", "Siberian Husky", "Whippet"]

puppy_adj = ["active", 'good', "affectionate", "alert", "athletic", "brave", "bright-eyed", "crafty", "cuddly", 
 			"cute", "energetic", "fluffy", "frisky", "gentle", "goofy", "happy", "huggable", "mischievous", "potty-trained", "zippy", "wonderful", "well-trained", "wagging", "unique", "trusty", "tough", "smart"]

puppy_verb = ["adore", "beg", "care for", "cuddle", "defend", "dig", "do tricks", "greet", "heel", "hunt", "kiss", "love", "obey", "pamper", "perform tricks", "roll", "roll over", "run", "run and play", "shake", "sit", "snuggle"]


def descriptions():
	vowels = ('a','e','i','o','u','A','E','I','O','U')
	x = random.choice(puppy_adj)
	y = random.choice(breed)
	v = random.choice(puppy_verb)
	if x.startswith(vowels):
		z = " is an " + x
		return "What you have here is a " + y + ". " + "This "+ y + z + ' dog that will ' + v + " you and your family."
	else:
		z = " is a " + x
		return "What you have here is a " + y + ". " + "This "+ y + z + ' dog that will ' + v + " you and your family." 

def create_random_age():
	today = datetime.date.today()
	days_old = randint(0,540)
	birthday = today - datetime.timedelta(days = days_old)
	return birthday

#This method will create a random weight between 1.0-40.0 pounds (or whatever unit of measure you prefer)
def create_random_weight():
	return random.uniform(1.0, 40.0)


# Query the current occupancy of a specific shelter. 
def get_shelter_occupancy(shel_id):
	# return Shelter.query.filter(db.and_(Puppy.shelter_id==Shelter.id, Shelter.id == shel_id)).count()
	return db.session.query(Puppy, Shelter).join(Shelter).filter(Shelter.id == shel_id).count()

# Query the capacity for a shelter by it's ID.
def get_shelter_capacity(shel_id):
	return db.session.query(Shelter.maximum_capacity).filter(Shelter.id == shel_id).all()


# A Query that determines which Shelter to place a puppy in.
def add_puppy_to_shelter():
	shelter_id = randint(1,5)
	if (get_shelter_occupancy(shelter_id) >= get_shelter_capacity(shelter_id)):
		return shelter_id
	else:
		shelter_id = shelter_id + 1
		return shelter_id