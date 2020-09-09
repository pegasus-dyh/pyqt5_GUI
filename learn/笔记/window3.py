from PyQt5.QtWidgets import *
import sys
from door import door
from PyQt5.QtGui import *


class window3(QDialog):
    def __init__(self):
        super(window3, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('站台门检测系统')
        self.resize(300,200)

        layout = QVBoxLayout(self)
        # 下面这段代码通过两种方式将信号与槽相连
        self.button1 = QPushButton('数据1')
        self.button1.setText('数据1')
        self.button1.clicked.connect(lambda: self.whichbutton(self.button1))

        # 在文本前面显示图像

        self.button2 = QPushButton('数据2')
        self.button2.setText('数据2')
        self.button2.clicked.connect(lambda: self.whichbutton(self.button2))



        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)




    def whichbutton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")