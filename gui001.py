import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import learn001

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui=learn001.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())