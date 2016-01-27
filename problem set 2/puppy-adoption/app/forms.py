from flask_wtf import Form 
from wtforms import TextField, RadioField
from wtforms.validators import DataRequired


class CreatePuppy(Form):
	name = TextField('Name', validators=[DataRequired()])
	gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
	# specialNeeds = RadioField('Disability', choices=[('blind', 'Blind'), 
	# 												 ('deaf','Deaf'),
	# 												 ('3-legged', '3-Legged'),
	# 												 ('None', 'None')])