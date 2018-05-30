class UserRequest:
	def __init__(self, requestId,requestTitle,requestType,requestCategory,requestStatus):
		self.requestId=requestId
		self.requestTitle=requestTitle
		self.requestType=requestType
		self.requestCategory=requestCategory
		self.requestStatus=requestStatus

	def testDictionary(self):
		self.testData ={}
		
		return 	{
		'id' : self.requestId,
		'title' : self.requestTitle,
		'type' : self.requestType,
		'category' : self.requestCategory,
		'status' : self.requestStatus
		}





	
