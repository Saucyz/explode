from module import Module
from PyQt5 import QtWidgets, QtGui

class SubMod4(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod4')
		
		self.init = 1
		self.background = QtWidgets.QLabel()
		#self.label.setGeometry(10,10,100,200)

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.background, 0, 0, 100, 100)
		reader = QtGui.QImageReader("pie.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label.setPixmap(qpixmap)

	def resetModule(self):
		self.changeStateIncomplete()
		self.input = 0

	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
			#No input yet
			if(self.input == 0):
				pass
			else:
				if self.init == 1:
					self.buttonText = randint(1,4)
					self.buttonColour = randint(1,4)
					self.stripColour = randint(1,4)
					self.init = 0
				else:
					if self.buttonColour == 1 and self.buttonText == 1: #Blue, Abort
						pass
					elif self.buttonText == 2: #Detonate
						if self.input == 'BUTTONA'
							self.changeStateComplete()
					elif self.buttonColour == 2: #white
						pass
					elif self.buttonColour == 3: #yellow
						if self.input == 'BUTTONA'
							self.changeStateComplete()
					elif self.buttonColour == 4 and self.buttonText == 3: #red, hold
						if self.input == 'BUTTONA'
							self.changeStateComplete()
					else:
						pass

					if self.stripColour == 1: #Blue
						if self.input == 'BUTTONA':
							if BombTimer.secs%4 == 0:
								self.changeStateComplete()
							else:
								self.changeStateStrike()
					elif self.stripColour == 2: #White
						if self.input == 'BUTTONA':
							if BombTimer.secs%5 == 0:
								self.changeStateComplete()
							else:
								self.changeStateStrike()
					elif self.stripColour == 3: #Yellow
						if self.input == 'BUTTONA':
							if BombTimer.secs%6 == 0:
								self.changeStateComplete()
							else:
								self.changeStateStrike()
					else:
						if self.input == 'BUTTONA':
							if BombTimer.secs%3 == 0:
								self.changeStateComplete()
							else:
								self.changeStateStrike()





			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0
