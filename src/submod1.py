from module import Module

class SubMod1(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod1')

	#Resets module
	def resetModule(self):
		self.changeStateIncomplete()
		self.input = 0

	#Runs module minigame
	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
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
			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0
