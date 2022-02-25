class Bank:
	minbal=1000
	"""docstring for ClassName"""
	def __init__(self, acno,name,bal):
		self.acno=acno
		self.bal=bal
		self.name=name

	@classmethod
	def change_minbal(cls,amount):
		cls.minbal=amount
	
	@classmethod
	def from_string(cla,instr):
		acno,name,bal=instr.split('-')
		return clas(acno,name,bal)

	@staticmethod
	def workday(day):
		if day.weekday()==5
