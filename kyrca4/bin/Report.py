from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from design.ReportWindow import Ui_MainWindow
from PyQt5.QtPrintSupport import QPrintDialog
import sys, datetime

class ReportWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.exit.clicked.connect(self.close)
        
        current_year = datetime.datetime.now().year
        years_list = [str(year) for year in range(2000, current_year + 1)]
            
        self.start_date.addItems(years_list)
        self.end_date.addItems(years_list)
        
        self.start_date.setCurrentText(str(current_year))
        self.end_date.setCurrentText(str(current_year))
        
        self.view_table.clicked.connect(self.table)
        
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.start_printer.clicked.connect(self.print_btn_cl)
        
        
    def table(self):
        query = QSqlQueryModel()
        query.setQuery(f"SELECT salary, tax, EXTRACT(YEAR FROM year) AS employment_year, (tax - 0.12*salary) AS total_salary FROM job WHERE year BETWEEN '01.01.{self.start_date.currentText()}' AND '01.01.{self.end_date.currentText()}';")
        self.tableView.setModel(query)
        query.setHeaderData(0, Qt.Horizontal, "Сумма зарплаты")
        query.setHeaderData(1, Qt.Horizontal, "Исчисляемые налоги")
        query.setHeaderData(2, Qt.Horizontal, "Год")
        query.setHeaderData(3, Qt.Horizontal, "Оплаченные налоги")
        
    def mousePressEvent(self, event):
        self.offset = event.pos()
        self.window_position = self.pos()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton and self.offset is not None:
                new_position = event.globalPos() - self.offset
                self.move(new_position)
        except:
            pass

    def mouseReleaseEvent(self, event):
        self.offset = None
        self.window_position = None
        
    def print_btn_cl(self):
        if len(self.start_date.currentText()) > 0 and len(self.end_date.currentText()) > 0:
            self.dialog = QPrintDialog(self.tableView)
            if self.dialog.exec_() == 1:
                textDoc = QTextDocument()
                html = self.build_document()
                textDoc.setHtml(html)
                printer = self.dialog.printer()
                textDoc.print(printer)
            
    def build_document(self):
        html = f"""<h1 style='text-align: center;'>Отчет</h1>
              <h3 style='text-align: center; margin-bottom: 100px'>Оплаченные налоги за период с {self.start_date.currentText()} по {self.end_date.currentText()}</h3>
              <table style='text-align: center; margin: auto; border-collapse: collapse;'>
              <thead>
              <tr>
                  <th style='border: 1px solid black; width: 100px;'>Сумма зарплаты</th>
                  <th style='border: 1px solid black; width: 100px;'>Исчисляемые налоги</th>
                  <th style='border: 1px solid black; width: 100px;'>Год</th>
                  <th style='border: 1px solid black; width: 100px;'>Оплаченные налоги</th>
              </tr>
              </thead>
              <tbody>"""

        model = self.tableView.model()
        row_count = model.rowCount()
        column_count = model.columnCount()

        for row in range(row_count):
            html += "<tr>"
            for column in range(column_count):
                index = model.index(row, column)
                data = model.data(index)
                if isinstance(data, QDate):
                    data = data.toString("yyyy")
                html += f"<td style='border: 1px solid black; width: 100px;'>{int(data)}</td>"
            html += "</tr>"

        html += "</tbody></table>"

        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertHtml(html)
        return document.toHtml()
    
def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = ReportWindow()
        window.show()
        app.exec_()
main()