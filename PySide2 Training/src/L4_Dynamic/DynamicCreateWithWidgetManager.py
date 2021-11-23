'''
Created on 9 janv. 2020

@author: cchappet


This module demonstrates how to close a widget correctly
WARNING : Using the red X icon just hide the widget, not close is
Must overload closeEvent

!!! No need to disconnect SIGNALS, it is done automatically !!!
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import numpy


class MyLineEdit(QtWidgets.QLineEdit):
    """
    """
    def __init__(self, sLabel, parent = None):
        super(MyLineEdit, self).__init__(sLabel)
        self.parent = parent

        #create an array to show the memory impact
        self.aDummy = numpy.array(100000000)

    def PrintVisible(self):
        print ("Widget {} is {}".format(id(self),"Visible" if self.isVisible() else "Hidden"))
        

#     def closeEvent(self, event):
#         """
#           Uncomment closeEvent the force the widget deletion
#           Otherwise the widget is just hidden
#         """  
#  
#         # call parents'widget manager to delete the widget
#         self.parent.DeleteWidget(self)
             
        
class WidgetMng():
    """
    A class for widget persistence
    """
    def __init__(self):
        self.lstWdManager = []
        
        #set a timer to print widget ID until widget deletion
        self.timer = QtCore.QTimer()
        self.timer.start(1000.)
        
    def CreateWidget(self):                    
        wdLine = MyLineEdit(str(len(self.lstWdManager)),parent = self)
        self.lstWdManager.append(wdLine)
        wdLine.show()        

        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"),wdLine.PrintVisible)
        
    def DeleteWidget(self,idWidget):
        #widget deletion
        #Signal timeout is also disconnected
        self.lstWdManager[self.lstWdManager.index(idWidget)].deleteLater()
        
        #remove widget from manager list
        self.lstWdManager.remove(idWidget) 
    
        
    def RestoreWidget(self):
        for wd in self.lstWdManager: wd.show()
               
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