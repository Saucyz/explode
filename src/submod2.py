from module import Module

class SubMod2(Module):
	#Constructor
	def __init__(self):
		Module.__init__(self, 'submod2')
		self.instructions = ['UP','UP','DOWN','DOWN','LEFT','RIGHT','LEFT','RIGHT','BUTTONB','BUTTONA']
		self.instruction_index = 0

	def resetModule(self):
		self.changeStateIncomplete()
		self.instruction_index = 0
		self.input = 0

	def getCurrentInstruction(self):
		return self.instructions[self.instruction_index]

	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
			#No input yet
			if(self.input == 0):
				pass
			else:
				#Enter Konami code
				if(self.input == self.getCurrentInstruction()):
					self.instruction_index += 1
					if(self.instruction_index >= len(self.instructions)):
						self.changeStateComplete()
				#Other inputs cause strike
				else:
					self.changeStateStrike()
					self.instruction_index = 0
					print('Enter KONAMI code on Wiimote')
			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0
