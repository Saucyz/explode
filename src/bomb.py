#!/usr/bin/python3

import time
import module
import threading

numModules = 3
activeModule = 1

COMPLETE = 0
INCOMPLETE = 1
STRIKE = 2

class BombTimer:
	def __init__(self, secs):
		self.secs = secs

	def countdown(self):
		start = time.time()
		elapsed = 0

		while elapsed < self.secs:
			s = int(time.time() - start)

			if s > elapsed:
				with lock:
					print ('Time left:' + str(self.secs - s))
					elapsed = s


class TempMod:
	def __init__(self, level, name):
		self.level = level
		self.name = name

	def testFunction(self):
		print("hi")

#module generator dependent on level
def modGen(level):
	name = ['first', 'second', 'third']
	return TempMod(level, name[level])

class Bomb:
	def __init__(self, secs):
		self.moduleList = list()
		self.moduleStates = list()
		self.timer = BombTimer(secs)
	
	def populate(self):
		x = 1

		for x in range(numModules):	#for loop that runs 1 time for now 
			mod = modGen(x)
			self.moduleList.append(mod)
			self.moduleStates.append(INCOMPLETE)
			with lock:
				print('Made ' + self.moduleList[x].name + ' at ' + str(x))

		with lock:
			print('number of modules = ' + str(len(self.moduleList)))

	def start(self):
		th1 = threading.Thread(target = self.timer.countdown)
		th2 = threading.Thread(target = self.populate)
		th1.start()
		th2.start()

lock = threading.Lock()

#testing main function
def main():
	b = Bomb(3)
	b.start()
	#timer = BombTimer(100)
	#timer.countdown()

	#bomb = Bomb()
	#bomb.populate()

	#bomb.moduleList[0].testFunction()

main()