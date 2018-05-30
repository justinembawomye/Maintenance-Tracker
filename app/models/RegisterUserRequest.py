class RegisterUserRequest:
	def __init__(self, firstName,lastName,email,username,password):
		self.firstName=firstName
		self.lastName=lastName
		self.email=email
		self.username=username
		self.password=password

	def testDictionary(self):
		self.testData ={}
		
		return 	{
		'first_name' : self.firstName,
		'last_name' : self.lastName,
		'email' : self.email,
		'username' : self.username,
		'password' : self.password
		}