from models import *
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()




if __main__ == '__name__':
