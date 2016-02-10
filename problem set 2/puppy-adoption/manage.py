import os
from app import app,db

from flask.ext.script import Manager 
from flask.ext.migrate import Migrate, MigrateCommand 

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.add_command
def test():
	"""Runs the tests without coverage."""
	tests = unittest.Testloader().discover('.')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()