#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from design.DesignWindow import Ui_MainWindow
from design.Animation import AnimationButtons
from bin.db import Database
from bin.tables import Tables
import sys

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.providerNumber = 1
        
        self.database = Database(self)
        self.close_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)

        self.horizontalHeader = self.tableView.horizontalHeader()
        self.horizontalHeader.sectionEntered.connect(self.entered_table_1)
        
        self.amain = AnimationButtons(self)
        self.tables = Tables(self)
        
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
        
        self.ok.clicked.connect(lambda: self.tables.table_add_1(self))
        self.ok_2.clicked.connect(lambda: self.tables.table_add_2(self))
        
    def cell_item_provider(self):
        model_index = self.tableView.selectedIndexes()[0]
        id_invoice = self.tableView.model().data(model_index)
        self.providerNumber = id_invoice
        self.updateInvoice()
        
    def updateInvoice(self):
        model = self.tableView.model()
        selected_row_index = self.tableView.currentIndex().row()
        data = model.index(selected_row_index, 0).data()
        self.model = QSqlQueryModel()
        self.model.setQuery(f"SELECT inn_citizen, inn_company,  FROM public.invoice WHERE id_provider = '{data}' ORDER BY id")
        self.tableView_2.setModel(self.model)
        
        


        
if __name__ == "__main__":   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()