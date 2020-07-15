import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
import time

class A01(QMainWindow):
    def __init__(self,parent=None):
        super(A01,self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle('pegasus的第一个主窗口应用')

        #设置窗口尺寸
        self.resize(400,300)


        #设置状态栏并显示文字
        self.statusBar().showMessage('这段文字会显示10秒',10000)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=A01()
    main.show()
    sys.exit(app.exec_())