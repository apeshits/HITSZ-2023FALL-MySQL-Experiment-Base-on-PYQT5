# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numberSelectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumberSelectWindow(object):
    def setupUi(self, NumberSelectWindow):
        NumberSelectWindow.setObjectName("NumberSelectWindow")
        NumberSelectWindow.resize(1088, 778)
        self.centralwidget = QtWidgets.QWidget(NumberSelectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 170, 371, 241))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.numberSelectSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numberSelectSpinBox.setGeometry(QtCore.QRect(240, 60, 100, 50))
        self.numberSelectSpinBox.setMinimumSize(QtCore.QSize(100, 50))
        self.numberSelectSpinBox.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numberSelectSpinBox.setFont(font)
        self.numberSelectSpinBox.setMaximum(10)
        self.numberSelectSpinBox.setObjectName("numberSelectSpinBox")
        self.numberSelectConfirmButton = QtWidgets.QPushButton(self.widget)
        self.numberSelectConfirmButton.setGeometry(QtCore.QRect(50, 180, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numberSelectConfirmButton.setFont(font)
        self.numberSelectConfirmButton.setObjectName("numberSelectConfirmButton")
        self.numberSelectCancelButton = QtWidgets.QPushButton(self.widget)
        self.numberSelectCancelButton.setGeometry(QtCore.QRect(220, 180, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numberSelectCancelButton.setFont(font)
        self.numberSelectCancelButton.setObjectName("numberSelectCancelButton")
        NumberSelectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NumberSelectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 30))
        self.menubar.setObjectName("menubar")
        NumberSelectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NumberSelectWindow)
        self.statusbar.setObjectName("statusbar")
        NumberSelectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NumberSelectWindow)
        QtCore.QMetaObject.connectSlotsByName(NumberSelectWindow)

    def retranslateUi(self, NumberSelectWindow):
        _translate = QtCore.QCoreApplication.translate
        NumberSelectWindow.setWindowTitle(_translate("NumberSelectWindow", "MainWindow"))
        self.label.setText(_translate("NumberSelectWindow", "请选择菜品数量"))
        self.numberSelectConfirmButton.setText(_translate("NumberSelectWindow", "确认"))
        self.numberSelectCancelButton.setText(_translate("NumberSelectWindow", "取消"))
