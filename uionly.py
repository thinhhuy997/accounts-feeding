# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tds2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 741, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addAccountButton = QtWidgets.QPushButton(self.frame)
        self.addAccountButton.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addAccountButton.setFont(font)
        self.addAccountButton.setObjectName("addAccountButton")
        self.addProxyButton = QtWidgets.QPushButton(self.frame)
        self.addProxyButton.setGeometry(QtCore.QRect(130, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addProxyButton.setFont(font)
        self.addProxyButton.setObjectName("addProxyButton")


        self.saveProfiles = QtWidgets.QPushButton(self.frame)
        self.saveProfiles.setGeometry(QtCore.QRect(240, 20, 101, 31))
        self.saveProfiles.setObjectName("saveProfiles")
        self.importConfig = QtWidgets.QPushButton(self.frame)
        self.importConfig.setGeometry(QtCore.QRect(350, 20, 101, 31))
        self.importConfig.setObjectName("importConfig")
        self.feedAccounts = QtWidgets.QPushButton(self.frame)
        self.feedAccounts.setGeometry(QtCore.QRect(460, 20, 101, 31))
        self.feedAccounts.setObjectName("feedAccounts")
        self.configDays = QtWidgets.QComboBox(self.frame)
        self.configDays.setGeometry(QtCore.QRect(570, 25, 51, 21))
        self.configDays.setObjectName("configDays")
        self.configDays.addItem("")
        self.configDays.addItem("")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 1001, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 741, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
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
        self.addAccountButton.setText(_translate("MainWindow", "Add accounts"))
        self.addProxyButton.setText(_translate("MainWindow", "Add Proxies"))

        self.saveProfiles.setText(_translate("MainWindow", "Save Profiles"))
        self.importConfig.setText(_translate("MainWindow", "Import config"))
        self.feedAccounts.setText(_translate("MainWindow", "Feed accounts"))
        self.configDays.setItemText(0, _translate("MainWindow", "Day 1"))
        self.configDays.setItemText(1, _translate("MainWindow", "Day 2"))
        
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "tds_username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tds_pass"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "face_uid"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "face_pass"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "cookie"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "token"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "proxy"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "user_agent"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "status"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "action"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "tds-user1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "tds-pass1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "61552711387154"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "buichieu2im"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "cookie-str-1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "tds-user2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "tds-pass2"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "61552997995019"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "hoangbinh0dj"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "cookie-str-2"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "File:"))
