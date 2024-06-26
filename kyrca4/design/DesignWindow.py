# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1081)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:     #37393D;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(15, 70, 701, 450))
        self.tableView.setStyleSheet("QTableView{\n"
"    background-color:     #FFFFFF;\n"
"    border: 2px outset     #23272A;\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(114, 137, 218);\n"
"}\n"
"")
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(15, 600, 701, 431))
        self.tableView_2.setStyleSheet("QTableView{\n"
"    background-color:     #FFFFFF;\n"
"    border: 2px outset     #23272A;\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(114, 137, 218);\n"
"}\n"
"")
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_3.setGeometry(QtCore.QRect(1030, 70, 661, 961))
        self.tableView_3.setStyleSheet("QTableView{\n"
"    background-color:     #FFFFFF;\n"
"    border: 2px outset     #23272A;\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(114, 137, 218);\n"
"}\n"
"")
        self.tableView_3.setObjectName("tableView_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1921, 21))
        self.label.setStyleSheet("background-color:     #23272A;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(1890, 0, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.close_btn.setObjectName("close_btn")
        self.minimize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minimize_btn.setGeometry(QtCore.QRect(1860, 0, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_btn.setFont(font)
        self.minimize_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.minimize_btn.setObjectName("minimize_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(18, 27, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1030, 30, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 560, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 27, 41, 41))
        self.label_5.setStyleSheet("image: url(images/citizen); ")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1230, 30, 41, 41))
        self.label_6.setStyleSheet("image: url(images/work); ")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 560, 41, 41))
        self.label_7.setStyleSheet("image: url(images/company); ")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(720, 69, 131, 211))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"    background-color:     #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.add = QtWidgets.QPushButton(self.groupBox)
        self.add.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setStyleSheet("")
        self.add.setObjectName("add")
        self.change = QtWidgets.QPushButton(self.groupBox)
        self.change.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change.setObjectName("change")
        self.delete_btn = QtWidgets.QPushButton(self.groupBox)
        self.delete_btn.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setObjectName("delete_btn")
        self.report = QtWidgets.QPushButton(self.groupBox)
        self.report.setGeometry(QtCore.QRect(10, 170, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.report.setFont(font)
        self.report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report.setObjectName("report")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(720, 600, 131, 161))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"    background-color:     #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.add_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.add_2.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_2.setFont(font)
        self.add_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_2.setObjectName("add_2")
        self.change_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.change_2.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_2.setFont(font)
        self.change_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_2.setObjectName("change_2")
        self.delete_btn_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_btn_2.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn_2.setFont(font)
        self.delete_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn_2.setObjectName("delete_btn_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1710, 70, 131, 161))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"    background-color:     #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.add_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.add_3.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_3.setFont(font)
        self.add_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_3.setObjectName("add_3")
        self.change_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.change_3.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_3.setFont(font)
        self.change_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_3.setObjectName("change_3")
        self.delete_btn_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_btn_3.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn_3.setFont(font)
        self.delete_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn_3.setObjectName("delete_btn_3")
        self.groupBox_create = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_create.setGeometry(QtCore.QRect(720, 280, 191, 231))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_create.setFont(font)
        self.groupBox_create.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_create.setTitle("")
        self.groupBox_create.setObjectName("groupBox_create")
        self.inn_line = QtWidgets.QLineEdit(self.groupBox_create)
        self.inn_line.setGeometry(QtCore.QRect(10, 30, 171, 26))
        self.inn_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.inn_line.setObjectName("inn_line")
        self.fio_line = QtWidgets.QLineEdit(self.groupBox_create)
        self.fio_line.setGeometry(QtCore.QRect(10, 90, 171, 26))
        self.fio_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.fio_line.setObjectName("fio_line")
        self.address_line = QtWidgets.QLineEdit(self.groupBox_create)
        self.address_line.setGeometry(QtCore.QRect(10, 150, 171, 26))
        self.address_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.address_line.setObjectName("address_line")
        self.ok = QtWidgets.QPushButton(self.groupBox_create)
        self.ok.setGeometry(QtCore.QRect(10, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.groupBox_create)
        self.cancel.setGeometry(QtCore.QRect(100, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel.setObjectName("cancel")
        self.label_8 = QtWidgets.QLabel(self.groupBox_create)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_create)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 59, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_create)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 131, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.groupBox_change = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_change.setGeometry(QtCore.QRect(720, 280, 191, 231))
        self.groupBox_change.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_change.setTitle("")
        self.groupBox_change.setObjectName("groupBox_change")
        self.inn_line_change = QtWidgets.QLineEdit(self.groupBox_change)
        self.inn_line_change.setGeometry(QtCore.QRect(10, 30, 171, 26))
        self.inn_line_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.inn_line_change.setObjectName("inn_line_change")
        self.fio_line_change = QtWidgets.QLineEdit(self.groupBox_change)
        self.fio_line_change.setGeometry(QtCore.QRect(10, 90, 171, 26))
        self.fio_line_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.fio_line_change.setObjectName("fio_line_change")
        self.address_line_change = QtWidgets.QLineEdit(self.groupBox_change)
        self.address_line_change.setGeometry(QtCore.QRect(10, 150, 171, 26))
        self.address_line_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.address_line_change.setObjectName("address_line_change")
        self.ok_change = QtWidgets.QPushButton(self.groupBox_change)
        self.ok_change.setGeometry(QtCore.QRect(10, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_change.setFont(font)
        self.ok_change.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_change.setStyleSheet("")
        self.ok_change.setObjectName("ok_change")
        self.cancel_change = QtWidgets.QPushButton(self.groupBox_change)
        self.cancel_change.setGeometry(QtCore.QRect(100, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_change.setFont(font)
        self.cancel_change.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_change.setObjectName("cancel_change")
        self.label_17 = QtWidgets.QLabel(self.groupBox_change)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_change)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 59, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_change)
        self.label_19.setGeometry(QtCore.QRect(10, 130, 131, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.groupBox_create_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_create_2.setGeometry(QtCore.QRect(720, 760, 191, 231))
        self.groupBox_create_2.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_create_2.setTitle("")
        self.groupBox_create_2.setObjectName("groupBox_create_2")
        self.inn_company_line = QtWidgets.QLineEdit(self.groupBox_create_2)
        self.inn_company_line.setGeometry(QtCore.QRect(10, 30, 171, 26))
        self.inn_company_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.inn_company_line.setObjectName("inn_company_line")
        self.name_company = QtWidgets.QLineEdit(self.groupBox_create_2)
        self.name_company.setGeometry(QtCore.QRect(10, 90, 171, 26))
        self.name_company.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_company.setObjectName("name_company")
        self.address_company = QtWidgets.QLineEdit(self.groupBox_create_2)
        self.address_company.setGeometry(QtCore.QRect(10, 150, 171, 26))
        self.address_company.setStyleSheet("color: rgb(255, 255, 255);")
        self.address_company.setObjectName("address_company")
        self.ok_2 = QtWidgets.QPushButton(self.groupBox_create_2)
        self.ok_2.setGeometry(QtCore.QRect(10, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_2.setFont(font)
        self.ok_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_2.setStyleSheet("QPushButton{\n"
"    \n"
"\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.ok_2.setObjectName("ok_2")
        self.cancel_2 = QtWidgets.QPushButton(self.groupBox_create_2)
        self.cancel_2.setGeometry(QtCore.QRect(100, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_2.setFont(font)
        self.cancel_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_2.setStyleSheet("QPushButton{\n"
"    \n"
"\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.cancel_2.setObjectName("cancel_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_create_2)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_create_2)
        self.label_21.setGeometry(QtCore.QRect(10, 70, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_create_2)
        self.label_22.setGeometry(QtCore.QRect(10, 130, 141, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.groupBox_change_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_change_2.setGeometry(QtCore.QRect(720, 760, 191, 231))
        self.groupBox_change_2.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_change_2.setTitle("")
        self.groupBox_change_2.setObjectName("groupBox_change_2")
        self.inn_company_line_change = QtWidgets.QLineEdit(self.groupBox_change_2)
        self.inn_company_line_change.setGeometry(QtCore.QRect(10, 30, 171, 26))
        self.inn_company_line_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.inn_company_line_change.setObjectName("inn_company_line_change")
        self.name_company_change = QtWidgets.QLineEdit(self.groupBox_change_2)
        self.name_company_change.setGeometry(QtCore.QRect(10, 90, 171, 26))
        self.name_company_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_company_change.setObjectName("name_company_change")
        self.address_company_change = QtWidgets.QLineEdit(self.groupBox_change_2)
        self.address_company_change.setGeometry(QtCore.QRect(10, 150, 171, 26))
        self.address_company_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.address_company_change.setObjectName("address_company_change")
        self.ok_change_2 = QtWidgets.QPushButton(self.groupBox_change_2)
        self.ok_change_2.setGeometry(QtCore.QRect(10, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_change_2.setFont(font)
        self.ok_change_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_change_2.setStyleSheet("QPushButton{\n"
"    \n"
"\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.ok_change_2.setObjectName("ok_change_2")
        self.cancel_change_2 = QtWidgets.QPushButton(self.groupBox_change_2)
        self.cancel_change_2.setGeometry(QtCore.QRect(100, 190, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_change_2.setFont(font)
        self.cancel_change_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_change_2.setStyleSheet("QPushButton{\n"
"    \n"
"\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(119, 118, 123);\n"
"}")
        self.cancel_change_2.setObjectName("cancel_change_2")
        self.label_23 = QtWidgets.QLabel(self.groupBox_change_2)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_change_2)
        self.label_24.setGeometry(QtCore.QRect(10, 70, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_change_2)
        self.label_25.setGeometry(QtCore.QRect(10, 130, 141, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.groupBox_create_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_create_3.setGeometry(QtCore.QRect(1710, 230, 201, 311))
        self.groupBox_create_3.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_create_3.setTitle("")
        self.groupBox_create_3.setObjectName("groupBox_create_3")
        self.year_quta = QtWidgets.QLineEdit(self.groupBox_create_3)
        self.year_quta.setGeometry(QtCore.QRect(10, 40, 181, 25))
        self.year_quta.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_quta.setObjectName("year_quta")
        self.ok_3 = QtWidgets.QPushButton(self.groupBox_create_3)
        self.ok_3.setGeometry(QtCore.QRect(10, 260, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_3.setFont(font)
        self.ok_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_3.setObjectName("ok_3")
        self.cancel_3 = QtWidgets.QPushButton(self.groupBox_create_3)
        self.cancel_3.setGeometry(QtCore.QRect(110, 260, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_3.setFont(font)
        self.cancel_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_3.setObjectName("cancel_3")
        self.label_27 = QtWidgets.QLabel(self.groupBox_create_3)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.combo_year = QtWidgets.QComboBox(self.groupBox_create_3)
        self.combo_year.setGeometry(QtCore.QRect(10, 220, 181, 25))
        self.combo_year.setStyleSheet("QComboBox{\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox::off{\n"
"    \n"
"    background-color: rgb(114, 137, 218);\n"
"}\n"
"QComboBox::on{\n"
"    \n"
"    \n"
"    background-color: rgb(114, 137, 218);\n"
"}")
        self.combo_year.setObjectName("combo_year")
        self.label_30 = QtWidgets.QLabel(self.groupBox_create_3)
        self.label_30.setGeometry(QtCore.QRect(10, 195, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.label_33 = QtWidgets.QLabel(self.groupBox_create_3)
        self.label_33.setGeometry(QtCore.QRect(0, 70, 201, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_33.setObjectName("label_33")
        self.year_tax = QtWidgets.QLineEdit(self.groupBox_create_3)
        self.year_tax.setGeometry(QtCore.QRect(10, 95, 181, 26))
        self.year_tax.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_tax.setObjectName("year_tax")
        self.sell_tax = QtWidgets.QLineEdit(self.groupBox_create_3)
        self.sell_tax.setGeometry(QtCore.QRect(10, 160, 181, 26))
        self.sell_tax.setStyleSheet("color: rgb(255, 255, 255);")
        self.sell_tax.setObjectName("sell_tax")
        self.label_35 = QtWidgets.QLabel(self.groupBox_create_3)
        self.label_35.setGeometry(QtCore.QRect(10, 135, 181, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.groupBox_change_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_change_3.setGeometry(QtCore.QRect(1710, 230, 201, 311))
        self.groupBox_change_3.setStyleSheet("QGroupBox{\n"
"    \n"
"    background-color:      #23272A;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #7289DA;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(151, 168, 226);\n"
"}")
        self.groupBox_change_3.setTitle("")
        self.groupBox_change_3.setObjectName("groupBox_change_3")
        self.year_quta_change = QtWidgets.QLineEdit(self.groupBox_change_3)
        self.year_quta_change.setGeometry(QtCore.QRect(10, 40, 181, 26))
        self.year_quta_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_quta_change.setObjectName("year_quta_change")
        self.ok_change_3 = QtWidgets.QPushButton(self.groupBox_change_3)
        self.ok_change_3.setGeometry(QtCore.QRect(10, 260, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_change_3.setFont(font)
        self.ok_change_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_change_3.setStyleSheet("")
        self.ok_change_3.setObjectName("ok_change_3")
        self.cancel_change_3 = QtWidgets.QPushButton(self.groupBox_change_3)
        self.cancel_change_3.setGeometry(QtCore.QRect(110, 260, 80, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_change_3.setFont(font)
        self.cancel_change_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_change_3.setObjectName("cancel_change_3")
        self.label_29 = QtWidgets.QLabel(self.groupBox_change_3)
        self.label_29.setGeometry(QtCore.QRect(10, 15, 181, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.combo_year_change = QtWidgets.QComboBox(self.groupBox_change_3)
        self.combo_year_change.setGeometry(QtCore.QRect(10, 220, 181, 25))
        self.combo_year_change.setStyleSheet("QComboBox{\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox::off{\n"
"    \n"
"    background-color: rgb(114, 137, 218);\n"
"}\n"
"QComboBox::on{\n"
"    \n"
"    \n"
"    background-color: rgb(114, 137, 218);\n"
"}")
        self.combo_year_change.setObjectName("combo_year_change")
        self.label_31 = QtWidgets.QLabel(self.groupBox_change_3)
        self.label_31.setGeometry(QtCore.QRect(10, 195, 171, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_31.setObjectName("label_31")
        self.year_tax_change = QtWidgets.QLineEdit(self.groupBox_change_3)
        self.year_tax_change.setGeometry(QtCore.QRect(10, 95, 181, 26))
        self.year_tax_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_tax_change.setObjectName("year_tax_change")
        self.label_32 = QtWidgets.QLabel(self.groupBox_change_3)
        self.label_32.setGeometry(QtCore.QRect(0, 70, 201, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_32.setObjectName("label_32")
        self.sell_tax_change = QtWidgets.QLineEdit(self.groupBox_change_3)
        self.sell_tax_change.setGeometry(QtCore.QRect(10, 160, 181, 26))
        self.sell_tax_change.setStyleSheet("color: rgb(255, 255, 255);")
        self.sell_tax_change.setObjectName("sell_tax_change")
        self.label_34 = QtWidgets.QLabel(self.groupBox_change_3)
        self.label_34.setGeometry(QtCore.QRect(10, 135, 181, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1700, 600, 221, 231))
        self.label_11.setStyleSheet("image: url(images/wumpus);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.tableView.raise_()
        self.tableView_2.raise_()
        self.tableView_3.raise_()
        self.label.raise_()
        self.close_btn.raise_()
        self.minimize_btn.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_create.raise_()
        self.groupBox_change.raise_()
        self.groupBox_create_2.raise_()
        self.groupBox_change_2.raise_()
        self.groupBox_create_3.raise_()
        self.groupBox_change_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_btn.setText(_translate("MainWindow", "×"))
        self.minimize_btn.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Граждане"))
        self.label_3.setText(_translate("MainWindow", "Место работы"))
        self.label_4.setText(_translate("MainWindow", "Предприятие"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.delete_btn.setText(_translate("MainWindow", "Удалить"))
        self.report.setText(_translate("MainWindow", "Отчёт"))
        self.add_2.setText(_translate("MainWindow", "Добавить"))
        self.change_2.setText(_translate("MainWindow", "Изменить"))
        self.delete_btn_2.setText(_translate("MainWindow", "Удалить"))
        self.add_3.setText(_translate("MainWindow", "Добавить"))
        self.change_3.setText(_translate("MainWindow", "Изменить"))
        self.delete_btn_3.setText(_translate("MainWindow", "Удалить"))
        self.ok.setText(_translate("MainWindow", "ОК"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
        self.label_8.setText(_translate("MainWindow", "ИНН гражданина"))
        self.label_9.setText(_translate("MainWindow", "ФИО"))
        self.label_10.setText(_translate("MainWindow", "Домашний адрес"))
        self.ok_change.setText(_translate("MainWindow", "ОК"))
        self.cancel_change.setText(_translate("MainWindow", "Отмена"))
        self.label_17.setText(_translate("MainWindow", "ИНН гражданина"))
        self.label_18.setText(_translate("MainWindow", "ФИО"))
        self.label_19.setText(_translate("MainWindow", "Домашний адрес"))
        self.ok_2.setText(_translate("MainWindow", "ОК"))
        self.cancel_2.setText(_translate("MainWindow", "Отмена"))
        self.label_20.setText(_translate("MainWindow", "ИНН предприятия"))
        self.label_21.setText(_translate("MainWindow", "Название предприятия"))
        self.label_22.setText(_translate("MainWindow", "Адрес предприятия"))
        self.ok_change_2.setText(_translate("MainWindow", "ОК"))
        self.cancel_change_2.setText(_translate("MainWindow", "Отмена"))
        self.label_23.setText(_translate("MainWindow", "ИНН предприятия"))
        self.label_24.setText(_translate("MainWindow", "Название предприятия"))
        self.label_25.setText(_translate("MainWindow", "Адрес предприятия"))
        self.ok_3.setText(_translate("MainWindow", "ОК"))
        self.cancel_3.setText(_translate("MainWindow", "Отмена"))
        self.label_27.setText(_translate("MainWindow", "Годовая сумма зарплаты"))
        self.label_30.setText(_translate("MainWindow", "Год"))
        self.label_33.setText(_translate("MainWindow", "Годовой исчисленный налог"))
        self.label_35.setText(_translate("MainWindow", "Оплаченные налоги"))
        self.ok_change_3.setText(_translate("MainWindow", "ОК"))
        self.cancel_change_3.setText(_translate("MainWindow", "Отмена"))
        self.label_29.setText(_translate("MainWindow", "Годовая сумма зарплаты"))
        self.label_31.setText(_translate("MainWindow", "Год"))
        self.label_32.setText(_translate("MainWindow", "Годовой исчисленный налог"))
        self.label_34.setText(_translate("MainWindow", "Оплаченные налоги"))
