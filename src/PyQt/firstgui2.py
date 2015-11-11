import sys
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created: Mon Nov  9 09:46:58 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import time

class MainGUI(QtWidgets.QMainWindow):

	def button1pushed(self):
		self.button2.setText(self.button2.text() + "!")

	def timerDone(self):
		elapsed = int(time.time() - self.startTime)
		self.label2.setText(str(elapsed))

	def button2pushed(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.timerDone)
		self.timer.setSingleShot(False)
		self.timer.start()

		self.startTime = time.time()

	def __init__(self, app):
		super().__init__()

		self.button1 = QtWidgets.QPushButton("mytext1")
		self.button2 = QtWidgets.QPushButton("mytext2")
		self.button3 = QtWidgets.QPushButton("mytext3")
		
		self.list1 = QtWidgets.QListWidget()

		self.label = QtWidgets.QLabel()
		self.label2 = QtWidgets.QLabel("0")

		reader = QtGui.QImageReader("/home/david/cat.jpg")
		image = reader.read()
		
		qpixmap = QtGui.QPixmap()
		qpixmap.convertFromImage(image)

		self.label.setPixmap(qpixmap)

		grid = QtWidgets.QGridLayout()


		window = QtWidgets.QWidget()
		window.setLayout(grid)
		self.setCentralWidget(window)

		grid.addWidget(self.button1, 0, 0)
		grid.addWidget(self.button2, 1, 0)
		grid.addWidget(self.button3, 2, 0)
		grid.addWidget(self.list1, 0, 1, 4, 1)
		grid.addWidget(self.label,0, 2, 4, 1)
		grid.addWidget(self.label2, 3, 0)

		self.button1.clicked.connect(self.button1pushed)
		self.button2.clicked.connect(self.button2pushed)

		# self.
		self.show()


		# myfirstgui.setObjectName("myfirstgui")
		# myfirstgui.resize(598, 443)
		# self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
		# self.buttonBox.setGeometry(QtCore.QRect(200, 410, 381, 32))
		# self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		# self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
		# self.buttonBox.setObjectName("buttonBox")
		# self.myTextInput = QtWidgets.QLineEdit(myfirstgui)
		# self.myTextInput.setGeometry(QtCore.QRect(10, 10, 101, 21))
		# self.myTextInput.setObjectName("myTextInput")
		# self.listWidget = QtWidgets.QListWidget(myfirstgui)
		# self.listWidget.setGeometry(QtCore.QRect(120, 10, 181, 191))
		# self.listWidget.setObjectName("listWidget")
		# self.clearBtn = QtWidgets.QPushButton(myfirstgui)
		# self.clearBtn.setGeometry(QtCore.QRect(10, 70, 101, 23))
		# self.clearBtn.setObjectName("clearBtn")
		# self.addBtn = QtWidgets.QPushButton(myfirstgui)
		# self.addBtn.setGeometry(QtCore.QRect(10, 40, 101, 23))
		# self.addBtn.setObjectName("addBtn")
		# self.graphicsView = QtWidgets.QGraphicsView(myfirstgui)
		# self.graphicsView.setGeometry(QtCore.QRect(320, 10, 256, 192))
		# self.graphicsView.setObjectName("graphicsView")
		# self.graphicsView_2 = QtWidgets.QGraphicsView(myfirstgui)
		# self.graphicsView_2.setGeometry(QtCore.QRect(320, 210, 256, 192))
		# self.graphicsView_2.setObjectName("graphicsView_2")
		# self.graphicsView_3 = QtWidgets.QGraphicsView(myfirstgui)
		# self.graphicsView_3.setGeometry(QtCore.QRect(40, 210, 256, 192))
		# self.graphicsView_3.setObjectName("graphicsView_3")

		# self.retranslateUi(myfirstgui)
		# self.buttonBox.accepted.connect(myfirstgui.accept)
		# self.buttonBox.rejected.connect(myfirstgui.reject)
		# self.clearBtn.clicked.connect(self.listWidget.clear)
		# QtCore.QMetaObject.connectSlotsByName(myfirstgui)

	# def retranslateUi(self, myfirstgui):
	#     _translate = QtCore.QCoreApplication.translate
	#     myfirstgui.setWindowTitle(_translate("myfirstgui", "My First Gui!"))
	#     self.clearBtn.setText(_translate("myfirstgui", "clear"))
	#     self.addBtn.setText(_translate("myfirstgui", "add"))


if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	gui = MainGUI(app)

	sys.exit(app.exec_())

