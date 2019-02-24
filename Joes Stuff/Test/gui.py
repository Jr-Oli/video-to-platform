# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyGUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.serverBtn = QtWidgets.QPushButton(Dialog)
        self.serverBtn.setGeometry(QtCore.QRect(70, 200, 93, 28))
        self.serverBtn.setObjectName("serverBtn")
        self.clientBtn = QtWidgets.QPushButton(Dialog)
        self.clientBtn.setGeometry(QtCore.QRect(240, 200, 93, 28))
        self.clientBtn.setObjectName("clientBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "video-to-platform"))
        self.serverBtn.setText(_translate("Dialog", "Start Server"))
        self.clientBtn.setText(_translate("Dialog", "Start Client"))

