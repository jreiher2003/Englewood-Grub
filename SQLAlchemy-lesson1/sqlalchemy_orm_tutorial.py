import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
     name = Column(String(50))
     fullname = Column(String(50))
     password = Column(String(12))

     def __repr__(self):
         return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, primary_key=True)
	email_address = Column(String, nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'))
	user = relationship("User", backref=backref('addresses', order_by=id))

	def __repr__(self):
		return "<Address(emil_address='%s')>" % self.email_address


engine = create_engine('sqlite:///orm.db', echo=True)
# create table statement in SQL
Base.metadata.create_all(engine)