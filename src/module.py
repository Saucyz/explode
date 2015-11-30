from PyQt5 import QtWidgets

class Module(QtWidgets.QWidget):
	def __init__(self, modname):
		super(Module, self).__init__()
		self.name = modname
		self.state = 'INCOMPLETE'
		self.input = 0

	def getName(self):
		return self.name

	def getState(self):
		return self.state

	def changeState(self, changestate):
		self.state = changestate

	def changeStateIncomplete(self):
		self.changeState('INCOMPLETE')

	def changeStateComplete(self):
		self.changeState('COMPLETE')

	def changeStateStrike(self):
		self.changeState('STRIKE')

	def changeInput(self, userinput):
		self.input = userinput

