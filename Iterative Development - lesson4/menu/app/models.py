import datetime # pragma: no cover
from app import db

class Place(db.Model):
    __tablename__ = 'place' # names table
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Place %r>' % (self.name)