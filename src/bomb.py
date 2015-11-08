#!/usr/bin/python3

import time
import module

numModules = 1
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
				print (self.secs - s)
				elapsed = s



class TempMod:
	def __init__(self, rand_var, name):
		self.rand_var = rand_var
		self.name = name

	def testFunction(self):
		print("hi")

#module generator dependent on level
def modGen(level):
	name = ['first', 'second', 'third']
	return TempMod(level, name[level])

class Bomb:
	def __init__(self):
		self.moduleList = list()
		self.moduleStates = list()
	
	def populate(self):
		x = 1

		for x in range(numModules):	#for loop that runs 1 time for now 
			mod = modGen(x)
			self.moduleList.append(mod)
			self.moduleStates.append(INCOMPLETE)

		print('number of modules = ' + str(len(self.moduleList)))

#testing main function
def main():
	t = BombTimer(1)
	t.countdown()

	b = Bomb()
	b.populate()

	b.moduleList[0].testFunction()

main()