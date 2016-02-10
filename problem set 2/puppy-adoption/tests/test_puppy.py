import unittest
from base import BaseTestCase


class TestPuppyCase(BaseTestCase):



# Ensure that /new-puppy response is correct
    def test_new_puppy_adoptions(self):
        response = self.client.get('/new-puppy', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /new-puppy page loads correctly
    def test_new_puppy_page_loads(self):
        response = self.client.get('/new-puppy')
        self.assertIn(b'Check a puppy in to a shelter', response.data)