import sys
import time
import bomb
#Wii remote library!
import cwiid
#import serialCom

#TO DO: Look at check mod states to check mod states also instead of just game state, and disable button for module when complete. Maybe new widget or loop for module logics / game logic and connect to module buttons instead of change active module. Another label for completed modules.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

class Entry(QtWidgets.QWidget):
	def __init__(self, labelText, textcallback):
		super(Entry, self).__init__()

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

		#Set and display image
		#reader = QtGui.QImageReader("pie.png")
		#image = reader.read()
		#qpixmap = QtGui.QPixmap()
		#qpixmap.convertFromImage(image)
		#self.label.setPixmap(qpixmap)

		self.button1.clicked.connect(self.setEntryText)

	def setEntryText(self):
		#self.label.setGeometry(QtCore.QRect(0,0,400, 400))
		self.text = self.textEdit.text()
		reader = QtGui.QImageReader("pie2.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label.setPixmap(qpixmap)
		self.callback()

# class MainMenu(QtWidgets.QMainWindow):

# 		self.selectedButton = 1

# 		self.button1 = QtWidgets.QPushButton("Easy")
# 		self.button2 = QtWidgets.QPushButton("Hard")
# 		self.button3 = QtWidgets.QPushButton("Options")

# 		self.select1 = QtWidgets.QLabel()
# 		self.select2 = QtWidgets.QLabel()
# 		self.select3 = QtWidgets.QLabel()

# 		grid = QtWidgets.QGridLayout()elf.module1.setEnabled(True)
		# self.module2.setEnabled(True)
		# self.module3.setEnabled(True)
# 		self.setLayout(grid)

# 		grid.addWidget(self.button1, 1, 2)
# 		grid.addWidget(self.button2, 2, 2)
# 		grid.addWidget(self.button3, 3, 2)

# 		grid.addWidget(self.select1, 1, 1)
# 		grid.addWidget(self.select2, 2, 1)
# 		grid.addWidget(self.select3, 3, 1)

		# while(True):
		# 	if self.input == 'UP':
		# 		self.selectedButton -= 1 
		# 		if self.selectedButton < 1:
		# 				self.selectedButton = 3
		# 	elif self.input == 'DOWN':
		# 		self.selectedButton += 1
		# 		if self.selectedButton>3:
		# 				self.selectedButton = 1

		# 	if self.input == 'BUTTONA':
		# 		if self.selectedButton == 1:
		# 			return
		# 		elif self.selectedButton == 2:
		# 			return 
		# 		elif self.selectedButton == 3:
		# 			pass

class MainGUI(QtWidgets.QMainWindow):
	def __init__(self, app, totalTime):
		super(MainGUI, self).__init__()



		self.numButtons = 3
		self.verbose = False
		self.totalTime = totalTime
		self.DE2win = False

		#self.startButton = QtWidgets.QPushButton("Start Timer")
		
		self.list1 = QtWidgets.QListWidget()

		#Set and display image
		reader = QtGui.QImageReader("bombBackground.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label = QtWidgets.QLabel("Main")
		self.label.setPixmap(qpixmap)


		self.grid = QtWidgets.QGridLayout()


		window = QtWidgets.QWidget()
		window.setLayout(self.grid)
		self.setCentralWidget(window)
		self.grid.addWidget(self.label, 0, 0, 100, 100)
		#self.grid.addWidget(self.startButton, 0, 0)
		#self.grid.addWidget(self.list1, 0, 1, 4, 1)
		self.game = Game(self, totalTime)
		self.moduleSelect = 1
		self.faceSelect = 1
		self.input = 0
		self.startButtonPushed()
		self.show()

		#create Game
		#self.srl = serialCom.serialCom()
		
		modNum = 1
		for mod in self.game.bomb.moduleList:
			if modNum == 1:
				self.grid.addWidget(mod,1, 1)
			elif modNum == 2:
				self.grid.addWidget(mod,1, 2)
			elif modNum == 3:
				self.grid.addWidget(mod,2, 1)	
			elif modNum == 4:
				self.grid.addWidget(mod,2, 2)		
			modNum += 1
			#mod.hide()
			

		#self.grid.setMinimumRowHeight(r, 300)


	def startButtonPushed(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(self.totalTime)
		self.timer.timeout.connect(self.timerDone)
		self.timer.setSingleShot(False)

		self.timer.start()
		self.startTime = time.time()
		self.setModuleGuis()
		#disable button to prevent multiple presses of start before reset
		#self.startButton.setEnabled(False)
		# self.module1.setEnabled(True)
		# self.module2.setEnabled(True)
		# self.module3.setEnabled(True)
		self.game.bomb.changeActiveModule(0)

	def timerDone(self):
		self.input = self.game.wiiInput()
		if self.input == 'SWINGLEFT':
			self.faceSelect -= 1
			if self.faceSelect < 0:
				self.faceSelect = 3
		elif self.input == 'SWINGRIGHT':
			self.faceSelect += 1
			if self.faceSelect > 3:
				self.faceSelect = 0

		if self.faceSelect == 1:
			self.game.bomb.moduleList[1].show()
			self.game.bomb.moduleList[2].show()
			self.game.bomb.moduleList[3].show()
			self.game.bomb.moduleList[4].show()

			reader = QtGui.QImageReader("bombBackground.png")
			image = reader.read()
			qpixmap = QtGui.QPixmap()
			qpixmap.convertFromImage(image)
			self.label = QtWidgets.QLabel("Main")
			self.label.setPixmap(qpixmap)


			self.strikesLabel.hide()
			self.timeLabel.hide()
			self.stateLabel.hide()
		if self.faceSelect == 0 or self.faceSelect == 2:
			self.game.bomb.moduleList[1].hide()
			self.game.bomb.moduleList[2].hide()
			self.game.bomb.moduleList[3].hide()
			self.game.bomb.moduleList[4].hide()
			reader = QtGui.QImageReader("bombSlide.png")
			image = reader.read()
			qpixmap = QtGui.QPixmap()
			qpixmap.convertFromImage(image)
			self.label = QtWidgets.QLabel("Main")
			self.label.setPixmap(qpixmap)
			self.strikesLabel.show()
			self.timeLabel.show()
			self.stateLabel.show()
		if self.faceSelect == 3:
			self.game.bomb.moduleList[1].hide()
			self.game.bomb.moduleList[2].hide()
			self.game.bomb.moduleList[3].hide()
			self.game.bomb.moduleList[4].hide()

			reader = QtGui.QImageReader("bombBackground.png")
			image = reader.read()
			qpixmap = QtGui.QPixmap()
			qpixmap.convertFromImage(image)
			self.label = QtWidgets.QLabel("Main")
			self.label.setPixmap(qpixmap)

			self.strikesLabel.hide()
			self.timeLabel.hide()
			self.stateLabel.hide()

		if self.moduleSelect == 1:
			if self.input == 'MINUS':
				self.game.bomb.changeActiveModule(0)
				self.moduleSelect = 0
		elif self.moduleSelect == 0:
			if self.input == 'RIGHT':
				self.game.bomb.changeActiveModule(3)
				self.moduleSelect = 1
			elif self.input == 'UP':
				self.game.bomb.changeActiveModule(2)
				self.moduleSelect = 1
			elif self.input == 'LEFT':
				self.game.bomb.changeActiveModule(1)
				self.moduleSelect = 1
			elif self.input == 'DOWN':
				self.game.bomb.changeActiveModule(3)
				self.moduleSelect = 1
		self.checkGameState(self.verbose)
		
		if self.verbose:
			print('strikes: ' + str(self.game.totalStrikes))
		
		self.strikesLabel.setText(str(self.game.totalStrikes) + "/" + str(MAX_STRIKES) + ' Strikes')
		elapsed = int(time.time() - self.startTime)
		
		if self.game.state == 'Win':
			pass#self.srl.serialWrite("W")
		elif elapsed > self.totalTime or self.game.totalStrikes >= MAX_STRIKES:
			self.timeLabel.setText('BOOM!!!!!')
			self.game.state = 'Lose'
			#self.srl.serialWrite("L")
		else:
			self.timeLabel.setText('Time remaining: ' + str(self.totalTime - elapsed))
			#self.srl.serialWrite("U")
		
		self.stateLabel.setText('State: ' + self.game.state)

	def textHandler(self):
		#self.entry.label.setText('Enter text for module 1: ')
		self.game.bomb.getActiveModule().main()
		text = self.entry.text
		print(text)
		#text, ok = QInputDialog.getText(self, 'Input Answer', 'Enter number from 0 - 9: ')
		if text != None:
			#self.le.setText(str(text))
			self.game.inputHandler(text)

	def buttonHandler(self):
		pass

	def keyPressEvent(self, event):
		key = event.key()
		if (key == Qt.Key_Left):
			self.game.keyinput = 'LEFT'
		elif (key == Qt.Key_Right):
			self.game.keyinput = 'RIGHT'
		elif (key == Qt.Key_Down):
			self.game.keyinput = 'DOWN'
		elif (key == Qt.Key_Up):
			self.game.keyinput = 'UP'
		elif (key == Qt.Key_A):
			self.game.keyinput = 'BUTTONA'
		elif (key == Qt.Key_B):
			self.game.keyinput = 'BUTTONB'
		else:
			self.game.keyinput = 0

	def setModuleGuis(self):
		# self.module1 = QtWidgets.QPushButton("Module 1")
		# self.module2 = QtWidgets.QPushButton("Module 2 (Wiimote)")
		# self.module3 = QtWidgets.QPushButton("Module 3")
		# self.restartButton = QtWidgets.QPushButton("Restart")

		# self.entry = Entry("Enter something interesting...", self.textHandler)

		# self.module1.clicked.connect(lambda: self.game.bomb.changeActiveModule(0))
		# self.module2.clicked.connect(lambda: self.game.bomb.changeActiveModule(1))
		# self.module3.clicked.connect(lambda: self.game.bomb.changeActiveModule(2))
		# self.restartButton.clicked.connect(self.restart)
		


		# self.grid.addWidget(self.module1, 1, 0)
		# self.grid.addWidget(self.module2, 2, 0)
		# self.grid.addWidget(self.restartButton, 3, 0)
		# self.grid.addWidget(self.module3, 4, 0)
		self.stateLabel = QtWidgets.QLabel("State: ")
		self.timeLabel = QtWidgets.QLabel("Time remaining: ")
		self.strikesLabel = QtWidgets.QLabel(str(self.game.totalStrikes) + "/" + str(MAX_STRIKES) + ' Strikes')
		self.temp = QtWidgets.QLabel("DE2 input:")
		self.grid.addWidget(self.temp, 2, 3)


		self.grid.addWidget(self.stateLabel, 0, 2)
		self.grid.addWidget(self.timeLabel, 1, 2)
		self.grid.addWidget(self.strikesLabel, 2, 2)
		self.strikesLabel.hide()
		self.timeLabel.hide()
		self.stateLabel.hide()
		#Creating input text line
#		self.le = QLineEdit(self)
#		self.grid.addWidget(self.le, 3, 3)

		#self.grid.addWidget(self.entry, 4, 3)

		# self.grid.setColumnStretch(0, 1)
		# self.grid.setColumnStretch(1, 0)
		# self.grid.setColumnStretch(2, 1)
		# self.grid.setColumnStretch(3, 3)

		# self.grid.setRowStretch(0, 1)
		# self.grid.setRowStretch(1, 1)
		# self.grid.setRowStretch(2, 1)
		# self.grid.setRowStretch(3, 1)
		# self.grid.setRowStretch(4, 1)

		# self.newButton = QtWidgets.QPushButton(buttonText)
		# self.grid.addWidget(self.newButton, self.numButtons + 1, 0)
		# self.numButtons += 1
		# self.show()

	def restart(self):
		self.game = Game(self, self.totalTime)
		self.startButton.setEnabled(True)
		self.module1.setEnabled(False)
		self.module2.setEnabled(False)
		self.timer.stop()
		self.stateLabel.setText('')
		self.timeLabel.setText('')
		self.strikesLabel.setText('')
		self.entry.label.setText('')
		self.module3 = QtWidgets.QPushButton("Module Three")

		#needs to stop and reset timer as well
	def checkGameState(self, verbose):
		#Ignore controller inputs for types SubMod1 since this uses text field
		#if not isinstance(self.game.bomb.getActiveModule(), bomb.SubMod1):
			#Wii input! Otherwise using keyboard
			#self.game.wiiInput()
			#self.inputHandler(self.keyinput)
			#pass
			
		x = self.game.bomb.checkModStates(verbose)

		#reading DE2 module state
		#y = self.srl.serialRead()
		#self.temp.setText(y)
		#need to get rid of this line below for serial to work again
		y = "T"#kill this for serial
		if(y == "T"):
			self.DE2win = True
		if(y == "S"):
			if(x == -1):
				x += 2
			else:
				x = x+1
		if x > 0:
			self.game.totalStrikes += x
		elif x == 0 and self.DE2win:
			self.game.state = 'Win'

		if self.game.totalStrikes >= MAX_STRIKES:
			self.game.state = 'Lose'


MAX_STRIKES = 3

class Game:

	def __init__(self, frame, time):
		self.bomb = bomb.Bomb(frame, time)
		self.totalStrikes = 0
		self.state = 'ND'
		self.lastinput = 0
		#Wii remote setup!
		self.wiiSetUp()
		self.keyinput = 0
		#self.srl = srl

	'''def checkGameState(self, verbose):
		#Ignore controller inputs for types SubMod1 since this uses text field
		if not isinstance(self.bomb.getActiveModule(), bomb.SubMod1):
			#Wii input! Otherwise using keyboard
			self.wiiInput()
			#self.inputHandler(self.keyinput)
			
		x = self.bomb.checkModStates(verbose)
		#reading DE2 module state
		y = self.srl.serialRead()

		if (y == "S"):
			x+=1

		if x > 0:
			self.totalStrikes += x
		elif x == 0 and y == "T":
			self.state = 'Win'

		if self.totalStrikes >= MAX_STRIKES:
			self.state = 'Lose' '''

	#Gives input to bomb for bomb controls	not sure should use bomb.changeActiveModule
	def giveBombInput(self, bomb, bombinput):
		bomb.changeBombInput(bombinput)

	#gives input for active module on bomb.
	def giveModInput(self, bomb, modinput):
		bomb.getActiveModule().changeInput(modinput)
	
	def wiiSetUp(self):
		print ('Press 1 + 2 on your Wii Remote now ...')
		time.sleep(1)

		# Connect to the Wii Remote. If it times out
		# then quit.
		try:
			self.wii=cwiid.Wiimote()
		except RuntimeError:
			print( "Error opening wiimote connection")
			quit()
		
		print ('Wii Remote connected...\n')
		print ('Press some buttons!\n')
		print ('Press PLUS and MINUS together to disconnect and quit.\n')

		#set Wiimote to report button presses and accelerometer state 
		self.wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
		time.sleep(1)
		#turn on led to show connected 
		self.wii.led = 1

	def wiiInput(self):
		#self.motioninput = self.wii.state['acc']
		button_delay = 0.05 #was 0.1
		
		#while True:
		buttons = self.wii.state['buttons']

		#print(self.wii.state['acc'])
		time.sleep(0.1) #was 0.3
		if(buttons == 0):
			self.inputHandler(0)
		# If Plus and Minus buttons pressed
		# together then rumble and quit.
		if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
			print ('\nClosing connection ...')
			self.wii.rumble = 1
			time.sleep(1)
			self.wii.rumble = 0
			exit(self.wii)

		# Check if other buttons are pressed by
		# doing a bitwise AND of the buttons number
		# and the predefined constant for that button.
		if (buttons & cwiid.BTN_LEFT):
			print ('Left pressed')
			self.inputHandler('LEFT')
			return 'LEFT'

		if(buttons & cwiid.BTN_RIGHT):
			print ('Right pressed')
			self.inputHandler('RIGHT')
			return 'RIGHT'

		if (buttons & cwiid.BTN_UP):
			print ('Up pressed')        
			self.inputHandler('UP')
			return 'UP'

		if (buttons & cwiid.BTN_DOWN):
			print ('Down pressed')      
			self.inputHandler('DOWN')
			return 'DOWN'

		if (buttons & cwiid.BTN_1):
			print ('Button 1 pressed')
			self.inputHandler('BUTTON1')      
			return 'BUTTON1'   

		if (buttons & cwiid.BTN_2):
			print ('Button 2 pressed')
			self.inputHandler('BUTTON2')       
			return 'BUTTON2'  

		if (buttons & cwiid.BTN_A):
			print ('Button A pressed')
			self.inputHandler('BUTTONA')
			return 'BUTTONA'

		if (buttons & cwiid.BTN_B):
			print ('Button B pressed')
			self.inputHandler('BUTTONB')   
			return 'BUTTONB'   

		if (buttons & cwiid.BTN_HOME):
			print ('Home Button pressed')
			self.inputHandler('HOME')   
			return 'HOME'   

		if (buttons & cwiid.BTN_MINUS):
			print ('Minus Button pressed')
			#self.inputHandler('MINUS')  
			return 'MINUS'

		if (buttons & cwiid.BTN_PLUS):
			print( 'Plus Button pressed')
			self.inputHandler('PLUS')
			return 'PLUS'

		#time.sleep(button_delay)

	def inputHandler(self, item):
		if(self.lastinput == item):
			self.giveModInput(self.bomb, 0)
			return
		self.giveModInput(self.bomb, item)
		self.lastinput = item
