# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 120, 941, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.loginIDInputLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginIDInputLine.setMinimumSize(QtCore.QSize(0, 40))
        self.loginIDInputLine.setMaximumSize(QtCore.QSize(16777215, 40))
        self.loginIDInputLine.setText("")
        self.loginIDInputLine.setObjectName("loginIDInputLine")
        self.horizontalLayout_2.addWidget(self.loginIDInputLine)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.loginPasswordInputLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginPasswordInputLine.setMinimumSize(QtCore.QSize(0, 40))
        self.loginPasswordInputLine.setMaximumSize(QtCore.QSize(16777215, 40))
        self.loginPasswordInputLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPasswordInputLine.setObjectName("loginPasswordInputLine")
        self.horizontalLayout_3.addWidget(self.loginPasswordInputLine)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.loginLevelSelectComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.loginLevelSelectComboBox.setMinimumSize(QtCore.QSize(150, 40))
        self.loginLevelSelectComboBox.setMaximumSize(QtCore.QSize(150, 40))
        self.loginLevelSelectComboBox.setObjectName("loginLevelSelectComboBox")
        self.loginLevelSelectComboBox.addItem("")
        self.loginLevelSelectComboBox.addItem("")
        self.loginLevelSelectComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.loginLevelSelectComboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.loginConfirmButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginConfirmButton.setMinimumSize(QtCore.QSize(200, 50))
        self.loginConfirmButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginConfirmButton.setFont(font)
        self.loginConfirmButton.setObjectName("loginConfirmButton")
        self.horizontalLayout_5.addWidget(self.loginConfirmButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 30, 150, 93))
        self.label.setMinimumSize(QtCore.QSize(150, 61))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menubar.setObjectName("menubar")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.label_2.setText(_translate("loginWindow", "账号🙉"))
        self.label_3.setText(_translate("loginWindow", "密码🙈"))
        self.label_4.setText(_translate("loginWindow", "登录身份"))
        self.loginLevelSelectComboBox.setItemText(0, _translate("loginWindow", "普通用户🥳"))
        self.loginLevelSelectComboBox.setItemText(1, _translate("loginWindow", "商家🥸"))
        self.loginLevelSelectComboBox.setItemText(2, _translate("loginWindow", "食堂管理员🤠"))
        self.loginConfirmButton.setText(_translate("loginWindow", "登录"))
        self.label.setText(_translate("loginWindow", "登录"))
