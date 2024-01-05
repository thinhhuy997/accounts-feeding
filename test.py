import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QListView, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 190, 171, 131))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: white;")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.showWidgetButton = QtWidgets.QPushButton(self.centralwidget)
        self.showWidgetButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.showWidgetButton.setObjectName("showWidgetButton")

        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Test"))
        self.radioButton.setText(_translate("MainWindow", "Test2"))

        self.showWidgetButton.setText(_translate("MainWindow", "Show"))

        self.showWidgetButton.clicked.connect(self.toggle_list_view)

    def toggle_list_view(self):
        if self.widget.isHidden():
            self.widget.show()
        else:
            self.widget.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())