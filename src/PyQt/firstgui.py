# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created: Sun Nov  8 16:19:34 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myfirstgui(object):
    def setupUi(self, myfirstgui):
        myfirstgui.setObjectName("myfirstgui")
        myfirstgui.resize(598, 443)
        self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
        self.buttonBox.setGeometry(QtCore.QRect(200, 410, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.myTextInput = QtWidgets.QLineEdit(myfirstgui)
        self.myTextInput.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.myTextInput.setObjectName("myTextInput")
        self.listWidget = QtWidgets.QListWidget(myfirstgui)
        self.listWidget.setGeometry(QtCore.QRect(120, 10, 181, 191))
        self.listWidget.setObjectName("listWidget")
        self.clearBtn = QtWidgets.QPushButton(myfirstgui)
        self.clearBtn.setGeometry(QtCore.QRect(10, 70, 101, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.addBtn = QtWidgets.QPushButton(myfirstgui)
        self.addBtn.setGeometry(QtCore.QRect(10, 40, 101, 23))
        self.addBtn.setObjectName("addBtn")
        self.graphicsView = QtWidgets.QGraphicsView(myfirstgui)
        self.graphicsView.setGeometry(QtCore.QRect(320, 10, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(myfirstgui)
        self.graphicsView_2.setGeometry(QtCore.QRect(320, 210, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(myfirstgui)
        self.graphicsView_3.setGeometry(QtCore.QRect(40, 210, 256, 192))
        self.graphicsView_3.setObjectName("graphicsView_3")

        self.retranslateUi(myfirstgui)
        self.buttonBox.accepted.connect(myfirstgui.accept)
        self.buttonBox.rejected.connect(myfirstgui.reject)
        self.clearBtn.clicked.connect(self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(myfirstgui)

    def retranslateUi(self, myfirstgui):
        _translate = QtCore.QCoreApplication.translate
        myfirstgui.setWindowTitle(_translate("myfirstgui", "My First Gui!"))
        self.clearBtn.setText(_translate("myfirstgui", "clear"))
        self.addBtn.setText(_translate("myfirstgui", "add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfirstgui = QtWidgets.QDialog()
    ui = Ui_myfirstgui()
    ui.setupUi(myfirstgui)
    myfirstgui.show()
    sys.exit(app.exec_())

