class UserLoginRequest:
	def __init__(self, username,password):
		self.username=username
		self.password=password

	def testDictionary(self):
		return 	{
		'id' : self.username,
		'title' : self.password,
		}

	def onSuccess(self):
		return{
		'success':true,
		'message':"Login Succesful.",
		'token':123
		}