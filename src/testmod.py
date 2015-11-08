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

	'''test = Testmod()
	test.modSelect()
	while test.modselect == 1:
		x = int(getUserInput())
		if x == 0:
			modSelect()
		else:
			print("Your number +1 is: {}".format(x))'''

def main():
	print('Testing Module creation')
	testmodule = Module('testmodule')
	if( isinstance(testmodule, Module) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Testmodule creation test: ' + testresult)
	print('Testmod name: ' + testmodule.getName())
	if( testmodule.getName() == 'testmodule'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Testmod name test: ' + testresult + '\n')

	testmodstate = testmodule.getState()
	print('Testmod initial state: ' + testmodstate)
	if( testmodstate == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Testmod initialize test: ' + testresult + '\n')

	print('Testing change states')

	print('Change to INCOMPLETE')
	testmodule.changeStateIncomplete()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Test: ' + testresult + '\n')

	print('Change to COMPLETE')
	testmodule.changeStateComplete()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'COMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Test: ' + testresult + '\n')

	print('Change to STRIKE')
	testmodule.changeStateStrike()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'STRIKE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Test: ' + testresult + '\n')

	print('Change to INCOMPLETE')
	testmodule.changeStateIncomplete()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Test: ' + testresult + '\n')

	print ("Tests finished running.")

main()
