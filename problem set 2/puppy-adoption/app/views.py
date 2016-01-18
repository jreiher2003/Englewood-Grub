from app import app, db
from flask import render_template 

@app.route('/')
def index():
	return "yo first commit"