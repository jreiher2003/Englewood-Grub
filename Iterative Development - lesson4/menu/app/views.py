from app import app,db # pragma: no cover
from app.models import Place
from flask import render_template # pragma: no cover

@app.route('/') # pragma: no cover
def index():
	all_places = Place.query.all()
	return render_template('index.html', all_places=all_places)