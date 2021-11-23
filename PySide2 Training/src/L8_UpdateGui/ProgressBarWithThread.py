'''
Created on 7 juil. 2014

@author: cchappet

Demonstrate the animation of a QProgressBar in order to keep the GUI alive.
'''
import os, sys,time
import collections
from threading import Thread

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot 


class AnimeProgressBar(QtWidgets.QProgressBar):
    """
    A QProgressBar with an internal mainloop
    Update is made by a separate Thread
    """
    
    def __init__(self,iDelay):
        super(AnimeProgressBar, self).__init__()
        self.iDelay = iDelay
        
        #Create Thread and connect to update and finished signals
        self.process = CounterThread(self.iDelay)
        self.process.updateSignal.connect(self.setValue) 
        self.process.finished.connect(self.close)  
        
        #Start the counter     
        self.process.start()
    
        #Display the QProgressBar
        self.show()
        
        #Run a blocking MainLoop
        self._eventLoop = QtCore.QEventLoop()
        self._eventLoop.exec_()
        
        #Delete the widget when counter is finished
        self.deleteLater()
     

class CounterThread(QtCore.QThread, QtCore.QObject):
    """
    A Thread that emit a signal with a counter value
    """
    updateSignal = Signal(float)
    
    def __init__(self,iDelay):
        super(CounterThread, self).__init__()
        self.iDelay = iDelay
        
    def run(self):
        time0 = time.time()
         
        while time.time() - time0 < self.iDelay : 
            timeElapse = time.time() - time0
            self.updateSignal.emit(timeElapse * 100 / self.iDelay)
            time.sleep(0.02) #Let mainloop process the events
        
            
class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent
        
        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)
        
        self.wdShowProgessBar = QtWidgets.QPushButton("Show Progress Bar", parent = self)
        self.wdShowProgessBar.clicked.connect(self.ShowProgressBar)
        wdLayout.addWidget(self.wdShowProgessBar,2,0,1,2)

    def ShowProgressBar(self):
        self.tProgressBar = AnimeProgressBar(iDelay = 5)


# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    wdFrm.show()

    sys.exit(app.exec_())   
