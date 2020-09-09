'''

QLineEdit控件与回显模式
基本功能：输入单行的文本

一、Echomode（回显模式）
4种回显模式：
1 Normal 标准模式 输入什么显示什么
2 Noecho 不回显
3 Password 回显但只是一个字符对应一个黑点这类的，看不出实际内容，与我们输入qq密码时类似。
4 PasswordEchoOnEdit 回显 短时间内是模式1 过一段时间为模式3

二、placeholdertext:当文本输入框没有输入时 显示提示文字。

一些小操作：
MAC: Command   Windows:Control(ctrl)
'''
from PyQt5.QtWidgets import *
import sys
class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("文本输入框回显模式")
        formlayout   =   QFormLayout()
        NormalLineEdit   =    QLineEdit()
        NoechoLineEdit     =     QLineEdit()
        PasswordLineEdit     =     QLineEdit()
        PasswordEchoOnEditLineEdit = QLineEdit()

        formlayout.addRow('Normal',NormalLineEdit)
        formlayout.addRow('Noecho',NoechoLineEdit)
        formlayout.addRow('Password',PasswordLineEdit)
        formlayout.addRow('PasswordEchoOnEdit',PasswordEchoOnEditLineEdit)

        #placeholdertext
        NormalLineEdit.setPlaceholderText('normal模式')
        NoechoLineEdit.setPlaceholderText('noecho模式')
        PasswordLineEdit.setPlaceholderText('password模式')
        PasswordEchoOnEditLineEdit.setPlaceholderText('passwordEchoEdit模式')

        NormalLineEdit.setEchoMode(QLineEdit.Normal)
        NoechoLineEdit.setEchoMode(QLineEdit.NoEcho)
        PasswordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEditLineEdit.setEchoMode((QLineEdit.PasswordEchoOnEdit))

        self.setLayout(formlayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())


