from module import Module

class SubMod0(Module):
	#Constructor
	def __init__(self, frame):
		Module.__init__(self, frame, 'submod0')
		self.label = QtWidgets.QLabel()
		#self.label.setGeometry(10,10,100,200)

		grid = QtWidgets.QGridLayout()
		self.setLayout(grid)

		grid.addWidget(self.label, 0, 0, 1, 1)
		reader = QtGui.QImageReader("Mod2Line.png")
		image = reader.read()
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)
		self.label.setPixmap(qpixmap)
		self.changeStateComplete()
	def main(self):
		pass
