# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 410)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(10, 10, 167, 241))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__box_1)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(180, 10, 401, 241))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(180, 260, 321, 101))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.s3__send_button = QtWidgets.QPushButton(self.verticalGroupBox_2)
        self.s3__send_button.setObjectName("s3__send_button")
        self.verticalLayout_2.addWidget(self.s3__send_button)
        self.s3__clear_button = QtWidgets.QPushButton(Form)
        self.s3__clear_button.setGeometry(QtCore.QRect(510, 270, 71, 81))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(10, 250, 91, 71))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.hex_receive = QtWidgets.QCheckBox(self.formGroupBox1)
        self.hex_receive.setObjectName("hex_receive")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hex_receive)
        self.hex_send = QtWidgets.QCheckBox(self.formGroupBox1)
        self.hex_send.setObjectName("hex_send")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hex_send)
        self.state_label = QtWidgets.QLabel(Form)
        self.state_label.setGeometry(QtCore.QRect(20, 430, 145, 14))
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 161, 81))
        self.groupBox.setObjectName("groupBox")
        self.timer_send_cb = QtWidgets.QCheckBox(self.groupBox)
        self.timer_send_cb.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.dw = QtWidgets.QLabel(self.groupBox)
        self.dw.setGeometry(QtCore.QRect(80, 50, 54, 20))
        self.dw.setObjectName("dw")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.s2__clear_button = QtWidgets.QPushButton(Form)
        self.s2__clear_button.setGeometry(QtCore.QRect(110, 260, 61, 61))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 360, 411, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 370, 91, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 370, 48, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 370, 91, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 370, 48, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(500, 370, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_3.setObjectName("label_3")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.s3__clear_button.raise_()
        self.formGroupBox.raise_()
        self.state_label.raise_()
        self.groupBox.raise_()
        self.s2__clear_button.raise_()
        self.plainTextEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.s1__lb_6.setText(_translate("Form", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.open_button.setText(_translate("Form", "打开串口"))
        self.close_button.setText(_translate("Form", "关闭串口"))
        self.verticalGroupBox.setTitle(_translate("Form", "接受区"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.s3__send_button.setText(_translate("Form", "发送"))
        self.s3__clear_button.setText(_translate("Form", "清除发送"))
        self.formGroupBox1.setTitle(_translate("Form", "接收设置"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.hex_send.setText(_translate("Form", "Hex发送"))
        self.groupBox.setTitle(_translate("Form", "发送设置"))
        self.timer_send_cb.setText(_translate("Form", "定时发送"))
        self.dw.setText(_translate("Form", "ms/次"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.s2__clear_button.setText(_translate("Form", "清空接收"))
        self.label_2.setText(_translate("Form", "TX："))
        self.label.setText(_translate("Form", "RX："))
        self.label_3.setText(_translate("Form", "@later V1.0"))