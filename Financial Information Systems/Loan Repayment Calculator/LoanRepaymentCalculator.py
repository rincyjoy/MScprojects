from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtQml import * 
from PyQt5.QtQuick import *
import sys 
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 800)
        MainWindow.setStyleSheet("QWidget\n"

"{\n"
"    background-color: rgb(52, 52, 52);\n"
"    color: #000000;\n"
"}")
        validator = QRegExpValidator(QRegExp(r'[0-9]+'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(410, 280, 240, 40))
        self.SubmitButton.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 20px;    \n"
"    background-color: #ff3333;\n"
"    color: #fff;\n"
"    padding-top: 5px;\n"
"    border-left: 1px rgb(255, 75, 78);\n"
"    border-right: 1px rgb(255, 75, 78);\n"
"    border-bottom: 1px rgb(255, 75, 78);\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(255, 142, 144);\n"
"    border-left: 1px rgb(255, 75, 78);\n"
"    border-right: 1px rgb(255, 75, 78);\n"
"    border-bottom: 1px rgb(255, 75, 78);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(213, 0, 0);\n"
"    border-left: 1px rgb(255, 75, 78);\n"
"    border-right: 1px rgb(255, 75, 78);\n"
"    border-bottom: 1px rgb(255, 75, 78);\n"
"}")
        self.SubmitButton.setObjectName("SubmitButton")
        self.SubmitButton.clicked.connect(self.Calc)


        self.A = QtWidgets.QLabel(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(290, 80, 71, 20))
        self.A.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 13px;\n"
"\n"
"}")
        self.A.setObjectName("A")
        self.R = QtWidgets.QLabel(self.centralwidget)
        self.R.setGeometry(QtCore.QRect(310, 150, 71, 21))
        self.R.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 13px;\n"
"\n"
"}")
        self.R.setObjectName("R")
        self.N = QtWidgets.QLabel(self.centralwidget)
        self.N.setGeometry(QtCore.QRect(230, 220, 131, 21))
        self.N.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 13px;\n"
"\n"
"}")
        self.N.setObjectName("N")
        self.rate = QtWidgets.QLineEdit(self.centralwidget)
        self.rate.setGeometry(QtCore.QRect(410, 140, 240, 40))
        self.rate.setStyleSheet("QLineEdit {\n"
"    border-radius: 20px;\n"
"    color: #b1b1b1;\n"
"    background-color: #ffffff;\n"
"    border: 3px solid rgb(107, 107, 107);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 3px solid rgb(178, 127, 195);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid rgb(110, 171, 204)\n"
"}\n"
"")
        self.rate.setAlignment(QtCore.Qt.AlignCenter)
        self.rate.setObjectName("rate")

        self.months = QtWidgets.QLineEdit(self.centralwidget)
        self.months.setGeometry(QtCore.QRect(410, 210, 240, 40))
        self.months.setStyleSheet("QLineEdit {\n"
"    border-radius: 20px;\n"
"    color: #b1b1b1;\n"
"    background-color: #ffffff;\n"
"    border: 3px solid rgb(107, 107, 107);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 3px solid rgb(178, 127, 195);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid rgb(110, 171, 204)\n"
"}\n"
"")
        self.months.setAlignment(QtCore.Qt.AlignCenter)
        self.months.setObjectName("months")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(410, 70, 240, 40))
        self.amount.setStyleSheet("QLineEdit {\n"
"    border-radius: 20px;\n"
"    color: #b1b1b1;\n"
"    background-color: #ffffff;\n"
"    border: 3px solid rgb(107, 107, 107);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 3px solid rgb(178, 127, 195);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid rgb(110, 171, 204)\n"
"}\n"
"")
        self.amount.setAlignment(QtCore.Qt.AlignCenter)
        self.amount.setObjectName("amount")

        self.months.setValidator(validator)
        self.amount.setValidator(validator)
        self.rate.setValidator(validator)




        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 350, 750, 371))
        self.tableWidget.setStyleSheet("/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #252525;\n"
"    border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #fff;\n"
"    border-top: 0px;\n"
"    border-bottom: 1px solid gray;\n"
"    border-right: 1px solid gray;\n"
"    background-color: #343a49;\n"
"    margin-top:1px;\n"
"    margin-bottom:1px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #000;\n"
"    background-color: #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
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
        self.SubmitButton.setText(_translate("MainWindow", "Calculate"))
        self.A.setText(_translate("MainWindow", "Amount(A)"))
        self.R.setText(_translate("MainWindow", "Rate(R)"))
        self.N.setText(_translate("MainWindow", "Number of months(N)"))
        self.rate.setPlaceholderText(_translate("MainWindow", "Enter Rate"))
        self.months.setPlaceholderText(_translate("MainWindow", "Enter number of months"))
        self.amount.setPlaceholderText(_translate("MainWindow", "Enter Amount"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Payment Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PaymentAmount"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PrincipalAmount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "InterestAmount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OutstandingBalance"))



    def Calc(self):
        A = float(self.amount.text())
        R = float(self.rate.text())
        N = int(self.months.text())
        Rn = R/1200
        dlist=[]
        for n in range(1,N+1):
            d={}
            N = float(N)
            PaymentAmount = round((Rn*A)/(1-pow((1+Rn),-N)),2)
            PrincipalAmount = round(PaymentAmount*pow((1+Rn),-(1+N-n)),2)
            InterestAmount = round(PaymentAmount - PrincipalAmount,2)
            OutstandingBalance = round((InterestAmount/Rn)-PrincipalAmount,2)
            d['PaymentNumber'] = n
            d['PaymentAmount']= u"\xA3"+str(PaymentAmount)
            d['PrincipalAmount']=u"\xA3"+str(PrincipalAmount)
            d['InterestAmount']=u"\xA3"+str(InterestAmount)
            if OutstandingBalance<0 or (OutstandingBalance>0 and OutstandingBalance<1):
                d['OutstandingBalance']=u"\xA3"+str(0)
            else:
                d['OutstandingBalance']=u"\xA3"+str(OutstandingBalance)
            dlist.append(d)
        row = 0
        self.tableWidget.setRowCount(len(dlist))
        for item in dlist:
            self.tableWidget.setItem(row, 0,QtWidgets.QTableWidgetItem(str(item['PaymentNumber'])))
            self.tableWidget.setItem(row, 1,QtWidgets.QTableWidgetItem(str(item['PaymentAmount'])))
            self.tableWidget.setItem(row, 2,QtWidgets.QTableWidgetItem(str(item['PrincipalAmount'])))
            self.tableWidget.setItem(row, 3,QtWidgets.QTableWidgetItem(str(item['InterestAmount'])))
            self.tableWidget.setItem(row, 4,QtWidgets.QTableWidgetItem(str(item['OutstandingBalance'])))
            row = row + 1




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Loan Repayment Calculator')
    MainWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint)
    MainWindow.show()
    sys.exit(app.exec_())