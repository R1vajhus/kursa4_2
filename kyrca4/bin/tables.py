from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from design.Animation import AnimationButtons

class Tables:
    def __init__(self, main_window):
        super().__init__()
        self.mainwindow = main_window
        self.providerNumber = 1
        
        self.widget = QWidget()
        self.widget.move(570, 230)
        

        
        self.table_1()
        self.table_2()
        
        self.animation = AnimationButtons(self)
        
        self.mainwindow.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.mainwindow.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
        self.mainwindow.tableView_3.setEditTriggers(QTableView.NoEditTriggers)
        
        self.mainwindow.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainwindow.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainwindow.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
#& # # # # # # # # # # # # # # # VIEW TABLE # # # # # # # # # # # # # # # # 
    def table_1(self):
        self.query1 = QSqlQueryModel()
        self.query1.setQuery("SELECT * FROM citizen ORDER BY inn")
        self.mainwindow.tableView.setModel(self.query1)
        self.query1.setHeaderData(0, Qt.Horizontal, "ИНН гражданина")
        self.query1.setHeaderData(1, Qt.Horizontal, "ФИО")
        self.query1.setHeaderData(2, Qt.Horizontal, "Домашний адрес")
        
    def table_2(self):
        self.query2 = QSqlQueryModel()
        self.query2.setQuery("SELECT * FROM company ORDER BY inn")
        self.mainwindow.tableView_2.setModel(self.query2)
        self.query2.setHeaderData(0, Qt.Horizontal, "ИНН предприятия")
        self.query2.setHeaderData(1, Qt.Horizontal, "Название")
        self.query2.setHeaderData(2, Qt.Horizontal, "Адрес компании")
        
#* # # # # # # # # # # # # # # # ADD DATA # # # # # # # # # # # # # # # # 
    def table_add_1(self):
        if self.mainwindow.inn_line.text() and self.mainwindow.fio_line.text() and self.mainwindow.address_line.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO citizen(inn, fio, home_address) 
                    VALUES ('{self.mainwindow.inn_line.text()}', '{self.mainwindow.fio_line.text()}', '{self.mainwindow.address_line.text()}');""")
            if query.isActive() == True:
                self.table_1()
                self.mainwindow.inn_line.setText("")
                self.mainwindow.fio_line.setText("")
                self.mainwindow.address_line.setText("")
                self.mainwindow.add.setChecked(False)
                self.mainwindow.groupBox_create.hide()
                self.mainwindow.add.setFixedSize(111, 31)
                self.mainwindow.add.setText("Добавить")
                self.updateInvoice()
            else:
                message = QMessageBox()
                message.critical(self.widget, 'Ошибка!', 'Гражданин с данным инн\n уже есть в таблице!')
            last_inserted_id = query.lastInsertId()
            for row in range(self.query1.rowCount()):
                index = self.query1.index(row, 0)
                if index.data() == last_inserted_id:
                    self.mainwindow.tableView.selectRow(row)
                    break
            
    def table_add_2(self):
        if self.mainwindow.inn_company_line.text() and self.mainwindow.name_company.text() and self.mainwindow.address_company.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO company(inn, name, address) 
                    VALUES ('{self.mainwindow.inn_company_line.text()}', '{self.mainwindow.name_company.text()}', '{self.mainwindow.address_company.text()}');""")
            self.table_2()
            self.mainwindow.inn_company_line.setText("")
            self.mainwindow.name_company.setText("")
            self.mainwindow.address_company.setText("")
            self.mainwindow.add_2.setChecked(False)
            self.mainwindow.groupBox_create_2.hide()
            self.mainwindow.add_2.setFixedSize(111, 31)
            self.mainwindow.add_2.setText("Добавить")
            self.updateInvoice()
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(self.widget, 'Ошибка!', 'Компания с данным инн\n уже есть в таблице!')
            last_inserted_id = query.lastInsertId()
            for row in range(self.query2.rowCount()):
                index = self.query2.index(row, 0)
                if index.data() == last_inserted_id:
                    self.mainwindow.tableView_2.selectRow(row)
                    break
                
    def table_add_3(self):
        self.comb = self.mainwindow.combo_year.currentText()
        if self.mainwindow.year_tax.text() and self.mainwindow.year_quta.text() and self.mainwindow.tableView.selectedIndexes() and self.mainwindow.tableView_2.selectedIndexes():
            model_index = self.mainwindow.tableView.selectedIndexes()[0]
            id_invoice = self.mainwindow.tableView.model().data(model_index)
            model_index2 = self.mainwindow.tableView_2.selectedIndexes()[0]
            id_invoice2 = self.mainwindow.tableView_2.model().data(model_index2)
            query = QSqlQuery()
            query.exec(f"""INSERT INTO job(inn_citizen, inn_company, salary, tax, year) VALUES
                       ('{id_invoice}', '{id_invoice2}', '{self.mainwindow.year_quta.text()}', '{self.mainwindow.year_tax.text()}', '1.1.{self.comb_check()}');""")
            self.updateInvoice()
            self.mainwindow.year_tax.setText("")
            self.mainwindow.year_quta.setText("")
            self.mainwindow.add_3.setChecked(False)
            self.mainwindow.groupBox_create_3.hide()
        else:
            message = QMessageBox()
            message.critical(self.widget, 'Ошибка!', 'Введите коректные данные!')
            # self.mainwindow.year_tax.setText("")
            # self.mainwindow.year_quta.setText("")
            # self.mainwindow.address_company.setText("")
            # self.mainwindow.add_3.setChecked(False)
            # self.mainwindow.groupBox_create_3.hide()
            # self.mainwindow.add_3.setFixedSize(111, 31)
            # self.mainwindow.add_3.setText("Добавить")
            # last_inserted_id = query.lastInsertId()
            # for row in range(self.model.rowCount()):
            #     index = self.model.index(row, 0)
            #     if index.data() == last_inserted_id:
            #         self.mainwindow.tableView_3.selectRow(row)
            #         break
#! # # # # # # # # # # # # # # # DELETE DATA # # # # # # # # # # # # # # # # 
    def delete_data_1(self):
        if self.mainwindow.tableView.selectedIndexes():
            selected_indexes = self.mainwindow.tableView.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.mainwindow.tableView.model()
                self.data1 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.data1.append(model.data(index))
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.citizen WHERE inn = '{self.data1[0]}';")
            if query.isActive() == False:
                    QMessageBox.critical(self.widget, "Ошибка", "Вы не можете удалить\n эти данные!")
            self.table_1()
            self.updateInvoice()
        else:
             message = QMessageBox()
             message.critical(self.widget, "Ошибка", "Нечего удалять")
        
    def delete_data_2(self):
        if self.mainwindow.tableView_2.selectedIndexes():
            selected_indexes = self.mainwindow.tableView_2.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.mainwindow.tableView_2.model()
                self.data2 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.data2.append(model.data(index))
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.company WHERE inn = '{self.data2[0]}';")
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(self, "Ошибка", "Вы не можете удалить\n эти данные")
            self.table_2()
            self.updateInvoice()
        else:
            message = QMessageBox()
            message.critical(self.widget, "Ошибка", "Нечего удалять!")
        
    def delete_data_3(self):
        if self.mainwindow.tableView_3.selectedIndexes():
            selected_indexes = self.mainwindow.tableView_3.selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                model = self.mainwindow.tableView_3.model()
                self.data3 = []
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    self.data3.append(model.data(index))
            query = QSqlQuery()
            query.exec(f"DELETE FROM public.job WHERE id = '{self.data3[0]}';")
            print(query.lastError().text())
            if query.isActive() == False:
                message = QMessageBox()
                message.critical(self.widget, "Ошибка", "Вы не можете удалить\n эти данные!")
            self.updateInvoice()
        else:
            message = QMessageBox()
            message.critical(self.widget, "Ошибка", "Нечего удалять!")
        
    def cell_item_provider(self):
            if self.mainwindow.tableView.selectedIndexes() and self.mainwindow.tableView_2.selectedIndexes():
                model_index = self.mainwindow.tableView.selectedIndexes()[0]
                id_invoice = self.mainwindow.tableView.model().data(model_index)
                model_index2 = self.mainwindow.tableView_2.selectedIndexes()[0]
                id_invoice2 = self.mainwindow.tableView_2.model().data(model_index2)
                self.mainwindow.providerNumber = id_invoice
                self.mainwindow.providerNumber2 = id_invoice2
                self.updateInvoice()
        
    def updateInvoice(self):
        model = self.mainwindow.tableView.model()
        model2 = self.mainwindow.tableView_2.model()
        selected_row_index = self.mainwindow.tableView.currentIndex().row()
        selected_row_index2 = self.mainwindow.tableView_2.currentIndex().row()
        data = model.index(selected_row_index, 0).data()
        data2 = model2.index(selected_row_index2, 0).data()
        self.model = QSqlQueryModel()
        self.model.setQuery(f"SELECT id, inn_citizen, inn_company, salary, tax, EXTRACT(YEAR FROM year) AS employment_year FROM public.job WHERE inn_citizen = '{data}' AND inn_company = '{data2}';")
        self.mainwindow.tableView_3.setModel(self.model)
        self.mainwindow.tableView_3.hideColumn(0)
        self.model.setHeaderData(1, Qt.Horizontal, "ИНН гражданина")
        self.model.setHeaderData(2, Qt.Horizontal, "ИНН предприятия")
        self.model.setHeaderData(3, Qt.Horizontal, "Г. сумма зарплаты")
        self.model.setHeaderData(4, Qt.Horizontal, "Г. исчисленный налог")
        self.model.setHeaderData(5, Qt.Horizontal, "Год")
        
        
#TODO # # # # # # # # # # # # # # # ADD DATA # # # # # # # # # # # # # # # # 
    def change_table(self):
        if self.mainwindow.tableView.selectedIndexes():
            if self.mainwindow.inn_line_change.text() and self.mainwindow.fio_line_change.text() and self.mainwindow.address_line_change.text():
                selected_indexes = self.mainwindow.tableView.selectedIndexes()
                if selected_indexes:
                    row = selected_indexes[0].row()
                    model = self.mainwindow.tableView.model()
                    self.data1 = []
                    for column in range(model.columnCount()):
                        index = model.index(row, column)
                        self.data1.append(model.data(index))
                query = QSqlQuery()
                query.exec(f"UPDATE citizen SET inn = '{self.mainwindow.inn_line_change.text()}', fio = '{self.mainwindow.fio_line_change.text()}', home_address = '{self.mainwindow.address_line_change.text()}' WHERE inn = '{self.data1[0]}';")
                print(query.lastError().text())
                if query.isActive() == False:
                    message = QMessageBox()
                    message.critical(self.widget, "Ошибка", "Данные, на которые\n вы хотите изменить строку\n уже есть в таблице!")
                self.mainwindow.change.setChecked(False)
                self.mainwindow.groupBox_change.hide()
                self.table_1()
                self.updateInvoice()
            else:
                message = QMessageBox()
                message.critical(self.widget, "Ошибка", "Введите коректные данные!")
        else: 
            QMessageBox.critical(self.widget, "Ошибка", "Нечего изменять!")
            
    def change_table_2(self):
        if self.mainwindow.tableView_2.selectedIndexes():
            if self.mainwindow.inn_company_line_change.text() and self.mainwindow.name_company_change.text() and self.mainwindow.address_company_change.text():
                selected_indexes = self.mainwindow.tableView_2.selectedIndexes()
                if selected_indexes:
                    row = selected_indexes[0].row()
                    model = self.mainwindow.tableView_2.model()
                    self.data2 = []
                    for column in range(model.columnCount()):
                        index = model.index(row, column)
                        self.data2.append(model.data(index))
                query = QSqlQuery()
                query.exec(f"UPDATE company SET inn = '{self.mainwindow.inn_company_line_change.text()}', name = '{self.mainwindow.name_company_change.text()}', address = '{self.mainwindow.address_company_change.text()}' WHERE inn = '{self.data2[0]}';")
                if query.isActive() == False:
                    message = QMessageBox()
                    message.critical(self.widget, "Ошибка", "Данные, на которые\n вы хотите изменить строку\n уже есть в таблице!")
                self.mainwindow.change_2.setChecked(False)
                self.mainwindow.groupBox_change_2.hide()
                self.table_2()
                self.updateInvoice()
            else:
                message = QMessageBox()
                message.critical(self.widget, "Ошибка", "Введите коректные данные!")
        else: 
            QMessageBox.critical(self.widget, "Ошибка", "Нечего изменять!")
            
    def change_table_3(self):
        if self.mainwindow.tableView_3.selectedIndexes():
            if self.mainwindow.tableView_3.selectedIndexes():
                selected_indexes = self.mainwindow.tableView_3.selectedIndexes()
                if selected_indexes:
                    row = selected_indexes[0].row()
                    model = self.mainwindow.tableView_3.model()
                    self.data3 = []
                    for column in range(model.columnCount()):
                        index = model.index(row, column)
                        self.data3.append(model.data(index))
                query = QSqlQuery()
                query.exec(f"""UPDATE public.job SET 
                           salary = '{self.mainwindow.year_tax_change.text()}', tax = '{self.mainwindow.year_quta_change.text()}', year = '1.1.{self.mainwindow.combo_year_change.currentText()}' WHERE id = '{self.data3[0]}';""")
                print(query.lastError().text())
                if query.isActive() == False:
                    message = QMessageBox()
                    message.critical(self.widget, "Ошибка", "Данные, на которые\n вы хотите изменить строку\n уже есть в таблице!")
                self.updateInvoice()
                self.mainwindow.change_3.setChecked(False)
                self.mainwindow.groupBox_change_3.hide()
            else:
                message = QMessageBox()
                message.critical(self.widget, "Ошибка", "Введите коректные данные!")
        else: 
            QMessageBox.critical(self.widget, "Ошибка", "Нечего изменять!")
            
    def save_selection(self):
        self.selected_indexes = self.mainwindow.tableView.selectionModel().selectedIndexes()

    def restore_selection(self):
        for index in self.selected_indexes:
            self.tableView.selectionModel().select(index, QItemSelectionModel.Select)
    
    def comb_check(self):
        return self.mainwindow.combo_year.currentText()
        