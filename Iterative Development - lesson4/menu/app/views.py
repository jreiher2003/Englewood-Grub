from app import app,db # pragma: no cover
from flask import render_template # pragma: no cover

@app.route('/') # pragma: no cover
def index():
	return render_template('index.html')