class UserRequest:
	def __init__(self, requestId,requestTitle,requestType,requestCategory,requestStatus):
		self.requestId=requestId
		self.requestTitle=requestTitle
		self.requestType=requestType
		self.requestCategory=requestCategory
		self.requestStatus=requestStatus

	def testDictionary(self):
		self.testData ={}
		self.testData['id']=self.requestId
		self.testData['title']=self.requestTitle
		self.testData['type']=self.requestType
		self.testData['category']=self.requestCategory
		self.testData['status']=self.requestStatus
		return 	str(self.testData)





	
