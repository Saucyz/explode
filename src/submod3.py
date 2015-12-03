from module import Module
from PyQt5 import QtWidgets, QtGui
from random import randint
"""
Manual:

Stage 1:
If the display is 1, press the button in the first position.
If the display is 2, press the button in the second position.
If the display is 3, press the button in the third position.

Stage 2:
If the display is 1, press the button labeled "3".
If the display is 2, press the button in the same position as you pressed in stage 1.
If the display is 3, press the button in the first position.


Stage 3:
If the display is 1, press the button with the same label you pressed in stage 1.
If the display is 2, press the button in the third position.
If the display is 3, press the button labeled "3".

Stage 4:
If the display is 1, press the button in the same position as you pressed in stage 1.
If the display is 2, press the button in the same position as you pressed in stage 2.
If the display is 3, press the button in the same position as you pressed in stage 3.
"""

class SubMod3(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod3')
		
		stage = 0

		self.background = QtWidgets.QLabel()
		self.button1 = QtWidgets.QPushButton()
		self.button2 = QtWidgets.QPushButton()
		self.button3 = QtWidgets.QPushButton()
		self.displayNum = QtWidgets.QLabel()

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.background, 0, 0, 100, 100)
		grid.addWidget(self.button3, 2, 3)
		grid.addWidget(self.button2, 2, 2)
		grid.addWidget(self.button1, 2, 1)
		grid.addWidget(self.displayNum, 1, 2)

		reader = QtGui.QImageReader("pie.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.background.setPixmap(qpixmap)

	def resetModule(self):
		self.changeStateIncomplete()
		self.input = 0

	def correctAns(self):
		stage = stage + 1

	def incorrectAns(self);
		self.changeStateStrike()

	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
			#No input yet
			if(self.input == 0):
				pass
			else:
				if stage == 0:
					orderStage0 = randint(1,6)
					displayStage0 = randint(1,3)

					if displayStage0 == 1:
						self.displayNum = QtWidgets.QLabel("1")
					elif displayStage0 == 2:
						self.displayNum = QtWidgets.QLabel("2")
					elif displayStage0 == 3:
						self.displayNum = QtWidgets.QLabel("3")

					if orderStage0 = 1:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("3")
						if displayStage0 == 1:
							labelStage0 = 1
						elif displayStage0 == 2:
							labelStage0 = 2
						elif displayStage0 == 3:
							labelStage0 = 3
					elif orderStage0 = 2:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("2")
						if displayStage0 == 1:
							labelStage0 = 1
						elif displayStage0 == 2:
							labelStage0 = 3
						elif displayStage0 == 3:
							labelStage0 = 2
					elif orderStage0 = 3:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("3")
						if displayStage0 == 1:
							labelStage0 = 2
						elif displayStage0 == 2:
							labelStage0 = 1
						elif displayStage0 == 3:
							labelStage0 = 3
					elif orderStage0 = 4:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("1")
						if displayStage0 == 1:
							labelStage0 = 2
						elif displayStage0 == 2:
							labelStage0 = 3
						elif displayStage0 == 3:
							labelStage0 = 1
					elif orderStage0 = 5:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("2")
						if displayStage0 == 1:
							labelStage0 = 3
						elif displayStage0 == 2:
							labelStage0 = 1
						elif displayStage0 == 3:
							labelStage0 = 2
					elif orderStage0 = 6:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("1")
						if displayStage0 == 1:
							labelStage0 = 3
						elif displayStage0 == 2:
							labelStage0 = 2
						elif displayStage0 == 3:
							labelStage0 = 1

					self.show()

					if displayStage0 == 1:
						self.button1.clicked.connect(self.correctAns)
						self.button2.clicked.connect(self.incorrectAns)
						self.button3.clicked.connect(self.incorrectAns)
					elif displayStage0 == 2:
						self.button1.clicked.connect(self.incorrectAns)
						self.button2.clicked.connect(self.correctAns)
						self.button3.clicked.connect(self.incorrectAns)
					elif displayStage0 == 3:
						self.button1.clicked.connect(self.incorrectAns)
						self.button2.clicked.connect(self.incorrectAns)
						self.button3.clicked.connect(self.correctAns)

					
				elif stage == 1:
					orderStage1 = randint(1,6)
					displayStage1 = randint(1,3)

					if displayStage1 == 1:
						self.displayNum = QtWidgets.QLabel("1")
					elif displayStage1 == 2:
						self.displayNum = QtWidgets.QLabel("2")
					elif displayStage1 == 3:
						self.displayNum = QtWidgets.QLabel("3")

					if orderStage1 = 1:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage1 = 2:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage1 = 3:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage1 = 4:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("1")
					elif orderStage1 = 5:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage1 = 6:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("1")

					self.show()

					if displayStage1 == 1:
						if orderStage1 == 5 or orderStage1 == 6:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
							posState1 = 3
						if orderStage1 == 1 or orderStage1 == 3:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState1 = 1
						if orderStage1 == 2 or orderStage1 == 4:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState1 = 2
					elif displayStage1 == 2:
						if displayStage0 == 1:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState1 == 1
						elif displayStage0 == 2:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState1 == 2
						elif displayStage0 == 3:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
							posState1 == 3
					elif displayStage1 == 3:
						self.button1.clicked.connect(self.correctAns)
						self.button2.clicked.connect(self.incorrectAns)
						self.button3.clicked.connect(self.incorrectAns)
						posState1 = 1
				elif stage == 2:
					orderStage2 = randint(1,6)
					displayStage2 = randint(1,3)

					if displayStage2 == 1:
						self.displayNum = QtWidgets.QLabel("1")
					elif displayStage2 == 2:
						self.displayNum = QtWidgets.QLabel("2")
					elif displayStage2 == 3:
						self.displayNum = QtWidgets.QLabel("3")

					if orderStage2 = 1:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage2 = 2:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage2 = 3:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage2 = 4:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("1")
					elif orderStage2 = 5:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage2 = 6:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("1")

					self.show()

					if displayStage2 == 1:
						if labelStage0 == 1:
							if orderStage2 == 1 or orderStage2 == 2:
								self.button1.clicked.connect(self.correctAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 1
							if orderStage2 == 3 or orderStage2 == 5:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.correctAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 2
							if orderStage2 == 4 or orderStage2 == 6:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.correctAns)
								posState2 = 3
						if labelStage0 == 2:
							if orderStage2 == 3 or orderStage2 == 4:
								self.button1.clicked.connect(self.correctAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 1
							if orderStage2 == 1 or orderStage2 == 6:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.correctAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 2
							if orderStage2 == 2 or orderStage2 == 5:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.correctAns)
								posState2 = 3
						if labelStage0 == 3:
							if orderStage2 == 5 or orderStage2 == 6:
								self.button1.clicked.connect(self.correctAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 1
							if orderStage2 == 2 or orderStage2 == 4:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.correctAns)
								self.button3.clicked.connect(self.incorrectAns)
								posState2 = 2
							if orderStage2 == 1 or orderStage2 == 3:
								self.button1.clicked.connect(self.incorrectAns)
								self.button2.clicked.connect(self.incorrectAns)
								self.button3.clicked.connect(self.correctAns)
								posState2 = 3
					if displayStage2 == 2:
						self.button1.clicked.connect(self.incorrectAns)
						self.button2.clicked.connect(self.incorrectAns)
						self.button3.clicked.connect(self.correctAns)
						posState2 = 3
					if displayStage2 == 3:
						if orderStage2 == 5 or orderStage2 == 6:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState2 = 1
						if orderStage2 == 2 or orderStage2 == 4:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
							posState2 = 2
						if orderStage2 == 1 or orderStage2 == 3:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
							posState2 = 3
				elif stage == 3:
					orderStage3 = randint(1,6)
					displayStage3 = randint(1,3)

					if displayStage3 == 1:
						self.displayNum = QtWidgets.QLabel("1")
					elif displayStage3 == 2:
						self.displayNum = QtWidgets.QLabel("2")
					elif displayStage3 == 3:
						self.displayNum = QtWidgets.QLabel("3")

					if orderStage3 = 1:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage3 = 2:
						self.button1 = QtWidgets.QPushButton("1")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage3 = 3:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("3")
					elif orderStage3 = 4:
						self.button1 = QtWidgets.QPushButton("2")
						self.button2 = QtWidgets.QPushButton("3")
						self.button3 = QtWidgets.QPushButton("1")
					elif orderStage3 = 5:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("1")
						self.button3 = QtWidgets.QPushButton("2")
					elif orderStage3 = 6:
						self.button1 = QtWidgets.QPushButton("3")
						self.button2 = QtWidgets.QPushButton("2")
						self.button3 = QtWidgets.QPushButton("1")

					self.show()

					if displayStage3 == 1:
						if displayStage0 == 1:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
						if displayStage0 == 2:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
						if displayStage0 == 3:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
					if displayStage3 == 2:
						if posState1 == 1:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
						if posState1 == 2:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
						if posState1 == 3:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
					if displayStage3 == 3:
						if posState2 == 1:
							self.button1.clicked.connect(self.correctAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.incorrectAns)
						if posState2 == 2:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.correctAns)
							self.button3.clicked.connect(self.incorrectAns)
						if posState2 == 3:
							self.button1.clicked.connect(self.incorrectAns)
							self.button2.clicked.connect(self.incorrectAns)
							self.button3.clicked.connect(self.correctAns)
				elif stage == 4:
					self.changeStateComplete()




			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0