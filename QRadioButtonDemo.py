'''

QRadioButton(单选按钮控件)
注：此控件需放入到一个容器内
'''

import sys
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout=QHBoxLayout()
        self.button1=QRadioButton('单选按钮1')
        self.button1.setChecked(True) #默认按钮1为选中状态

        self.button1.toggled.connect(self.buttonstate)
        layout.addWidget(self.button1)

        self.button2=QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonstate)
        layout.addWidget(self.button2)
        self.setLayout(layout)




    def buttonstate(self):
        radiobutton=self.sender()
        if radiobutton.text()=='单选按钮1':
            if radiobutton.isChecked==True:
                print('<' + radiobutton.text() + '>被选中')
            else:
                print('<'+radiobutton.text()+'>被取消选中状态')
        if radiobutton.text()=='单选按钮2':
            if radiobutton.isChecked==True:
                print('<' + radiobutton.text() + '>被选中')
            else:
                print('<'+radiobutton.text()+'>被取消选中状态')


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
