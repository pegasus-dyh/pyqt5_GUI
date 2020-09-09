'''
用像素点绘制正弦曲线

drawPoint(x,y)
'''
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
class DrawPointDemo(QWidget):
    def __init__(self):
        super(DrawPointDemo, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('在窗口上用像素点绘制正弦曲线')

    def paintEvent(self, QPaintEvent):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size=self.size()
        for i in range(1000):
            x=100*(-1+2.0*i/1000)++size.width()/2.0 #此处的size相当于将函数向右平移，让界面中心位于图形中心
            y=-50*math.sin((x-+size.width()/2.0)*math.pi/50)+size.height()/2.0
            painter.drawPoint(x,y)
        painter.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawPointDemo()
    main.show()
    sys.exit(app.exec_())