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
def user_query():
	name = session.query(User).order_by(User.id)
	for i in name:
		print i.name, i.fullname


def user_query2():
	for name, fullname in session.query(User.name, User.fullname):
		print fullname, name


def user_filter():
	for name in session.query(User.name).filter(User.fullname=='Jeff Reiher'):
		print name


def user_like():
	query = session.query(User).filter(User.name.like('%jeff')).order_by(User.id)
	print query.all()
	print query.first()


def user_count():
	new_query = session.query(User).filter(User.name.like("%jeff")).count()
	print new_query

# if __name__ == '__main__':
# 	user_query()
# 	print "\n"
# 	user_query2()
# 	print "\n"
# 	user_filter()
# 	print "\n"
# 	user_like()
# 	print "\n"
# 	user_count()

##################################################################
# Working with Related objects
jack = User(name='jack', fullname='Jack Bean', password='12345')
jack.addresses = [Address(email_address='jack@google.com'),
				  Address(email_address='j25@yahoo.com')]

# print jack.addresses[1]
# print '\n'
# print jack.addresses[1].user
# session.add(jack)
# session.commit()

jack = session.query(User).filter_by(name='jack').first()
# print "\n"
# print jack
# print "\n"
# print jack.addresses