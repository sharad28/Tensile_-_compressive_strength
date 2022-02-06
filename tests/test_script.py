import unittest

from app import app
import os


class TestToPerform(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_page1(self):
        response = self.app.get('/test', follow_redirects=True)
        print(response)
        print("*******************"
              "************************"
              "*********************")

        print(response.json)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
