'''
文件对话框(QFileDialog)

本例中实现了按钮与图像和文本的关联（图在label上，信号与槽的绑定）
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QFileDialog案例,文件对话窗口')
        layout=QVBoxLayout()
        self.button1=QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel=QLabel()
        layout.addWidget(self.imageLabel)

        self.button2=QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
    def loadImage(self):
        fname,_=QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))
    def loadText(self):
        dialog=QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filenames=dialog.selectedFiles()
            f=open(filenames[0],ecoding='utf-8',mode='r')
            with f:#这里使用with语句是为了自动关闭文件
                data=f.read()
                self.contents.setText(data)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
