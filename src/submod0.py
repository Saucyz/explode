from module import Module

class SubMod0(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod0')
		self.changeStateComplete()
	def main(self):
		pass
