from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class Tables:
    def __init__(self, main_window):
        super().__init__()
        self.mainwindow = main_window
        self.table_1()
        self.table_2()
        self.table_3()
        
        self.mainwindow.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.mainwindow.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
        self.mainwindow.tableView_3.setEditTriggers(QTableView.NoEditTriggers)
        
        self.mainwindow.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainwindow.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainwindow.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.mainwindow.tableView_3.hideColumn(0)
        
#& # # # # # # # # # # # # # # # VIEW TABLE # # # # # # # # # # # # # # # # 
    def table_1(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM citizen ORDER BY inn")
        self.mainwindow.tableView.setModel(query)
        query.setHeaderData(0, Qt.Horizontal, "ИНН гражданина")
        query.setHeaderData(1, Qt.Horizontal, "ФИО")
        query.setHeaderData(2, Qt.Horizontal, "Домашний адрес")
        
    def table_2(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM company ORDER BY inn")
        self.mainwindow.tableView_2.setModel(query)
        query.setHeaderData(0, Qt.Horizontal, "ИНН предприятия")
        query.setHeaderData(1, Qt.Horizontal, "Название")
        query.setHeaderData(2, Qt.Horizontal, "Адрес компании")
        
    def table_3(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM job ORDER BY id")
        self.mainwindow.tableView_3.setModel(query)
        query.setHeaderData(1, Qt.Horizontal, "ИНН гражданина")
        query.setHeaderData(2, Qt.Horizontal, "ИНН предприятия")
        query.setHeaderData(3, Qt.Horizontal, "Годовая сумма зарплаты")
        query.setHeaderData(4, Qt.Horizontal, "Годовой исчисленный налог")
#* # # # # # # # # # # # # # # # ADD TABLE # # # # # # # # # # # # # # # # 
    def table_add_1(self, window):
        if self.mainwindow.inn_line.text() and self.mainwindow.fio_line.text() and self.mainwindow.address_line.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO citizen(inn, fio, home_address) 
                    VALUES ('{self.mainwindow.inn_line.text()}', '{self.mainwindow.fio_line.text()}', '{self.mainwindow.address_line.text()}');""")
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(window, 'Ошибка!', 'Гражданин с данным инн\n уже есть в таблице!')
            self.table_1()
            
    def table_add_2(self, window):
        if self.mainwindow.inn_company_line.text() and self.mainwindow.name_company.text() and self.mainwindow.address_company.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO company(inn, name, address) 
                    VALUES ('{self.mainwindow.inn_company_line.text()}', '{self.mainwindow.name_company.text()}', '{self.mainwindow.address_company.text()}');""")
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(window, 'Ошибка!', 'Компания с данным инн\n уже есть в таблице!')
            self.table_2()
            
    def table_add_3(self, window):
        if self.mainwindow.inn_line.text() and self.mainwindow.fio_line.text() and self.mainwindow.address_line.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO citizen(inn_citizen, inn_company, salary, tax) 
                    VALUES ('{self.mainwindow.inn_line.text()}', '{self.mainwindow.fio_line.text()}', '{self.mainwindow.address_line.text()}');""")
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(window, 'Ошибка!', 'Гражданин с данным инн\n уже есть в таблице!')
            self.table_3()