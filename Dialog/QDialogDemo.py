'''
对话框（QDialog）

5个对话框：
    1 QMessageBox 用来显示消息
    2 QColorDialog 用来显示颜色
    3 QFileDialog 用来显示文件打开或者保存
    4 QFontDialog 用来设置字体
    5 QInputDialog 用来获取用户输入信息

注：dialog.setWindowModality(Qt.ApplicationModal)  弹出对话框后，后面的主窗口不可选中
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)
        self.button=QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog=QDialog()
        button=QPushButton('退出',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QDialogDemo()
    main.show()
    sys.exit(app.exec_())
