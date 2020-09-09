'''

QComboBox(下拉列表控件)
1 如何将列表项添加到QComboBox控件中
2 如何获取选中的列表项

槽--currentIndexChanged
'''
import sys
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(400,100)
        layout=QVBoxLayout()
        self.lable=QLabel('请选择编程语言')
        self.cb=QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Go'])

        self.cb.currentIndexChanged.connect(self.selectionChange) #与槽绑定

        layout.addWidget(self.lable)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self,i):
        self.lable.setText(self.cb.currentText())
        self.lable.adjustSize()

        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
            print('current index',i,"selection changed",self.cb.currentText())

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())


