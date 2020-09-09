'''
在表格中快速定位到特定的行
1. 数据的定位：findItems  返回一个列表
2. 如果找到了满足条件的单元格，会定位到单元格所在的行：setSliderPosition(row)

Python笔记：
python字符串格式化有两种方法  https://www.cnblogs.com/poloyy/p/12443158.html
1 %
2 format（功能更强大）

1 %示例

%o：oct 八进制
%d：dec 十进制
%x：hex 十六进制

输入
print("整数：%d,%d,%d" % (1, 22.22, 33))
print("整数不足5位，左边补空格   %5d   " % 22)
print("整数不足5位，左边补0     %05d   " % 22)
print("整数不足5位，右边补空格  %-5d   " % 22, "end")
print("八进制 %o" % 222)
print("十六进制 %x" % 12)
输出
整数：1,22,33
整数不足5位，左边补空格      22
整数不足5位，左边补0     00022
整数不足5位，右边补空格  22       end
八进制 336
十六进制 c

输入
print("浮点数：%f,%f " % (1, 22.22))
print("浮点数保留两位小数：%.2f  " % 22.222)
print("浮点数保留两位小数，宽5位，不足补0：%05.2f  " % 2.222)
输出
浮点数：1.000000,22.220000
浮点数保留两位小数：22.22
浮点数保留两位小数，宽5位，不足补0：02.22

输入
print("字符串：%s,%s,%s" % (1, 22.22, [1, 2]))
print("字符串不足5位，左边补空格   %5s   " % '2')
print("字符串不足5位，右边补空格   %-5s   " % '2', "end")
print("字符串宽10位，截取两位      %10.2s " % "hello.world")
输出
字符串：1,22.22,[1, 2]
字符串不足5位，左边补空格       2
字符串不足5位，右边补空格   2        end
字符串宽10位，截取两位              he

2 format 示例


'''

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800);

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                itemContent = '(%d,%d)' %(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))
        self.setLayout(layout)

        # 搜索满足条件的Cell
        text = '(1'
        items = tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0,255,0)))
            item.setForeground(QBrush(QColor(255,0,0)))

            row = item.row()

            # 定位到指定的行
            tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DataLocation()
    example.show()
    sys.exit(app.exec_())