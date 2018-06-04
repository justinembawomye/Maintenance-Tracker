from flask_testing import TestCase
from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

class TestModifyRequests(BaseTest):

	def test_if_URL_exists(self):
		response = self.client.put('/api/v1/users/requests/0' )
		assert "200 OK" ==response.status

	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.put('/api/v1/users/requests/0')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	def test_api_when_no_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':'123'}
			response = self.client.put('/api/v1/users/requests/0',headers = head )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply,{
        'success':False,
        'message':"Not a valid Request ID."
        })

	def test_api_when_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':'123'}
			request={'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'}
			response = self.client.put('/api/v1/users/requests/0',headers = head,data=request )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply,{
        'success':False,
        'message':"Not a valid Request ID."
        })

   

