'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates an application signal broadcast
when the signal receiver is created BEFORE a signal emitter, connect signals between emitter and receiver
using emitter's classe signal is not possible.

Use case : 
Create several widgets and change the widgets'color using a color dialog created later.

'''
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Signal, Slot 

import sys
import numpy


#Create a custom widget that inherited from QLineEdit
class MyDisplay(QtWidgets.QLineEdit):
    """
    A custom QLineEdit
    """
    def __init__(self,parent = None):
        super().__init__()
        
        self.parent = parent

        self.setText(str(1 + int(numpy.random.random() * 10)))        
        self.show()
        
        QApplication.instance().connect(QtCore.SIGNAL("CHANGE_COLOR(QColor)"),self.ChangeColor)
 
    def ChangeColor(self, color):
        self.setStyleSheet("background-color:rgb({},{},{})".format(color.red(), color.green(), color.blue()))
   

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    #######################################
    #A color editor to change all Display's colors  

    def GetColor():
        """
        Select a color using a QColorDialog
        """
        color = QtWidgets.QColorDialog().getColor()
        
        #Signal is emitted from the QApplication in order to be broadcasted
        print ("Color {} selected".format(color))
        app.emit(QtCore.SIGNAL("CHANGE_COLOR(QColor)"),color) 

    wdCmdGetColor = QtWidgets.QPushButton("GET COLOR")
    wdCmdGetColor.clicked.connect(GetColor)  
    wdCmdGetColor.show()

    #######################################
    #A simple Display generator    
    lstWd = []
        

    def CreateDisplay():
        lstWd.append(MyDisplay(app))
    
    wdCmdShow = QtWidgets.QPushButton("Show Display")
    wdCmdShow.clicked.connect(CreateDisplay)  
    wdCmdShow.show()

      
    sys.exit(app.exec_())