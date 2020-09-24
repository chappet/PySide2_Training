'''
Created on 23 sept. 2020

@author: cchappet
'''
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Signal, Slot 

import time
import sys
    
class MyClock(QtCore.QObject):
    """
    Must inherited QObject to emit a Signal
    """
    tick = Signal(float)

    def __init__(self):
        super().__init__()
        
        self.timer = QtCore.QTimer()
        self.timer.start(1000.)
        self.timer.timeout.connect(self.Tick)
    
    def Start(self):
        self.timer.timeout.connect(self.Tick)
                
    def Tick(self):
        t = time.time()
        print ("Emit: ",t)
        self.tick.emit(t)
        
class ClockDisplay():
    def __init__(self):
        super(ClockDisplay,self).__init__()

    def Display(self,t):
        print ("Received: ", t)
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    clock = MyClock()

    display = ClockDisplay()

    clock.tick.connect(display.Display)

    sys.exit(app.exec_())