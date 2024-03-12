from design.DesignWindow import Ui_MainWindow
import sys, psycopg2, PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtGui import QIntValidator, QTextDocument, QTextCursor
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QSize, QDate, QItemSelectionModel, QModelIndex
from PyQt5.QtPrintSupport import QPrintDialog



class MainWindow(Ui_MainWindow):
    def __init__(self, role, check_press):
        super().__init__()
        #TODO # # # # # # # # # # # # # # # # # # CONNECT DB # # # # # # # # # # # # # # # # # # #
        self.providerNumber = 1
        self.providerNumber2 = 1
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setPort(5432)
        self.db.setDatabaseName('shop2')
        self.db.setUserName('postgres')
        self.db.setPassword('student')
        self.db.open()
        # LoginMain.auth_login_cl
        self.db2 = psycopg2.connect(dbname= 'shop2', user = 'postgres', password = 'student', host = 'localhost', port = 5432)
        self.cursor = self.db2.cursor()
        #TODO # # # # # # # # # # # # # # # # # # CONNECT DB # # # # # # # # # # # # # # # # # # #
        self.idInvoices = []
        self.idProviders = []
        self.dataRow = []
        
        # self.login = login
        # self.password = password
        self.check = check_press
        self.role_id = role
        self.get_roles()
        
        self.table_1()
        self.table_2()
        self.table_3()
        self.table_4()
        self.table_5()
        
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_5.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.number.setValidator(QIntValidator())
        self.number_change.setValidator(QIntValidator())
        self.name.setValidator(QIntValidator())
        self.name_change.setValidator(QIntValidator())
        self.price.setValidator(QIntValidator())
        self.price_change.setValidator(QIntValidator())
        self.quantity.setValidator(QIntValidator())
        self.quantity_change.setValidator(QIntValidator())

        self.printer.clicked.connect(self.print_btn_cl)
        
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_3.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_4.setEditTriggers(QTableView.NoEditTriggers)
        
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.alert_delete.hide()
        self.alert_delete_2.hide()
        self.alert_delete_3.hide()
        self.alert_delete_4.hide()
        self.alert_delete_5.hide()
        
        self.pushButton.setCheckable(True)
        self.calendarWidget.hide()
        
        self.pushButton.clicked.connect(self.calendar)
        self.date.setReadOnly(True)
        
        self.calendarWidget_change.hide()
        self.pushButton_2.setCheckable(True)
        
        self.pushButton_2.clicked.connect(self.calendar_2)
        self.date_change.setReadOnly(True)
        
        self.start_date_line.setReadOnly(True)
        self.end_date_line.setReadOnly(True)
        
        self.other.clicked.connect(self.btn_other)
        self.other_2.clicked.connect(self.btn_other_2)
        
        self.add.clicked.connect(self.btn_show_1)
        self.add.setCheckable(True)
        self.add_2.clicked.connect(self.btn_show_2)
        self.add_2.setCheckable(True)
        self.add_3.clicked.connect(self.btn_show_3)
        self.add_3.setCheckable(True)
        self.add_4.clicked.connect(self.btn_show_4)
        self.add_4.setCheckable(True)
        self.add_5.clicked.connect(self.btn_show_5)
        self.add_5.setCheckable(True)
        
        self.change_btn.clicked.connect(self.change_show)
        self.change_btn.setCheckable(True)
        self.change_btn_2.clicked.connect(self.change_show_2)
        self.change_btn_2.setCheckable(True)
        self.change_btn_3.clicked.connect(self.change_show_3)
        self.change_btn_3.setCheckable(True)
        self.change_btn_4.clicked.connect(self.change_show_4)
        self.change_btn_4.setCheckable(True)
        self.change_btn_5.clicked.connect(self.change_show_5)
        self.change_btn_5.setCheckable(True)
        self.print_report.setCheckable(True)
        self.print_report.clicked.connect(self.animation_open_print)
        
        self.start_date_btn.setCheckable(True)
        self.start_date_btn.clicked.connect(self.start_date_btn_click)
        
        self.end_date_btn.setCheckable(True)
        self.end_date_btn.clicked.connect(self.end_date_btn_click)
        
        self.exit_print.clicked.connect(self.exit_print_click)
        
        self.printer.clicked.connect(self.printer_click)
        
        self.ok_print.clicked.connect(self.ok_print_click)
        
        self.calendarWidget_end.clicked.connect(self.cal_4)   
        
        self.dele.setCheckable(True)
        self.del_2.setCheckable(True)
        self.del_3.setCheckable(True)
        self.dele_2.setCheckable(True)
        self.dele_3.setCheckable(True)
        
        self.cancel.clicked.connect(self.btn_cancel_1)
        self.cancel_2.clicked.connect(self.btn_cancel_2)
        self.cancel_3.clicked.connect(self.btn_cancel_3)
        self.cancel_4.clicked.connect(self.btn_cancel_4)
        self.cancel_7.clicked.connect(self.btn_cancel_5)
        
        self.cancel_change.clicked.connect(self.btn_cancel_change_1)
        self.cancel_change_2.clicked.connect(self.btn_cancel_change_2)
        self.cancel_change_3.clicked.connect(self.btn_cancel_change_3)
        self.cancel_change_4.clicked.connect(self.btn_cancel_change_4)
        self.cancel_change_5.clicked.connect(self.btn_cancel_change_5)
        
        self.cancel_delete.clicked.connect(self.cancel_delete_btn)
        self.cancel_delete_2.clicked.connect(self.cancel_delete_btn_2)
        self.cancel_delete_3.clicked.connect(self.cancel_delete_btn_3)
        self.cancel_delete_4.clicked.connect(self.cancel_delete_btn_4)
        self.cancel_delete_5.clicked.connect(self.cancel_delete_btn_5)
        
        self.dele.clicked.connect(self.delete_show_1)
        self.ok_delete.clicked.connect(self.delete_db_1)
        self.del_2.clicked.connect(self.delete_show_2)
        self.ok_delete_2.clicked.connect(self.delete_db_2)
        self.del_3.clicked.connect(self.delete_show_3)
        self.ok_delete_3.clicked.connect(self.delete_db_3)
        self.dele_2.clicked.connect(self.delete_show_4)
        self.ok_delete_4.clicked.connect(self.delete_db_4)
        self.dele_3.clicked.connect(self.delete_show_5)
        self.ok_delete_5.clicked.connect(self.delete_db_5)
        
        self.ok.clicked.connect(self.add_tb_1)
        self.ok_2.clicked.connect(self.add_tb_2)
        self.ok_3.clicked.connect(self.add_tb_3)
        self.ok_4.clicked.connect(self.add_tb_4)
        self.ok_7.clicked.connect(self.add_tb_5)
        
        self.ok_change.clicked.connect(self.change_1)
        self.ok_change_2.clicked.connect(self.change_2)
        self.ok_change_3.clicked.connect(self.change_3)
        self.ok_change_4.clicked.connect(self.change_4)
        self.ok_change_5.clicked.connect(self.change_5)
        
        self.group_postav.hide()
        self.group_postav_2.hide()
        self.group_postav_3.hide()
        self.group_postav_4.hide()
        self.group_postav_5.hide()
        self.groupBox_print.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
        self.group_postav_change.hide()
        self.group_postav_change_2.hide()
        self.group_postav_change_3.hide()
        self.group_postav_change_4.hide()
        self.group_postav_change_5.hide()
        
        self.provider_2.currentIndexChanged.connect(self.change_ons)
        self.provider_change_2.currentIndexChanged.connect(self.change_ons_2)
        
        self.cal()
        self.cal_2()
        self.cal_3()
        self.cal_4()
        
        self.calendarWidget_start.hide()
        self.calendarWidget_end.hide()
        
        self.tableView.selectRow(0)
        self.cell_item_provider()
        self.cell_item_provider2()
        self.cell_item_provider3()
        
        self.tableView_2.selectRow(0)
        self.tableView_4.selectRow(0)
        self.tableView_5.selectRow(0)
        
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
        self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
        self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_4)
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.tableView.clicked.connect(self.cell_item_provider)
        self.tableView_2.clicked.connect(self.cell_item_provider2)
        self.tableView_4.clicked.connect(self.cell_item_provider3)
        self.on_selection_changed_all()
        self.on_selection_changed_all2()
        self.on_selection_changed_all3()
        self.on_selection_changed_all4()
        self.updateInvoice3()
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed_all)
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_all2)
        self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_all3)
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_all4)
        
        self.on_selection_changed()
        self.on_selection_changed_2()
        self.on_selection_changed_3()
        self.on_selection_changed_4()
        self.on_selection_changed_5()
        
        self.comboBox_change.clear()
        self.provider_2.clear()
        self.provider_change_2.clear()
        self.numberdate.clear()
        self.numberdate_change.clear()

        self.ons2()
        self.ons3()
        self.ons3_2()
        
        self.add.clicked.connect(self.animation_add)
        self.add_2.clicked.connect(self.animation_add_2)
        self.add_3.clicked.connect(self.animation_add_3)
        self.add_4.clicked.connect(self.animation_add_4)
        self.add_5.clicked.connect(self.animation_add_5)
        
        self.change_btn.clicked.connect(self.animation_opt)
        self.change_btn_2.clicked.connect(self.animation_opt_2)
        self.change_btn_3.clicked.connect(self.animation_opt_3)
        self.change_btn_4.clicked.connect(self.animation_opt_4)
        self.change_btn_5.clicked.connect(self.animation_opt_5)
        
        self.dele.clicked.connect(self.animation_delete)
        self.del_2.clicked.connect(self.animation_delete_2)
        self.del_3.clicked.connect(self.animation_delete_3)
        self.dele_2.clicked.connect(self.animation_delete_4)
        self.dele_3.clicked.connect(self.animation_delete_5)
        
        self.ok_delete.enterEvent = self.animation_ok
        self.ok_delete.leaveEvent = self.animation_ok_else
        self.ok_delete_2.enterEvent = self.animation_ok_2
        self.ok_delete_2.leaveEvent = self.animation_ok_else_2
        self.ok_delete_3.enterEvent = self.animation_ok_3
        self.ok_delete_3.leaveEvent = self.animation_ok_else_3
        self.ok_delete_4.enterEvent = self.animation_ok_4
        self.ok_delete_4.leaveEvent = self.animation_ok_else_4
        self.ok_delete_5.enterEvent = self.animation_ok_5
        self.ok_delete_5.leaveEvent = self.animation_ok_else_5
        
        self.cancel_delete.enterEvent = self.animation_cancel
        self.cancel_delete.leaveEvent = self.animation_cancel_else
        self.cancel_delete_2.enterEvent = self.animation_cancel_2
        self.cancel_delete_2.leaveEvent = self.animation_cancel_else_2
        self.cancel_delete_3.enterEvent = self.animation_cancel_3
        self.cancel_delete_3.leaveEvent = self.animation_cancel_else_3
        self.cancel_delete_4.enterEvent = self.animation_cancel_4
        self.cancel_delete_4.leaveEvent = self.animation_cancel_else_4
        self.cancel_delete_5.enterEvent = self.animation_cancel_5
        self.cancel_delete_5.leaveEvent = self.animation_cancel_else_5
        
        self.other.clicked.connect(self.animation_other_1)
        self.other_2.clicked.connect(self.animation_other_2)

        self.tableView.hideColumn(0)
        self.tableView_2.hideColumn(0)
        self.tableView_4.hideColumn(0)
        self.tableView_4.hideColumn(3)
        self.tableView_2.hideColumn(3)
        self.tableView_3.hideColumn(5)
        self.tableView_3.hideColumn(6)
        self.tableView_2.hideColumn(4)
        self.tableView_3.hideColumn(0)
        self.tableView_3.hideColumn(7)
        
        self.comboBox.currentIndexChanged.connect(self.on_selection_for_combobox)
        self.comboBox.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(0)
    #     self.selection_model = self.tableView.selectionModel()
    #     self.save_selection()
    #     self.restore_selection()
    # def save_selection(self):
    #     selected_indexes = self.selection_model.selectedIndexes()
    #     self.saved_selection = selected_indexes
        
    # def restore_selection(self):
    #     for index in self.saved_selection:
    #         self.selection_model.select(index, QItemSelectionModel.Select)
        
    #^ # # # # # # # # # # # # # # # # # # ANIMATIONS # # # # # # # # # # # # # # # # # # #
    def animation_open_print(self):
        if self.print_report.isChecked():
            self.anim_1 = QPropertyAnimation(self.groupBox_print, b"size")
            self.anim_1.setEndValue(QSize(1920, 1080))
            self.anim_1.setDuration(500)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.groupBox_print, b"size")
            self.anim_1.setEndValue(QSize(0, 0))
            self.anim_1.setDuration(500)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
    
    def animation_off_delete(self):
        self.anim_1 = QPropertyAnimation(self.red_del, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_delete_2(self):
        self.anim_1 = QPropertyAnimation(self.red_del_2, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_delete_3(self):
        self.anim_1 = QPropertyAnimation(self.red_del_3, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_delete_4(self):
        self.anim_1 = QPropertyAnimation(self.red_del_4, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_delete_5(self):
        self.anim_1 = QPropertyAnimation(self.red_del_5, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
    
    def animation_off_opt(self):
        self.anim_1 = QPropertyAnimation(self.blue_opt, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_opt_2(self):
        self.anim_1 = QPropertyAnimation(self.blue_opt_2, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_opt_3(self):
        self.anim_1 = QPropertyAnimation(self.blue_opt_3, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_opt_4(self):
        self.anim_1 = QPropertyAnimation(self.blue_opt_4, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_opt_5(self):
        self.anim_1 = QPropertyAnimation(self.blue_opt_5, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_add(self):
        self.anim_1 = QPropertyAnimation(self.green_add, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_add_2(self):
        self.anim_1 = QPropertyAnimation(self.green_add_2, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_add_3(self):
        self.anim_1 = QPropertyAnimation(self.green_add_3, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_add_4(self):
        self.anim_1 = QPropertyAnimation(self.green_add_4, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_off_add_5(self):
        self.anim_1 = QPropertyAnimation(self.green_add_5, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()

    def animation_ok(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_else(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_2(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_2, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_else_2(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_2, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_3(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_3, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_else_3(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_3, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_4(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_4, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_else_4(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_4, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_5(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_5, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_ok_else_5(self, event):
        self.anim_1 = QPropertyAnimation(self.green_ok_5, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_else(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_2(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_2, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_else_2(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_2, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_3(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_3, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_else_3(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_3, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_4(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_4, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_else_4(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_4, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_5(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_5, b"size")
        self.anim_1.setEndValue(QSize(141, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        
    def animation_cancel_else_5(self, event):
        self.anim_1 = QPropertyAnimation(self.red_no_5, b"size")
        self.anim_1.setEndValue(QSize(41, 41))
        self.anim_1.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
    
    def animation_add(self):
        if self.add.isChecked():
            self.anim_1 = QPropertyAnimation(self.green_add, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.blue_opt, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
            
        else:
            self.anim_1 = QPropertyAnimation(self.green_add, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_add_2(self):
        if self.add_2.isChecked():
            self.anim_1 = QPropertyAnimation(self.green_add_2, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.blue_opt_2, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.green_add_2, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_add_3(self):
        if self.add_3.isChecked():
            self.anim_1 = QPropertyAnimation(self.green_add_3, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.blue_opt_3, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.green_add_3, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_add_4(self):
        if self.add_4.isChecked():
            self.anim_1 = QPropertyAnimation(self.green_add_4, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.blue_opt_4, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.green_add_4, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_add_5(self):
        if self.add_5.isChecked():
            self.anim_1 = QPropertyAnimation(self.green_add_5, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.blue_opt_5, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.green_add_5, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
        
    def animation_opt(self):
        if self.change_btn.isChecked():
            self.anim_1 = QPropertyAnimation(self.blue_opt, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.green_add, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.blue_opt, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_opt_2(self):
        if self.change_btn_2.isChecked():
            self.anim_1 = QPropertyAnimation(self.blue_opt_2, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.green_add_2, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.blue_opt_2, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_opt_3(self):
        if self.change_btn_3.isChecked():
            self.anim_1 = QPropertyAnimation(self.blue_opt_3, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.green_add_3, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.blue_opt_3, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_opt_4(self):
        if self.change_btn_4.isChecked():
            self.anim_1 = QPropertyAnimation(self.blue_opt_4, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.green_add_4, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.blue_opt_4, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_opt_5(self):
        if self.change_btn_5.isChecked():
            self.anim_1 = QPropertyAnimation(self.blue_opt_5, b"size")
            self.anim_1.setEndValue(QSize(101, 31))
            self.anim_1.setDuration(100)
            self.anim_2 = QPropertyAnimation(self.green_add_5, b"size")
            self.anim_2.setEndValue(QSize(31, 31))
            self.anim_2.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim_2)
            self.anim_group.start()
        else:
            self.anim_1 = QPropertyAnimation(self.blue_opt_5, b"size")
            self.anim_1.setEndValue(QSize(31, 31))
            self.anim_1.setDuration(100)
            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.start()
            
    def animation_delete(self):
        selectedIndex = self.tableView.selectedIndexes()
        if selectedIndex:
            if self.dele.isChecked():
                self.anim_1 = QPropertyAnimation(self.red_del, b"size")
                self.anim_1.setEndValue(QSize(101, 31))
                self.anim_1.setDuration(100)
                self.anim_group = QSequentialAnimationGroup()
                self.anim_group.addAnimation(self.anim_1)
                self.anim_group.start()
            else:
                self.anim_1 = QPropertyAnimation(self.red_del, b"size")
                self.anim_1.setEndValue(QSize(31, 31))
                self.anim_1.setDuration(100)
                self.anim_group = QSequentialAnimationGroup()
                self.anim_group.addAnimation(self.anim_1)
                self.anim_group.start()
            
    def animation_delete_2(self):
        selectedIndex = self.tableView_2.selectedIndexes()
        if selectedIndex:
                if self.del_2.isChecked():
                    self.anim_1 = QPropertyAnimation(self.red_del_2, b"size")
                    self.anim_1.setEndValue(QSize(101, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
                else:
                    self.anim_1 = QPropertyAnimation(self.red_del_2, b"size")
                    self.anim_1.setEndValue(QSize(31, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
            
    def animation_delete_3(self):
        selectedIndex = self.tableView_3.selectedIndexes()
        if selectedIndex:
                if self.del_3.isChecked():
                    self.anim_1 = QPropertyAnimation(self.red_del_3, b"size")
                    self.anim_1.setEndValue(QSize(101, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
                else:
                    self.anim_1 = QPropertyAnimation(self.red_del_3, b"size")
                    self.anim_1.setEndValue(QSize(31, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
            
    def animation_delete_4(self):
        selectedIndex = self.tableView_4.selectedIndexes()
        if selectedIndex:
                if self.dele_2.isChecked():
                    self.anim_1 = QPropertyAnimation(self.red_del_4, b"size")
                    self.anim_1.setEndValue(QSize(101, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
                else:
                    self.anim_1 = QPropertyAnimation(self.red_del_4, b"size")
                    self.anim_1.setEndValue(QSize(31, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
            
    def animation_delete_5(self):
        selectedIndex = self.tableView_5.selectedIndexes()
        if selectedIndex:
                if self.dele_3.isChecked():
                    self.anim_1 = QPropertyAnimation(self.red_del_5, b"size")
                    self.anim_1.setEndValue(QSize(101, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
                else:
                    self.anim_1 = QPropertyAnimation(self.red_del_5, b"size")
                    self.anim_1.setEndValue(QSize(31, 31))
                    self.anim_1.setDuration(100)
                    self.anim_group = QSequentialAnimationGroup()
                    self.anim_group.addAnimation(self.anim_1)
                    self.anim_group.start()
                    
    def animation_other_1(self):
        self.anim_1 = QPropertyAnimation(self.red_del_7, b"size")
        self.anim_2 = QPropertyAnimation(self.red_del_6, b"size")
        self.anim_1.setEndValue(QSize(101, 31))
        self.anim_1.setDuration(100)
        self.anim_2.setEndValue(QSize(101, 31))
        self.anim_2.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        
    def animation_other_2(self):
        self.anim_1 = QPropertyAnimation(self.red_del_7, b"size")
        self.anim_2 = QPropertyAnimation(self.red_del_6, b"size")
        self.anim_1.setEndValue(QSize(31, 31))
        self.anim_1.setDuration(100)
        self.anim_2.setEndValue(QSize(31, 31))
        self.anim_2.setDuration(100)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
         
    #^ # # # # # # # # # # # # # # # # # # COMBOBOXES # # # # # # # # # # # # # # # # # # #
    def ons2(self):
        model = self.tableView_4.model()
        for row in range(model.rowCount()):
            index = model.index(row, 1)
            self.comboBox.addItem(str(model.data(index)))
            self.comboBox_change.addItem(str(model.data(index)))
            
    def ons3(self):
        try:
            self.numberdate.clear()
            self.provider_2.clear()
            self.cursor.execute(f"SELECT id, provider FROM public.providers")
            self.query_p = self.cursor.fetchall()
            for i in self.query_p:
                self.provider_2.addItem(i[1])
                self.idProviders.append(i[0])
            self.numberdate.clear()
            self.cursor.execute(f"SELECT * FROM public.invoice")
            self.query_i = self.cursor.fetchall()
            for i in self.query_i:
                if i[3] == self.idProviders[0]:
                    self.numberdate.addItem(f"{str(i[1])}/{i[2]}")
                    self.idInvoices.append(i[0])
        except:
            pass
    

        
    def change_ons(self, index):
        self.cursor.execute(f"SELECT * FROM public.invoice")
        self.query_i = self.cursor.fetchall()
        idInvoices = self.query_p[index][0] 
        self.numberdate.clear()
        self.idInvoices.clear() 
        for i in self.query_i: 
            if i[3] == idInvoices:
                self.numberdate.addItem(f"{str(i[1])}/{i[2]}")
                self.idInvoices.append(i[0])
                
    def ons3_2(self):
        try:
            self.numberdate_change.clear()
            self.provider_change_2.clear()
            self.cursor.execute(f"SELECT id, provider FROM public.providers")
            self.query_p2 = self.cursor.fetchall()
            for i in self.query_p2:
                self.provider_change_2.addItem(i[1])
                self.idProviders.append(i[0])
            self.numberdate_change.clear()
            self.cursor.execute(f"SELECT * FROM public.invoice")
            self.query_i2 = self.cursor.fetchall()
            for i in self.query_i2:
                if i[3] == self.idProviders[0]:
                    self.numberdate_change.addItem(f"{str(i[1])}/{i[2]}")
                    self.idInvoices.append(i[0])
        except:
            pass

        
    def change_ons_2(self, index):
        self.cursor.execute(f"SELECT * FROM public.invoice")
        self.query_i2 = self.cursor.fetchall()
        idInvoices = self.query_p2[index][0] 
        self.numberdate_change.clear()
        self.idInvoices.clear()
        for i in self.query_i2: 
            if i[3] == idInvoices:
                self.numberdate_change.addItem(f"{str(i[1])}/{i[2]}")
                self.idInvoices.append(i[0])

    #^ # # # # # # # # # # # # # # # # # # SHOWS # # # # # # # # # # # # # # # # # # #
    def btn_other(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def btn_other_2(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def btn_show_1(self):
        if self.add.isChecked():
            self.group_postav.show()
            self.group_postav_change.hide()
            self.change_btn.setChecked(False)
        else:
            self.group_postav.hide()
    
    def btn_show_2(self):
        if self.add_2.isChecked():
            self.group_postav_2.show()
            self.group_postav_change_2.hide()
            self.calendarWidget_change.hide()
            self.change_btn_2.setChecked(False)
            self.pushButton_2.setChecked(False)
            self.idProviders = []
        else:
            self.group_postav_2.hide()
            self.calendarWidget.hide()
    
    def btn_show_3(self):
        if self.tableView_3.horizontalHeader().count() > 0:
            if self.add_3.isChecked():
                self.group_postav_3.show()
                self.group_postav_change_3.hide()
                self.change_btn_3.setChecked(False)
            else:
                self.group_postav_3.hide()
        elif self.tableView_3.horizontalHeader().count() == 0:
            QMessageBox.critical(self, "Ошибка!", "Нет выбраной накладной!")
            self.add_3.setChecked(False)
            
    def btn_show_4(self):
        if self.add_4.isChecked():
            self.group_postav_4.show()
            self.group_postav_change_4.hide()
            self.change_btn_4.setChecked(False)
        else:
            self.group_postav_4.hide()
            
    def btn_show_5(self):
        if self.add_5.isChecked():
            self.group_postav_5.show()
            self.group_postav_change_5.hide()
            self.change_btn_5.setChecked(False)
        else:
            self.group_postav_5.hide()
            
    def change_show(self):
        if self.tableView.selectedIndexes():
            if self.change_btn.isChecked():
                self.group_postav_change.show()
                self.group_postav.hide()
                self.add.setChecked(False)
            else:
                self.group_postav_change.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего изменять!")
            self.change_btn.setChecked(False)
            
    def change_show_2(self):
        if self.tableView_2.selectedIndexes():
            if self.change_btn_2.isChecked():
                self.group_postav_change_2.show()
                self.group_postav_2.hide()
                self.calendarWidget.hide()
                self.add_2.setChecked(False)
                self.pushButton.setChecked(False)
            else:
                self.group_postav_change_2.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего изменять!")
            self.change_btn_2.setChecked(False)
            
    def change_show_3(self):
        if self.tableView_3.selectedIndexes():
            if self.change_btn_3.isChecked():
                self.group_postav_change_3.show()
                self.group_postav_3.hide()
                self.add_3.setChecked(False)
            else:
                self.group_postav_change_3.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего изменять!")
            self.change_btn_3.setChecked(False)
            
    def change_show_4(self):
        if self.tableView_4.selectedIndexes():
            if self.change_btn_4.isChecked():
                self.group_postav_change_4.show()
                self.group_postav_4.hide()
                self.add_4.setChecked(False)
            else:
                self.group_postav_change_4.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего изменять!")
            self.change_btn_4.setChecked(False)
            
    def change_show_5(self):
        if self.tableView_5.selectedIndexes():
            if self.change_btn_5.isChecked():
                self.group_postav_change_5.show()
                self.group_postav_5.hide()
                self.add_5.setChecked(False)
            else:
                self.group_postav_change_5.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего изменять!")
            self.change_btn_5.setChecked(False)
    #^ # # # # # # # # # # # # # # # # # # CANCELS # # # # # # # # # # # # # # # # # # #
    def btn_cancel_1(self):
        self.group_postav.hide()
        self.animation_off_add()
        self.add.setChecked(False)
        
    def btn_cancel_2(self):
        self.group_postav_2.hide()
        self.calendarWidget.hide()
        self.pushButton.setChecked(False)
        self.animation_off_add_2()
        self.add_2.setChecked(False)
        
    def btn_cancel_3(self):
        self.group_postav_3.hide()
        self.animation_off_add_3()
        self.add_3.setChecked(False)
    
    def btn_cancel_4(self):
        self.group_postav_4.hide()
        self.animation_off_add_4()
        self.add_4.setChecked(False)
               
    def btn_cancel_5(self):
        self.group_postav_5.hide()
        self.add_5.setChecked(False)
        self.animation_add_5()
        
    def btn_cancel_change_1(self):
        self.group_postav_change.hide()
        self.animation_off_opt()
        self.change_btn.setChecked(False)
        
    def btn_cancel_change_2(self):
        self.group_postav_change_2.hide()
        self.animation_off_opt_2()
        self.change_btn_2.setChecked(False)
        self.calendarWidget_change.hide()
        self.pushButton_2.setChecked(False)
        
    def btn_cancel_change_3(self):
        self.group_postav_change_3.hide()
        self.animation_off_opt_3()
        self.change_btn_3.setChecked(False)
        
    def btn_cancel_change_4(self):
        self.group_postav_change_4.hide()
        self.animation_off_opt_4()
        self.change_btn_4.setChecked(False)
        
    def btn_cancel_change_5(self):
        self.group_postav_change_5.hide()
        self.animation_off_opt_5()
        self.change_btn_5.setChecked(False)
        
    def cancel_delete_btn(self):
        self.alert_delete.hide()
        self.dele.setChecked(False)
        self.animation_off_delete()
        
    def cancel_delete_btn_2(self):
        self.alert_delete_2.hide()
        self.del_2.setChecked(False)
        self.animation_off_delete_2()
        
    def cancel_delete_btn_3(self):
        self.alert_delete_3.hide()
        self.del_3.setChecked(False)
        self.animation_off_delete_3()
        
    def cancel_delete_btn_4(self):
        self.alert_delete_4.hide()
        self.animation_off_delete_4()
        self.dele_2.setChecked(False)
        
    def cancel_delete_btn_5(self):
        self.alert_delete_5.hide()
        self.dele_3.setChecked(False)
        self.animation_off_delete_5()
        
    #^ # # # # # # # # # # # # # # # # # # CALENDARS # # # # # # # # # # # # # # # # # # #
    def calendar(self):
        if self.pushButton.isChecked():
            self.calendarWidget.show()
        else:
            self.calendarWidget.hide()
    
    def calendar_2(self):
        if self.pushButton_2.isChecked():
            self.calendarWidget_change.show()
        else:
            self.calendarWidget_change.hide()
        
    def cal(self):
        def update_line_edit_date():
            selected_date = self.calendarWidget.selectedDate().toString('dd.MM.yyyy')
            self.date.setText(selected_date)
            if self.date.text():
                self.calendarWidget.hide()
                self.pushButton.setChecked(False)
        self.calendarWidget.clicked.connect(update_line_edit_date)
        
    def cal_2(self):
        def update_line_edit_date():
            selected_date = self.calendarWidget_change.selectedDate().toString('dd.MM.yyyy')
            self.date_change.setText(selected_date)
            if self.date_change.text():
                self.calendarWidget_change.hide()
                self.pushButton_2.setChecked(False)
        self.calendarWidget_change.clicked.connect(update_line_edit_date)
    
    def cal_3(self):
        def update_line_edit_date():
            selected_date = self.calendarWidget_start.selectedDate().toString('dd.MM.yyyy')
            self.start_date_line.setText(selected_date)
            if self.start_date_line.text():
                self.calendarWidget_start.hide()
                self.start_date_btn.setChecked(False)
        self.calendarWidget_start.clicked.connect(update_line_edit_date)
    
    def cal_4(self):
            selected_date = self.calendarWidget_end.selectedDate().toString('dd.MM.yyyy')
            self.end_date_line.setText(selected_date)
            if self.end_date_line.text():
                self.calendarWidget_end.hide()
                self.end_date_btn.setChecked(False) 
    
    #^ # # # # # # # # # # # # # # # # # # TABLES # # # # # # # # # # # # # # # # # # #
    def table_1(self):
        self.stm1 = QSqlQueryModel()
        self.stm1.setQuery("SELECT * FROM providers ORDER BY id")
        self.tableView.setModel(self.stm1)
        self.stm1.setHeaderData(1, QtCore.Qt.Horizontal, "Поставщик")
        self.stm1.setHeaderData(2, QtCore.Qt.Horizontal, "Адрес")
        
    def table_2(self):
        self.stm2 = QSqlTableModel(parent=self.tableView_2)
        self.stm2.setTable('invoice')
        self.stm2.select()
        self.tableView_2.setModel(self.stm2)
        self.stm2.setHeaderData(1, QtCore.Qt.Horizontal, "Номер")
        self.stm2.setHeaderData(2, QtCore.Qt.Horizontal, "Дата")
        self.tableView_2.hideColumn(3)
        self.tableView_2.hideColumn(4)
    
    def table_3(self):
        self.stm3 = QSqlTableModel(parent=self.tableView_3)
        self.stm3.setTable('product_of_invoice')
        self.stm3.select()
        self.tableView_3.setModel(self.stm3)
        self.stm3.setHeaderData(1, QtCore.Qt.Horizontal, "Товар")
        self.stm3.setHeaderData(2, QtCore.Qt.Horizontal, "Цена")
        self.stm3.setHeaderData(3, QtCore.Qt.Horizontal, "Количество")
        self.stm3.setHeaderData(4, QtCore.Qt.Horizontal, "Стоимость")
        self.tableView_3.hideColumn(5)
        
    def table_4(self):
        self.stm = QSqlQueryModel(parent=self.tableView_4)
        self.stm.setQuery('SELECT * FROM public.product ORDER BY id')
        self.tableView_4.setModel(self.stm)
        self.stm.setHeaderData(1, QtCore.Qt.Horizontal, "Товар")
        self.stm.setHeaderData(2, QtCore.Qt.Horizontal, "Цена")
    
    def table_5(self):
        self.stm5 = QSqlQueryModel()
        self.stm5.setQuery('SELECT providers.id, invoice.numbers, invoice.date, invoice.id_invoice, product_of_invoice.quantity, product_of_invoice.id_invoice, product_of_invoice.id_product FROM providers JOIN invoice ON providers.id = invoice.id_provider JOIN product_of_invoice ON invoice.id_invoice = product_of_invoice.id_invoice;')
        self.tableView_5.setModel(self.stm5)
        self.stm5.setHeaderData(1, QtCore.Qt.Horizontal, "Поставщик")
        self.stm5.setHeaderData(2, QtCore.Qt.Horizontal, "Накладные")
        self.stm5.setHeaderData(3, QtCore.Qt.Horizontal, "Дата")
        self.stm5.setHeaderData(4, QtCore.Qt.Horizontal, "Количество")
    
    #! # # # # # # # # # # # # # # # # # # DELETE SHOW # # # # # # # # # # # # # # # # # # #
    def delete_show_1(self):
        selectedIndex = self.tableView.selectedIndexes()
        if selectedIndex:
                if self.dele.isChecked():
                    self.alert_delete.show()
                else:
                    self.alert_delete.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele.setChecked(False)
            self.animation_off_delete()
        
    def delete_show_2(self):
        selectedIndex = self.tableView_2.selectedIndexes()
        if selectedIndex:
            if self.del_2.isChecked():
                self.alert_delete_2.show()
            else:
                self.alert_delete_2.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.del_2.setChecked(False)
            self.animation_off_delete_2()
            
    def delete_show_3(self):
        selectedIndex = self.tableView_3.selectedIndexes()
        if selectedIndex:
            if self.del_3.isChecked():
                self.alert_delete_3.show()
            else:
                self.alert_delete_3.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.del_3.setChecked(False)
            self.animation_off_delete_3()
            
    def delete_show_4(self):
        selectedIndex = self.tableView_4.selectedIndexes()
        if selectedIndex:
            if self.dele_2.isChecked():
                self.alert_delete_4.show()
            else:
                self.alert_delete_4.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele_2.setChecked(False)
            self.animation_off_delete_4()
            
    def delete_show_5(self):
        selectedIndex = self.tableView_5.selectedIndexes()
        if selectedIndex:
            if self.dele_3.isChecked():
                self.alert_delete_5.show()
            else:
                self.alert_delete_5.hide()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele_3.setChecked(False)
            self.animation_off_delete_5()
    
    #! # # # # # # # # # # # # # # # # # # DELETE DB # # # # # # # # # # # # # # # # # # #
    def delete_db_1(self):
        if self.tableView.selectedIndexes():
            selected_indexes = self.tableView.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView.model()
                datas_del = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    datas_del.append(model.data(index))
                print(datas_del[0])
                if self.tableView_2.model().rowCount() > 0:
                    QMessageBox.critical(self, "Ошибка!", "Вы не можете удалять поставщиков,\n у которых есть накладные!")
                else:
                    stm = QSqlQueryModel()
                    stm.setQuery(f"DELETE FROM public.providers WHERE id = '{str(datas_del[0])}'")
                    self.table_1()
            self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
            self.ons3_2()
            self.alert_delete.hide()
            self.dele.setChecked(False)
            self.animation_off_delete()
            self.tableView.selectRow(selected_indexes[0].row())
            if self.tableView.selectRow(selected_indexes[0].row()):
                self.tableView_2.selectRow(selected_indexes[0].row())
                self.cell_item_provider()
                self.cell_item_provider2()
            self.tableView.selectRow(0)
            self.cell_item_provider()
            self.cell_item_provider2()
            self.updateInvoice()
            self.updateInvoice2()
            self.updateInvoice3()
            self.ons3_2()
            self.ons3()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele.setChecked(False)
            self.alert_delete.hide()
            self.animation_off_delete()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
            
    def delete_db_2(self):
        if self.tableView_2.selectedIndexes():
            selected_indexes = self.tableView_2.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_2.model()
                datas_del2 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    datas_del2.append(model.data(index))
                print(datas_del2[0])
                if self.tableView_3.model().rowCount() > 0:
                    QMessageBox.critical(self, "Ошибка!", "Вы не можете удалять накладные,\n в которых есть товары!")
                else:
                    stm = QSqlQueryModel()
                    stm.setQuery(f"DELETE FROM public.invoice WHERE id = '{str(datas_del2[0])}'")
            self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
            self.alert_delete_2.hide()
            self.del_2.setChecked(False)
            self.cell_item_provider()
            self.animation_off_delete_2()
            self.tableView_2.selectRow(selected_indexes[0].row())
            self.ons3_2()
            self.ons3()
            last_row = self.tableView_2.model().rowCount() - 1
            self.tableView_2.selectRow(last_row)
            self.cell_item_provider2()
            self.updateInvoice()
            self.updateInvoice2()
            self.updateInvoice3()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.del_2.setChecked(False)
            self.alert_delete_2.hide()
            self.animation_off_delete_2()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
                 
    def delete_db_3(self):
        if self.tableView_3.selectedIndexes():
            selected_indexes = self.tableView_3.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_3.model()
                self.datas_del3 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_del3.append(model.data(index))
                print(self.datas_del3[0])
                stm = QSqlQueryModel()
                stm.setQuery(f"DELETE FROM public.product_of_invoice WHERE id = '{str(self.datas_del3[0])}'")
            self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
            self.alert_delete_3.hide()
            self.del_3.setChecked(False)
            self.animation_off_delete_3()
            self.updateInvoice()
            self.updateInvoice2()
            self.updateInvoice3()
            self.ons3_2()
            self.ons3()
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.del_3.setChecked(False)
            self.alert_delete_3.hide()
            self.animation_off_delete_3()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.name_change.setText("")
        
    def delete_db_4(self):
        if self.tableView_4.selectedIndexes():
            selected_indexes = self.tableView_4.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_4.model()
                self.datas_del4 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_del4.append(model.data(index))
                print(self.datas_del4[0])
                stm = QSqlQueryModel()
                stm.setQuery(f"DELETE FROM public.product WHERE id = '{str(self.datas_del4[0])}'")
                self.cell_item_provider()
            self.table_4()
            self.tableView_4.selectRow(0)
            self.updateInvoice3()
            self.comboBox.clear()
            self.comboBox_change.clear()
            self.ons2()
            self.alert_delete_4.hide()
            self.animation_off_delete_4()
            self.dele_2.setChecked(False)
            self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_4)
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele_2.setChecked(False)
            self.alert_delete_4.hide()
            self.animation_off_delete_4()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
                       
    def delete_db_5(self):
        if self.tableView_5.selectedIndexes():
            selected_indexes = self.tableView_5.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_5.model()
                self.datas_del5 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_del5.append(model.data(index))
                print(self.datas_del5[6])
                stm = QSqlQueryModel()
                stm.setQuery(f"DELETE FROM public.product_of_invoice WHERE id = '{str(self.datas_del5[7])}'")
                print(stm.lastError().text())
                self.updateInvoice3()
            self.alert_delete_5.hide()
            self.del_3.setChecked(False)
            self.animation_off_delete_5()
            self.dele_3.setChecked(False)
            self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        else:
            QMessageBox.critical(self, "Ошибка!", "Нечего удалять!")
            self.dele_3.setChecked(False)
            self.alert_delete_5.hide()
            self.animation_off_delete_5()
        self.quantity_change.setText("")
        self.numberdate_change.setCurrentIndex(0)
        self.provider_change_2.setCurrentIndex(0)
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
    
    #* # # # # # # # # # # # # # # # # # # ADD DB # # # # # # # # # # # # # # # # # # #
    def add_tb_1(self):
        query = QSqlQuery()
        try:
            if self.provider.text() and self.address.text():
                query.exec(f"INSERT INTO public.providers(provider, address) VALUES ('{self.provider.text()}','{self.address.text()}');")
                self.table_1()
                if query.isActive() == False:
                    QMessageBox.critical(self, "Ошибка!", "Такой поставщик уже есть в таблице!")
        except:
            pass
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed_all)
        self.ons3_2()
        self.ons3()
        self.add.setChecked(False)
        self.btn_cancel_1()
        self.updateInvoice3()
        last_inserted_id = query.lastInsertId()
        for row in range(self.stm1.rowCount()):
            index = self.stm1.index(row, 0)  # Предполагаем, что идентификатор находится в первом столбце
            if index.data() == last_inserted_id:
                self.tableView.selectRow(row)
                break
        self.updateInvoice()
        
    def add_tb_2(self):
        query = QSqlQuery()
        model = QSqlTableModel()
        model.setTable("invoice")
        model.select()
        try:
                query.exec(f"INSERT INTO public.invoice(numbers, date, id_provider, id_invoice) "
                           f"VALUES ('{self.number.text()}', '{self.date.text()}', '{str(self.datas[0])}', '{str(self.datas[0])}');")
                if query.isActive() == False:
                    QMessageBox.critical(self, "Ошибка!", "Такая накладная уже есть в таблице!")
                    self.table_2()
        except:
                error = query.lastError()
                print(error.text())
        self.ons3_2()
        self.ons3()
        self.btn_cancel_2()
        self.updateInvoice()
        last_inserted_id = query.lastInsertId()
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 0)  # Предполагаем, что идентификатор находится в первом столбце
            if index.data() == last_inserted_id:
                self.tableView_2.selectRow(row)
                break
        self.updateInvoice2()
        self.updateInvoice3()
        
    def add_tb_3(self):
        self.comboBox.currentIndexChanged.connect(self.on_selection_for_combobox)
        query = QSqlQuery()
        try:
            selected_data = self.comboBox.currentText()
            model = self.tableView_4.model()
            for row in range(model.rowCount()):
                self.cell_data = [model.index(row, col).data() for col in range(model.columnCount())]
                if selected_data in self.cell_data:
                    a = self.cell_data[2]
            query.exec(f"""INSERT INTO public.product_of_invoice(quantity, cost, id_provider, id_product, id_invoice) VALUES
                       ('{self.name.text()}', '{str(a * int(self.name.text()))}', '{str(int(self.datas2[0]))}', '{str(self.row_data[0])}', '{str(self.datas2[0])}');""")
            if query.isActive() == False:
                    QMessageBox.critical(self, "Ошибка!", "Такой товар уже есть в накладной!")
                    self.table_2()
        except:
            print("error")
        self.btn_cancel_3()
        self.ons3()
        self.ons3_2()
        self.updateInvoice2()
        self.updateInvoice3()
        self.updateInvoice()
        last_inserted_id = query.lastInsertId()
        for row in range(self.model2.rowCount()):
                index = self.model2.index(row, 0)  # Предполагаем, что идентификатор находится в первом столбце
                if index.data() == last_inserted_id:
                    self.tableView_3.selectRow(row)
                    break
 
    def add_tb_4(self):
        try:
            query = QSqlQuery()
            model = self.tableView_4.model()
            lastRow = model.rowCount() - 1
            firstColumn = 0
            data = model.index(lastRow, firstColumn).data()
            print(data)
            query = QSqlQuery()
            query.exec(f"INSERT INTO public.product(products, price) VALUES ('{self.product.text()}','{self.price.text()}');")
            print(query.lastError().text())
            self.table_4()
            self.comboBox.clear()
            self.comboBox_change.clear()
            self.product.setText("")
            self.price.setText("")
            self.group_postav_4.hide()
            self.ons2()
            self.add_4.setChecked(False)
            self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_4)
            last_inserted_id = query.lastInsertId()
            for row in range(self.stm.rowCount()):
                index = self.stm.index(row, 0)  # Предполагаем, что идентификатор находится в первом столбце
                if index.data() == last_inserted_id:
                    self.tableView_4.selectRow(row)
                    break
            self.updateInvoice()
            self.updateInvoice2()
            self.updateInvoice3()
        except:
            print("error")
            
    def add_tb_5(self):
        self.on_selection_changed_all4()
        self.on_selection_changed_all3()
        query = QSqlQuery()
        try:
            query.exec(f"INSERT INTO public.product_of_invoice(quantity, cost, id_provider, id_product, id_invoice) " 
                       f"VALUES ('{self.quantity.text()}', '{str(int(self.quantity.text()) * int(self.datas3[2]))}', '{str(self.idInvoices[self.numberdate.currentIndex()])}', '{str(self.datas3[0])}', '{str(self.idInvoices[self.numberdate.currentIndex()])}');")
            print(query.isActive())
            print(query.lastError().text())
            self.updateInvoice3()
            self.provider_2.clear()
            self.numberdate.clear()
            self.ons3()
        except:
            print("error")
        self.btn_cancel_5()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
        last_inserted_id = query.lastInsertId()
        for row in range(self.model3.rowCount()):
            index = self.model3.index(row, 0)  # Предполагаем, что идентификатор находится в первом столбце
            if index.data() == last_inserted_id:
                self.tableView_5.selectRow(row)
                break
    #? # # # # # # # # # # # # # # # # # # CHANGES # # # # # # # # # # # # # # # # # # #
    def change_1(self):
        try:
            self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
            if self.provider_change.text() and self.address_change.text():
                sql = QSqlQueryModel()
                sql.setQuery(f"UPDATE providers SET provider = '{self.provider_change.text()}', address = '{self.address_change.text()}' WHERE id = '{self.dw}'")
                self.table_1()
                self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
                self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed_all)
        except:
            print("error")
            self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
            self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed_all)       
        self.ons3_2()
        self.ons3()
        self.btn_cancel_change_1()
        self.animation_opt()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.tableView.selectRow(self.last_selected_row)
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
        
    def on_selection_changed_last(self, selected, deselected):
            indexes = selected.indexes()
            if indexes:
                self.last_selected_row = indexes[-1].row()
                print("hello: " + str(self.last_selected_row))
                  
    def change_2(self):
        try:
            selected_indexes = self.tableView_2.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_2.model()
                self.datas_ch1 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_ch1.append(model.data(index))
            stm = QSqlQuery()
            stm.exec_(f"UPDATE invoice SET numbers = '{self.number_change.text()}', date = '{self.date_change.text()}' WHERE id = '{str(self.datas_ch1[0])}'")
            if stm.isActive() == False:
                QMessageBox.critical(self, "Ошибка!", "Такая накладная уже есть в таблице!")
            self.updateInvoice()
            self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
            self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_last)
        except:
            print("error")
            self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
            self.updateInvoice()
        self.updateInvoice()
        self.btn_cancel_change_2()
        self.animation_opt_2()
        self.ons3_2()
        self.ons3()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.tableView_2.selectRow(self.last_selected_row) 
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
    
    def change_3(self):
        model2 = QSqlTableModel()
        model2.setTable('product_of_invoice')
        model2.select()
        try:
            selected_data = self.comboBox_change.currentText()
            model = self.tableView_4.model()
            for row in range(model.rowCount()):
                self.cell_data2 = [model.index(row, col).data() for col in range(model.columnCount())]
                if selected_data in self.cell_data2:
                    a = self.cell_data2[2]
                    b = self.cell_data2
            selected_indexes = self.tableView_3.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_3.model()
                self.datas_ch2 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_ch2.append(model.data(index))
            stm = QSqlQuery()
            stm.exec(f"""UPDATE product_of_invoice SET quantity = '{self.name_change.text()}',
                         cost = '{str(a * int(self.name_change.text()))}', id_product = '{b[0]}' WHERE id = '{str(self.datas_ch2[0])}'""")
            if stm.isActive() == False:
                    QMessageBox.critical(self, "Ошибка!", "Такой товар уже есть в накладной!")
            self.updateInvoice2()
        except:
            print("error")
            self.updateInvoice2()
            self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
        self.btn_cancel_change_3()
        self.animation_opt_3()
        self.cell_item_provider2()
        self.ons3_2()
        self.ons3()
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.updateInvoice()
        self.updateInvoice2()
        self.tableView_3.selectRow(self.last_selected_row)
        self.updateInvoice3()
        
    def change_4(self):
        # try:
            model = QSqlTableModel()
            model.setTable('product')
            model.select()
            stm = QSqlQueryModel()
            stm.setQuery(f"UPDATE product SET products = '{self.product_change.text()}', price = '{self.price_change.text()}' WHERE id = '{self.id}'")
            stm.setQuery(f"""UPDATE product_of_invoice
            SET cost = poi.quantity * p.price
            FROM product_of_invoice AS poi
            JOIN product AS p ON poi.id_product = p.id
            WHERE poi.id_product = '{self.id}';""")
            self.tableView_4.selectRow(self.last_selected_row) 
            self.comboBox.clear()
            self.comboBox_change.clear()
            self.ons2()
            self.cell_item_provider3()
            self.updateInvoice3()
        # except:
        #     print("error")
        #     self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_4)
            self.btn_cancel_change_4()
            self.animation_opt_4()
            self.ons3_2()
            self.ons3()
            self.table_4()
            self.tableView_4.selectionModel().selectionChanged.connect(self.on_selection_changed_4)
            self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
            self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
            self.tableView_4.selectRow(self.last_selected_row)
            self.updateInvoice()
            self.updateInvoice2()
            self.updateInvoice3()
            
    def change_5(self):
        self.on_selection_changed_all4()
        self.on_selection_changed_all3()
        try:
            selected_indexes = self.tableView_5.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.tableView_5.model()
                self.datas_ch3 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.datas_ch3.append(model.data(index))
            print(self.datas_ch3[7])
            stm = QSqlQueryModel()
            stm.setQuery(f"UPDATE product_of_invoice SET cost = '{str(int(self.quantity_change.text()) * int(self.datas3[2]))}', id_provider = '{str(self.idInvoices[self.numberdate_change.currentIndex()])}', id_invoice = '{str(self.idInvoices[self.numberdate_change.currentIndex()])}', quantity = '{self.quantity_change.text()}' WHERE id = '{str(self.datas_ch3[7])}';")
            selected_indexes = self.tableView_5.selectedIndexes()
            self.updateInvoice3()
        except:
            print("error")
            self.updateInvoice3()
            QMessageBox().critical(self, 'Ошибка!', 'Нечего изменять!') 
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.updateInvoice2()
        self.group_postav_change_5.hide()
        self.animation_off_opt_5()
        self.change_btn_5.setChecked(False)
        self.tableView_5.selectRow(self.last_selected_row)
        self.updateInvoice()
        self.updateInvoice2()
        self.updateInvoice3()
    
    #^ # # # # # # # # # # # # # # # # # # SELECTS # # # # # # # # # # # # # # # # # # #
    def on_selection_changed(self):
        selected_indexes = self.tableView.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.provider_change.setText(str(data[1]))
            self.address_change.setText(str(data[2]))
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.dw = data[0]
            
    def on_selection_changed_2(self):
        selected_indexes = self.tableView_2.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_2.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.number_change.setText(str(data[1]))
            self.date_change.setText(str(data[2].toString("dd.MM.yyyy")))
            print(data[2].toString("dd.MM.yyyy"))
            
    def on_selection_changed_3(self):
        selected_indexes = self.tableView_3.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_3.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.comboBox_change.setCurrentText(str(data[1]))
            self.name_change.setText(str(data[3]))
            
    def on_selection_changed_4(self):
        selected_indexes = self.tableView_4.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_4.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.product_change.setText(str(data[1]))
            self.price_change.setText(str(data[2]))
            self.id = data[0]
            self.name_id = data[1]
            
    def on_selection_changed_5(self):
        selected_indexes = self.tableView_5.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_5.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.provider_change_2.setCurrentText(str(data[2]))
            self.numberdate_change.setCurrentText(str(str(data[3]) +"/"+ str(data[4])))
            self.quantity_change.setText(str(data[5]))
            
    def on_selection_changed_all(self):
        selected_indexes = self.tableView.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView.model()
            self.datas = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                self.datas.append(model.data(index))
            print(self.datas[0])
            
    def on_selection_changed_all2(self):
        selected_indexes = self.tableView_2.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_2.model()
            self.datas2 = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                self.datas2.append(model.data(index))
            print(self.datas2[0])
    
    def on_selection_changed_all3(self):
        selected_indexes = self.tableView_4.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_4.model()
            self.datas3 = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                self.datas3.append(model.data(index))
            print(self.datas3)

            
    def on_selection_changed_all4(self):
        selected_indexes = self.tableView_5.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_5.model()
            self.datas4 = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                self.datas4.append(model.data(index))
            print(self.datas4)
            
    def on_selection_for_combobox(self, index):
        selected_text = self.comboBox.currentText()
        for row in range(self.tableView_4.model().rowCount()):
            for column in range(self.tableView_4.model().columnCount()):
                item = self.tableView_4.model().index(row, column).data()
                if item == selected_text:
                    self.row_data = []
                    for column2 in range(self.tableView_4.model().columnCount()):
                        self.row_data.append(self.tableView_4.model().index(row, column2).data())
                    print(self.row_data)
                    

#^ # # # # # # # # # # # # # # # # # # SELECT ITEM IN TABLE # # # # # # # # # # # # # # # # # # #    
    def cell_item_provider(self):
        try:
            model_index = self.tableView.selectedIndexes()[0]
            id_invoice = self.tableView.model().data(model_index)
            self.providerNumber = id_invoice
            self.updateInvoice()
        except:
            pass
        
    def updateInvoice(self):
        model = self.tableView.model()
        selected_row_index = self.tableView.currentIndex().row()
        data = model.index(selected_row_index, 0).data()
        self.model = QSqlQueryModel()
        self.model.setQuery(f"SELECT id, numbers, date FROM public.invoice WHERE id_provider = '{data}' ORDER BY id")
        self.tableView_2.setModel(self.model)
        self.tableView_2.hideColumn(0)
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Номер")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Дата")
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_all2)
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        self.tableView_2.selectRow(0)
        self.cell_item_provider2()
        self.updateInvoice2()
        
    def cell_item_provider2(self):
        try:
            model_index = self.tableView_2.selectedIndexes()[0]
            id_invoice = self.tableView_2.model().data(model_index)
            self.providerNumber2 = id_invoice
            self.updateInvoice2()
        except:
            pass
    
    def updateInvoice2(self):
        model = self.tableView_2.model()
        selected_row_index = self.tableView_2.currentIndex().row()
        data = model.index(selected_row_index, 0).data()
        self.model2 = QSqlQueryModel()
        self.model2.setQuery(f"""SELECT poi.id AS id,
        p.products AS tovar,
        p.price AS price,
        poi.quantity AS quantity,
        poi.cost AS cost,
        poi.id_provider AS id_provider,
        poi.id_product AS id_product,
        poi.id_invoice AS id_invoice
        FROM product_of_invoice AS poi
        JOIN product AS p ON poi.id_product = p.id WHERE id_provider = '{data}' ORDER BY id""")
        self.tableView_3.setModel(self.model2)
        self.tableView_3.hideColumn(0)
        self.tableView_3.hideColumn(5)
        self.tableView_3.hideColumn(6)
        self.tableView_3.hideColumn(7)
        self.model2.setHeaderData(1, QtCore.Qt.Horizontal, "Товар")
        self.model2.setHeaderData(2, QtCore.Qt.Horizontal, "Цена")
        self.model2.setHeaderData(3, QtCore.Qt.Horizontal, "Количество")
        self.model2.setHeaderData(4, QtCore.Qt.Horizontal, "Стоимость")
        self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
        self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        
    def cell_item_provider3(self):
        try:
            model_index = self.tableView_4.selectedIndexes()[0]
            id_invoice = self.tableView_4.model().data(model_index)
            self.providerNumber3 = id_invoice
            self.updateInvoice3()
        except:
            pass
    
    def updateInvoice3(self):
        try:
            model = self.tableView_4.model()
            selected_row_index = self.tableView_4.currentIndex().row()
            data = model.index(selected_row_index, 0).data()
            self.model3 = QSqlQueryModel()
            self.model3.setQuery(f"""SELECT poi.id, poi.id_invoice, p.provider, i.numbers, i.date, poi.quantity, poi.id_product, poi.id
                        FROM product_of_invoice poi
                        INNER JOIN invoice i ON poi.id_invoice = i.id
                        INNER JOIN providers p ON i.id_provider = p.id
                        WHERE poi.id_product = {data} ORDER BY id""")
            self.tableView_5.setModel(self.model3)
            self.tableView_5.hideColumn(0)
            self.tableView_5.hideColumn(1)
            self.tableView_5.hideColumn(6)
            self.tableView_5.hideColumn(7)
            self.model3.setHeaderData(2, QtCore.Qt.Horizontal, "Поставщик")
            self.model3.setHeaderData(3, QtCore.Qt.Horizontal, "Накладные")
            self.model3.setHeaderData(4, QtCore.Qt.Horizontal, "Дата")
            self.model3.setHeaderData(5, QtCore.Qt.Horizontal, "Количество")
            self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
            self.tableView_5.selectionModel().selectionChanged.connect(self.on_selection_changed_5)
        except:
            pass
        
#~ # # # # # # # # # # # # # # # # # # PRINT # # # # # # # # # # # # # # # # # # #
    def exit_print_click(self):
        self.anim_1 = QPropertyAnimation(self.groupBox_print, b"size")
        self.anim_1.setEndValue(QSize(0, 0))
        self.anim_1.setDuration(500)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.start()
        self.print_report.setChecked(False)
        
    def start_date_btn_click(self):
        if self.start_date_btn.isChecked():
            self.calendarWidget_start.show()
        else:
            self.calendarWidget_start.hide()
            
    def end_date_btn_click(self):
        if self.end_date_btn.isChecked():
            self.calendarWidget_end.show()
        else:
            self.calendarWidget_end.hide()
            
    def printer_click(self):
        self.dialog = QPrintDialog()
        self.dialog.show()
        
    def ok_print_click(self):
            query = QSqlQueryModel()
            query.setQuery(f"""SELECT i.date, p.address, p.provider, i.numbers, pr.products, poi.cost, poi.quantity
FROM product_of_invoice poi
INNER JOIN invoice i ON poi.id_invoice = i.id
INNER JOIN providers p ON i.id_provider = p.id
INNER JOIN product pr ON poi.id_product = pr.id WHERE date BETWEEN '{self.start_date_line.text()}' AND '{self.end_date_line.text()}';""")
            print(query.lastError().text())
            self.tableView_print.setModel(query)
            query.setHeaderData(0, QtCore.Qt.Horizontal, "Дата")
            query.setHeaderData(1, QtCore.Qt.Horizontal, "Поставщик")
            query.setHeaderData(2, QtCore.Qt.Horizontal, "Адрес")
            query.setHeaderData(3, QtCore.Qt.Horizontal, "Номер")
            query.setHeaderData(4, QtCore.Qt.Horizontal, "Товар")
            query.setHeaderData(5, QtCore.Qt.Horizontal, "Стоимость")
            query.setHeaderData(6, QtCore.Qt.Horizontal, "Количество")
    
    def print_btn_cl(self):
        if len(self.start_date_line.text()) > 0 and len(self.end_date_line.text()) > 0:
            self.dialog = QPrintDialog(self.tableView_print)
            if self.dialog.exec_() == 1:
                textDoc = QTextDocument()
                html = self.build_document()
                textDoc.setHtml(html)
                printer = self.dialog.printer()
                textDoc.print(printer)
                
                
    def build_document(self):
        html = f"""<h1 style='text-align: center;'>Отчет</h1>
              <h3 style='text-align: center; margin-bottom: 100px'>О поступлении товара за период с {self.start_date_line.text()} по {self.end_date_line.text()}</h3>
              <table style='text-align: center; margin-left:20%; border-collapse: collapse;'>
              <thead>
              <tr>
                  <th style='border: 1px solid black; width: 100px;'>Дата</th>
                  <th style='border: 1px solid black; width: 100px;'>Поставщик</th>
                  <th style='border: 1px solid black; width: 100px;'>Адрес</th>
                  <th style='border: 1px solid black; width: 100px;'>Номер накладной</th>
                  <th style='border: 1px solid black; width: 100px;'>Товар</th>
                  <th style='border: 1px solid black; width: 100px;'>Стоимость</th>
                  <th style='border: 1px solid black; width: 100px;'>Количество</th>
              </tr>
              </thead>
              <tbody>"""

        model = self.tableView_print.model()
        row_count = model.rowCount()
        column_count = model.columnCount()

        for row in range(row_count):
            html += "<tr>"
            for column in range(column_count):
                index = model.index(row, column)
                data = model.data(index)
                if isinstance(data, QDate):
                    # Преобразование QDate в строку
                    data = data.toString("dd.MM.yyyy")  # Можно выбрать любой нужный формат
                html += f"<td style='border: 1px solid black; width: 100px;'>{data}</td>"
            html += "</tr>"

        html += "</tbody></table>"

        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertHtml(html)
        return document.toHtml()
    
    def get_roles(self):
            if self.check > 0:
                self.groupBox_4.resize(120, 50)
                self.add_4.hide()
                self.other_2.move(10, 10)
                self.red_del_7.move(10, 10)
                self.label_123.move(10, 10)
                self.groupBox_5.hide()
                self.label_58.hide()
                self.label_57.hide()
                self.green_add_4.hide()
                self.label_66.hide()
                self.label_120.move(10, 10)
                self.label_121.move(10, 10)
                self.red_del_6.move(10, 10)
                self.groupBox_2.hide()
                self.groupBox_3.hide()
                self.groupBox.resize(120, 50)
                self.add.hide()
                self.green_add.hide()
                self.label_65.hide()
                self.other.move(10, 10)
                self.print_report.hide()
                self.label_35.hide()
            elif self.role_id[3] == str(8):
                pass
            elif self.role_id[3] == str(7):
                self.groupBox_3.hide()
                self.groupBox_4.resize(120, 50)
                self.add_4.hide()
                self.other_2.move(10, 10)
                self.red_del_7.move(10, 10)
                self.label_123.move(10, 10)
                self.groupBox_5.hide()
                self.label_58.hide()
                self.label_57.hide()
                self.green_add_4.hide()
                self.print_report.hide()
                self.label_35.hide()
            elif self.role_id[3] == str(6):
                self.label_66.hide()
                self.label_120.move(10, 10)
                self.label_121.move(10, 10)
                self.red_del_6.move(10, 10)
                self.groupBox_2.hide()
                self.groupBox_3.hide()
                self.groupBox.resize(120, 50)
                self.add.hide()
                self.green_add.hide()
                self.label_65.hide()
                self.other.move(10, 10)
                self.stackedWidget.setCurrentIndex(1)
                self.other.setChecked(True)
                


