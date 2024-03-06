# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/untitled_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 271)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.label.setStyleSheet("background-color: #323339;\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(20, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:     #23272A;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(20, 60, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color:     #23272A;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 261, 151))
        self.label_4.setStyleSheet("image: url(images/wumpus-none-blocked);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.auth = QtWidgets.QPushButton(self.centralwidget)
        self.auth.setGeometry(QtCore.QRect(20, 190, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.auth.setFont(font)
        self.auth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auth.setStyleSheet("QPushButton{\n"
"    background-color:     #7289DA;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:     #8E9EDA;\n"
"}\n"
"")
        self.auth.setObjectName("auth")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(519, 10, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("QPushButton{\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}")
        self.exit.setObjectName("exit")
        self.neighbor = QtWidgets.QPushButton(self.centralwidget)
        self.neighbor.setGeometry(QtCore.QRect(20, 230, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.neighbor.setFont(font)
        self.neighbor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.neighbor.setStyleSheet("QPushButton{\n"
"    background-color:     #7289DA;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:     #8E9EDA;\n"
"}\n"
"")
        self.neighbor.setObjectName("neighbor")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Логин:"))
        self.label_3.setText(_translate("MainWindow", "Пароль:"))
        self.auth.setText(_translate("MainWindow", "Войти"))
        self.exit.setText(_translate("MainWindow", "×"))
        self.neighbor.setText(_translate("MainWindow", "Гость"))
