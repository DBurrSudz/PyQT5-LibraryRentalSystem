# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewAccount(object):
    def setupUi(self, NewAccount):
        NewAccount.setObjectName("NewAccount")
        NewAccount.resize(439, 302)
        NewAccount.setFixedSize(439,302)
        self.centralwidget = QtWidgets.QWidget(NewAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 47, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 91, 21))
        self.label_5.setObjectName("label_5")
        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(140, 40, 191, 20))
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(140, 80, 191, 20))
        self.lastname.setObjectName("lastname")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(140, 120, 191, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(140, 170, 191, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirm = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(140, 210, 191, 20))
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setObjectName("confirm")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(340, 230, 91, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Img/create_account.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createButton.setIcon(icon)
        self.createButton.setIconSize(QtCore.QSize(22, 24))
        self.createButton.setObjectName("createButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 61, 21))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        NewAccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewAccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 21))
        self.menubar.setObjectName("menubar")
        NewAccount.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewAccount)
        self.statusbar.setObjectName("statusbar")
        NewAccount.setStatusBar(self.statusbar)

        self.retranslateUi(NewAccount)
        QtCore.QMetaObject.connectSlotsByName(NewAccount)

    def retranslateUi(self, NewAccount):
        _translate = QtCore.QCoreApplication.translate
        NewAccount.setWindowTitle(_translate("NewAccount", "MainWindow"))
        self.label.setText(_translate("NewAccount", "Firstname"))
        self.label_2.setText(_translate("NewAccount", "Lastname"))
        self.label_3.setText(_translate("NewAccount", "Username"))
        self.label_4.setText(_translate("NewAccount", "Password"))
        self.label_5.setText(_translate("NewAccount", "Confirm Password"))
        self.createButton.setText(_translate("NewAccount", "CREATE"))
        self.pushButton_2.setText(_translate("NewAccount", "Back"))
