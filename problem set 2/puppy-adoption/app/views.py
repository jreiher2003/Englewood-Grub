from app import app, db
from flask import render_template 
from app.models import Shelter, Puppy, Profile

@app.route('/')
def index():
	puppy = db.session.query(Puppy).all()
	return render_template('index.html', puppy=puppy)