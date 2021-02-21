import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from qt_interface_styled import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.pushButton.clicked.connect(self.goDashboard)
        self.ui.pushButton_5.clicked.connect(self.goHome)
        self.ui.pushButton_4.clicked.connect(self.goVideo)
        self.ui.pushButton_6.clicked.connect(self.goDashboard)

    def show(self):
        self.main_win.show()

    def goDashboard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def goHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def goVideo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
