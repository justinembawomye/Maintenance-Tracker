from unittest import TestCase
from flask import json
from app.models import *
from project import app

class BaseTest(TestCase):

	USER_LOGIN_DETAILS = UserLoginRequest("Bes","1234567890").testDictionary()

	USER_REGISTRATION_DETAILS = RegisterUserRequest("Besufekad","Shifferaw","besufekadsm@gmail.com","Bes","1234567890").testDictionary()

	##Setup Client and Context
	def setUp(self):
        self.app = app
        self.context = self.app..app_context()
        self.context.push()
        self.client = self.app.test_client()
        self.new_user = self.create_user(USER_REGISTRATION_DETAILS)

    def create_user(self, data):
        return self.client.post(
            '/api/v1/register',
            data=json.dumps(data),
            content_type='application/json'
        )
        
    def tearDown(self):
        self.app_context.pop()