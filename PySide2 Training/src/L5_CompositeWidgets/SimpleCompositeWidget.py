'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys

class QMyHelloWorld(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QtWidgets.QVBoxLayout(self)
        
        wdButton = QtWidgets.QPushButton("PRINT")
        layout.addWidget(wdButton)
        wdButton.clicked.connect(self.PrintLine)
 
        self.wdLineEdit = QtWidgets.QLineEdit('')
        layout.addWidget(self.wdLineEdit)
        
    def PrintLine(self):
        print (self.wdLineEdit.text())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdFrame = QtWidgets.QFrame()
    layout = QtWidgets.QHBoxLayout(wdFrame)
    
    wdCal = QtWidgets.QCalendarWidget()
    layout.addWidget(wdCal)
    
    wd = QMyHelloWorld()
    layout.addWidget(wd)
    
    wdFrame.show()

    sys.exit(app.exec_())
