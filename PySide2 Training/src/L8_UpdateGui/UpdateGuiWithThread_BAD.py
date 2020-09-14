'''
Created on 9 janv. 2020

@author: cchappet

!!! NOT TO BE REPRODUCE !!!
This module demonstrates a BAD way to update a widget created in the main thread from another thread
This code lead to umpredictable crashes of application (after minutes, hours or days ...)
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
import threading
import time

class TimerUpdate(threading.Thread):
    """
    This thread will update a widget label created in the main thread 
    and pass as an argument
    """
    def __init__(self, wdCounter, fDelay):
        super(TimerUpdate, self).__init__()
        self.wdCounter = wdCounter
        self.fDelay = fDelay
    
    def run(self):
        while(1):
            self.wdCounter.setText(str(int(self.wdCounter.text()) + 1))
            time.sleep(self.fDelay)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wdFrm = QtWidgets.QFrame()
    layout = QtWidgets.QVBoxLayout()
    wdFrm.setLayout(layout)
    
    #Create label that will display a counter
    wdCounter = QtWidgets.QLabel("0")
    layout.addWidget(wdCounter)

    #Launch the updating thread
    timerThread = TimerUpdate(wdCounter, 0.005)
    timerThread.start()

    
    wdFrm.show()
    sys.exit(app.exec_())