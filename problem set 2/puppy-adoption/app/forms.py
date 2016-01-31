from flask_wtf import Form 
from wtforms import TextField, RadioField, BooleanField, TextAreaField, SelectField, IntegerField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, URL, NumberRange


class CreatePuppy(Form):
	name = TextField('Name', validators=[DataRequired()])
	gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
	picture = TextField('Photo-Url')
	weight = IntegerField('Weight')
	specialNeeds = SelectField('Special Needs', choices=[('None','None'),('3-legged', '3-legged'), ('Blind', 'Blind'),('Deaf', 'Deaf')])
	description = TextAreaField('Description', validators=[Length(max=500)])
	breed = SelectField('Breed', choices=[('Bulldog','Bulldog'),('Boston Terrier','Boston Terrier'),('Chihuahua', 'Chihuahua'),('German Shepherd', 'German Shepherd'),("Greyhound","Greyhound"),("Labrador Retriever","Labrador Retriever"),("Maltese","Maltese"),("Schnauzer","Schnauzer"),("Pug","Pug"),("Saint Bernard","Saint Bernard"),("Shih-Tzu","Shih-Tzu"),("Siberian Husky","Siberian Husky"),("Whippet","Whippet")])

class CreateShelter(Form):
	name = TextField('Name', validators=[DataRequired()])
	address = TextField('Address', validators=[DataRequired()])
	city = TextField('City')
	state = TextField('State')
	zipCode = IntegerField('Zip')
	website = TextField('Website')
	maximum_capacity = IntegerField('Max Capacity')
	current_capacity = IntegerField('Current Capacity')

class CreateAdoptor(Form):
	name = TextField('Name', validators=[DataRequired()])


