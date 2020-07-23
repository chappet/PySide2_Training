'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates a way to update a widget created in the main thread from another thread using Qt Signal
ALWAYS use L3_Signals when you want to update widget created in the main thread
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot 

import sys
import threading
import time


class TimerUpdate(threading.Thread):
    """
    This thread will update a widget label created in the main thread 
    and pass as an argument
    """
    def __init__(self, app, fDelay):
        super(TimerUpdate, self).__init__()
        self.app = app
        self.iCounter = 0
        self.fDelay = fDelay
    
    def run(self):
        while(1):
            self.app.emit(QtCore.SIGNAL("UPDATE(int)"),self.iCounter)
            
            # WARNING : argument's type is not checked and no error message is generated if wrong !!!
#             self.app.emit(QtCore.SIGNAL("UPDATE(int)"),str(self.iCounter)) #DOES NOT WORK : argument's type is wrong
#             self.app.emit(QtCore.SIGNAL("UPDATE(str)"),self.iCounter) #DOES NOT WORK : func's prototype is wrong
                        
            self.iCounter += 1 
                     
            time.sleep(self.fDelay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wdFrm = QtWidgets.QFrame()
    layout = QtWidgets.QVBoxLayout()
    wdFrm.setLayout(layout)
    
    #Create two labels that will display a counter
    wdCounter = QtWidgets.QLineEdit("0")
    layout.addWidget(wdCounter)


    #Create a function for widget updating
    def UpdateCounter(iCounter):
        wdCounter.setText(str(iCounter))

    app.connect(QtCore.SIGNAL("UPDATE(int)"),UpdateCounter)
        
        
    #Launch the updating thread
    timerThread = TimerUpdate(app, 0.005)
    timerThread.start()


    wdFrm.show()
    sys.exit(app.exec_())