from app import app, db
from flask import render_template 
from app.models import Shelter, Puppy, Profile

## front page with  ordered by shelter, place to create adoptor. 
## shelter page display puppyies with pagination
## click on a puppy to see profile of puppy

@app.route('/')
def index():
	shelter = db.session.query(Shelter).all()
	return render_template('index.html', shelter=shelter)


## CRUD operations Puppy, Shelter Adoptors ##
#############################################

## create a new puppy ########################
## create a new shelter ######################
## create a new adoptor ######################


