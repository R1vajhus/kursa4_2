from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from design.LoginWindow import Ui_MainWindow
from bin.db import Database
from bin.App import MainWindow
import sys

class LoginWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.auth.clicked.connect(self.login_window)
        self.db = Database(self)
        
    def login_window(self):
        username = self.login.text()
        password = self.password.text()
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'")
        query.bindValue(":username", username)
        query.bindValue(":password", password)
        if not query.exec():
            print("Query Error:", query.lastError().text())
            return False
        if query.next():
            self.main = MainWindow()
            self.main.show()
            self.close()
        
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

          
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()
