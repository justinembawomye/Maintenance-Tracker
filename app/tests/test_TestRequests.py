from flask_testing import TestCase
#from app.models.UserRequest import UserRequest 

from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

class TestUserRequests(BaseTest):

	def test_if_URL_exists(self):
		response = self.client.get('/api/v1/users/requests')
		assert "401 UNAUTHORIZED" ==response.status

	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.get('/api/v1/users/requests')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	def test_api_check_requests(self):
		with self.client:
			head={'Authorization':self.get_auth_token()}
			response = self.client.get('/api/v1/users/requests',headers = head)
			reply = json.loads(response.data.decode())
			self.assertEquals(reply[1]['category'] ,'Cars')
			self.assertEquals(reply[1]['status'],'In Progress')
			self.assertEquals(reply[1]['title'],'Range Rover')
			self.assertEquals(reply[1]['type'],"Repair")

   

