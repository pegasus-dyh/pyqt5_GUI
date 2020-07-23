'''

按钮控件(QPushButton)

父类： QAbstractButton

子类：QPushButton:常规按钮
     AToolButton:工具条按钮
     QradioButton:单选按钮
     QCheckBox:多选按钮

本例种基于QPushButton主要学习：1两类信号与槽的绑定方式
                           2在按钮中加入图片
'''

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        self.resize(300,200)

        layout=QVBoxLayout()

#下面这段代码通过两种方式将信号与槽相连
        self.button1=QPushButton('第一个按钮')
        self.button1.setText('first button')
        self.button1.setCheckable(True) #此行与下面一行实现按钮不自动抬起，按下后保持按下状态再次按下恢复原态。
        self.button1.toggle()
        self.button1.clicked.connect(lambda : self.whichbutton(self.button1))
        self.button1.clicked.connect(self.buttonstate)

#在文本前面显示图像

        self.button2=QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))
        self.button2.clicked.connect(lambda : self.whichbutton(self.button2))

        self.button3=QPushButton('不可用按钮')
        self.button3.setEnabled(False)

        self.button4=QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda : self.whichbutton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)



    def whichbutton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")

    def buttonstate(self):
        if self.button1.isChecked():
                print("按钮1已被选中")










if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())

