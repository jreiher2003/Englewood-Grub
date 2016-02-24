import unittest 
from base import BaseTestCase 
from app import app,db 
from app.models import Place

class TestFrontPage(BaseTestCase):

    def test_index_loads(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testname', response.data)

    def test_stylesheet_loads(self):
        response = self.client.get('/static/styles.css', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_place_database(self):
    	place = Place.query.filter_by(id=1).one()
    	self.assertEqual(place.id, 1)
    	self.assertEqual(place.name, 'Testname')




