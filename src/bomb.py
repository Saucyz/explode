#!/usr/bin/python3

import time
import module
from submod1 import SubMod1
import threading

numModules = 1

COMPLETE = 'COMPLETE'#0
INCOMPLETE = 'INCOMPLETE'#1
STRIKE = 'STRIKE'#2

class BombTimer:
	def __init__(self, secs):
		self.secs = secs
		self.timeOut = False

	def countdown(self):
		start = time.time()
		elapsed = 0

		while elapsed < self.secs:
			s = int(time.time() - start)

			if s > elapsed:
				with lock:
					print ('Time left:' + str(self.secs - s))
					elapsed = s

		#ran out of time hence lose
		self.timeOut()

	def timeOut(self):
		print('Time has run out...')
		self.timeOut = True


class TempMod:
	def __init__(self, level, name):
		self.level = level
		self.name = name

	def testFunction(self):
		print("hi")

#module generator dependent on level
def modGen(level):
	name = ['first', 'second', 'third']
	#TEMPORY USES ONLY SUBMOD1'S!
	return SubMod1() #TempMod(level, name[level])

class Bomb:
	def __init__(self, secs):
		self.moduleList = list()
		self.timer = BombTimer(secs)
		self.input = 0
		self.activeModule = 0
		self.populate()
		#Not starting timer initially gets in the way of other tests
		#self.start()
	
	def populate(self):
		for x in range(numModules):
			mod = modGen(x)
			self.moduleList.append(mod)
			with lock:
				print('Made ' + self.moduleList[x].name + ' at ' + str(x))

		with lock:
			print('Finished populating module list. # of modules = ' + str(len(self.moduleList)))

	def start(self):
		#init the bomb module
		self.populate()

		#start timer and run seperate thread for module
		th1 = threading.Thread(target = self.timer.countdown)
		
		#need to be able to cancel a thread and reinit the module when we switch to other modules
		th2 = threading.Thread(target = self.moduleList[self.activeModule].submod1main())
		th1.start()
		th2.start()

	def changeBombInput(self, bombinput):
		self.input = bombinput

	def changeActiveModule(self, direction):
		#so far only 1 module, later add logic for more modules based on directions
		#modules should reset themselves when deactivated
		#create and run module on thread
		self.activeModule = 0

	def getActiveModIndex(self):
		return self.activeModule

	def getActiveModule(self):
		return self.moduleList[self.getActiveModIndex()]

	def checkModStates(self, verbose):
		strikes = 0
		modulesCompleted = 0

		for y in range(numModules):
			if verbose:
				print(str(y))

			z = self.moduleList[y].getState()
			if z == STRIKE:
				strikes += 1
				self.moduleList[y].changeStateIncomplete()
			elif z == COMPLETE:
				modulesCompleted += 1
			else:
				pass

			if verbose:
				print(z)

		if strikes > 0:
			return strikes
		elif modulesCompleted == numModules:
			return 0
		else:
			return -1

lock = threading.Lock()