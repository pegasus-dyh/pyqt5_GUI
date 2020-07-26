'''
使用剪切板
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()