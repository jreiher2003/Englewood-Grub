from flask_wtf import Form 
from wtforms import TextField, RadioField
from wtforms.validators import DataRequired, url


class CreatePuppy(Form):
	name = TextField('Name', validators=[DataRequired()])
	gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
	picture = TextField('Photo-Url')