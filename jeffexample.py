class Player:
	def __init__(self):
		self.name = ""
		self.items = []

	def addItem(self, item):
		self.items.append(item)

class SpecialPlayer(Player):
	def printItems(self):
		print self.items

	

def main():
	print "hi"
	p1 = SpecialPlayer() 
	p1.name = "Jeff"
	
	p1.addItem(45)
	p1.addItem(3)
	p1.addItem(13)

	print p1.items
	print p1.items

	for item in p1.items:
		print "\t" + str(item)

	players = {}
	players["jeff"] = p1
	
	print	players["jeff"].items	
	p1.printItems()

	if  (3 in p1.items):
		print ("hello")

main()
