from flask import json
from app.tests.API.BaseTest import BaseTest

class TestLogin(BaseTestCase):
    def test_response_status(self):
        with self.client:
            response = self.login_user(self.USER_CREDENTIALS['username'], self.USER_CREDENTIALS['password'])
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_response_messages(self):
        with self.client:
            response = self.login_user(self.USER_CREDENTIALS['username'], self.USER_CREDENTIALS['password'])
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'], 'User successfully Logged in.')

    def test_token_returned(self):
        with self.client:
            response = self.login_user(self.USER_CREDENTIALS['username'], self.USER_CREDENTIALS['password'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['auth_token'])

    def test_invalid_credentials(self):
        with self.client:
            response = self.login_user('some_username', 'some_password')
            data = json.loads(response.data.decode())
            self.assertTrue(response is not None)
            self.assertEqual(response.status_code, 403)
            self.assertEqual(data['message'], 'Invalid username or password')

    def test_empty_credentials(self):
        with self.client:
            response = self.login_user('', '')
            data = json.loads(response.data.decode())
            self.assertTrue(response is not None)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data['message'], 'Username and password required.')
