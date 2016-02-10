import unittest
from base import BaseTestCase


class TestShelterCase(BaseTestCase):

	 # Ensure that /new-shelterresponse is correct
    def test_new_shelter_adoptions(self):
        response = self.client.get('/new-shelter', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /new-puppy page loads correctly
    def test_new_shelter_page_loads(self):
        response = self.client.get('/new-shelter')
        self.assertIn(b'Add a shelter', response.data)
