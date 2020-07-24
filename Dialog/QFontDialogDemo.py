'''
字体对话框（QFontDialog）
'''
import  sys
from PyQt5.QtWidgets import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('字体对话框QFontDialogDemo')
        self.resize(300,400)

        layout=QVBoxLayout()
        self.button1=QPushButton('选择字体')
        self.button1.clicked.connect(self.getFont)
        layout.addWidget(self.button1)

        self.fontlable=QLabel('Hellow,测试字体')
        layout.addWidget(self.fontlable)

        self.setLayout(layout)

    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fontlable.setFont(font)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())


