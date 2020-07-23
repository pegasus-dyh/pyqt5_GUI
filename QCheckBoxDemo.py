'''

复选框控件(QCheckBox)(多选)
3种状态：
    未选中：0
    半选中：1
    选中 ：2

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        layout=QHBoxLayout()

        self.CheckBox1=QCheckBox('复选框控件1')
        self.CheckBox1.setChecked(True)
        self.CheckBox1.stateChanged.connect(lambda :self.CheckBoxState(self.CheckBox1))
        layout.addWidget(self.CheckBox1)

        self.CheckBox2=QCheckBox('复选框控件2')
        self.CheckBox2.stateChanged.connect(lambda :self.CheckBoxState(self.CheckBox2))
        layout.addWidget(self.CheckBox2)

        self.CheckBox3=QCheckBox('半选中')
        self.CheckBox3.stateChanged.connect(lambda :self.CheckBoxState(self.CheckBox3))
        self.CheckBox3.setTristate(True)
        self.CheckBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.CheckBox3)

        self.setLayout(layout)


    def CheckBoxState(self,cb):
        checkstate1=self.CheckBox1.text()+',is checked='+str(
            self.CheckBox1.isChecked())+',checkState='+str(self.CheckBox1.checkState())+'\n'
        checkstate2 = self.CheckBox2.text() + ',is checked=' + str(
            self.CheckBox2.isChecked()) + ',checkState=' + str(self.CheckBox2.checkState()) + '\n'
        checkstate3 = self.CheckBox3.text() + ',is checked=' + str(
            self.CheckBox3.isChecked()) + ',checkState=' + str(self.CheckBox3.checkState()) + '\n'
        print(checkstate1+checkstate2+checkstate3)


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())

