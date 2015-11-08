#!/usr/bin/python3

import time
import module
import submod1
import threading

numModules = 3

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
		self.timer = BombTimer(secs)
		self.activeModule = 1
	
	def populate(self):
		x = 1

		for x in range(numModules):	#for loop that runs 1 time for now 
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

		for x in range(numModules):
			if self.moduleList[x].state == STRIKE:
				strikes += 1
				self.moduleList[x].changeStateIncomplete()
			elif self.moduleList[x].state == COMPLETE:
				modulesCompleted += 1
			else:
				pass

		if strikes > 0:
			return strikes
		elif modulesCompleted == numModules:
			return 0
		else:
			return -1

lock = threading.Lock()
