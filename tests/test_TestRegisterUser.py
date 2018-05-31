from flask import json
from app.tests.API.base_test import BaseTest

class TestRegisterUser:
	def test_response_status(self):
		response = self.create_user(self.USER_DETAILS)
		self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 201)
    def test_response_messages(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertTrue(data is not None)
            self.assertEqual(data['message'], 'User registered successfully.')

    def test_token_returned(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertTrue(data['auth_token'])

    def test_user_exists(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            self.assertEqual(response.status_code, 201)
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 403)
            self.assertEqual(data['message'], 'User already exists!')

    def test_missing_params(self):
        with self.client:
            response = self.create_user({})
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data['message'], 'Missing required parameters.')