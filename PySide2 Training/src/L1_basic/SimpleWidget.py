'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
import PySide2
print (PySide2.__version__)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wd = QtWidgets.QWidget()
    
    wd.show()

    sys.exit(app.exec_())
