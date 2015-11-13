#!/usr/bin/python
import bomb
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

MAX_STRIKES = 3

class Game(QtWidgets.QMainWindow):
	def __init__(self, app, totalTime):
		super().__init__()

		self.numButtons = 3
		self.totalTime = totalTime

		self.startButton = QtWidgets.QPushButton("Start Timer")
		self.state = 'ND'
		self.list1 = QtWidgets.QListWidget()
		self.bomb = bomb.Bomb(totalTime)
		self.totalStrikes = 0
		self.won = False

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
		
		#Creating input text line
		self.le = QLineEdit(self)
		self.grid.addWidget(self.le, 3, 3)
		self.show()

	def startButtonPushed(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(self.totalTime)
		self.timer.timeout.connect(self.timerDone)
		self.timer.setSingleShot(False)

		self.timer.start()
		self.startTime = time.time()
		self.setModuleGuis()

	def timerDone(self):
		elapsed = int(time.time() - self.startTime)
		if elapsed > self.totalTime or self.totalStrikes >= MAX_STRIKES:
			self.timeLabel.setText('BOOM!!!!!')
			self.state = 'Lose'
			self.stateLabel.setText('State: ' + self.state)
		else:
			self.timeLabel.setText('Time remaining: ' + str(self.totalTime - elapsed))
			self.stateLabel.setText('State: ' + self.state)

	def textHandler(self):
		self.bomb.getActiveModule().submod1main()
			
		text, ok = QInputDialog.getText(self, 'Input Answer', 'Enter answer...')
		if ok:
			self.le.setText(str(text))
			self.inputHandler(text)
			self.checkGameState()
		else:
			pass

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
		self.strikesLabel = QtWidgets.QLabel(str(self.totalStrikes) + "/" + str(MAX_STRIKES) + ' strikes')

		self.grid.addWidget(self.stateLabel, 0, 2)
		self.grid.addWidget(self.timeLabel, 1, 2)
		self.grid.addWidget(self.strikesLabel, 2, 2)

		# self.newButton = QtWidgets.QPushButton(buttonText)
		# self.grid.addWidget(self.newButton, self.numButtons + 1, 0)
		# self.numButtons += 1
		#self.show()

	def restart(self):
		self = Game(self.totalTime)
		#needs to stop and reset timer as well

	def keyPressEvent(self, event):
		key = event.key()
		print(key)

		if key == QtCore.Qt.Key_A:
			print('A Key Pressed')

		elif key == QtCore.Qt.Key_D:
			print('D Key Pressed')

		elif key == QtCore.Qt.Key_S:
			print('S Key Pressed')

		elif key == QtCore.Qt.Key_W:
			print('W Key Pressed')
		self.giveModInput(self.bomb, key)

	def checkGameState(self):
		self.state = 'ND'
		x = self.bomb.checkModStates()

		if x > 0:
			self.totalStrikes += x
		elif x == 0:
			self.won = True
			self.win()
			self.state = 'Win'
		else:
			pass

		if self.totalStrikes >= 3:
			self.lose()
			self.state = 'Lose'

		return self.state

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

	def inputHandler(self, text):
		item = text
		if item == '':
			print('Waiting...')	#replace for when the input signal becomes continuous
			return True
		else:
			#self.giveModInput(self.bomb, item)
			return False

	def inputWaitLoop(self):
		wait = True
		while wait == True:
			wait = self.inputHandler()

	def gameLoop(self):
		while self.bomb.timer.timeOut == False:
			self.bomb.getActiveModule().submod1main()
			gamestate = self.checkGameState()
			if gamestate == 'ND':
				pass
				#self.inputWaitLoop()
			elif gamestate == 'Lose':
				print('You lose...')
				return

def main():
	g = Game(5)
	g.gameLoop()

#main()
