from unittest import TestCase
from flask import json
from app.models.UserLoginRequest import UserLoginRequest
from app.models.RegisterUserRequest import RegisterUserRequest
from app.models.UserRequest import UserRequest
from project import app
#from app import create_app
class BaseTest(TestCase):

    USER_LOGIN_DETAILS = UserLoginRequest("Bes","1234567890").testDictionary()
    USER_REGISTRATION_DETAILS = RegisterUserRequest("Besufekad","Shifferaw","besufekadsm@gmail.com","Bes","1234567890").testDictionary()
    TEST_USER_REQUEST=UserRequest(20003,"Range Rover","Repair","Cars","Completed").testDictionary()
    
    def create_app(self):
        return app
	##Setup Client and Context
    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()
        #self.new_user = self.create_user(USER_REGISTRATION_DETAILS)

    def create_user(self, data):
        return self.client.post(
            '/api/v1/register',
            data=json.dumps(data),
            content_type='application/json'
        )
    def login_user(self, username, password):
        return self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(dict(
                username=username,
                password=password
            )),
            content_type='application/json'
        )       
    def tearDown(self):
        self.context.pop()

    