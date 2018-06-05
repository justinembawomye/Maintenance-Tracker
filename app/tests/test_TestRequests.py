from flask_testing import TestCase
#from app.models.UserRequest import UserRequest 

from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

####################################################################################
#
#       The TestUserRequests class contains all the tests that need to be run for 
#       Create Request API
#
####################################################################################

class TestUserRequests(BaseTest):

	# Check if URL path exists and is protected
	def test_if_URL_exists(self):
		response = self.client.get('/api/v1/users/requests')
		assert "401 UNAUTHORIZED" ==response.status

	# Test For a non authenticated user
	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.get('/api/v1/users/requests')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	# Test for authenticated user
	def test_api_check_requests(self):
		with self.client:
			head={'Authorization':self.get_auth_token()}
			response = self.client.get('/api/v1/users/requests',headers = head)
			reply = json.loads(response.data.decode())
			assert "200 OK" ==response.status
			self.assertEquals(reply[1]['category'] ,'Cars')
			self.assertEquals(reply[1]['status'],'In Progress')
			self.assertEquals(reply[1]['title'],'Range Rover')
			self.assertEquals(reply[1]['type'],"Repair")