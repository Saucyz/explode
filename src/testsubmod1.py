from submod1 import SubMod1
from module import Module

def main():
	print('Testing Module creation')
	testmodule = SubMod1('testmodule')
	if( isinstance(testmodule, Module) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Testmodule is Module test: ' + testresult)
	if( isinstance(testmodule, SubMod1) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
	print('Testmodule is SubMod1 test: ' + testresult)
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
