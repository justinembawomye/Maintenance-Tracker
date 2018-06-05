from unittest import TestCase
from flask import json
from project import app
from app.models.User import User
####################################################################################
#
#       The Base Case class comtains all the functions that need to be run in 
#       every API request and inherited by all API end point classes
#
####################################################################################


class BaseTest(TestCase):

    # Setup Client and Context for test
    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()
  
    # Release Context
    def tearDown(self):
        self.context.pop()

    # Create token from login for testing pourposes
    def get_auth_token(self):
        response = self.client.post('/api/v1/login',content_type='application/json', data=json.dumps(dict(username='Sam', password='123')))
        reply = json.loads(response.data.decode())
        self.assertEquals(reply['success'],True)
        if reply['success']:
            return reply['token']
        else:
            return None

    # Get Request Id for Test Pourposes
    def get_request_id(self):
        head={'Authorization':self.get_auth_token(),'content_type':'application/json'}
        request={'title': 'Range Rover','type': 'Repair','category': 'Cars','status':'Completed'}
        response = self.client.post('/api/v1/users/requests',headers=head,data=json.dumps(request))
        reply = json.loads(response.data.decode())
        assert "200 OK" ==response.status
        if reply['success']:
            return reply['data']['id']