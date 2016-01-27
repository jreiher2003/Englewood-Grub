from flask_wtf import Form 
from wtforms import TextField, RadioField, FileField
from wtforms.validators import DataRequired


class CreatePuppy(Form):
	name = TextField('Name', validators=[DataRequired()])
	gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
	photo = FileField("Your Puppy Photo")