'''

限制QLineEdit控件的输入（校验器）
如限制只能输入整数、浮点数或满足一定条件的字符串

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('校验器')
        layout=QFormLayout()

        IntLineEdit=QLineEdit()
        DoubleLineEdit=QLineEdit()
        ValidatorLineEdit=QLineEdit()

        layout.addRow('整数（Int）类型',IntLineEdit)
        layout.addRow('浮点（Double）类型',DoubleLineEdit)
        layout.addRow('数字和字母(Validator)类型',ValidatorLineEdit)

        IntLineEdit.setPlaceholderText('允许输入整数（整型）')
        DoubleLineEdit.setPlaceholderText('允许输入浮点型数据')
        ValidatorLineEdit.setPlaceholderText('允许输入数字和字母')

        #整数校验器
        intvalidator=QIntValidator(self)
        intvalidator.setRange(1,99)

        #浮点校验器 精度小数点后两位
        doublevalidator=QDoubleValidator(self)
        doublevalidator.setRange(-360,360)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度
        doublevalidator.setDecimals(2)

        #字符和数字校验器
        reg=QRegExp('[a-zA-Z0-9]+$')  #这里是正则表达式
        validator=QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器（使LineEdit与validator绑定）
        IntLineEdit.setValidator(intvalidator)
        DoubleLineEdit.setValidator(doublevalidator)
        ValidatorLineEdit.setValidator(validator)

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditValidator()
    main.show()
    sys.exit(app.exec_())





