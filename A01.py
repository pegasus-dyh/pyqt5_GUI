'''
初级窗口，最后有修改窗口左上角图标的方法
'''

import sys
from PyQt5.QtWidgets import QApplication,QDesktopWidget,QMainWindow
from PyQt5.QtGui import QIcon

class A01(QMainWindow):
    def __init__(self,parent=None):
        super(A01,self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle('pegasus的第一个主窗口应用')

        #设置窗口尺寸
        self.resize(500,300)


        #设置状态栏并显示文字
        self.statusBar().showMessage('这段文字会显示10秒',10000)



    #窗口居中模块
        self.center()
    def center(self):
        screen=QDesktopWidget().screenGeometry() #获取屏幕坐标
        size=self.geometry() #获取窗口坐标
        newleft=(screen.width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)






if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Logo.ico')) #设置左上角窗口图标
    main=A01()
    main.show()
    sys.exit(app.exec_())