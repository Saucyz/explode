import module

#A test module
class Testmod:
	#Constructor
	def __init__(self):
		#Can't have function do nothing, uses pass
		pass

def strike():
	return true

def complete():
	return true

def main():
	x = raw_input('Type a number\n')
	x = int(x)+1
	print("Your number +1 is: {}".format(x))
	print "main() finished running."

main()
