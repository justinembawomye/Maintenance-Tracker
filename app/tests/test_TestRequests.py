from flask_testing import TestCase
#from app.models.UserRequest import UserRequest 

from project import app
import unittest
import json
from app.tests.BaseTest import BaseTest

class TestUserRequests(BaseTest):

	def test_if_URL_exists(self):
		response = self.client.get('/api/v1/requests')
		assert "200 OK" ==response.status

	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.get('/api/v1/requests')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	def test_api_check_requests(self):
		with self.client:
			head={'Authorization':'123'}
			response = self.client.get('/api/v1/requests',headers = head)
			reply = json.loads(response.data.decode())
			self.assertEquals(reply[1] ,{'category':'Phones and Tablet','id':20004,'status':'In Progress','title':'Samsung S7','type':"Repair"})

   

