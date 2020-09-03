'''
Created on 9 janv. 2020

@author: cchappet

!!! NOT PERFECT !!!
This module demonstrates a way to create and display one or several widgets from the main application
IT IS NOT PERFECT because the widgets are not deleted by the red cross (simply hidden) !!!
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys, numpy


class WidgetMng():
    def __init__(self):
        
        #Create a list to persist the widget handles
        self.lstWdManager = []
        
        #create an array to show the memory impact
        self.aDummy = numpy.array(1000000)

        #set a timer to print widget visible state
        self.timer = QtCore.QTimer()
        self.timer.start(1000.)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"),self.PrintVisible)

    def CreateWidget(self):            
        wdLabel = QtWidgets.QLabel(str(len(self.lstWdManager)))
        self.lstWdManager.append(wdLabel)
        wdLabel.show()        

    def RestoreWidget(self):
        for wd in self.lstWdManager: 
            print ("Restore Widget Id {}".format(id(wd)))
            wd.show()

    def PrintVisible(self):
        for wd in self.lstWdManager: 
            print ("Widget {} is {}".format(id(wd),"Visible" if wd.isVisible() else "Hidden"))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widgetMng = WidgetMng()
            
    wdButtonShow = QtWidgets.QPushButton("Show")
    wdButtonShow.clicked.connect(widgetMng.CreateWidget)    
    wdButtonShow.move(400,400)
    wdButtonShow.show()

    wdButtonRestore = QtWidgets.QPushButton("Restore")
    wdButtonRestore.clicked.connect(widgetMng.RestoreWidget)  
    wdButtonRestore.move(500,500)  
    wdButtonRestore.show()
    
    sys.exit(app.exec_())