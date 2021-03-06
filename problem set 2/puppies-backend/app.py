from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from models import Base, Shelter, Puppy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///puppyshelter.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     address = db.Column(db.String(256))

if __name__ == '__main__':
    manager.run()