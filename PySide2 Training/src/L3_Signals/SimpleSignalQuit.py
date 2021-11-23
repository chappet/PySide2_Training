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
    
    #Some signals on QPushButton
    wdButton = QtWidgets.QPushButton("QUIT")
    wdButton.clicked.connect(app.quit)
    
    #--------------------------------------------------------------
    #Exercise : Connect signal to print something before exit
    #--------------------------------------------------------------

    wdButton.show()
    
    sys.exit(app.exec_())