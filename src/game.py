#!/usr/bin/python
import bomb

MAX_STRIKES = 3

class Game:
	def __init__(self, level):
		self.bomb = Bomb(30)
		self.totalStrikes = 0
		self.won = False

	def checkGameState(self):
		x = bomb.checkModStates()
		if x > 0:
			self.totalStrikes += x
		elif x == 0:
			self.won = True
			self.win()
		else:
			self.checkLose()

		#Temporary get console input
	def consoleInput(self):
		return input()

	#Gives input to bomb for bomb controls
	def giveBombInput(self, bomb, bombinput):
		bomb.changeBombInput(bombinput)

	#gives input for active module on bomb.
	def giveModInput(self, bomb, modinput):
		bomb.getActiveModule().changeInput(modinput)

	def win(self):
		#print win screen and exit game
		pass

	def checkLose(self):
		#print lose screen and exit game
		pass
