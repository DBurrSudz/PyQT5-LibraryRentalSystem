# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 295)
        MainWindow.setFixedSize(514,295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 47, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 47, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 162, 47, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 130, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 192, 47, 21))
        self.label_6.setObjectName("label_6")
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 10, 161, 20))
        self.title.setObjectName("title")
        self.author = QtWidgets.QLineEdit(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(190, 40, 161, 20))
        self.author.setObjectName("author")
        self.genre = QtWidgets.QLineEdit(self.centralwidget)
        self.genre.setGeometry(QtCore.QRect(190, 70, 161, 20))
        self.genre.setObjectName("genre")
        self.publicationDate = QtWidgets.QDateEdit(self.centralwidget)
        self.publicationDate.setGeometry(QtCore.QRect(210, 130, 110, 22))
        self.publicationDate.setObjectName("publicationDate")
        self.amount = QtWidgets.QSpinBox(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(240, 220, 42, 22))
        self.amount.setObjectName("amount")
        self.publisher = QtWidgets.QLineEdit(self.centralwidget)
        self.publisher.setGeometry(QtCore.QRect(190, 160, 161, 20))
        self.publisher.setObjectName("publisher")
        self.bookID = QtWidgets.QLineEdit(self.centralwidget)
        self.bookID.setGeometry(QtCore.QRect(190, 190, 161, 20))
        self.bookID.setObjectName("bookID")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 220, 47, 21))
        self.label_7.setObjectName("label_7")
        self.addBook = QtWidgets.QPushButton(self.centralwidget)
        self.addBook.setGeometry(QtCore.QRect(420, 230, 75, 23))
        self.addBook.setObjectName("addBook")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 230, 75, 23))
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.collectionID = QtWidgets.QLineEdit(self.centralwidget)
        self.collectionID.setGeometry(QtCore.QRect(190, 100, 161, 20))
        self.collectionID.setObjectName("collectionID")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 90, 71, 41))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "Author(s)"))
        self.label_3.setText(_translate("MainWindow", "Genre(s)"))
        self.label_4.setText(_translate("MainWindow", "Publisher"))
        self.label_5.setText(_translate("MainWindow", "Publication Date"))
        self.label_6.setText(_translate("MainWindow", "Book ID"))
        self.label_7.setText(_translate("MainWindow", "Amount "))
        self.addBook.setText(_translate("MainWindow", "Add Book"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label_8.setText(_translate("MainWindow", "Collection ID"))

