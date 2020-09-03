# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(267, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 81, 61, 51))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(70, 81, 61, 51))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(130, 81, 61, 51))
        self.btn_3.setObjectName("btn_3")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(190, 81, 61, 51))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(70, 51, 121, 31))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(130, 131, 61, 51))
        self.btn_6.setObjectName("btn_6")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(70, 131, 61, 51))
        self.btn_5.setObjectName("btn_5")
        self.btn_mines = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mines.setGeometry(QtCore.QRect(190, 131, 61, 51))
        self.btn_mines.setObjectName("btn_mines")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 131, 61, 51))
        self.btn_4.setObjectName("btn_4")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(130, 181, 61, 51))
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(70, 181, 61, 51))
        self.btn_8.setObjectName("btn_8")
        self.btn_multi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multi.setGeometry(QtCore.QRect(190, 181, 61, 51))
        self.btn_multi.setObjectName("btn_multi")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 181, 61, 51))
        self.btn_7.setObjectName("btn_7")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(130, 231, 61, 51))
        self.btn_dot.setObjectName("btn_dot")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 51, 61, 31))
        self.btn_back.setObjectName("btn_back")
        self.btn_devetion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_devetion.setGeometry(QtCore.QRect(190, 231, 61, 51))
        self.btn_devetion.setObjectName("btn_devetion")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(10, 231, 121, 51))
        self.btn_0.setObjectName("btn_0")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 41))
        self.lineEdit.setStyleSheet("font-size:20px;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.btn_quals = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quals.setGeometry(QtCore.QRect(190, 50, 61, 31))
        self.btn_quals.setObjectName("btn_quals")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 267, 21))
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
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_clear.setText(_translate("MainWindow", "clear"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_mines.setText(_translate("MainWindow", "-"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_multi.setText(_translate("MainWindow", "*"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_back.setText(_translate("MainWindow", "<"))
        self.btn_devetion.setText(_translate("MainWindow", "/"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_quals.setText(_translate("MainWindow", "="))
        #my code function
        self.btn_0.clicked.connect(lambda:self.add_number("0"))
        self.btn_1.clicked.connect(lambda:self.add_number("1"))
        self.btn_2.clicked.connect(lambda:self.add_number("2"))
        self.btn_3.clicked.connect(lambda:self.add_number("3"))
        self.btn_4.clicked.connect(lambda:self.add_number("4"))
        self.btn_5.clicked.connect(lambda:self.add_number("5"))
        self.btn_6.clicked.connect(lambda:self.add_number("6"))
        self.btn_7.clicked.connect(lambda:self.add_number("7"))
        self.btn_8.clicked.connect(lambda:self.add_number("8"))
        self.btn_9.clicked.connect(lambda:self.add_number("9"))
        self.btn_mines.clicked.connect(lambda:self.add_number("-"))
        self.btn_plus.clicked.connect(lambda:self.add_number("+"))
        self.btn_multi.clicked.connect(lambda:self.add_number("*"))
        self.btn_devetion.clicked.connect(lambda:self.add_number("/"))
        self.btn_quals.clicked.connect(self.calculate_numbers)
        self.btn_clear.clicked.connect(self.clear_numbers)
        self.btn_back.clicked.connect(self.back_number)
    #my code
    def add_number(self,number):
        txt_on_line=self.lineEdit.text()
        self.lineEdit.setText(txt_on_line+number)
    def calculate_numbers(self):
        try:
            txt_on_line=self.lineEdit.text()
            self.lineEdit.setText(str(eval(txt_on_line)))
        except:
            self.lineEdit.setText("error")
    def clear_numbers(self):
        self.lineEdit.setText("")
    
    def back_number(self):
        txt_on_line=self.lineEdit.text()
        self.lineEdit.setText(txt_on_line[:-1])







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
