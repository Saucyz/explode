# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created: Thu Nov 12 12:22:51 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myfirstgui(object):
    def setupUi(self, myfirstgui):
        myfirstgui.setObjectName("myfirstgui")
        myfirstgui.resize(598, 443)
        
        self.label = QtWidgets.QLabel(myfirstgui)

        reader = QtGui.QImageReader("/home/david/cat.jpg")
        image = reader.read()
        
        qpixmap = QtGui.QPixmap()
        qpixmap.convertFromImage(image)

        self.label.setPixmap(qpixmap)
        self.label.setGeometry(QtCore.QRect(0, 0, 583, 443))
        self.label.setObjectName("background")
        self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
        self.buttonBox.setGeometry(QtCore.QRect(200, 410, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.myTextInput = QtWidgets.QLineEdit(myfirstgui)
        self.myTextInput.setGeometry(QtCore.QRect(200, 80, 101, 21))
        self.myTextInput.setObjectName("myTextInput")
        self.listWidget = QtWidgets.QListWidget(myfirstgui)
        self.listWidget.setGeometry(QtCore.QRect(200, 110, 191, 191))
        self.listWidget.setObjectName("listWidget")
        self.clearBtn = QtWidgets.QPushButton(myfirstgui)
        self.clearBtn.setGeometry(QtCore.QRect(350, 80, 41, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.addBtn = QtWidgets.QPushButton(myfirstgui)
        self.addBtn.setGeometry(QtCore.QRect(300, 80, 41, 23))
        self.addBtn.setObjectName("addBtn")
        self.pushButton = QtWidgets.QPushButton(myfirstgui)
        self.pushButton.setGeometry(QtCore.QRect(340, 240, 31, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 240, 31, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 240, 31, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 190, 31, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 190, 31, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 190, 31, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 140, 31, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 140, 31, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 140, 31, 27))
        self.pushButton_9.setObjectName("pushButton_9")

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
        self.pushButton.setText(_translate("myfirstgui", "3"))
        self.pushButton_2.setText(_translate("myfirstgui", "2"))
        self.pushButton_3.setText(_translate("myfirstgui", "1"))
        self.pushButton_4.setText(_translate("myfirstgui", "4"))
        self.pushButton_5.setText(_translate("myfirstgui", "5"))
        self.pushButton_6.setText(_translate("myfirstgui", "6"))
        self.pushButton_7.setText(_translate("myfirstgui", "7"))
        self.pushButton_8.setText(_translate("myfirstgui", "8"))
        self.pushButton_9.setText(_translate("myfirstgui", "9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfirstgui = QtWidgets.QDialog()
    ui = Ui_myfirstgui()
    ui.setupUi(myfirstgui)
    myfirstgui.show()
    sys.exit(app.exec_())

