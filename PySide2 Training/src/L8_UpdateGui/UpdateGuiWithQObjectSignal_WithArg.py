'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates a way to update a widget created in the main thread from another thread using Qt Signal
ALWAYS use Signals when you want to update widget created in the main thread
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import threading
import time

class SignalDefinitionClass(QObject):
    #Be careful with argument type !!!
    signalUpdate = Signal(int)

class TimerUpdate(threading.Thread):
    """
    This thread will update a widget label created in the main thread 
    and pass as an argument
    """
    def __init__(self, signalUpdate, fDelay):
        super(TimerUpdate, self).__init__()
        self.signalUpdate = signalUpdate
        self.iCounter = 0
        self.fDelay = fDelay
    
    def run(self):
        while(1):
            self.signalUpdate.emit(self.iCounter)
            
            self.iCounter += 1 
                     
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
    def UpdateCounter(iCounter):
        wdCounter.setText(str(iCounter))

    SignalObject = SignalDefinitionClass()
    SignalObject.signalUpdate.connect(UpdateCounter)
        
    #Launch the updating thread
    timerThread = TimerUpdate(SignalObject.signalUpdate, 0.005)
    timerThread.start()


    wdFrm.show()
    sys.exit(app.exec_())