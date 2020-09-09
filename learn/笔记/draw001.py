import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class draw001(QWidget):
    def __init__(self):
        super(draw001, self).__init__()
        self.resize(300,500)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        #绘制图像
        image=QImage('G:\\pyqt5_GUI\\controls\\images\\screen.png')
        rect1=QRect(10,600,image.width()/4,image.height()/4)
        painter.drawImage(rect1,image)


        painter.end()
