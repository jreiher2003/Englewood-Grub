from app import app, db
from flask import render_template 
from app.models import Shelter, Puppy, Profile

## front page with  ordered by shelter, place to create adoptor. 
## shelter page display puppyies with pagination
## click on a puppy to see profile of puppy


@app.route('/')
def index():
	""" front page of site that lists all shelters"""
	shelter = db.session.query(Shelter).all()
	return render_template('index.html', shelter=shelter)

@app.route('/<int:shelter_id>/<path:shelter_name>')
def shelter_profile(shelter_id,shelter_name):
	shelter_profile = db.session.query(Shelter).filter_by(id=shelter_id).one()
	puppy = db.session.query(Puppy).filter_by(shelter_id=shelter_id).all()
	return render_template('shelter_profile.html', shelter_profile=shelter_profile, puppy=puppy)


@app.route('/<int:shelter_id>/<path:shelter_name>/<int:puppy_id>')
def puppy_profile(shelter_id,shelter_name,puppy_id):
	puppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	return render_template('puppy_profile.html', puppy=puppy)

## CRUD operations Puppy, Shelter Adoptors ##
#############################################

## create a new puppy ########################
## create a new shelter ######################
## create a new adoptor ######################


