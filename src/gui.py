import sys
import time
import bomb

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

class MainGUI(QtWidgets.QMainWindow):
	def __init__(self, app, totalTime):
		super().__init__()

		self.numButtons = 3
		self.verbose = True
		self.totalTime = totalTime

		self.startButton = QtWidgets.QPushButton("Start Timer")
		
		self.list1 = QtWidgets.QListWidget()

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

		self.grid.addWidget(self.startButton, 0, 0)
		#self.grid.addWidget(self.list1, 0, 1, 4, 1)
		
		self.startButton.clicked.connect(self.startButtonPushed)
		self.show()

		#create Game
		self.game = Game(totalTime)

	def startButtonPushed(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(self.totalTime)
		self.timer.timeout.connect(self.timerDone)
		self.timer.setSingleShot(False)

		self.timer.start()
		self.startTime = time.time()
		self.setModuleGuis()
		#disable button to prevent multiple presses of start before reset
		self.startButton.setEnabled(False)

	def timerDone(self):
		self.game.checkGameState(self.verbose)
		if self.verbose:
			print('strikes: ' + str(self.game.totalStrikes))
		self.strikesLabel.setText(str(self.game.totalStrikes) + "/" + str(MAX_STRIKES) + ' Strikes')
		elapsed = int(time.time() - self.startTime)
		if self.game.state == 'Win':
			 self.timer.stop()
		elif elapsed > self.totalTime or self.game.totalStrikes >= MAX_STRIKES:
			self.timeLabel.setText('BOOM!!!!!')
			self.game.state = 'Lose'
		else:
			self.timeLabel.setText('Time remaining: ' + str(self.totalTime - elapsed))
		self.stateLabel.setText('State: ' + self.game.state)

	def textHandler(self):
		self.game.bomb.getActiveModule().submod1main()
		text, ok = QInputDialog.getText(self, 'Input Answer', 'Enter number from 0 - 9: ')
		if ok:
			self.le.setText(str(text))
			self.game.inputHandler(text)

	def buttonHandler(self):
		pass

	def setModuleGuis(self):
		self.module1 = QtWidgets.QPushButton("Module 1")
		self.module2 = QtWidgets.QPushButton("Module 2 (Nothing)")
		self.restartButton = QtWidgets.QPushButton("Restart")

		self.module1.clicked.connect(self.textHandler)
		#self.module2.clicked.connect(self.someFunc)
		self.restartButton.clicked.connect(self.restart)

		self.grid.addWidget(self.module1, 1, 0)
		self.grid.addWidget(self.module2, 2, 0)
		self.grid.addWidget(self.restartButton, 3, 0)

		self.stateLabel = QtWidgets.QLabel("State: ")
		self.timeLabel = QtWidgets.QLabel("Time remaining: ")
		self.strikesLabel = QtWidgets.QLabel(str(self.game.totalStrikes) + "/" + str(MAX_STRIKES) + ' Strikes')

		self.grid.addWidget(self.stateLabel, 0, 2)
		self.grid.addWidget(self.timeLabel, 1, 2)
		self.grid.addWidget(self.strikesLabel, 2, 2)

		#Creating input text line
		self.le = QLineEdit(self)
		self.grid.addWidget(self.le, 3, 3)

		# self.newButton = QtWidgets.QPushButton(buttonText)
		# self.grid.addWidget(self.newButton, self.numButtons + 1, 0)
		# self.numButtons += 1
		#self.show()

	def restart(self):
		self.game = Game(self.totalTime)
		self.startButton.setEnabled(True)
		self.timer.stop()
		self.stateLabel.setText('')
		self.timeLabel.setText('')
		self.strikesLabel.setText('')
		#needs to stop and reset timer as well


MAX_STRIKES = 3

class Game:
	def __init__(self, time):
		self.bomb = bomb.Bomb(time)
		self.totalStrikes = 0
		self.state = 'ND'

	def checkGameState(self, verbose):
		x = self.bomb.checkModStates(verbose)

		if x > 0:
			self.totalStrikes += x
		elif x == 0:
			self.state = 'Win'
		else:
			pass

		if self.totalStrikes >= MAX_STRIKES:
			self.state = 'Lose'

	#Gives input to bomb for bomb controls	not sure should use bomb.changeActiveModule
	def giveBombInput(self, bomb, bombinput):
		bomb.changeBombInput(bombinput)

	#gives input for active module on bomb.
	def giveModInput(self, bomb, modinput):
		bomb.getActiveModule().changeInput(modinput)

	def inputHandler(self, item):
		self.giveModInput(self.bomb, item)
