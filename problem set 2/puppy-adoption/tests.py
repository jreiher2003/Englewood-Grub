import unittest
from flask.ext.testing import TestCase
from app import app, db
from app.models import Shelter, Puppy, Profile, Adoptors


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        print app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        # db.session.add(BlogPost("Test post", "This is a test. Only a test."))
        # db.session.add(User("admin", "ad@min.com", "admin"))
        # db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertIn(b'Welcome to our puppy adoption web app!', response.data)

      # Ensure that Flask was set up correctly
    def test_adoptors(self):
        response = self.client.get('/adoptors', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_adoptors_page_loads(self):
        response = self.client.get('/adoptors')
        self.assertIn(b'A list of potenial Adoptors', response.data)

    # # Ensure that main page requires user login
    # def test_main_route_requires_login(self):
    #     response = self.client.get('/', follow_redirects=True)
    #     self.assertIn(b'You need to login first.', response.data)

    # # Ensure that logout page requires user login
    # def test_logout_route_requires_login(self):
    #     response = self.client.get('/logout', follow_redirects=True)
    #     self.assertIn(b'You need to login first.', response.data)

    # # Ensure that posts show up on the main page
    # def test_posts_show_up_on_main_page(self):
    #     response = self.client.post(
    #         '/login',
    #         data=dict(username="admin", password="admin"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'This is a test. Only a test.', response.data)


if __name__ == '__main__':
    unittest.main()