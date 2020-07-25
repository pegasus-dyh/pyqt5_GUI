'''
绘图API:绘制文本
1文本
2各种图形（直线、点、椭圆、扇形、圆、多边形等）
3图像

基本过程
QPainter
painter=Qpainter()
painter.begin()
painter.drawText(...)
painter.end()
必须在paintEvent事件方法中绘制各种元素
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
class drawTextDemo(QWidget):
    def __init__(self):
        super(drawTextDemo, self).__init__()
        self.setWindowTitle('在窗口绘制文本')
        self.resize(300,200)
        self.text="南风知我意，吹梦到西洲"

    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(QColor(150,43,5)) #设置画笔颜色
        painter.setFont(QFont('SimSun',25)) #设置字体，字号
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=drawTextDemo()
    main.show()
    sys.exit(app.exec_())


