'''
颜色对话框(QColorDialog)
'''
import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QColorDialog颜色对话框')

        layout=QVBoxLayout()
        self.button1=QPushButton('设置颜色')
        self.button1.clicked.connect(self.getcolor)
        layout.addWidget(self.button1)

        self.button2=QPushButton('设置背景颜色')
        self.button2.clicked.connect(self.getBGcolor)
        layout.addWidget(self.button2)

        self.colorLabel=QLabel('Hellow,测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)
    def getcolor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)

    def getBGcolor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())

