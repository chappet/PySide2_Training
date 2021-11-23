'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates the use of different types of signals
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import threading
import time

"""
Define some SLOT functions
"""

def FocusChanged(wOld, wNew):
    print ("focus changed from old : {} to new {}".format(wOld, wNew))
    
def PrintOk(): 
    print ("OK")

def PrintPressed(): 
    print ("Pressed")

def PrintPosition(iOld, iNew):
    print ("Old :{} New : {}".format(iOld, iNew))

def PrintText(sText):
    print (sText)

def ShowItem(item):    
    print (item.text())

"""
Create the demo windows
"""        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #the only QApplication signal : focusChanged
    app.focusChanged.connect(FocusChanged)
    
    #Create the demo container
    wdFrm = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(wdFrm)

    #Some signals on QPushButton
    wdButton = QtWidgets.QPushButton("OK")
    
    #SIGNALS : clicked,pressed
    wdButton.clicked.connect(PrintOk)
    wdButton.pressed.connect(PrintPressed)

    layout.addWidget(wdButton)

    #Some signals on QLineEdit
    wdLineEdit = QtWidgets.QLineEdit("")
    layout.addWidget(wdLineEdit)
    
    #SIGNALS : textChanged, cursorPositionChanged
    wdLineEdit.textChanged.connect(PrintText)
    wdLineEdit.cursorPositionChanged.connect(PrintPosition)
    
    #Some signals on QListWidget
    wdListWidget = QtWidgets.QListWidget()
    layout.addWidget(wdListWidget)
    wdListWidget.addItem(QtWidgets.QListWidgetItem("line 1"))
    wdListWidget.addItem(QtWidgets.QListWidgetItem("line 2"))
    wdListWidget.addItem(QtWidgets.QListWidgetItem("line 3"))
    
    #SIGNALS : itemDoubleClicked
    wdListWidget.itemDoubleClicked.connect(ShowItem)

    #Connect a PushButton SIGNAL to a QListWidget SLOT
    wdButtonClear = QtWidgets.QPushButton("CLEAR LIST")
    layout.addWidget(wdButtonClear)
    
    #SIGNALS : clicked
    wdButtonClear.clicked.connect(wdListWidget.clear)

    #Some signals on QSlider
    wdSlider = QtWidgets.QSlider(orientation = QtCore.Qt.Horizontal)
    wdSlider.setMinimum(0)
    wdSlider.setMaximum(5)
    
    layout.addWidget(wdSlider)
    wdSlider.valueChanged.connect(PrintText)

    wdFrm.show()
    
    sys.exit(app.exec_())