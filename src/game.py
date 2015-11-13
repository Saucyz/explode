#!/usr/bin/python
import bomb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog, QLineEdit)

MAX_STRIKES = 3

class Game(QMainWindow):
	def __init__(self, time):
		self.bomb = bomb.Bomb(time)
		self.totalStrikes = 0
		self.won = False

	def checkGameState(self):
		state = 'ND'
		x = self.bomb.checkModStates()

		if x > 0:
			self.totalStrikes += x
		elif x == 0:
			self.won = True
			self.win()
			state = 'Win'
		else:
			pass

		if self.totalStrikes >= 3:
			self.lose()
			state = 'Lose'

		return state

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

	def inputHandler(self):
		item = input('Enter an answer...   ')
		if item == '':
			print('Waiting...')	#replace for when the input signal becomes continuous
			return True
		else:
			self.giveModInput(self.bomb, item)
			return False

	def inputWaitLoop(self):
		wait = True
		while wait == True:
			wait = self.inputHandler()

	def keyPressEvent(self, event):
		key = event.key()
		print(key)

		if key == QtCore.Qt.Key_Left:
			print('Left Arrow Pressed')
			
		elif key == QtCore.Qt.Key_D:
			print('D Key Pressed')

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
