# from flask_testing import TestCase
# from project import app
# import unittest
# import json
# from app.tests.BaseTest import BaseTest

# class TestLoginRequest(BaseTest):

# 	def test_if_URL_exists(self):
# 		response = self.client.post('/api/v1/login' )
# 		assert "200 OK" ==response.status

# 	def test_api_when_no_parameters_have_been_passed(self):
# 		with self.client:
# 			response = self.client.post('/api/v1/login' )
# 			reply = json.loads(response.data.decode())
# 			self.assertEquals(reply['success'],False)
# 			self.assertEquals(reply['message'],"Login Failed.")

# 	def test_api_when_parameters_have_been_passed(self):
# 		with self.client:
			
# 			request={'username': 'Sam','password': '123'}
# 			response = self.client.post('/api/v1/login',data=request )
# 			reply = json.loads(response.data.decode())

# 			self.assertEquals(reply['success'],True)
# 			self.assertEquals(reply['message'],"User loged In.")
# 			if(reply['success']==true):
# 				self.token=reply['token']
       

   

