# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Door01.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(642, 392)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 100, 101, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 100, 177, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.pushButton1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.horizontalLayout.addWidget(self.pushButton1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(270, 130, 177, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout_2.addWidget(self.lineEdit2)
        self.pushButton2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton2.setObjectName("pushButton2")
        self.horizontalLayout_2.addWidget(self.pushButton2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(270, 160, 177, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit3.setObjectName("lineEdit3")
        self.horizontalLayout_3.addWidget(self.lineEdit3)
        self.pushButton3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton3.setObjectName("pushButton3")
        self.horizontalLayout_3.addWidget(self.pushButton3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(270, 190, 177, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit4.setObjectName("lineEdit4")
        self.horizontalLayout_4.addWidget(self.lineEdit4)
        self.pushButton4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton4.setObjectName("pushButton4")
        self.horizontalLayout_4.addWidget(self.pushButton4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.pushButton1.clicked['bool'].connect(self.lineEdit1.clear)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "站台门监控系统"))
        self.label.setText(_translate("mainWindow", "1号站台  状态"))
        self.label_2.setText(_translate("mainWindow", "2号站台  状态"))
        self.label_3.setText(_translate("mainWindow", "3号站台  状态"))
        self.label_4.setText(_translate("mainWindow", "4号站台  状态"))
        self.pushButton1.setText(_translate("mainWindow", "进入1号监控界面"))
        self.pushButton2.setText(_translate("mainWindow", "进入2号监控界面"))
        self.pushButton3.setText(_translate("mainWindow", "进入3号监控界面"))
        self.pushButton4.setText(_translate("mainWindow", "进入4号监控界面"))
