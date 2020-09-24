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
    def __init__(self):
        super().__init__()
        
        self.timer = QtCore.QTimer()
        self.timer.start(1000.)
        self.timer.timeout.connect(self.Tick)
    
    def Start(self):
        self.timer.timeout.connect(self.Tick)
                
    def Tick(self):
        t = time.time()
        print (id(self),"->Emit: ",t)
        QApplication.instance().emit(QtCore.SIGNAL("TICK_{}(double)".format(id(self))),t) 
        
class ClockDisplay():
    def __init__(self):
        super(ClockDisplay,self).__init__()

    def Display(self,t):
        print (id(self),"->Received: ", t)
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    #create two clocks and tow displays
    clock_1 = MyClock()
    display1 = ClockDisplay()

    time.sleep(0.5)
    
    clock_2 = MyClock()
    display2 = ClockDisplay()
    
    #connect clocks to display using a custom signal
    app.connect(QtCore.SIGNAL("TICK_{}(double)".format(id(clock_1))),display1.Display)
    app.connect(QtCore.SIGNAL("TICK_{}(double)".format(id(clock_2))),display2.Display)

    sys.exit(app.exec_())