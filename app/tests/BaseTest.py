from unittest import TestCase
from flask import json
#from app.models.UserRequest import UserRequest
from project import app
from app.models.User import User

class BaseTest(TestCase):
    
    def create_app(self):
        return app
	##Setup Client and Context
    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()
        #self.token=self.test_api_when_parameters_have_been_passed()
       # self.registerUser()
  
    def tearDown(self):
        self.context.pop()

    def get_auth_token(self):
        head={'Content-Type':'application/json'}      
        response = self.client.post('/api/v1/login',content_type='application/json' ,data=json.dumps(dict(username='Sam',password='123')))
        reply = json.loads(response.data.decode())
        self.assertEquals(reply['success'],True)
        if reply['success']:
            return reply['token']
        else:
            return None

    def get_request_id(self):
        head={'Authorization':self.get_auth_token(),'content_type':'application/json'}
        request={'title': 'Range Rover','type': 'Repair','category': 'Cars','status':'Completed'}
        response = self.client.post('/api/v1/users/requests',headers=head,data=json.dumps(request))
        reply = json.loads(response.data.decode())
        assert "200 OK" ==response.status
        if reply['success']:
            return reply['data']['id']


       

    