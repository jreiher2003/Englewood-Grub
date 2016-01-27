from app import app, db
from random import randint
import datetime
import random
from flask import render_template, url_for, flash, redirect
from forms import CreatePuppy
from app.models import Shelter, Puppy, Profile
from app.utils import *

## front page with  ordered by shelter, place to create adoptor. 
## shelter page display puppyies with pagination
## click on a puppy to see profile of puppy


@app.route('/')
def index():
	""" front page of site that lists all shelters"""
	shelter = db.session.query(Shelter).order_by("current_capacity asc").all()
	return render_template('index.html', shelter=shelter)

@app.route('/<int:shelter_id>/<path:shelter_name>/page/<int:page>')
def shelter_profile(shelter_id,shelter_name, page=1):
	shelter_profile = db.session.query(Shelter).filter_by(id=shelter_id).one()
	puppy = Puppy.query.filter(Puppy.shelter_id==shelter_id).paginate(page,5,False)
	return render_template('shelter_profile.html', 
							shelter_id=shelter_id,
							shelter_name=shelter_name,
							shelter_profile=shelter_profile,
						    puppy=puppy)


@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>')
def puppy_profile(shelter_id,shelter_name,puppy_id):
	puppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	return render_template('puppy_profile.html', puppy=puppy)

## CRUD operations Puppy, Shelter Adoptors ##
#############################################
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

## create a new puppy ########################
@app.route('/new-puppy', methods=['GET', 'POST'])
def new_puppy():
	form = CreatePuppy()
	if form.validate_on_submit():
		newpuppy = Puppy(name=form.name.data,gender=form.gender.data,dateOfBirth=create_random_age(),picture="",shelter_id=add_puppy_to_shelter(),weight=create_random_weight())
		# newprofile = db.session.query(Profile).one()
		# newprofile.description = descriptions()
		# newprofile.specialNeeds = form.specialNeeds.data 
		currentcapacity = db.session.query(Shelter).filter(Shelter.id==newpuppy.shelter_id).one()
		currentcapacity.current_capacity = currentcapacity.current_capacity + 1
		db.session.add(newpuppy)
		# db.session.add(newprofile)
		db.session.add(currentcapacity)
		db.session.commit()
		flash('Successfully Added a Puppy to '+ currentcapacity.name, 'success')
		return redirect(url_for('index'))

	return render_template('new_puppy.html', form=form)
## create a new shelter ######################
## create a new adoptor ######################


