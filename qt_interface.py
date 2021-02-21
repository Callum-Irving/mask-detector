import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from ui_test import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.pushButton.clicked.connect(self.goDashboard)

    def show(self):
        self.main_win.show()

    def goDashboard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
