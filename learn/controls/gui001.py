import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from learn.controls import Door01

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui= Door01.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())