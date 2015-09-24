from sqlalchemy_orm_tutorial import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

###########################################################
# Adding new objects

jeff = User(name="jeff", fullname="Jeff Reiher", password="12345")
# session.add(jeff)
# print "User %s added" % (jeff.fullname)

# our_user = session.query(User).filter_by(name="Jeff").first()
# print our_user

# print jeff is our_user

# session.add_all([
# 		User(name='wendy', fullname='Wendy Williams', password='foobar'),
# 		User(name='mary', fullname='Mary Contrary', password='xyz'),
# 		User(name='fred', fullname='Fred Flinstone', password='blah')
# 	])
# jeff.password = '54321'
# print session.dirty
# print session.new

# session.commit()


##########################################################
# Querying
# jeff.name = 'jeff'
# session.rollback()
# session.add(jeff)
# session.commit()
name = session.query(User).order_by(User.id)
for i in name:
	print i.name, i.fullname

print "\n"

for name, fullname in session.query(User.name, User.fullname):
	print fullname, name

print "\n"

for name in session.query(User.name).filter(User.fullname=='Jeff Reiher'):
	print name

print "\n"

query = session.query(User).filter(User.name.like('%jeff')).order_by(User.id)
print query.all()

print "\n"
print query.first()
# print query.one()
print "\n"

new_query = session.query(User).filter(User.name.like("%jeff")).count()
print new_query