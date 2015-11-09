import bomb

#testing main function
def main():
	failcount = 0
	print('Creating bomb with three modules.')
	b = bomb.Bomb(3)
	if( isinstance(b, bomb.Bomb)):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1

	print('Type test: ' + testresult)
	b.start()

	print('Checking number of modules in bomb')
	print(str(len(b.moduleList)))
	if(len(b.moduleList) == bomb.numModules):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Module count test: ' + testresult)

	print('Checking initial states of bombs')
	b.checkModStates()

	print('Changing bomb states')
	b.moduleList[0].changeStateComplete()
	b.moduleList[1].changeStateIncomplete()
	b.moduleList[2].changeStateStrike()

	if( b.moduleList[0].getState() == 'COMPLETE' and b.moduleList[1].getState() == 'INCOMPLETE' and b.moduleList[2].getState() == 'STRIKE'):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1

	print('Change states test: ' + testresult)
	b.checkModStates()

	print ("Tests finished running.")
	print ("Tests failed: " + str(failcount))

	#timer = BombTimer(100)
	#timer.countdown()

	#bomb = Bomb()
	#bomb.populate()

	#bomb.moduleList[0].testFunction()

main()
