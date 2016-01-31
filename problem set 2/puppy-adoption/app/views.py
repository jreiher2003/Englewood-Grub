from app import app, db
from random import randint
import datetime
import random
from werkzeug import secure_filename
from flask import render_template, url_for, flash, redirect, request
from forms import CreatePuppy, CreateShelter, CreateAdoptor
from app.models import Shelter, Puppy, Profile, Adoptors, AdoptorsPuppies
from app.utils import *


## front page with  ordered by shelter, place to create adoptor. 
## shelter page display puppyies with pagination
## click on a puppy to see profile of puppy


@app.route('/')
def index():
	""" front page of site that lists all shelters"""
	shelter = db.session.query(Shelter).order_by("current_capacity asc").all()
	return render_template('index.html', shelter=shelter)

##  CRUD for Shelter class  ##
@app.route('/<int:shelter_id>/<path:shelter_name>/page/<int:page>')
def shelter_profile(shelter_id,shelter_name, page=1):
	shelter_profile = db.session.query(Shelter).filter_by(id=shelter_id).one()
	puppy = Puppy.query.filter(db.and_(Puppy.shelter_id==shelter_id, Puppy.show==True)).paginate(page,5,False)
	return render_template('shelter_profile.html', 
							shelter_id=shelter_id,
							shelter_name=shelter_name,
							shelter_profile=shelter_profile,
						    puppy=puppy)


@app.route('/new-shelter', methods=['GET', 'POST'])
def new_shelter():
	error = None
	form = CreateShelter()
	if form.validate_on_submit():
		newshelter = Shelter(name=form.name.data, 
							 address=form.address.data,
							 city=form.city.data,
							 state=form.state.data,
							 zipCode=form.zipCode.data,
							 website=form.website.data,
							 maximum_capacity=form.maximum_capacity.data,
							 current_capacity=form.current_capacity.data
							 )
		db.session.add(newshelter)
		db.session.commit()
		flash("Congrats You just created a new shelter named %s" % newshelter.name)
		return redirect(url_for('index'))

	return render_template('create_shelter.html', 
							form=form, 
							error=error)

@app.route('/<int:shelter_id>/<path:shelter_name>/edit/', methods=['GET','POST'])
def edit_shelter(shelter_id,shelter_name):
	editshelter = db.session.query(Shelter).filter_by(id=shelter_id).one()
	form = CreateShelter(obj=editshelter)
	if form.validate_on_submit():
		editshelter.name = form.name.data
		editshelter.address = form.address.data
		editshelter.city = form.city.data
		editshelter.state = form.state.data
		editshelter.zipCode = form.zipCode.data
		editshelter.website = form.website.data
		editshelter.maximum_capacity = form.maximum_capacity.data
		editshelter.current_capacity = form.current_capacity.data
		db.session.add(editshelter)
		db.session.commit()
		flash("You just edited shelter %s" % editshelter.name)
		return redirect(url_for('index'))
	return render_template('edit_shelter.html', 
							editshelter=editshelter, 
							form=form)

@app.route('/<int:shelter_id>/<path:shelter_name>/delete/', methods=['GET', 'POST'])
def delete_shelter(shelter_id, shelter_name):
	deleteshelter = db.session.query(Shelter).filter_by(id=shelter_id).one()
	if request.method == "POST":
		db.session.delete(deleteshelter)
		db.session.commit()
		flash('Successfully deleted shelter %s' % deleteshelter.name)
		return redirect(url_for('index'))
	return render_template('delete_shelter.html', deleteshelter=deleteshelter)

###  CRUD for Puppy  ######
@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>')
def puppy_profile(shelter_id,shelter_name,puppy_id):
	puppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	return render_template('puppy_profile.html', puppy=puppy)


## create 
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

	return render_template('create_puppy.html', form=form)


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
		flash('%s was successfully edited' % editpuppy.name, 'success')
		return redirect(url_for('puppy_profile', 
								shelter_id=editpuppy.shelter.id,
								shelter_name=editpuppy.shelter.name_slug,
								puppy_id=editpuppy.id))
	return render_template("edit_puppy_profile.html", 
							editpuppy=editpuppy, 
							form=form)


@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>/delete/', methods=['GET','POST'])
def delete_puppy(shelter_id, shelter_name, puppy_id):
	deletepuppy = db.session.query(Puppy).join(Profile, Puppy.id==Profile.puppy_id).filter(Puppy.id==puppy_id).one()
	if request.method == 'POST':
		db.session.delete(deletepuppy)
		db.session.commit()
		currentcapacity = db.session.query(Shelter).filter(Shelter.id==deletepuppy.shelter_id).one()
		currentcapacity.current_capacity = currentcapacity.current_capacity - 1
		db.session.add(currentcapacity)
		db.session.commit()
		flash('Puppy %s Deleted' % deletepuppy.name)
		return redirect(url_for('index'))
	return render_template('delete_puppy_profile.html', deletepuppy=deletepuppy)

	
# CRUD adoptor ######################
@app.route('/adoptors', methods=['GET', 'POST'])
def adoptor_list():
	adoptors = db.session.query(Adoptors).order_by(Adoptors.id.desc()).all()
	return render_template('adoptor_list.html', adoptors=adoptors)


@app.route('/new-adoptor', methods=['GET', 'POST'])
def new_adoptor():
	form = CreateAdoptor()
	if form.validate_on_submit():
		newadoptor = Adoptors(name=form.name.data)
		db.session.add(newadoptor)
		db.session.commit()
		flash('Just created a new adoptor named %s' % newadoptor.name)
		return redirect(url_for('adoptor_list'))
	return render_template('create_adoptor.html', form=form)


@app.route('/adoptors/profile/<int:adoptor_id>/edit/', methods=['GET','POST'])
def edit_adoptor(adoptor_id):
	editadoptor = db.session.query(Adoptors).filter_by(id=adoptor_id).one()
	form = CreateAdoptor(obj=editadoptor)
	if form.validate_on_submit():
		editadoptor.name = form.name.data
		db.session.add(editadoptor)
		db.session.commit()
		flash('Successful edit of this adoptor who is now named %s' % editadoptor.name)
		return redirect(url_for('adoptor_list'))
	return render_template('edit_adoptor.html', 
							editadoptor=editadoptor, 
							form=form)


@app.route('/adoptors/profile/<int:adoptor_id>/delete/', methods=['GET','POST'])
def delete_adoptor(adoptor_id):
	deleteadoptor = db.session.query(Adoptors).filter_by(id=adoptor_id).one()
	if request.method == 'POST':
		db.session.delete(deleteadoptor)
		db.session.commit()
		flash('You just deleted %s' % deleteadoptor.name)
		return redirect(url_for('adoptor_list'))

	return render_template('delete_adoptor.html', deleteadoptor=deleteadoptor)


### CRUD for adopting a puppy
@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>/adopt/', methods=['GET','POST'])
def adoptions(shelter_id,shelter_name,puppy_id):
	puppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	adoptors = db.session.query(Adoptors).all()
	return render_template('adopt_puppy.html',  
							puppy=puppy, 
							adoptors=adoptors)

@app.route('/<int:shelter_id>/<path:shelter_name>/profile/<int:puppy_id>/adopt/<int:adoptor_id>/', methods=['GET','POST'])
def adoption_success(shelter_id,shelter_name,puppy_id,adoptor_id):
	puppy = db.session.query(Puppy).filter_by(id=puppy_id).one()
	adoptor = db.session.query(Adoptors).filter_by(id=adoptor_id).one()
	if request.method == 'POST':
		adoption = AdoptorsPuppies(puppy_id=request.form['puppyname'], adoptor_id=request.form['adoptorname'])
		puppy.show = False
		db.session.add(adoption)
		db.session.add(puppy)
		db.session.commit()
		flash('Successful adoption')
		return redirect(url_for('list_adoptions'))
	return render_template('adoption_success.html', puppy=puppy, adoptor=adoptor)



@app.route('/list-adoptions', methods=['GET', 'POST'])
def list_adoptions():
	adoptions = db.session.query(AdoptorsPuppies).all()
	return render_template('list_adoptions.html', adoptions=adoptions)