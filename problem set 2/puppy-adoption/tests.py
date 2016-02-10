import unittest
import datetime
from flask.ext.testing import TestCase
from app import app, db
from app.models import Shelter, Puppy, Profile, Adoptors, AdoptorsPuppies


class BaseTestCase(TestCase):
    """A base test case."""
 
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Adoptors(name='Testname'))
        db.session.add(Shelter(name="Testshelter", address="123 Fake st.", city="Fake", state="FK", zipCode="12345", website="http://test.com", maximum_capacity=10, current_capacity=5))
        db.session.add(Puppy(name="Testpup", shelter_id=1, gender="Male", dateOfBirth=datetime.datetime.now(),picture="http://testpup.com",weight=1, show=True))
        db.session.add(Profile(puppy_id=1, breed="Testbreed",description="This is a test description", specialNeeds="Testblind"))
        db.session.add(AdoptorsPuppies(adoptor_id=1, puppy_id=1))
        db.session.commit()

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
        self.assertIn(b'Testshelter', response.data)

    # ensure that /id/name/page/1 response is correct
    def test_shelter_profile(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the shelter profile loads correctly
    def test_shelter_profile_page_loads(self):
        response = self.client.get('/1/testshelter/page/1')
        self.assertIn(b'Testshelter', response.data)
        self.assertIn(b'123 Fake st.', response.data)
        self.assertIn(b'Fake', response.data)
        self.assertIn(b'http://test.com', response.data)
        self.assertIn(b'Testpup', response.data)

    # Ensure that puppy-profile correctly
    def test_puppy_profile(self):
        response = self.client.get('/1/testshelter/profile/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_puppy_profile_page_loads(self):
        response = self.client.get('/1/testshelter/profile/1')
        self.assertIn(b'Testshelter', response.data)
        self.assertIn(b'Testpup', response.data)
        self.assertIn(b'1', response.data)
        self.assertIn(b'Testbreed', response.data)
        self.assertIn(b'Testblind', response.data)
        self.assertIn(b'This is a test description', response.data)

    # Ensure that Flask was set up correctly
    def test_adopt_puppy_page(self):
        response = self.client.get('/1/testshelter/profile/1/adopt/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_adopt_puppy_page_loads(self):
        response = self.client.get('/1/testshelter/profile/1/adopt/')
        self.assertIn(b'Who do you want to adopt', response.data)

    # Ensure that test adpot page 2 set up correctly
    def test_adopt_2_puppy_page(self):
        response = self.client.get('/1/testshelter/profile/1/adopt/1/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_adopt_2_puppy_page_loads(self):
        response = self.client.get('/1/testshelter/profile/1/adopt/1/')
        self.assertIn(b'Are you sure you want <mark>Testpup</mark> to be adopted by <mark>Testname</mark>?', response.data)
    
      # Ensure that /adoptors response correctly
    def test_adoptors(self):
        response = self.client.get('/adoptors', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /adoptors page loads correctly
    def test_adoptors_page_loads(self):
        response = self.client.get('/adoptors')
        self.assertIn(b'A list of potenial Adoptors', response.data)
        self.assertIn(b'Testname', response.data)

      # Ensure that list-adoptions response is correct
    def test_list_adoptions(self):
        response = self.client.get('/list-adoptions', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /list-adoptions page loads correctly
    def test_list_adoptions_page_loads(self):
        response = self.client.get('/list-adoptions')
        self.assertIn(b'List of past adoptions', response.data)
        self.assertIn(b'Testname</span></mark>\thas adopted  <mark><span class="text-success">Testpup</span></mark> from <mark><span class="text-danger">Testshelter', response.data)

     # Ensure that /new-puppy response is correct
    def test_new_puppy_adoptions(self):
        response = self.client.get('/new-puppy', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /new-puppy page loads correctly
    def test_new_puppy_page_loads(self):
        response = self.client.get('/new-puppy')
        self.assertIn(b'Check a puppy in to a shelter', response.data)

     # Ensure that /new-shelterresponse is correct
    def test_new_shelter_adoptions(self):
        response = self.client.get('/new-shelter', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /new-puppy page loads correctly
    def test_new_shelter_page_loads(self):
        response = self.client.get('/new-shelter')
        self.assertIn(b'Add a shelter', response.data)


    def test_add_new_adoptor(self):
        response = self.client.post('/new-adoptor', data=dict(name='Jefftest'))
        self.assertEqual(response.status_code, 302)
        

    # def test_new_adoptor_page_loads(self):
    #     response = self.client.get('/adoptors')
    #     self.assertIn(b'Jefftest', response.data)



# if __name__ == '__main__':
#     # unittest.main()
#     suite = unittest.TestLoader().loadTestsFromTestCase(FlaskTestCase)
#     unittest.TextTestRunner(verbosity=2).run(suite)