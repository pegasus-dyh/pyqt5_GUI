
from PyQt5.QtWidgets import *



class sondoor(QDialog):
    def __init__(self,parent=None):
        super(door,self).__init__(parent)

        self.setWindowTitle("站台门")

        layout = QGridLayout(self)
#下面这段代码通过两种方式将信号与槽相连
        self.button1=QPushButton('1号传感器')
        self.button1.setText('1号传感器')
        self.button1.clicked.connect(lambda : self.whichbutton(self.button1))
        self.lineedit1=QLineEdit("优秀")


#在文本前面显示图像

        self.button2=QPushButton('2号传感器')
        self.button2.setText('2号传感器')
        self.button2.clicked.connect(lambda : self.whichbutton(self.button2))
        self.lineedit2 = QLineEdit("良好")


        self.button3=QPushButton('3号传感器')
        self.button3.setText('3号传感器')
        self.button3.clicked.connect(lambda : self.whichbutton(self.button3))
        self.lineedit3 = QLineEdit("差")


        self.button4=QPushButton('4号站传感器')
        self.button4.setText('4号传感器')

        self.button4.clicked.connect(lambda : self.whichbutton(self.button4))
        self.lineedit4 = QLineEdit("中")

        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.lineedit1,1,1)

        layout.addWidget(self.button2,2,0)
        layout.addWidget(self.lineedit2,2,1)

        layout.addWidget(self.button3,3,0)
        layout.addWidget(self.lineedit3,3,1)

        layout.addWidget(self.button4,4,0)
        layout.addWidget(self.lineedit4,4,1)



        self.setLayout(layout)

    def whichbutton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")
