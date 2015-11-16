import gui

def testWiimote():
	testgame = gui.Game(50)
	while True:
		testgame.wii.rumble = (testgame.wii.state['acc'][0] < 134)
		if testgame.wii.state['buttons'] & gui.cwiid.BTN_A:
			testgame.wii.led = (testgame.wii.state['led'] + 1 % 16)
		gui.time.sleep(0.1)
testWiimote()
