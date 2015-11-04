#!/usr/bin/python3

import time
import module

num_Modules = 1

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



class temp_Mod():
	def __init__(self, rand_var):
		self.rand_var = rand_var

class ModuleHolder:
	def module_Holder(self):
		x = 1
		module_List = [BombTimer]

		for x in range(0, num_Modules):	#for loop that runs 1 time for now 
			mod = mod_Gen(x)
			module_List = [mod]

		print('number of modules = ' + str(len(module_List)))

#module generator dependent on level
def mod_Gen(level):
	return temp_Mod(1)

#testing main function
def main():
	b = BombTimer()
	b.countdown()

	holder = ModuleHolder()
	holder.module_Holder()

	holder.module_Holder()

main()