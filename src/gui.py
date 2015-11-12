import sys
import time
import bomb

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

class MainGUI(QtWidgets.QMainWindow):
	def __init__(self, app, totalTime):
		super().__init__()

		self.numButtons = 3
		self.totalTime = totalTime

		self.button1 = QtWidgets.QPushButton("Start Timer")
		self.button2 = QtWidgets.QPushButton("mytext2")
		self.button3 = QtWidgets.QPushButton("mytext3")
		
		self.list1 = QtWidgets.QListWidget()

		self.label = QtWidgets.QLabel()
		self.label2 = QtWidgets.QLabel("0")

		#Set and display image
		# reader = QtGui.QImageReader("bomb-154456_1280.png")
		# image = reader.read()
		# qpixmap = QtGui.QPixmap()
		# qpixmap.convertFromImage(image)
		# self.label.setPixmap(qpixmap)


		self.grid = QtWidgets.QGridLayout()


		window = QtWidgets.QWidget()
		window.setLayout(self.grid)
		self.setCentralWidget(window)

		self.grid.addWidget(self.button1, 0, 0)
		self.grid.addWidget(self.button2, 1, 0)
		self.grid.addWidget(self.button3, 2, 0)
		self.grid.addWidget(self.list1, 0, 1, 4, 1)
		self.grid.addWidget(self.label,0, 2, 4, 1)
		self.grid.addWidget(self.label2, 3, 0)

		self.button1.clicked.connect(self.button1pushed)
		self.button2.clicked.connect(self.button2pushed)

		#Creating input text line
		self.le = QLineEdit(self)
		self.grid.addWidget(self.le, 3, 3)
		self.show()

		#create Game
		self.game = Game(totalTime)

	def button1pushed(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(self.totalTime)
		self.timer.timeout.connect(self.timerDone)
		self.timer.setSingleShot(False)

		self.timer.start()
		self.startTime = time.time()
		self.gameLoop()

	def timerDone(self):
		elapsed = int(time.time() - self.startTime)
		if elapsed > self.totalTime :
			self.label2.setText('BOOM!!!!!')
		else:
			self.label2.setText(str(elapsed))

	def gameLoop(self):
		while self.game.state == 'ND':
			self.game.bomb.getActiveModule().submod1main()
			self.game.checkGameState()
			if self.game.state == 'ND':
				text, ok = QInputDialog.getText(self, 'Input Answer', 'Enter answer...')
				if ok:
					self.le.setText(str(text))
					self.game.inputHandler(text)
				else:
					return


	def button2pushed(self):
		pass

	def addButton(self, buttonText):
		self.newButton = QtWidgets.QPushButton(buttonText)
		self.grid.addWidget(self.newButton, self.numButtons + 1, 0)
		self.numButtons += 1
		self.show()


MAX_STRIKES = 3

class Game:
	def __init__(self, time):
		self.bomb = bomb.Bomb(time)
		self.totalStrikes = 0
		self.state = 'ND'

	def checkGameState(self):
		state = 'ND'
		x = self.bomb.checkModStates()

		if x > 0:
			self.totalStrikes += x
		elif x == 0:
			self.win()
			self.state = 'Win'
		else:
			pass

		if self.totalStrikes >= 3:
			self.lose()
			self.state = 'Lose'

		#Temporary get console input
	def consoleInput(self):
		return input()

	#Gives input to bomb for bomb controls	not sure should use bomb.changeActiveModule
	def giveBombInput(self, bomb, bombinput):
		bomb.changeBombInput(bombinput)

	#gives input for active module on bomb.
	def giveModInput(self, bomb, modinput):
		bomb.getActiveModule().changeInput(modinput)

	def win(self):
		#print win screen and exit game
		pass

	def lose(self):
		#print lose screen and exit game
		pass

	def inputHandler(self, item):
		self.giveModInput(self.bomb, item)
