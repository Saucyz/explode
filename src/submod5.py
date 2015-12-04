from module import Module
from PyQt5 import QtWidgets, QtGui
from random import randint

class SubMod5(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod5')
		
		self.init = 1
		self.stage = 0
		self.selectedButton = 1

		self.label = QtWidgets.QLabel()
		self.outline1 = QtWidgets.QLabel()
		self.outline2 = QtWidgets.QLabel()
		self.outline3 = QtWidgets.QLabel()
		self.outline4 = QtWidgets.QLabel()
		#self.label.setGeometry(10,10,100,200)
		self.button1 = QtWidgets.QPushButton()
		self.button2 = QtWidgets.QPushButton()
		self.button3 = QtWidgets.QPushButton()
		self.button4 = QtWidgets.QPushButton()
		self.select1 = QtWidgets.QLabel()
		self.select2 = QtWidgets.QLabel()
		self.select3 = QtWidgets.QLabel()
		self.select4 = QtWidgets.QLabel()
		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.label, 0, 0, 100, 100)
		grid.addWidget(self.outline1, 2, 2)
		grid.addWidget(self.outline2, 2, 3)
		grid.addWidget(self.outline3, 3, 2)
		grid.addWidget(self.outline4, 3, 3)
		grid.addWidget(self.button1, 2, 2)
		grid.addWidget(self.button2, 2, 3)
		grid.addWidget(self.button3, 3, 2)
		grid.addWidget(self.button4, 3, 3)
		grid.addWidget(self.select1, 2, 1)
		grid.addWidget(self.select2, 2, 4)
		grid.addWidget(self.select3, 3, 1)
		grid.addWidget(self.select4, 3, 4)

		reader = QtGui.QImageReader("moduleBox.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label.setPixmap(qpixmap)

		reader = QtGui.QImageReader("buttonBox.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.outline1.setPixmap(qpixmap)
		self.outline2.setPixmap(qpixmap)
		self.outline3.setPixmap(qpixmap)
		self.outline4.setPixmap(qpixmap)

	def resetModule(self):
		self.changeStateIncomplete()
		self.instruction_index = 0
		self.input = 0

	def correctAns(self):
		
		self.stage += 1
		
		
		print ("stage1reach")
		

	def incorrectAns(self):
		self.changeStateStrike()
		print ("stage1strike")

	def checkAns0(self):
		if self.posGen == 1:
			if self.selectedButton == 1:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 2:
			if self.selectedButton == 2:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 3:
			if self.selectedButton == 3:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 4:
			if self.selectedButton == 4:
				self.correctAns()
			else:
				self.incorrectAns()

	def checkAns1(self):
		if self.posGen == 1:
			if self.selectedButton == 2:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 2:
			if self.selectedButton == 3:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 3:
			if self.selectedButton == 4:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 4:
			if self.selectedButton == 1:
				self.correctAns()
			else:
				self.incorrectAns()	

	def checkAns2(self):
		if self.posGen == 1:
			if self.selectedButton == 3:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 2:
			if self.selectedButton == 4:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 3:
			if self.selectedButton == 1:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 4:
			if self.selectedButton == 2:
				self.correctAns()
			else:
				self.incorrectAns()	

	def checkAns3(self):
		if self.posGen == 1:
			if self.selectedButton == 4:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 2:
			if self.selectedButton == 1:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 3:
			if self.selectedButton == 2:
				self.correctAns()
			else:
				self.incorrectAns()
		if self.posGen == 4:
			if self.selectedButton == 3:
				self.correctAns()
			else:
				self.incorrectAns()	

	def main(self):
		if self.getState() == 'COMPLETE':
			pass
		else:
			#No input yet
			if(False):
				pass
			else:
				if self.init == 1:
					self.init = 0

					self.symbolGen = randint(1,6)
					self.posGen = randint(1,4)
					if self.symbolGen == 1:
						if self.posGen == 1:
							self.button1.setText('[')
							self.button2.setText('<')
							self.button3.setText('3')
							self.button4.setText(']')
						if self.posGen == 2:
							self.button2.setText('[')
							self.button3.setText('<')
							self.button4.setText('3')
							self.button1.setText(']')
						if self.posGen == 3:
							self.button3.setText('[')
							self.button4.setText('<')
							self.button1.setText('3')
							self.button2.setText(']')
						if self.posGen == 4:
							self.button4.setText('[')
							self.button1.setText('<')
							self.button2.setText('3')
							self.button3.setText(']')
					elif self.symbolGen == 2:
						if self.posGen == 1:
							self.button1.setText('$')
							self.button2.setText('@')
							self.button3.setText('#')
							self.button4.setText('!')
						if self.posGen == 2:
							self.button2.setText('$')
							self.button3.setText('@')
							self.button4.setText('#')
							self.button1.setText('!')
						if self.posGen == 3:
							self.button3.setText('$')
							self.button4.setText('@')
							self.button1.setText('#')
							self.button2.setText('!')
						if self.posGen == 4:
							self.button4.setText('$')
							self.button1.setText('@')
							self.button2.setText('#')
							self.button3.setText('!')
					elif self.symbolGen == 3:
						if self.posGen == 1:
							self.button1.setText('^')
							self.button2.setText('&')
							self.button3.setText('%')
							self.button4.setText('*')
						if self.posGen == 2:
							self.button2.setText('^')
							self.button3.setText('&')
							self.button4.setText('%')
							self.button1.setText('*')
						if self.posGen == 3:
							self.button3.setText('^')
							self.button4.setText('&')
							self.button1.setText('%')
							self.button2.setText('*')
						if self.posGen == 4:
							self.button4.setText('^')
							self.button1.setText('&')
							self.button2.setText('%')
							self.button3.setText('*')
					elif self.symbolGen == 4:
						if self.posGen == 1:
							self.button1.setText('<')
							self.button2.setText('~')
							self.button3.setText('>')
							self.button4.setText(',')
						if self.posGen == 2:
							self.button2.setText('<')
							self.button3.setText('~')
							self.button4.setText('>')
							self.button1.setText(',')
						if self.posGen == 3:
							self.button3.setText('<')
							self.button4.setText('~')
							self.button1.setText('>')
							self.button2.setText(',')
						if self.posGen == 4:
							self.button4.setText('<')
							self.button1.setText('~')
							self.button2.setText('>')
							self.button3.setText(',')
					elif self.symbolGen == 5:
						if self.posGen == 1:
							self.button1.setText(':')
							self.button2.setText('&')
							self.button3.setText('=')
							self.button4.setText('{')
						if self.posGen == 2:
							self.button2.setText(':')
							self.button3.setText('&')
							self.button4.setText('=')
							self.button1.setText('{')
						if self.posGen == 3:
							self.button3.setText(':')
							self.button4.setText('&')
							self.button1.setText('=')
							self.button2.setText('{')
						if self.posGen == 4:
							self.button4.setText(':')
							self.button1.setText('&')
							self.button2.setText('=')
							self.button3.setText('{')
					elif self.symbolGen == 6:
						if self.posGen == 1:
							self.button1.setText('/')
							self.button2.setText('+')
							self.button3.setText('#')
							self.button4.setText('?')
						if self.posGen == 2:
							self.button2.setText('/')
							self.button3.setText('+')
							self.button4.setText('#')
							self.button1.setText('?')
						if self.posGen == 3:
							self.button3.setText('/')
							self.button4.setText('+')
							self.button1.setText('#')
							self.button2.setText('?')
						if self.posGen == 4:
							self.button4.setText('/')
							self.button1.setText('+')
							self.button2.setText('#')
							self.button3.setText('?')
				else:
					if self.selectedButton == 1:
						if self.input == 'RIGHT':
							self.selectedButton = 2
						if self.input == 'DOWN':
							self.selectedButton = 3
						else:
							pass
					elif self.selectedButton == 2:
						if self.input == 'LEFT':
							self.selectedButton = 1
						if self.input == 'DOWN':
							self.selectedButton = 4
						else:
							pass
					elif self.selectedButton == 3:
						if self.input == 'RIGHT':
							self.selectedButton = 4
						if self.input == 'UP':
							self.selectedButton = 1
						else:
							pass
					elif self.selectedButton == 4:
						if self.input == 'LEFT':
							self.selectedButton = 3
						if self.input == 'UP':
							self.selectedButton = 2
						else:
							pass

					
					if self.selectedButton == 1:
						self.select1.setText(">")
						self.select1.show()
						self.select2.hide()
						self.select3.hide()
						self.select4.hide()
					elif self.selectedButton == 2:
						self.select2.setText("<")
						self.select2.show()
						self.select1.hide()
						self.select3.hide()
						self.select4.hide()
					elif self.selectedButton == 3:
						self.select4.hide()
						self.select3.setText(">")
						self.select3.show()
						self.select2.hide()
						self.select1.hide()
					elif self.selectedButton == 4:
						self.select4.setText("<")
						self.select4.show()
						self.select1.hide()
						self.select2.hide()
						self.select3.hide()

					if self.input == 'BUTTONA':
						if self.stage == 0:
							if self.symbolGen == 1:
								self.checkAns0()		
							elif self.symbolGen == 2:
								self.checkAns0()
							elif self.symbolGen == 3:
								self.checkAns0()
							elif self.symbolGen == 4:
								self.checkAns0()
							elif self.symbolGen == 5:
								self.checkAns0()
							elif self.symbolGen == 6:
								self.checkAns0()

						elif self.stage == 1:
							if self.symbolGen == 1:
								self.checkAns1()		
							elif self.symbolGen == 2:
								self.checkAns1()
							elif self.symbolGen == 3:
								self.checkAns1()
							elif self.symbolGen == 4:
								self.checkAns1()
							elif self.symbolGen == 5:
								self.checkAns1()
							elif self.symbolGen == 6:
								self.checkAns1()

						elif self.stage == 2:
							if self.symbolGen == 1:
								self.checkAns2()		
							elif self.symbolGen == 2:
								self.checkAns2()
							elif self.symbolGen == 3:
								self.checkAns2()
							elif self.symbolGen == 4:
								self.checkAns2()
							elif self.symbolGen == 5:
								self.checkAns2()
							elif self.symbolGen == 6:
								self.checkAns2()

						elif self.stage == 3:
							if self.symbolGen == 1:
								self.checkAns3()		
							elif self.symbolGen == 2:
								self.checkAns3()
							elif self.symbolGen == 3:
								self.checkAns3()
							elif self.symbolGen == 4:
								self.checkAns3()
							elif self.symbolGen == 5:
								self.checkAns3()
							elif self.symbolGen == 6:
								self.checkAns3()

						elif self.stage == 4:
							self.changeStateComplete()

			#ADDED THIS SO INPUT WOULDN'T STAY, NEED TO FIX!
			self.input = 0
