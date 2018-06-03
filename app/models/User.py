from passlib.apps import custom_app_context as pwd_context

class User:
	def __init__(self, firstName,lastName,email,username,password):
		self.firstName=firstName
		self.lastName=lastName
		self.email=email
		self.username=username
		self.password=hash_password(password)
		self.token =generate_auth_token(username)

	def getFirstName(self):
		return self.firstName

	def getLastName(self):
		return self.lastName

	def getEmail(self):
		return self.email

	def getUserName(self):
		return self.username

	def getPassword(self):
		return self.password

	def setFirstName(self,firstName):
		self.firstName=firstName

	def setLastName(self,lastName):
		self.lastName=lastName

	def setEmail(self,email):
		self.email=email

	def setUsername(self,username):
		self.username=username

	def setPassword(self,password):
		self.password=password

	def hash_password(self, password):
		return pwd_context.encrypt(password)

	def getDictionary():		
		return{
		'first_name' : self.firstName,
		'last_name' : self.lastName,
		'email' : self.email,
		'username' : self.username,
		'token':self.token
		}
	def verify_password(self, password):
		return pwd_context.verify(password, self.password)

	def generate_auth_token(self, user_id):
		try:
			payload ={
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=1200),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
			return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
		except Exception as e:
			return e

	@staticmethod
	def verify_auth_token(auth_token):
		try:
			payload = jwt.decode(auth_token, Config.SECRET_KEY)
			return payload['sub']
		except jwt.ExpiredSignatureError:
			return "Signature expired, please log in again!"
		except jwt.InvalidTokenError:
			return "Invalid token! Try again."
