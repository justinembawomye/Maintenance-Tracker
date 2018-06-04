from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify
from app.models.Responses import * 
from functools import wraps
from flask import request

class DataStore:

	def __init__(self,users=[],requests=[]):
		self.users=users
		self.requests=requests
		self.username_table = {u.username: u for u in users}
		self.key="this_is_my_key"
		#jwt = JWT(app, authenticate, identity)
		#self.jwt = JWT(app, authenticate)

	def checkIfUserExists(self,user):
		return {user.username: user for user in self.users}

	# def addUser(self,user):
	# 	self.users.append(user)

	# def removeUser(self,user):
	

	# def modifyUser(self,user):
		

	# def addRequest(self,request):
	# 	self.requests.append()

	# def removeRequest(self,request):
		

	# def modify(self,user):
	# 	del self.users[]
	def addRequest(self, req):
		self.requests.append(req)
		return req

	def getAllUsers(self):
		return self.users

	def getAllRequestsForUser(self,user):
		response=[]
		for req in self.requests:
			print(user)
			if req.getOwner() == user:
				response.append(req.testDictionary())
		return response

	def getASpecificRequestsForUser(self,requestId):
		for req in self.requests:
			if req.getId() == requestId:
				return req.testDictionary()
		return None

	def searchList(self,username):
		for item in self.users:
			if item.getUserName() == username:
				return item
			else:
				return None


	def generate_auth_token(self, user):
		try:
			payload ={
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1200),
                'iat': datetime.datetime.utcnow(),
                'user': user
            }
			return  jwt.encode(
                payload,
                self.key,
                algorithm='HS256'
            ).decode('utf-8')
		except Exception as e:
			return e

	def token_required(self,func):
		@wraps(func)
		def decorated(*args,**kwargs):
			token = None
			if "Authorization" in request.headers:
				token =request.headers['Authorization']
			else:
				return jsonify(login_fail), 401

			try:
				data = jwt.decode(token,self.key)
				current_user = self.searchList(data['user']['username'])

			except:
				return jsonify(login_fail), 401

			return func(current_user,*args,**kwargs)
		return decorated

	# @staticmethod
	# def verify_auth_token(auth_token):
	# 	try:
	# 		payload = jwt.decode(auth_token, Config.SECRET_KEY)
	# 		return payload['sub']
	# 	except jwt.ExpiredSignatureError:
	# 		return "Signature expired, please log in again!"
	# 	except jwt.InvalidTokenError:
	# 		return "Invalid token! Try again."

	# def authenticate(username, password):
 #    	user = self.username_table.get(username, None)
 #    	if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
 #        	return user