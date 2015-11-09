from module import Module

class SubMod1(Module):
	def __init__(self):
		Module.__init__(self, 'submod1')

	def resetModule(self):
		self.changeStateIncomplete()

	#Temporary get console input
	def consoleInput(self):
		self.getInput(input('Type a number from 0 to 9: '))

	def submod1main(self):
		while True:
			#win if enter 1, strike otherwise.
			self.consoleInput()
			if (self.input == '1'):
				self.changeStateComplete() 
			else:
				self.changeStateStrike()
			print('Submod1 current state: ' + self.getState())
			print('Reset')
			self.changeStateIncomplete()
			print('Submod1 current state: ' + self.getState())
