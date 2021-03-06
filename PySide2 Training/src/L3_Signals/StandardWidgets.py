'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates connection between standard widget signals and simple slots
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import threading
import time


"""
Create the demo windows
"""        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    wdLine = QtWidgets.QLineEdit("Some Information")
    wdLine.show()

    wdButton = QtWidgets.QPushButton("CLEAR")
    wdButton.clicked.connect(wdLine.clear)
    
    #Signal can be emitted by code
#     wdButton.clicked.emit()

    wdButton.show()
    
    sys.exit(app.exec_())