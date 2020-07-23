'''
QTextEdit控件
'''
from PyQt5.QtWidgets import *
import sys
class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QText控件演示')
        self.resize(300,320)
        self.TextEdit=QTextEdit()
        self.button1=QPushButton('显示文本')
        self.button2=QPushButton('显示HTML')
        self.button3=QPushButton('获取文本')
        self.button4=QPushButton('获取HTML')

        layout=QVBoxLayout()
        layout.addWidget(self.TextEdit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

        #将槽与信号绑定
        self.button1.clicked.connect(self.on_click_button_text)
        self.button2.clicked.connect(self.on_click_button_html)
        self.button3.clicked.connect(self.totext)
        self.button4.clicked.connect(self.tohtml)
    def on_click_button_text(self):
        self.TextEdit.setPlainText('Hellow,world')
    def on_click_button_html(self):
        self.TextEdit.setHtml('<font color="blue" size="5">Hellow World </font>')
    def totext(self):
        a1=self.TextEdit.toPlainText()
        print("获取的文本"+a1)
    def tohtml(self):
        a2=self.TextEdit.toHtml()
        print('获取的HTML'+a2)


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QTextEditDemo()
    main.show()
    sys.exit(app.exec_())