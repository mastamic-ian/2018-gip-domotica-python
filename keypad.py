# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyPad(object):
    def setupUi(self, KeyPad):
        KeyPad.setObjectName("KeyPad")
        KeyPad.resize(800, 480)
        self.ster = QtWidgets.QPushButton(KeyPad)
        self.ster.setGeometry(QtCore.QRect(140, 330, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.ster.setFont(font)
        self.ster.setObjectName("ster")
        self.zes = QtWidgets.QPushButton(KeyPad)
        self.zes.setGeometry(QtCore.QRect(360, 130, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.zes.setFont(font)
        self.zes.setObjectName("zes")
        self.twee = QtWidgets.QPushButton(KeyPad)
        self.twee.setGeometry(QtCore.QRect(250, 30, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.twee.setFont(font)
        self.twee.setObjectName("twee")
        self.negen = QtWidgets.QPushButton(KeyPad)
        self.negen.setGeometry(QtCore.QRect(360, 230, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.negen.setFont(font)
        self.negen.setObjectName("negen")
        self.nul = QtWidgets.QPushButton(KeyPad)
        self.nul.setGeometry(QtCore.QRect(250, 330, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.nul.setFont(font)
        self.nul.setObjectName("nul")
        self.zeven = QtWidgets.QPushButton(KeyPad)
        self.zeven.setGeometry(QtCore.QRect(140, 230, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.zeven.setFont(font)
        self.zeven.setObjectName("zeven")
        self.vijf = QtWidgets.QPushButton(KeyPad)
        self.vijf.setGeometry(QtCore.QRect(250, 130, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.vijf.setFont(font)
        self.vijf.setObjectName("vijf")
        self.drie = QtWidgets.QPushButton(KeyPad)
        self.drie.setGeometry(QtCore.QRect(360, 30, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.drie.setFont(font)
        self.drie.setObjectName("drie")
        self.een = QtWidgets.QPushButton(KeyPad)
        self.een.setGeometry(QtCore.QRect(140, 30, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.een.setFont(font)
        self.een.setObjectName("een")
        self.vier = QtWidgets.QPushButton(KeyPad)
        self.vier.setGeometry(QtCore.QRect(140, 130, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.vier.setFont(font)
        self.vier.setObjectName("vier")
        self.hek = QtWidgets.QPushButton(KeyPad)
        self.hek.setGeometry(QtCore.QRect(360, 330, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hek.setFont(font)
        self.hek.setObjectName("hek")
        self.acht = QtWidgets.QPushButton(KeyPad)
        self.acht.setGeometry(QtCore.QRect(250, 230, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.acht.setFont(font)
        self.acht.setObjectName("acht")
        self.fout = QtWidgets.QFrame(KeyPad)
        self.fout.setGeometry(QtCore.QRect(550, 80, 191, 261))
        self.fout.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.fout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fout.setObjectName("fout")

        self.retranslateUi(KeyPad)
        QtCore.QMetaObject.connectSlotsByName(KeyPad)

    def retranslateUi(self, KeyPad):
        _translate = QtCore.QCoreApplication.translate
        KeyPad.setWindowTitle(_translate("KeyPad", "alarm"))
        self.ster.setText(_translate("KeyPad", "*"))
        self.zes.setText(_translate("KeyPad", "6"))
        self.twee.setText(_translate("KeyPad", "2"))
        self.negen.setText(_translate("KeyPad", "9"))
        self.nul.setText(_translate("KeyPad", "0"))
        self.zeven.setText(_translate("KeyPad", "7"))
        self.vijf.setText(_translate("KeyPad", "5"))
        self.drie.setText(_translate("KeyPad", "3"))
        self.een.setText(_translate("KeyPad", "1"))
        self.vier.setText(_translate("KeyPad", "4"))
        self.hek.setText(_translate("KeyPad", "#"))
        self.acht.setText(_translate("KeyPad", "8"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KeyPad = QtWidgets.QDialog()
    ui = Ui_KeyPad()
    ui.setupUi(KeyPad)
    KeyPad.show()
    sys.exit(app.exec_())

