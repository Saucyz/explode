import gui

def testWiimote():
	testgame = gui.Game(50)
	print('Testing no inputs, do not press anything')	
	testgame.wiiInput()
	failcount = 0
	if( testgame.bomb.getActiveModule().input == 0 ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test for no input: ' + testresult)

	print('Testing BUTTONA')
	while (testgame.bomb.getActiveModule().input == 0 ):
		testgame.wiiInput()
	print('Input received: ' + testgame.bomb.getActiveModule().input )
	if( testgame.bomb.getActiveModule().input == 'BUTTONA' ):
		testresult = 'PASS'
	else:
		testresult = 'FAIL'
		failcount += 1
	print('Test for no input: ' + testresult)

	'''while True:
		testgame.wii.rumble = (testgame.wii.state['acc'][0] < 134)
		print (testgame.wii.state['acc'])
		if testgame.wii.state['buttons'] & gui.cwiid.BTN_A:
			testgame.wii.led = (testgame.wii.state['led'] + 1 % 16)
		gui.time.sleep(0.1)'''
	print('Tests failed: ' + str(failcount) )

testWiimote()
