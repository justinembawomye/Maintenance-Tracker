from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify
from app.models.Responses import * 
from functools import wraps
from flask import request

class DataStore:

	#Initialize Data Store with Dummy Data If Necessary
	def __init__(self,users=[],requests=[]):
		self.users=users
		self.requests=requests
		self.key="this_is_my_key"

	#Methods handling CRUD operations for Requests
	def modifyRequest(self, user_request):
		i=0
		for req in self.requests:
			if req.getId() == user_request.getId():
				self.requests[i]=user_request
				return user_request.getDictionary()
			i=i+1
		return None

	def addRequest(self, req):
		self.requests.append(req)
		return req

	def getRequestSize(self):
		return len(requests)

	def getAllUsers(self):
		return self.users

	def getAllRequestsForUser(self,user):
		response=[]
		for req in self.requests:
			if req.getOwner() == user:
				response.append(req.getDictionary())
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

	#Checking Authorization 
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