'''
Created on 9 janv. 2020

@author: cchappet

!!! NOT PERFECT !!!
This module demonstrates a way to create, display and delete several widgets from the main application
the widgets are deleted by the red cross !!!
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import numpy


class MyLabel(QtWidgets.QLabel):
    """
    
    """
    def __init__(self, sLabel, parent = None):
        super(MyLabel, self).__init__(sLabel)
        self.parent = parent

        #create an array to show the memory impact
        self.aDummy = numpy.array(1000000)
        
    def closeEvent(self, event):
        """
        the widget must be explicitly deleted !
        """
        # delete the widget handle
        self.parent.DeleteWidget(self)
        
        # or delete the widget
#         self.deleteLater()
    
        
class WidgetMng():
    """
    A class for widget persistence
    """
    def __init__(self):
        self.lstWdManager = []
        
        #set a timer to print widget ID until widget deletion
        self.timer = QtCore.QTimer()
        self.timer.start(1000.)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"),self.PrintVisible)
        
    def CreateWidget(self):                    
        wdLabel = MyLabel(str(len(self.lstWdManager)),parent = self)
        self.lstWdManager.append(wdLabel)
        wdLabel.show()        

    def DeleteWidget(self,idWidget):
        del self.lstWdManager[self.lstWdManager.index(idWidget)]
        
    def RestoreWidget(self):
        for wd in self.lstWdManager: wd.show()
    
    def PrintVisible(self):
        print()
        for wd in self.lstWdManager: 
            print ("Widget {} is {}".format(id(wd),"Visible" if wd.isVisible() else "Hidden"))
           
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widgetMng = WidgetMng()
            
    wdButtonShow = QtWidgets.QPushButton("Show")
    wdButtonShow.clicked.connect(widgetMng.CreateWidget)    
    wdButtonShow.show()
    wdButtonShow.move(400,400)

    wdButtonRestore = QtWidgets.QPushButton("Restore")
    wdButtonRestore.clicked.connect(widgetMng.RestoreWidget)    
    wdButtonRestore.show()
    wdButtonRestore.move(500,500)
    
    sys.exit(app.exec_())