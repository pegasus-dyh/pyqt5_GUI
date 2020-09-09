from PyQt5.QtWidgets import *
import sys
from door import door
from PyQt5.QtGui import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('站台门检测系统')
        self.resize(300,200)

        layout = QVBoxLayout(self)
        # 下面这段代码通过两种方式将信号与槽相连
        self.button1 = QPushButton('1号站台')
        self.button1.setText('1号站台')
        self.button1.clicked.connect(lambda: self.whichbutton(self.button1))

        # 在文本前面显示图像

        self.button2 = QPushButton('2号站台')
        self.button2.setText('2号站台')
        self.button2.clicked.connect(lambda: self.whichbutton(self.button2))

        self.button3 = QPushButton('3号站台')
        self.button3.setText('3号站台')
        self.button3.clicked.connect(lambda: self.whichbutton(self.button3))

        self.button4 = QPushButton('4号站台')
        self.button4.setText('4号站台')

        self.button4.clicked.connect(lambda: self.whichbutton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)




    def whichbutton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")
        dialog = door(self)
        dialog.exec()


    def buttonstate(self):
        if self.button1.isChecked():
                print("按钮1已被选中")











if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())