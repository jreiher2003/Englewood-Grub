import unittest
from base import BaseTestCase


class TestAdoptorCase(BaseTestCase):
	 # Ensure that /adoptors response correctly
    def test_adoptors(self):
        response = self.client.get('/adoptors', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the /adoptors page loads correctly
    def test_adoptors_page_loads(self):
        response = self.client.get('/adoptors')
        self.assertIn(b'A list of potenial Adoptors', response.data)
        self.assertIn(b'Testname', response.data)

      # Ensure that /new-shelterresponse is correct
    def test_new_adoptor(self):
        response = self.client.get('/new-adoptor', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add_new_adoptor(self):
        response = self.client.post('/new-adoptor', data=dict(name='Jefftest'), follow_redirects=True)
        self.assertIn(b'<strong>Just created</strong> a new adoptor named <u>Jefftest</u>', response.data)

    def test_add_new_adoptor_from_index(self):
        response = self.client.post('/', data=dict(name='Jefftest1'), follow_redirects=True)
        self.assertIn(b'<strong>Just created</strong> a new adoptor named <u>Jefftest1</u>', response.data)

    def test_adoptors_delete_status(self):
        response = self.client.get('/adoptors/profile/2/delete', content_type='html/text')
        self.assertEqual(response.status_code, 301)

    def test_adoptors_edit_status(self):
        response = self.client.get('/adoptors/profile/2/edit', content_type='html/text')
        self.assertEqual(response.status_code, 301)