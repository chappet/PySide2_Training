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
    def __init__(self, fDelay):
        super(TimerUpdate, self).__init__()
        self.fDelay = fDelay
    
    def run(self):
        while(1):
            print (type(QtCore.SIGNAL("UPDATE()")))
            # SIGNAL is application wide
            QApplication.instance().emit(QtCore.SIGNAL("UPDATE()"))
#             self.app.emit(QtCore.SIGNAL("UPDATE()"))            
            time.sleep(self.fDelay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wdFrm = QtWidgets.QFrame()
    layout = QtWidgets.QVBoxLayout()
    wdFrm.setLayout(layout)
    
    #Create two labels that will display a counter
    wdCounter = QtWidgets.QLabel("0")
    layout.addWidget(wdCounter)


    #Create a function for widget updating
    @Slot()
    def UpdateCounter():
        wdCounter.setText(str(int(wdCounter.text()) + 1))

    QtCore.QObject.connect(app,QtCore.SIGNAL("UPDATE()"),UpdateCounter)
        
        
    #Launch the updating thread
    timerThread = TimerUpdate(0.005)
    timerThread.start()


    wdFrm.show()
    sys.exit(app.exec_())