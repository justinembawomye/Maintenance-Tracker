from flask_testing import TestCase
from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

####################################################################################
#
#       The TestCreateRequests class contains all the tests that need to be run for 
#       Create Request API
#
####################################################################################


class TestCreateRequests(BaseTest):

    # Check if URL path exists and is protected
	def test_if_URL_exists(self):
		response = self.client.post('/api/v1/users/requests' )
		assert "401 UNAUTHORIZED" ==response.status

	#Test for non authenticated user
	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.post('/api/v1/users/requests')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	# Test for authenticated user but no parameters
	def test_api_when_no_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':self.get_auth_token()}
			response = self.client.post('/api/v1/users/requests',headers = head,data=json.dumps({}) )
			reply = json.loads(response.data.decode())
			self.assertEquals(reply['success'],False)
			self.assertEquals(reply['message'],'All fields required.')

	# Test for authenticated and parameters provided
	def test_api_when_parameters_have_been_passed(self):
		with self.client:
			head={'Authorization':self.get_auth_token(),'content_type':'application/json'}
			request={'title': 'Range Rover','type': 'Repair','category': 'Cars','status':'Completed'}
			response = self.client.post('/api/v1/users/requests',headers=head,data=json.dumps(request))
			reply = json.loads(response.data.decode())
			assert "200 OK" ==response.status
			self.assertEquals(reply['success'],True)
			self.assertEquals(reply['message'],'Your request was submitted successfully.')