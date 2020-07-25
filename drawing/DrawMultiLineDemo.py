'''
绘制不同的直线
绘制了5类风格的线和一条自定义线
'''
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
class DrawMulitiLineDemo(QWidget):
    def __init__(self):
        super(DrawMulitiLineDemo, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')


    def paintEvent(self, QPaintEvent):
        painter=QPainter()
        painter.begin(self)
        pen=QPen(Qt.red,3,Qt.SolidLine) #设置画笔，红色 粗细3 实线
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,10,5,4]) #一个有宽度为1和5的子线 组成的线  1和4宽10 4和1宽4
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)

        

        painter.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawMulitiLineDemo()
    main.show()
    sys.exit(app.exec_())