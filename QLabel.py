'''
QLable 控件
setAlignment():设置文本对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText():返回所选的字符
setWordWrap():设置是否允许换行

QLable常用的信号（事件）：
1、 当鼠标滑过QLable控件时触发：linkHovered
2、 当鼠标单击QLable控件时触发：linkActivated
'''

import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPalette,QPixmap   #调色板，图片
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lable1 = QLabel(self)
        lable2 = QLabel(self)
        lable3 = QLabel(self)
        lable4 = QLabel(self)

        lable1.setText('<font color = yellow>这是一个文本标签.</font>')
        lable1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue) #添加背景色
        lable1.setPalette(palette)
        lable1.setAlignment(Qt.AlignCenter)

        lable2.setText('<a href="#">欢迎使用python GUI程序</a>')

        lable3.setAlignment(Qt.AlignCenter)
        lable3.setToolTip("这是一个图片标签")
        lable3.setPixmap(QPixmap("./images/python.jpg"))

        #如果设置为true用浏览器打开网页，设置为false调用槽函数
        lable4.setOpenExternalLinks(True)
        lable4.setText("<a href='https://geekori.com'>欢迎来到本网站</a>")
        lable4.setAlignment(Qt.AlignRight)
        lable4.setToolTip('这是一个超级链接')

        vbox=QVBoxLayout()
        vbox.addWidget(lable1)
        vbox.addWidget(lable2)
        vbox.addWidget(lable3)
        vbox.addWidget(lable4)

        lable2.linkHovered.connect(self.linkHovered)
        lable4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLable教例窗口')


    def linkHovered(self):
        print('当鼠标滑过lable2标签时，触发事件')
    def linkClicked(self):
        print('当鼠标单击lable4标签时，触发事件')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLabelDemo()
    main.show()
    sys.exit(app.exec_())