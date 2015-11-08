from module import Module

#A test module
class Testmod:
	#Constructor
	def __init__(self):
		self.userinput = None
		self.modselect = 0
		#Can't have function do nothing, uses pass
		pass

	def strike(self):
		return True

	def complete(self):
		return True

	def getUserInput(self):
		self.userinput = raw_input('Type a number\n')
		return userinput

	def modSelect(self):
		modselect = 1

	def deSelect(self):
		modselect = 0

def main():
	testmodule = Module()
	if( isinstance(testmodule, Module) ):
		print('Testmodule successfully created')

	'''test = Testmod()
	test.modSelect()
	while test.modselect == 1:
		x = int(getUserInput())
		if x == 0:
			modSelect()
		else:
			print("Your number +1 is: {}".format(x))'''
	testmodstate = testmodule.getState()
	print('Testmod initial state: ' + testmodstate)
	if( testmodstate == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'

	print('Testmod state test: ' + testresult + '\n')
	print ("Tests finished running.")

main()
