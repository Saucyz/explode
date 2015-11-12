from module import Module

class SubMod1(Module):
	#Constructor
	def __init__(self):
		Module.__init__(self, 'submod1')

	#Resets module
	def resetModule(self):
		self.changeStateIncomplete()
		self.input = 0

	#Runs module minigame
	def check(self):
		#No input yet
		if(self.input == 0):
			pass
		else:
			#Win if enter 1, strike otherwise.
			if(self.input == '1'):
				self.changeStateComplete() 
			#Other inputs cause strike
			else:
				self.changeStateStrike()
			print('Submod1 current state: ' + self.getState())
			print('Reset')
			self.resetModule()
			print('Submod1 current state: ' + self.getState())
