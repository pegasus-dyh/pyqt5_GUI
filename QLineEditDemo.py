'''
QLineEdit 综合案例
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QLineEdit综合应用")

        edit1=QLineEdit()
        #设置int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4) #不超过9999
        edit1.setAlignment(Qt.AlignRight) #输入文本的对齐方式
        edit1.setFont(QFont('Arial',20)) #字体字号

        edit2=QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;_')

        edit4=QLineEdit()
        edit4.textChanged.connect(self.textchange)

        edit5=QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterpress)

        edit6=QLineEdit("hellow PYQT5")
        edit6.setReadOnly(True)


        formlayout=QFormLayout()
        formlayout.addRow('整数校验',edit1)
        formlayout.addRow('浮点数校验',edit2)
        formlayout.addRow('掩码Input mask',edit3)
        formlayout.addRow('文本变化',edit4)
        formlayout.addRow('密码',edit5)
        formlayout.addRow('只读',edit6)

        self.setLayout(formlayout)

    def textchange(self,text):
        print('输入的内容'+text)
    def enterpress(self):
        print('已输入值')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditDemo()
    main.show()
    sys.exit(app.exec_())









