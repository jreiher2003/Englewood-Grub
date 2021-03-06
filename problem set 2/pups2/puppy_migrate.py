from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from db_model import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///puppyshelter.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
