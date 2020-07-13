import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':  #从别的程序调用本程序为false，只能运行本程序时才为真

    #创建QApplication实例
    app=QApplication(sys.argv) #sys用来获取命令行参数的

    #创建一个窗口
    w=QWidget()
    w.resize(400,200) #设置窗口的尺寸 长300，宽150

    #移动窗口（移动窗口左上角坐标）
    w.move(300,300)

    #设置窗口标题
    w.setWindowTitle('我的第一个基于PyQt5的应用')

    #显示窗口
    w.show()

    #进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
