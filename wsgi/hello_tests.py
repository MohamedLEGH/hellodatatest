import os
import hello
import unittest
import tempfile

page_test = "https://facebook.en.aptoide.com/"

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        hello.app.testing = True
        self.app = hello.app.test_client()

    def tearDown(self):
        pass

    def test_get(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_post(self):
        rv = self.app.post('/',data=dict(aptoide_search=page_test))
        assert rv.status_code == 200

    def test_api(self):
        rv = self.app.get('/api/' + page_test)
        assert rv.status_code == 200


if __name__ == '__main__':
    unittest.main()
