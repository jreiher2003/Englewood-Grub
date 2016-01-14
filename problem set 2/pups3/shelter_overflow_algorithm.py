from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Base, Shelter, Puppy, Profile, Adopter, PuppyAdopterLink

from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()