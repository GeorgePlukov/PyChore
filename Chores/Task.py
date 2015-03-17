# Contains a list of subtasks per task
class Task:
	taskDescription = ""
	subtaskList = []
	def __init__ (self, description, subtasks):
		self.description = description
		self.subtaskList = subtasks

# Holds a specific subtasks description
class Subtask:
	description = ""

	def __init__(sefl, description):
		self.description = description

	def getDescription():
		return description