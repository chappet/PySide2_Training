'''
Created on 15 nov. 2019

@author: cchappet

Display a simple QFrame and set some properties
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys

def PrintDate(date):
    print (date)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdCal = QtWidgets.QCalendarWidget()
    
    wdCal.clicked.connect(PrintDate)
        
    wdCal.show()

    sys.exit(app.exec_())
