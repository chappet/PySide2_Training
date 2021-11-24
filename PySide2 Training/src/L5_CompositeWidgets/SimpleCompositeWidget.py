'''
Created on 15 nov. 2019

@author: cchappet

Demonstrate the creation of a composite widget
Useful for user defines widgets that use diffents kings of widget to fullfill a tack
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys

class QMyHelloWorld(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setMaximumHeight(100)
        
        layout = QtWidgets.QVBoxLayout(self)
 
        horLayout = QtWidgets.QHBoxLayout()
        layout.addLayout(horLayout)
        
        wdLabel = QtWidgets.QLabel("Name :")
        horLayout.addWidget(wdLabel)
        
        self.wdLineEdit = QtWidgets.QLineEdit('')
        horLayout.addWidget(self.wdLineEdit)

        wdButton = QtWidgets.QPushButton("Say Hello")
        layout.addWidget(wdButton)
        wdButton.clicked.connect(self.PrintLine)
        
    def PrintLine(self):
        print ("Hello {}".format(self.wdLineEdit.text()))
        
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
