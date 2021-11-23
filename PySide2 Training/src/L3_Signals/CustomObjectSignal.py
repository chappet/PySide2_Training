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
    #Signal must be declared as a class variable
    tick = Signal(float)

    def __init__(self):
        super().__init__()
        
        self.init_t = time.time()
        
        ########################################################
        # A Signal can be emitted even if there are no receivers.
        ########################################################
#         t = time.time()
#         self.tick.emit(t)
        
        #Create a 1 Hz Timer and connect to an internal method
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.__Tick) # no () for a function handle !
        
    def StartTimer(self):   
        self.timer.start(1000.)  
             
    def __Tick(self):
        t = time.time() - self.init_t
        print ("Emit: ",t)
        #Emit the time elapsed since object creation
        self.tick.emit(t)
        
class ClockDisplay():
    def __init__(self):
        super(ClockDisplay,self).__init__()
        
    def Display(self,t):
        print ("Received: ", t)
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    clock = MyClock()
    
    time.sleep(2)
    
    display = ClockDisplay()
    
    clock.tick.connect(display.Display)
    clock.StartTimer()

    sys.exit(app.exec_())