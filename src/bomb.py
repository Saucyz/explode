#!/usr/bin/python3

import time
import module
from submod1 import SubMod1
from submod2 import SubMod2
import threading

numModules = 2

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

class Bomb:
	def __init__(self, frame, secs):
		self.frame = frame
		self.moduleList = list()
		self.timer = BombTimer(secs)
		self.input = 0
		self.activeModule = 0
		self.populate()
		#Not starting timer initially gets in the way of other tests
		#self.start()

	#module generator dependent on level
	def modGen(self,level):
		name = ['first', 'second', 'third']
		if(level == 0):
			return SubMod1(self.frame)
		else:
			return SubMod2(self.frame)

	def populate(self):
		for x in range(numModules):
			mod = self.modGen(x)
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
		th2 = threading.Thread(target = self.moduleList[self.activeModule].main())
		th1.start()
		th2.start()

	def changeBombInput(self, bombinput):
		self.input = bombinput

	def changeActiveModule(self, direction):
		#for now changes active mod to direction index in list
		#modules should reset themselves when deactivated
		#create and run module on thread
		self.activeModule = direction
		i = 0
		while (i < len(self.moduleList)):
			if (i != direction):
				self.moduleList[i].hide()
			i += 1
		
		self.getActiveModule().show()
		

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
			#Small fix for checking submodmain more often may be threading problem
			self.moduleList[y].main()
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
