from PyQt5 import QtCore, QtGui, QtWidgets

from webcam_widget import Webcam


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(944, 688)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(216, 195, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setStyleSheet("*{background colour: rgb(17, 100, 102)}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)

        # Webcam widget
        self.vidcap = Webcam()
        self.vidcap.setObjectName("webcam_stream")
        self.verticalLayout_4.addWidget(self.vidcap)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_7.setStyleSheet("background-color: rgb(233, 128, 116);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionshortcut_is = QtWidgets.QAction(MainWindow)
        self.actionshortcut_is.setObjectName("actionshortcut_is")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Mask Detector System</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Go to dashboard"))
        self.pushButton_5.setText(_translate("MainWindow", "Go Back"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Admin Dashboard</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "View Live Stream"))
        self.pushButton_3.setText(_translate("MainWindow", "View Screenshots"))
        self.pushButton_6.setText(_translate("MainWindow", "Go Back"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Current Video Streams</p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "Go Back"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Images of detected people without masks</p></body></html>"))
        self.actionshortcut_is.setText(
            _translate("MainWindow", "shortcut is:"))
        self.actionshortcut_is.setShortcut(_translate("MainWindow", "Ctrl+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
