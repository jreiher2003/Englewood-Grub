from app import app, db
from flask import render_template 
from app.models import Shelter, Puppy, Profile

## front page with  ordered by shelter
## shelter page display puppyies with pagination

@app.route('/')
def index():
	puppy = db.session.query(Puppy).all()
	return render_template('index.html', puppy=puppy)


## CRUD operations Puppy, Shelter Adoptors ##
#############################################

## create a new puppy ########################
## create a new shelter ######################
## create a new adoptor ######################

