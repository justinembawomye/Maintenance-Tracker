from flask_testing import TestCase
from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

####################################################################################
#
#       The TestModifyRequests class contains all the tests that need to be run for 
#       Modify Request API
#
####################################################################################

class TestModifyRequests(BaseTest):

	#Check if URL path exists and is protected
	def test_if_URL_exists(self):
		response = self.client.put('/api/v1/users/requests/0' )
		assert "401 UNAUTHORIZED" ==response.status

	#test for a non authorized user
	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.put('/api/v1/users/requests/0')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	#Test for authorised user with no parameters
	def test_api_when_no_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':self.get_auth_token()}
			response = self.client.put('/api/v1/users/requests/0',headers = head,data=json.dumps({})  )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply['success'],False)
			self.assertEquals(reply['message'],'All fields required.')

	#Test for authenticated user with parameters
	def test_api_when_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':self.get_auth_token()}
			request={'title': 'Range Rover','type': 'Repair','category': 'Cars','status':'Completed'}
			response = self.client.put('/api/v1/users/requests/{}'.format(self.get_request_id()),headers = head,data=json.dumps(request))
			reply = json.loads(response.data.decode())
			assert "200 OK" ==response.status
			self.assertEquals(reply['success'],True)
			self.assertEquals(reply['message'],"Your request was submitted successfully.")

   

