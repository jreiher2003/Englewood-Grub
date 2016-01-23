from app import db 
 
AssociationTable = db.Table('association',
    db.Column('id', Integer, primary_key=True), 
    db.Column('puppy_id', db.Integer, db.ForeignKey('puppy.id')),
    db.Column('adopters_id', db.Integer, db.ForeignKey('adopters.id'))
    )


class Shelter(db.Model):

    __tablename__ = "shelter"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    address = db.Column(db.String(250))
    city = db.Column(db.String(80))
    state = db.Column(db.String(20))
    zipCode = db.Column(db.String(10))
    website = db.Column(db.String)
    maximum_capacity = db.Column(db.Integer,nullable=True)
    current_capacity = db.Column(db.Integer,nullable=True)
    

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
    shelter = db.relationship(Shelter)
    weight = db.Column(db.Numeric(10))
    profile = db.relationship("Profile", uselist=False, backref="puppy")
    adopters = db.relationship("Adpoters", secondary=AssociationTable, backref="puppy")

    def __repr__(self):
        return '<name>: {}'.format(self.name)


class Profile(db.Model):

    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String)
    description = db.Column(db.String(500))
    specialNeeds = db.Column(db.String(500))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))
    puppy = db.relationship("Puppy", back_populates="profile")

    def __repr__(self):
        return '<name>: {}'.format(self.name)
        

class Adpoters(db.Model):

    __tablename__ = "adopters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    puppy = db.relationship("Puppy", secondary=AssociationTable, backref="adopters")

    def __repr__(self):
        return '<name>: {}'.format(self.name)




