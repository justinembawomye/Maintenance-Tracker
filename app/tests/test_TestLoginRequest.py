from flask_testing import TestCase
from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

class TestLoginRequest(BaseTest):

	def test_if_URL_exists(self):
		response = self.client.put('/api/v1/login' )
		assert "200 OK" ==response.status

	def test_api_when_no_parameters_have_been_passed(self):
		with self.client:
			response = self.client.post('/api/v1/login' )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply,{
        'success':False,
        'message':"Login Failed."
        })

	def test_api_when_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':'123'}
			request={'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'}
			response = self.client.put('/api/v1/login',headers = head,data=request )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply,{
        'success':False,
        'message':"Not a valid Request ID."
        })

   

