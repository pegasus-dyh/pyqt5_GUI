'''
绘制各种图形

弧
圆
矩形
绘制图像
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class DrawMulitiLineDemo(QWidget):
    def __init__(self):
        super(DrawMulitiLineDemo, self).__init__()
        self.resize(300,800)
        self.setWindowTitle('绘制各种图形')
    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        #绘制弧
        rect=QRect(0,10,100,100) #前两位左上角坐标 后两位长宽
        #alen : 一个alen等于1/16度 45度=45*16
        painter.drawArc(rect,0,50*16)  #此弧形的角度起始是0结束是50度

        #通过弧绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(120,10,100,100,0,360*16)

        #绘制带弦的弧
        painter.drawChord(10,120,100,100,0,130*16)

        #绘制扇形
        painter.drawPie(10,240,100,100,12,130*16)

        #椭圆
        painter.drawEllipse(120,120,150,100)

        #绘制多边形(5)
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(290,512)
        point4 = QPoint(290,588)
        point5 = QPoint(200,533)
        polygon=QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polygon)

        #绘制图像
        image=QImage('G:\\pyqt5_GUI\\controls\\images\\screen.png')
        rect1=QRect(10,600,image.width()/4,image.height()/4)
        painter.drawImage(rect1,image)


        painter.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawMulitiLineDemo()
    main.show()
    sys.exit(app.exec_())