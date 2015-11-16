import time
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

Note: some strike when there shouldn't be
"""

class SubMod3(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod3')
		
		self.stage = 0
		self.init = 1
		self.posState2 = 0
		self.posState1 = 0
		self.selectedButton = 1
		self.background = QtWidgets.QLabel()
		self.button1 = QtWidgets.QPushButton()
		self.button2 = QtWidgets.QPushButton()
		self.button3 = QtWidgets.QPushButton()
		self.displayNum = QtWidgets.QLabel()
		self.select1 = QtWidgets.QLabel()
		self.select2 = QtWidgets.QLabel()
		self.select3 = QtWidgets.QLabel()

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.background, 0, 0, 100, 100)
		grid.addWidget(self.button3, 2, 3)
		grid.addWidget(self.button2, 2, 2)
		grid.addWidget(self.button1, 2, 1)
		grid.addWidget(self.select3, 3, 3)
		grid.addWidget(self.select2, 3, 2)
		grid.addWidget(self.select1, 3, 1)
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
		if self.init ==0:
			self.stage += 1
			self.init = 1
			self.selectedButton = 1
			print ("stage1reach")
		else:
			pass

	def incorrectAns(self):
		self.changeStateStrike()
		print ("stage1strike")

	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
			#No input yet

			if(False):
				pass
			else:
				if self.input == 'UP' or self.input == 'RIGHT':
					self.selectedButton += 1
					if self.selectedButton>3:
						self.selectedButton = 1
				elif self.input == 'DOWN' or self.input == 'LEFT':
					self.selectedButton -= 1
					if self.selectedButton < 1:
						self.selectedButton = 3

				if self.selectedButton == 1:
					self.select1.setText("?")
					self.select1.show()
					self.select2.hide()
					self.select3.hide()
				elif self.selectedButton == 2:
					self.select2.setText("?")
					self.select2.show()
					self.select1.hide()
					self.select3.hide()
				elif self.selectedButton == 3:
					self.select3.show()
					self.select3.setText("?")
					self.select2.hide()
					self.select1.hide()

				if self.stage == 0:
					if self.init == 1:
						print ("stage0init")
						self.orderStage0 = randint(1,6)
						self.displayStage0 = randint(1,3)
						self.init = 0
					else:
				
						if self.displayStage0 == 1:
							self.displayNum.setText("1")
						elif self.displayStage0 == 2:
							self.displayNum.setText("2")
						elif self.displayStage0 == 3:
							self.displayNum.setText("3")

						if self.orderStage0 == 1:
							self.button1.setText("1")
							self.button2.setText("2")
							self.button3.setText("3")
							if self.displayStage0 == 1:
								self.labelStage0 = 1
							elif self.displayStage0 == 2:
								self.labelStage0 = 2
							elif self.displayStage0 == 3:
								self.labelStage0 = 3
						elif self.orderStage0 == 2:
							self.button1.setText("1")
							self.button2.setText("3")
							self.button3.setText("2")
							if self.displayStage0 == 1:
								self.labelStage0 = 1
							elif self.displayStage0 == 2:
								self.labelStage0 = 3
							elif self.displayStage0 == 3:
								self.labelStage0 = 2
						elif self.orderStage0 ==3:
							self.button1.setText("2")
							self.button2.setText("1")
							self.button3.setText("3")
							if self.displayStage0 == 1:
								self.labelStage0 = 2
							elif self.displayStage0 == 2:
								self.labelStage0 = 1
							elif self.displayStage0 == 3:
								self.labelStage0 = 3
						elif self.orderStage0 == 4:
							self.button1.setText("2")
							self.button2.setText("3")
							self.button3.setText("1")
							if self.displayStage0 == 1:
								self.labelStage0 = 2
							elif self.displayStage0 == 2:
								self.labelStage0 = 3
							elif self.displayStage0 == 3:
								self.labelStage0 = 1
						elif self.orderStage0 == 5:
							self.button1.setText("3")
							self.button2.setText("1")
							self.button3.setText("2")
							if self.displayStage0 == 1:
								self.labelStage0 = 3
							elif self.displayStage0 == 2:
								self.labelStage0 = 1
							elif self.displayStage0 == 3:
								self.labelStage0 = 2
						elif self.orderStage0 == 6:
							self.button1.setText("3")
							self.button2.setText("2")
							self.button3.setText("1")
							if self.displayStage0 == 1:
								self.labelStage0 = 3
							elif self.displayStage0 == 2:
								self.labelStage0 = 2
							elif self.displayStage0 == 3:
								self.labelStage0 = 1

						if self.input == 'BUTTONA':
							if self.displayStage0 == 1:
								if self.selectedButton == 1:
									self.correctAns()
								else:
									self.incorrectAns()
								#self.button1.clicked.connect(self.correctAns())
								#self.button2.clicked.connect(self.incorrectAns())
								#self.button3.clicked.connect(self.incorrectAns())
							elif self.displayStage0 == 2:
								if self.selectedButton == 2:
									self.correctAns()
								else:
									self.incorrectAns()
								# self.button1.clicked.connect(self.incorrectAns())
								# self.button2.clicked.connect(self.correctAns())
								# self.button3.clicked.connect(self.incorrectAns())
							elif self.displayStage0 == 3:
								if self.selectedButton == 3:
									self.correctAns()
								else:
									self.incorrectAns()
								# self.button1.clicked.connect(self.incorrectAns())
								# self.button2.clicked.connect(self.incorrectAns())
								# self.button3.clicked.connect(self.correctAns())

					
				elif self.stage == 1:
					if self.init == 1:
						print ("stage1init")
						self.orderStage1 = randint(1,6)
						self.displayStage1 = randint(1,3)
						self.init = 0
					else:
						if self.displayStage1 == 1:
							self.displayNum.setText("1")
						elif self.displayStage1 == 2:
							self.displayNum.setText("2")
						elif self.displayStage1 == 3:
							self.displayNum.setText("3")

						if self.orderStage1 == 1:
							self.button1.setText("1")
							self.button2.setText("2")
							self.button3.setText("3")
						elif self.orderStage1 == 2:
							self.button1.setText("1")
							self.button2.setText("3")
							self.button3.setText("2")
						elif self.orderStage1 == 3:
							self.button1.setText("2")
							self.button2.setText("1")
							self.button3.setText("3")
						elif self.orderStage1 == 4:
							self.button1.setText("2")
							self.button2.setText("3")
							self.button3.setText("1")
						elif self.orderStage1 == 5:
							self.button1.setText("3")
							self.button2.setText("1")
							self.button3.setText("2")
						elif self.orderStage1 == 6:
							self.button1.setText("3")
							self.button2.setText("2")
							self.button3.setText("1")

						if self.input == 'BUTTONA':
							if self.displayStage1 == 1:
								if self.orderStage1 == 1 or self.orderStage1 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 = 3
								if self.orderStage1 == 5 or self.orderStage1 == 6:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 = 1
								if self.orderStage1 == 2 or self.orderStage1 == 4:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 = 2
							elif self.displayStage1 == 2:
								if self.displayStage0 == 1:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 == 1
								elif self.displayStage0 == 2:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 == 2
								elif self.displayStage0 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState1 == 3
							elif self.displayStage1 == 3:
								if self.selectedButton == 1:
									self.correctAns()
								else:
									self.incorrectAns()
								self.posState1 = 1
				elif self.stage == 2:
					if self.init == 1:
						print ("stage2init")
						self.orderStage2 = randint(1,6)
						self.displayStage2 = randint(1,3)
						self.init = 0
					else:
						if self.displayStage2 == 1:
							self.displayNum.setText("1")
						elif self.displayStage2 == 2:
							self.displayNum.setText("2")
						elif self.displayStage2 == 3:
							self.displayNum.setText("3")

						if self.orderStage2 == 1:
							self.button1.setText("1")
							self.button2.setText("2")
							self.button3.setText("3")
						elif self.orderStage2 == 2:
							self.button1.setText("1")
							self.button2.setText("3")
							self.button3.setText("2")
						elif self.orderStage2 == 3:
							self.button1.setText("2")
							self.button2.setText("1")
							self.button3.setText("3")
						elif self.orderStage2 == 4:
							self.button1.setText("2")
							self.button2.setText("3")
							self.button3.setText("1")
						elif self.orderStage2 == 5:
							self.button1.setText("3")
							self.button2.setText("1")
							self.button3.setText("2")
						elif self.orderStage2 ==6:
							self.button1.setText("3")
							self.button2.setText("2")
							self.button3.setText("1")

						if self.input == 'BUTTONA':
							if self.displayStage2 == 1:
								if self.labelStage0 == 1:
									if self.orderStage2 == 1 or self.orderStage2 == 2:
										if self.selectedButton == 1:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 1
									if self.orderStage2 == 3 or self.orderStage2 == 5:
										if self.selectedButton == 2:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 2
									if self.orderStage2 == 4 or self.orderStage2 == 6:
										if self.selectedButton == 3:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 3
								if self.labelStage0 == 2:
									if self.orderStage2 == 3 or self.orderStage2 == 4:
										if self.selectedButton == 1:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 1
									if self.orderStage2 == 1 or self.orderStage2 == 6:
										if self.selectedButton == 2:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 2
									if self.orderStage2 == 2 or self.orderStage2 == 5:
										if self.selectedButton == 3:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 3
								if self.labelStage0 == 3:
									if self.orderStage2 == 5 or self.orderStage2 == 6:
										if self.selectedButton == 1:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 1
									if self.orderStage2 == 2 or self.orderStage2 == 4:
										if self.selectedButton == 2:
											self.correctAns()
										else:
											self.incorrectAns()
										self.posState2 = 2
									if self.orderStage2 == 1 or self.orderStage2 == 3:
										if self.selectedButton == 3:
											self.correctAns()
										else:
											self.incorrectAns()										
										self.posState2 = 3
							if self.displayStage2 == 2:
								if self.selectedButton == 3:
									self.correctAns()
								else:
									self.incorrectAns()
								self.posState2 = 3
							if self.displayStage2 == 3:
								if self.orderStage2 == 5 or self.orderStage2 == 6:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState2 = 1
								if self.orderStage2 == 2 or self.orderStage2 == 4:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState2 = 2
								if self.orderStage2 == 1 or self.orderStage2 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
									self.posState2 = 3
				elif self.stage == 3:
					if self.init == 1:
						print ("stage3init")
						self.orderStage3 = randint(1,6)
						self.displayStage3 = randint(1,3)
						self.init = 0
					else:
						if self.displayStage3 == 1:
							self.displayNum.setText("1")
						elif self.displayStage3 == 2:
							self.displayNum.setText("2")
						elif self.displayStage3 == 3:
							self.displayNum.setText("3")

						if self.orderStage3 == 1:
							self.button1.setText("1")
							self.button2.setText("2")
							self.button3.setText("3")
						elif self.orderStage3 == 2:
							self.button1.setText("1")
							self.button2.setText("3")
							self.button3.setText("2")
						elif self.orderStage3 == 3:
							self.button1.setText("2")
							self.button2.setText("1")
							self.button3.setText("3")
						elif self.orderStage3 == 4:
							self.button1.setText("2")
							self.button2.setText("3")
							self.button3.setText("1")
						elif self.orderStage3 == 5:
							self.button1.setText("3")
							self.button2.setText("1")
							self.button3.setText("2")
						elif self.orderStage3 == 6:
							self.button1.setText("3")
							self.button2.setText("2")
							self.button3.setText("1")

						if self.input == 'BUTTONA':
							if self.displayStage3 == 1:
								if self.displayStage0 == 1:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.displayStage0 == 2:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.displayStage0 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
							if self.displayStage3 == 2:
								if self.posState1 == 1:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.posState1 == 2:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.posState1 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
							if self.displayStage3 == 3:
								if self.posState2 == 1:
									if self.selectedButton == 1:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.posState2 == 2:
									if self.selectedButton == 2:
										self.correctAns()
									else:
										self.incorrectAns()
								if self.posState2 == 3:
									if self.selectedButton == 3:
										self.correctAns()
									else:
										self.incorrectAns()
				elif self.stage == 4:
					self.changeStateComplete()
					print ("done")
			#self.update()
			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0
