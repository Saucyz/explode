#!/usr/bin/python

import init
from game import Game
import display
import module
from gui import MainGUI
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets

def main():
	time = 30
	if __name__ == "__main__":
		app = QtWidgets.QApplication(sys.argv)
		gui = MainGUI(app, time)


		#adding buttons works
		#gui.addButton("test")

		#g.gameLoop()

		sys.exit(app.exec_())



main()
