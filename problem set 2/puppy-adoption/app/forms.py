from flask_wtf import Form 
from wtforms import TextField, RadioField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, URL, NumberRange


class CreatePuppy(Form):
	name = TextField('Name', validators=[DataRequired()])
	gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
	picture = TextField('Photo-Url')
	weight = IntegerField('Weight')
	specialNeeds = SelectField('Special Needs', choices=[('None','None'),('3-legged', '3-legged'), ('Blind', 'Blind'),('Deaf', 'Deaf')])
	description = TextAreaField('Description', validators=[Length(max=500)])