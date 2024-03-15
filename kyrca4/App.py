#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from design.Animation import AnimationButtons
from design.DesignWindow import Ui_MainWindow
from bin.tables import Tables
from bin.Report import ReportWindow
import datetime, sys

class MainWindow(Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        
        if username == "Петров":
            self.groupBox_2.hide()
            self.groupBox_3.hide()
            self.groupBox.setFixedSize(131, 161)
        elif username == "Сидоров":
            self.groupBox_2.hide()
            self.groupBox_3.hide()
            self.groupBox.hide()
        elif username == "Иванов":
            pass
        
        self.providerNumber = 1
        self.providerNumber2 = 1
        
        current_year = datetime.datetime.now().year
        years_list = [str(year) for year in range(2000, current_year + 1)]
            
        self.combo_year.addItems(years_list)
        self.combo_year_change.addItems(years_list)
        
        self.combo_year.setCurrentText(str(current_year))
        self.combo_year_change.setCurrentText(str(current_year))
        
        self.combo_year.setMaxVisibleItems(1)
        self.combo_year_change.setMaxVisibleItems(1)
        
        self.tableView.clicked.connect(self.on_selection_changed_cl)
        self.tableView_2.clicked.connect(self.on_selection_changed_cl_2)
        self.tableView_3.clicked.connect(self.on_selection_changed_cl_3)
        
        self.inn_company_line.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.inn_company_line_change.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.inn_line.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.inn_line_change.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.sell_tax.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.sell_tax_change.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.year_tax.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.year_tax_change.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.year_quta.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.year_quta_change.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_3.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self.close_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)
        
        self.amain = AnimationButtons(self)
        self.tables = Tables(self)
        
        self.tableView.clicked.connect(lambda: self.tables.cell_item_provider())
        self.tableView_2.clicked.connect(lambda: self.tables.cell_item_provider())
        
        self.groupBox_create.hide()
        self.groupBox_create_2.hide()
        self.groupBox_create_3.hide()
        
        self.groupBox_change.hide()
        self.groupBox_change_2.hide()
        self.groupBox_change_3.hide()
        
        self.add.setCheckable(True)
        self.add_2.setCheckable(True)
        self.add_3.setCheckable(True)
        
        self.change.setCheckable(True)
        self.change_2.setCheckable(True)
        self.change_3.setCheckable(True)
        self.amain.animation_add()
        
        self.add.clicked.connect(self.amain.animation_add)
        self.add_2.clicked.connect(self.amain.animation_add_2)
        self.add_3.clicked.connect(self.amain.animation_add_3)
        
        self.change.clicked.connect(self.amain.animation_change)
        self.change_2.clicked.connect(self.amain.animation_change_2)
        self.change_3.clicked.connect(self.amain.animation_change_3)
        
        self.ok.clicked.connect(lambda: self.tables.table_add_1())
        self.ok_2.clicked.connect(lambda: self.tables.table_add_2())
        self.ok_3.clicked.connect(lambda: self.tables.table_add_3())
        
        self.delete_btn.clicked.connect(self.tables.delete_data_1)
        self.delete_btn_2.clicked.connect(self.tables.delete_data_2)
        self.delete_btn_3.clicked.connect(self.tables.delete_data_3)
        
        self.ok_change.clicked.connect(self.tables.change_table)
        self.ok_change_2.clicked.connect(self.tables.change_table_2)
        self.ok_change_3.clicked.connect(self.tables.change_table_3)
        
        self.cancel.clicked.connect(self.cancel_table)
        self.cancel_2.clicked.connect(self.cancel_table_2)
        self.cancel_3.clicked.connect(self.cancel_table_3)
        
        self.cancel_change.clicked.connect(self.cancel_table_change)
        self.cancel_change_2.clicked.connect(self.cancel_table_change_2)
        self.cancel_change_3.clicked.connect(self.cancel_table_change_3)
        
        self.report.clicked.connect(self.report_cl)
        
        self.tableView.selectRow(0)
        self.tableView_2.selectRow(0)
        self.tables.updateInvoice()
        
        self.on_selection_changed()
        self.on_selection_changed_2()
        self.on_selection_changed_3()
        
    def report_cl(self):
        self.report_window = ReportWindow()
        self.report_window.show()
        
    def cancel_table(self):
        self.groupBox_create.hide()
        self.add.setChecked(False)
    
    def cancel_table_2(self):
        self.groupBox_create_2.hide()
        self.add_2.setChecked(False)
        
    def cancel_table_3(self):
        self.groupBox_create_3.hide()
        self.add_3.setChecked(False)
        
    def cancel_table_change(self):
        self.groupBox_change.hide()
        self.change.setChecked(False)
        
    def cancel_table_change_2(self):
        self.groupBox_change_2.hide()
        self.change_2.setChecked(False)
        
    def cancel_table_change_3(self):
        self.groupBox_change_3.hide()
        self.change_3.setChecked(False)
        
    def on_selection_changed_cl(self):
        self.on_selection_changed()
        self.tableView.selectionModel().selectionChanged.connect(self.on_selection_changed)
        
    def on_selection_changed_cl_2(self):
        self.on_selection_changed_2()
        self.tableView_2.selectionModel().selectionChanged.connect(self.on_selection_changed_2)
        
    def on_selection_changed_cl_3(self):
        self.on_selection_changed_3()
        self.tableView_3.selectionModel().selectionChanged.connect(self.on_selection_changed_3)
    
    def on_selection_changed(self):
        selected_indexes = self.tableView.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.inn_line_change.setText(str(data[0]))
            self.fio_line_change.setText(str(data[1]))
            self.address_line_change.setText(str(data[2]))
            
    def on_selection_changed_2(self):
        selected_indexes = self.tableView_2.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_2.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.inn_company_line_change.setText(str(data[0]))
            self.name_company_change.setText(str(data[1]))
            self.address_company_change.setText(str(data[2]))
        
    def on_selection_changed_3(self):
        selected_indexes = self.tableView_3.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            model = self.tableView_3.model()
            data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data.append(model.data(index))
            self.year_tax_change.setText(str(data[4]).split('.')[0])
            self.year_quta_change.setText(str(data[3]).split('.')[0])
            self.combo_year_change.setCurrentText(str(data[5]).split('.')[0])
            self.sell_tax_change.setText(str(data[6]).split('.')[0])
            
def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()
        
main()
        