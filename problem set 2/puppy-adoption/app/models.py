from app import db 
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

# Base = declarative_base()

class Shelter(db.Model):

    __tablename__ = "shelter"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    address = db.Column(db.String(250))
    city = db.Column(db.String(80))
    state = db.Column(db.String(20))
    zipCode = db.Column(db.String(10))
    website = db.Column(db.String)

    def __repr__(self):
        return '<name>: {}'.format(self.name)

class Puppy(db.Model):

    __tablename__ = "puppy"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(6), nullable = False)
    dateOfBirth = db.Column(db.Date)
    picture = db.Column(db.String)
    shelter_id = db.Column(db.Integer, db.ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = db.Column(db.Numeric(10))

    def __repr__(self):
        return '<name>: {}'.format(self.name)


# 
