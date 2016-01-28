from app import app, db
from random import randint
import datetime
import random
from werkzeug import secure_filename
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


## create a new puppy ########################
@app.route('/new-puppy', methods=['GET', 'POST'])
def new_puppy():
	form = CreatePuppy()
	if form.validate_on_submit():
		newpuppy = Puppy(name=form.name.data, gender=form.gender.data, dateOfBirth=create_random_age(), picture=form.picture.data, shelter_id=add_puppy_to_shelter(), weight=create_random_weight())
		db.session.add(newpuppy)
		db.session.commit()
		newprofile = Profile(specialNeeds=form.specialNeeds.data,description=descriptions(), puppy_id=newpuppy.id)
		db.session.add(newprofile)
		db.session.commit()
		currentcapacity = db.session.query(Shelter).filter(Shelter.id==newpuppy.shelter_id).one()
		currentcapacity.current_capacity = currentcapacity.current_capacity + 1
		db.session.add(currentcapacity)
		db.session.commit()
		flash('Successfully Added a Puppy to '+ currentcapacity.name, 'success')
		return redirect(url_for('index'))

	return render_template('new_puppy.html', form=form)


@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>/edit/', methods=['GET','POST'])
def edit_puppy(shelter_id,shelter_name,puppy_id):
	# editpuppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	editpuppy=db.session.query(Puppy).join(Profile, Puppy.id==Profile.puppy_id).filter(Puppy.id==puppy_id).one()
	form = CreatePuppy(obj=editpuppy)
	if form.validate_on_submit():
		editpuppy.name = form.name.data
		editpuppy.gender = form.gender.data
		editpuppy.picture = form.picture.data
		editpuppy.weight = form.weight.data
		editpuppy.profile.specialNeeds = form.specialNeeds.data
		db.session.add(editpuppy)
		db.session.commit()
		flash('Puppy was successfully edited', 'success')
		return redirect(url_for('index'))
	return render_template("edit_puppy_profile.html", editpuppy=editpuppy, form=form)


@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>/delete/', methods=['GET','POST'])
def delete_puppy(shelter_id, shelter_name, puppy_id):
	return 'delete'

	
# create a new shelter ######################
# create a new adoptor ######################


