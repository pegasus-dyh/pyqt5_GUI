import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class doorwindow(QWidget) :
    def __init__(self):
        super(doorwindow,self).__init__()

        #设置主窗口的标题
        self.setWindowTitle('站台门PHM子系统')
        #设置窗口尺寸
        self.resize(400,600)
        #设置状态栏并显示文字


        layout = QGridLayout()
        #按钮
        self.button1 = QPushButton("站台1")
        self.button2 = QPushButton("站台2")
        self.button3 = QPushButton("站台3")
        self.button4 = QPushButton("站台4")
        self.button5 = QPushButton("站台5")
        self.button6 = QPushButton("站台6")
        self.button7 = QPushButton("站台7")
        self.button8 = QPushButton("站台8")
        self.button9 = QPushButton("站台9")
        self.button10 = QPushButton("站台10")

        self.button1.clicked.connect(lambda : self.buttonslot1(self.button1))
        self.button1.clicked.connect(self.openwindow)

        self.button2.clicked.connect(lambda: self.buttonslot1(self.button2))
        self.button2.clicked.connect(self.openwindow)

        self.button3.clicked.connect(lambda: self.buttonslot1(self.button3))
        self.button3.clicked.connect(self.openwindow)

        self.button4.clicked.connect(lambda: self.buttonslot1(self.button4))
        self.button4.clicked.connect(self.openwindow)

        self.button5.clicked.connect(lambda: self.buttonslot1(self.button5))
        self.button5.clicked.connect(self.openwindow)

        self.button6.clicked.connect(lambda: self.buttonslot1(self.button6))
        self.button6.clicked.connect(self.openwindow)

        self.button7.clicked.connect(lambda: self.buttonslot1(self.button7))
        self.button7.clicked.connect(self.openwindow)

        self.button8.clicked.connect(lambda: self.buttonslot1(self.button8))
        self.button8.clicked.connect(self.openwindow)

        self.button9.clicked.connect(lambda: self.buttonslot1(self.button9))
        self.button9.clicked.connect(self.openwindow)

        self.button10.clicked.connect(lambda: self.buttonslot1(self.button10))
        self.button10.clicked.connect(self.openwindow)

        layout.addWidget(self.button1, 1, 2, 1, 1)
        layout.addWidget(self.button2, 2, 2, 1, 1)
        layout.addWidget(self.button3, 3, 2, 1, 1)
        layout.addWidget(self.button4, 4, 2, 1, 1)
        layout.addWidget(self.button5, 5, 2, 1, 1)
        layout.addWidget(self.button6, 6, 2, 1, 1)
        layout.addWidget(self.button7, 7, 2, 1, 1)
        layout.addWidget(self.button8, 8, 2, 1, 1)
        layout.addWidget(self.button9, 9, 2, 1, 1)
        layout.addWidget(self.button10, 10, 2, 1, 1)



        #label1
        self.l1 = QLabel("1号站台   状态")
        self.l2 = QLabel("2号站台   状态")
        self.l3 = QLabel("3号站台   状态")
        self.l4 = QLabel("4号站台   状态")
        self.l5 = QLabel("5号站台   状态")
        self.l6 = QLabel("6号站台   状态")
        self.l7 = QLabel("7号站台   状态")
        self.l8 = QLabel("8号站台   状态")
        self.l9 = QLabel("9号站台   状态")
        self.l10 = QLabel("10号站台  状态")

        layout.addWidget(self.l1, 1, 0, 1, 2)
        layout.addWidget(self.l2, 2, 0, 1, 2)
        layout.addWidget(self.l3, 3, 0, 1, 2)
        layout.addWidget(self.l4, 4, 0, 1, 2)
        layout.addWidget(self.l5, 5, 0, 1, 2)
        layout.addWidget(self.l6, 6, 0, 1, 2)
        layout.addWidget(self.l7, 7, 0, 1, 2)
        layout.addWidget(self.l8, 8, 0, 1, 2)
        layout.addWidget(self.l9, 9, 0, 1, 2)
        layout.addWidget(self.l10, 10, 0, 1, 2)

        #label2
        self.l21 = QLabel("运行状态")
        self.l22 = QLabel("运行状态")
        self.l23 = QLabel("运行状态")
        self.l24 = QLabel("运行状态")
        self.l25 = QLabel("运行状态")
        self.l26 = QLabel("运行状态")
        self.l27 = QLabel("运行状态")
        self.l28 = QLabel("运行状态")
        self.l29 = QLabel("运行状态")
        self.l210 = QLabel("运行状态")

        layout.addWidget(self.l21, 1, 1, 1, 1)
        layout.addWidget(self.l22, 2, 1, 1, 1)
        layout.addWidget(self.l23, 3, 1, 1, 1)
        layout.addWidget(self.l24, 4, 1, 1, 1)
        layout.addWidget(self.l25, 5, 1, 1, 1)
        layout.addWidget(self.l26, 6, 1, 1, 1)
        layout.addWidget(self.l27, 7, 1, 1, 1)
        layout.addWidget(self.l28, 8, 1, 1, 1)
        layout.addWidget(self.l29, 9, 1, 1, 1)
        layout.addWidget(self.l210, 10, 1, 1, 1)


        self.setLayout(layout)


    def buttonslot1(self,btn):
        str=btn.text()
        print("被单击的按钮是<" + str + ">")
    def openwindow(self):
        dialog = sonwindow()
        dialog.show()
        dialog.exec()

class sonwindow(QDialog) :
    def __init__(self):
        super(sonwindow,self).__init__()

        #设置主窗口的标题
        self.setWindowTitle('站台门')
        #设置窗口尺寸
        self.resize(400,600)
        #设置状态栏并显示文字


        layout = QGridLayout()




        #label1
        self.l31 = QLabel("直流母线电流")
        self.l32 = QLabel("直流母线电压")
        self.l33 = QLabel("控制器输出电流")
        self.l34 = QLabel("控制器输出电压")
        self.l35 = QLabel("锁电压")
        self.l36 = QLabel("锁电流")
        self.l37 = QLabel("电机温度")
        self.l38 = QLabel("电池温度")
        self.l39 = QLabel("电池电压")
        self.l310 = QLabel("电池电流")
        self.l311 = QLabel("开关次数")
        self.l312 = QLabel("速度曲线")

        layout.addWidget(self.l31, 1, 0, 1, 2)
        layout.addWidget(self.l32, 1, 1, 1, 2)
        layout.addWidget(self.l33, 1, 2, 1, 2)

        layout.addWidget(self.l34, 2, 0, 1, 2)
        layout.addWidget(self.l35, 2, 1, 1, 2)
        layout.addWidget(self.l36, 2, 2, 1, 2)

        layout.addWidget(self.l37, 3, 0, 1, 2)
        layout.addWidget(self.l38, 3, 1, 1, 2)
        layout.addWidget(self.l39, 3, 2, 1, 2)

        layout.addWidget(self.l310, 4, 0, 1, 2)
        layout.addWidget(self.l311, 4, 1, 1, 2)
        layout.addWidget(self.l312, 4, 2, 1, 2)

        self.setLayout(layout)










if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('images/Logo.ico'))
    main=doorwindow()
    main.show()
    sys.exit(app.exec_())
