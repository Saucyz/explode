import bomb

#testing main function
def main():
	b = bomb.Bomb(3)
	b.start()
	
	b.checkModStates()

	b.moduleList[0].changeStateComplete()
	b.moduleList[1].changeStateIncomplete()
	b.moduleList[2].changeStateStrike()

	b.checkModStates()
	#timer = BombTimer(100)
	#timer.countdown()

	#bomb = Bomb()
	#bomb.populate()

	#bomb.moduleList[0].testFunction()

main()
