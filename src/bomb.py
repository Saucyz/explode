#!/usr/bin/python3

import time
import module
from submod1 import SubMod1
import threading

numModules = 3

COMPLETE = 'COMPLETE'#0
INCOMPLETE = 'INCOMPLETE'#1
STRIKE = 'STRIKE'#2

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
	return SubMod1() #TempMod(level, name[level])

class Bomb:
	def __init__(self, secs):
		self.moduleList = list()
		self.timer = BombTimer(secs)
		self.activeModule = 1
	
	def populate(self):
		for x in range(numModules):
			mod = modGen(x)
			self.moduleList.append(mod)
			with lock:
				print('Made ' + self.moduleList[x].name + ' at ' + str(x))

		with lock:
			print('number of modules = ' + str(len(self.moduleList)))

	def start(self):
		th1 = threading.Thread(target = self.timer.countdown)
		th2 = threading.Thread(target = self.populate)
		th1.start()
		th2.start()

	def changeActiveModule(self, direction):
		#so far only 1 module, later add logic for more modules based on directions
		#modules should reset themselves when deactivated
		self.activeModule = 1

	def checkModStates(self):
		strikes = 0
		modulesCompleted = 0

		for y in range(numModules):
			z = self.moduleList[y].getState()
			if z == STRIKE:
				strikes += 1
				self.moduleList[y].changeStateIncomplete()
			elif z == COMPLETE:
				modulesCompleted += 1
			else:
				pass
			print(z)

		if strikes > 0:
			return strikes
		elif modulesCompleted == numModules:
			return 0
		else:
			return -1

lock = threading.Lock()
