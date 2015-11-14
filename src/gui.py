import sys
import time
import bomb

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

class Ui_myfirstgui(object):
	def setupUi(self, myfirstgui):
		myfirstgui.setObjectName("myfirstgui")
		myfirstgui.resize(598, 443)

		self.label = QtWidgets.QLabel(myfirstgui)

		reader = QtGui.QImageReader("/home/david/cat.jpg")
		image = reader.read()

		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)

		self.label.setPixmap(qpixmap)
		self.label.setGeometry(QtCore.QRect(0, 0, 583, 443))
		self.label.setObjectName("background")
		self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
		self.buttonBox.setGeometry(QtCore.QRect(200, 410, 381, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
		self.buttonBox.setObjectName("buttonBox")
		self.myTextInput = QtWidgets.QLineEdit(myfirstgui)
		self.myTextInput.setGeometry(QtCore.QRect(200, 80, 101, 21))
		self.myTextInput.setObjectName("myTextInput")
		self.listWidget = QtWidgets.QListWidget(myfirstgui)
		self.listWidget.setGeometry(QtCore.QRect(200, 110, 191, 191))
		self.listWidget.setObjectName("listWidget")
		self.clearBtn = QtWidgets.QPushButton(myfirstgui)
		self.clearBtn.setGeometry(QtCore.QRect(350, 80, 41, 23))
		self.clearBtn.setObjectName("clearBtn")
		self.addBtn = QtWidgets.QPushButton(myfirstgui)
		self.addBtn.setGeometry(QtCore.QRect(300, 80, 41, 23))
		self.addBtn.setObjectName("addBtn")
		self.pushButton = QtWidgets.QPushButton(myfirstgui)
		self.pushButton.setGeometry(QtCore.QRect(340, 240, 31, 27))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_2.setGeometry(QtCore.QRect(280, 240, 31, 27))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_3.setGeometry(QtCore.QRect(220, 240, 31, 27))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_4 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_4.setGeometry(QtCore.QRect(220, 190, 31, 27))
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_5 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_5.setGeometry(QtCore.QRect(280, 190, 31, 27))
		self.pushButton_5.setObjectName("pushButton_5")
		self.pushButton_6 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_6.setGeometry(QtCore.QRect(340, 190, 31, 27))
		self.pushButton_6.setObjectName("pushButton_6")
		self.pushButton_7 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_7.setGeometry(QtCore.QRect(220, 140, 31, 27))
		self.pushButton_7.setObjectName("pushButton_7")
		self.pushButton_8 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_8.setGeometry(QtCore.QRect(280, 140, 31, 27))
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_9 = QtWidgets.QPushButton(myfirstgui)
		self.pushButton_9.setGeometry(QtCore.QRect(340, 140, 31, 27))
		self.pushButton_9.setObjectName("pushButton_9")

		self.retranslateUi(myfirstgui)
		self.buttonBox.accepted.connect(myfirstgui.accept)
		self.buttonBox.rejected.connect(myfirstgui.reject)
		self.clearBtn.clicked.connect(self.listWidget.clear)
		QtCore.QMetaObject.connectSlotsByName(myfirstgui)

	def retranslateUi(self, myfirstgui):
		_translate = QtCore.QCoreApplication.translate
		myfirstgui.setWindowTitle(_translate("myfirstgui", "My First Gui!"))
		self.clearBtn.setText(_translate("myfirstgui", "clear"))
		self.addBtn.setText(_translate("myfirstgui", "add"))
		self.pushButton.setText(_translate("myfirstgui", "3"))
		self.pushButton_2.setText(_translate("myfirstgui", "2"))
		self.pushButton_3.setText(_translate("myfirstgui", "1"))
		self.pushButton_4.setText(_translate("myfirstgui", "4"))
		self.pushButton_5.setText(_translate("myfirstgui", "5"))
		self.pushButton_6.setText(_translate("myfirstgui", "6"))
		self.pushButton_7.setText(_translate("myfirstgui", "7"))
		self.pushButton_8.setText(_translate("myfirstgui", "8"))
		self.pushButton_9.setText(_translate("myfirstgui", "9"))

class MyFirstGuiProgram(Ui_myfirstgui):
	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.addBtn.clicked.connect(self.addInputTextToListbox)

	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)

class Entry(QtWidgets.QWidget):
	def __init__(self, labelText, textcallback):
		super().__init__()

		self.text = None

		self.label = QtWidgets.QLabel(labelText)
		self.textEdit = QtWidgets.QLineEdit()
		self.button1 = QtWidgets.QPushButton('Enter')
		self.callback = textcallback

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.label, 0, 0, 1, 2)
		grid.addWidget(self.textEdit,1,0, 1, 2)
		grid.addWidget(self.button1, 2, 0)

		self.button1.clicked.connect(self.setEntryText)

	def setEntryText(self):
		self.text = self.textEdit.text()
		self.callback()


class MainGUI(QtWidgets.QMainWindow):
	def __init__(self, app, totalTime):
		super().__init__()

		self.numButtons = 3
		self.verbose = False
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
		self.module1.setEnabled(True)
		self.module2.setEnabled(True)

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
		self.entry.label.setText('Enter text for module 1: ')
		self.game.bomb.getActiveModule().submod1main()
		text = self.entry.text
		print(text)
		#text, ok = QInputDialog.getText(self, 'Input Answer', 'Enter number from 0 - 9: ')
		if text != None:
			#self.le.setText(str(text))
			self.game.inputHandler(text)

	def buttonHandler(self):
		pass

	def setModuleGuis(self):
		self.module1 = QtWidgets.QPushButton("Module 1")
		self.module2 = QtWidgets.QPushButton("Module 2 (Nothing)")
		self.restartButton = QtWidgets.QPushButton("Restart")

		self.entry = Entry("Enter something interesting...", self.textHandler)

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
#		self.le = QLineEdit(self)
#		self.grid.addWidget(self.le, 3, 3)

		self.grid.addWidget(self.entry, 4, 3)

		self.grid.setColumnStretch(0, 1)
		self.grid.setColumnStretch(1, 0)
		self.grid.setColumnStretch(2, 1)
		self.grid.setColumnStretch(3, 3)

		self.grid.setRowStretch(0, 1)
		self.grid.setRowStretch(1, 1)
		self.grid.setRowStretch(2, 1)
		self.grid.setRowStretch(3, 1)
		self.grid.setRowStretch(4, 1)

		# self.newButton = QtWidgets.QPushButton(buttonText)
		# self.grid.addWidget(self.newButton, self.numButtons + 1, 0)
		# self.numButtons += 1
		#self.show()

	def restart(self):
		self.game = Game(self.totalTime)
		self.startButton.setEnabled(True)
		self.module1.setEnabled(False)
		self.module2.setEnabled(False)
		self.timer.stop()
		self.stateLabel.setText('')
		self.timeLabel.setText('')
		self.strikesLabel.setText('')
		self.entry.label.setText('')
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
