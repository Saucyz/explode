import game

def main():
	testgame = game.Game(5)
	failcount = 0
	print('Testing Game creation')
	if( isinstance(testgame, game.Game) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test Game type test: ' + testresult)

	print('Testing Mod/Bomb')
	if( isinstance(testgame.bomb.getActiveModule(), game.bomb.module.Module) ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test active module = module: ' + testresult)

	print('Testing Game inputs')
	testinput = testgame.consoleInput()
	testgame.giveModInput(testgame.bomb, testinput)
	if( testgame.bomb.getActiveModule().input == testinput ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Module.input = ' + testgame.bomb.getActiveModule().input)
	print('Test Game input test: ' + testresult)
	
	

main()
