#
#

#
#
class Chore:
	# Is the task completed or not
	# Task List
	def __init__ (self,description, completed, user):
		self.description = description
		self.completed = completed
		self.user = user

	def isCompleted(self):
		return self.completed
	def setCompleted(self, completed):
		self.completed = completed
	def getUser(self):
		return self.user
	def setUser(self, user):
		self.user = user

