from app import db 
 

class Shelter(db.Model):

    __tablename__ = "shelter"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    address = db.Column(db.String(250))
    city = db.Column(db.String(80))
    state = db.Column(db.String(20))
    zipCode = db.Column(db.String(10))
    website = db.Column(db.String)
    maximum_capacity = db.Column(db.Integer)
    current_capacity = db.Column(db.Integer)
    

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
    profile = db.relationship("Profile", uselist=False, back_populates="puppy")
    # adoption = db.relationship("Adopters", secondary=AdoptorsPuppies, back_populates="puppies")

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
        

class Adoptors(db.Model):

    __tablename__ = "adoptors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    # puppies = db.relationship("Puppy", secondary=AdoptorsPuppies, back_populates="adoption")

    def __repr__(self):
        return '<name>: {}'.format(self.name)


class AdoptorsPuppies(db.Model):
    __tablename__ = 'adopters_puppies'

    adoptor_id = db.Column(db.Integer,db.ForeignKey('adoptors.id'), primary_key = True)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppy.id'), primary_key = True)
    
    puppies = db.relationship(Puppy)
    adoptors = db.relationship(Adoptors)

# def puppy_by_shelter(shel_id):
#     """Counts puppies by shelter id """
#     return Puppy.query.filter(db.and_(Puppy.shelter_id==Shelter.id, Shelter.id == shel_id)).count()


