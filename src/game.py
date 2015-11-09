#!/usr/bin/python
import bomb

MAX_STRIKES = 3

class Game:
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

	#Gives input to bomb for bomb controls
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
			self.bomb.moduleList[self.bomb.activeModule].getInput(item)
			return False

	def inputWaitLoop(self):
		wait = True
		while wait == True:
			wait = self.inputHandler()

	def gameLoop(self):
		while self.bomb.timer.timeOut == False:
			if self.checkGameState() == 'ND':
				self.inputWaitLoop()
			else:
				print('You lose...')
				return

def main():
	g = Game(5)
	g.gameLoop()

main()
