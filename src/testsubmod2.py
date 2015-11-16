from submod2 import SubMod2
from module import Module

def main():
	failcount = 0
	print('Testing Module creation')
	testmodule = SubMod2()
	if( isinstance(testmodule, Module) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Testmodule is Module test: ' + testresult)
	if( isinstance(testmodule, SubMod2) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Testmodule is SubMod2 test: ' + testresult)
	print('Testmod name: ' + testmodule.getName())
	if( testmodule.getName() == 'submod2'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Testmod name test: ' + testresult + '\n')

	testmodstate = testmodule.getState()
	print('Testmod initial state: ' + testmodstate)
	if( testmodstate == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Testmod initialize test: ' + testresult + '\n')

	print('Testing change states')

	print('Change to INCOMPLETE')
	testmodule.changeStateIncomplete()
	testmodstate = testmodule.getState()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	print('Change to COMPLETE')
	testmodule.changeStateComplete()
	testmodstate = testmodule.getState()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'COMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	print('Change to STRIKE')
	testmodule.changeStateStrike()
	testmodstate = testmodule.getState()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'STRIKE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	print('Change to INCOMPLETE')
	testmodule.changeStateIncomplete()
	testmodstate = testmodule.getState()
	print('Testmod state: ' + testmodstate)
	if(testmodule.getState() == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	print('Testing submod2main()')
	print('Testing initial run, first instruction, no input, incomplete')
	testmodule.submod2main()
	print('State after running module with no inputs: ' + testmodule.getState())
	if(testmodule.getState() == 'INCOMPLETE' and testmodule.instruction_index == 0):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	testmodule.input = 'UP'
	print('Testing input: ' + testmodule.input)
	print('current_instruction before running: ' + testmodule.getCurrentInstruction())
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('current_instruction after running: ' + testmodule.getCurrentInstruction())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'INCOMPLETE' and testmodule.instruction_index == 1):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')	

	testmodule.input = 'DOWN'
	print('Testing wrong input: ' + testmodule.input)
	print('current_instruction before running: ' + testmodule.getCurrentInstruction())
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('current_instruction after running: ' + testmodule.getCurrentInstruction())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'STRIKE' and testmodule.instruction_index == 0):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')	

	print('Testing complete inputs UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A ')
	testmodule.input = 'UP'
	testmodule.submod2main()
	testmodule.input = 'UP'
	testmodule.submod2main()
	testmodule.input = 'DOWN'
	testmodule.submod2main()
	testmodule.input = 'DOWN'
	testmodule.submod2main()
	testmodule.input = 'LEFT'
	testmodule.submod2main()
	testmodule.input = 'RIGHT'
	testmodule.submod2main()
	testmodule.input = 'LEFT'
	testmodule.submod2main()
	testmodule.input = 'RIGHT'
	testmodule.submod2main()
	testmodule.input = 'BUTTONB'
	testmodule.submod2main()
	testmodule.input = 'BUTTONA'
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'COMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')	

	testmodule.input = 'UP'
	print('Testing input after complete: ' + testmodule.input)
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'COMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')	

	print('Testing reset: ')
	testmodule.resetModule()
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'INCOMPLETE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')

	print('Testing fail input on last: UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B PLUS ')
	testmodule.input = 'UP'
	testmodule.submod2main()
	testmodule.input = 'UP'
	testmodule.submod2main()
	testmodule.input = 'DOWN'
	testmodule.submod2main()
	testmodule.input = 'DOWN'
	testmodule.submod2main()
	testmodule.input = 'LEFT'
	testmodule.submod2main()
	testmodule.input = 'RIGHT'
	testmodule.submod2main()
	testmodule.input = 'LEFT'
	testmodule.submod2main()
	testmodule.input = 'RIGHT'
	testmodule.submod2main()
	testmodule.input = 'BUTTONB'
	testmodule.submod2main()
	testmodule.input = 'PLUS'
	testmodule.submod2main()
	print('State after running module: ' + testmodule.getState())
	print('instruction_index after running: ' + str(testmodule.instruction_index))
	if(testmodule.getState() == 'STRIKE' and testmodule.instruction_index == 0):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test: ' + testresult + '\n')	

	print ("Tests finished running.")
	print ("Tests failed: " + str(failcount))

main()
