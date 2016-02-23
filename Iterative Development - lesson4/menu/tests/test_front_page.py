import unittest 
from base import BaseTestCase 

class TestFrontPage(BaseTestCase):

    def test_index_loads(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.data)

    def test_stylesheet_loads(self):
        response = self.client.get('/static/styles.css', content_type='html/text')
        self.assertEqual(response.status_code, 200)

