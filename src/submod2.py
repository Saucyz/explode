from module import Module
from PyQt5 import QtWidgets, QtGui

class SubMod2(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod2')
		self.instructions = ['UP','UP','DOWN','DOWN','LEFT','RIGHT','LEFT','RIGHT','BUTTONB','BUTTONA']
		self.instruction_index = 0
		self.label = QtWidgets.QLabel()
		#self.label.setGeometry(10,10,100,200)

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.label, 0, 0, 100, 100)
		reader = QtGui.QImageReader("pie.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label.setPixmap(qpixmap)

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
