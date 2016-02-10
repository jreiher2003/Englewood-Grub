import unittest
from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

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
    
     
      # Ensure that list-adoptions response is correct
    def test_list_adoptions(self):
        response = self.client.get('/list-adoptions', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /list-adoptions page loads correctly
    def test_list_adoptions_page_loads(self):
        response = self.client.get('/list-adoptions')
        self.assertIn(b'List of past adoptions', response.data)
        self.assertIn(b'Testname</span></mark>\thas adopted  <mark><span class="text-success">Testpup</span></mark> from <mark><span class="text-danger">Testshelter', response.data)

     

    


   


        
