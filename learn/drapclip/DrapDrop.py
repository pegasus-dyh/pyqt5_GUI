'''
让控件支持拖拽动作
A.setDragEnabled(True)   A可拖动
B.setAcceptDrops(True)   B可接受

B需要两个事件
1 dragEnterEvent 将A拖拽到B触发
2 dropEvent 在B的区域放下A时触发
'''
import sys
from PyQt5.QtWidgets import *


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle('用画刷填充区域')
    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())
class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        layout=QFormLayout()
        layout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True) #让QLineEdit控件可拖动

        combo=MyComboBox()
        layout.addRow(lineEdit,combo)
        self.setLayout(layout)
        self.setWindowTitle('拖拽案例')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrapDropDemo()
    main.show()
    sys.exit(app.exec_())