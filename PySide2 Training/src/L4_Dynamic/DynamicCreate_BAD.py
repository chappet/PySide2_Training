'''
Created on 9 janv. 2020

@author: cchappet

!!! NOT TO BE REPRODUCE !!!
This module demonstrates a BAD way to create one or several widgets from the main application
As the new widget handle is not persistent, the widget is immediately destroyed by the garbage collector
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys

#a function that create a new label widget    
def CreateWidget():
    wdLabel = QtWidgets.QLabel()
    wdLabel.show()        
   
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
        
    #create and display a Push Button that call CreateWidget
    wdButton = QtWidgets.QPushButton("Show")
    wdButton.clicked.connect(CreateWidget)    

    wdButton.show()
    
    sys.exit(app.exec_())