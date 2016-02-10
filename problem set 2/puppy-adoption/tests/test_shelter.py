import unittest
from base import BaseTestCase


class TestShelterCase(BaseTestCase):

	# Ensure that the login page loads correctly
    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertIn(b'Welcome to our puppy adoption web app!', response.data)
        self.assertIn(b'Testshelter', response.data)


    # Ensure that the shelter profile loads correctly
    def test_shelter_profile_page_loads(self):
        response = self.client.get('/1/testshelter/page/1')
        self.assertIn(b'Testshelter', response.data)
        self.assertIn(b'123 Fake st.', response.data)
        self.assertIn(b'Fake', response.data)
        self.assertIn(b'http://test.com', response.data)
        self.assertIn(b'Testpup', response.data)

	 # Ensure that /new-shelterresponse is correct
    def test_new_shelter_adoptions(self):
        response = self.client.get('/new-shelter', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /new-puppy page loads correctly
    def test_new_shelter_page_loads(self):
        response = self.client.get('/new-shelter')
        self.assertIn(b'Add a shelter', response.data)
