from flask_testing import TestCase
from app.models.UserRequest import UserRequest 
from routes import app
import unittest
import json

class TestFlaskUserRequests(TestCase):
	def create_app(self):
		return app

	def tearDown(self):
		print("===> Tearing down after tests")

	def test_index(self):
		response = self.client.get('/')
		assert "200 OK" ==response.status

	def test_api_requests(self):
		response= self.client.get('/')
		test_request = UserRequest(20003,"Range Rover","Repair","Cars","Completed").testDictionary()
		test_request2 = UserRequest(20004,"Samsung S7","Repair","Phones and Tablet","In Progress").testDictionary()
		self.assertEquals(response.json, [test_request,test_request2])

   

