import unittest
import os
from app.config import basedir
from app import app, db

class TestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_hello(self):
        rv = self.app.get('/make_event')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_name(self):
        rv = self.app.get('/events')
        self.assertEqual(rv.status, '200 OK')
        
if __name__ == '__main__':
    print('Running tests')
    unittest.main()