'''
Created on 7 juil. 2014

@author: cchappet

Demonstrate running a long calculation while keeping GUI alive
and update a ProgressBar
'''
import os, sys,time
import ctypes
import collections

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot, QThread,QObject


class Worker(QObject):
    """
    Computation must be embedded into a 'worker'
    """
    finished = Signal()
    progress = Signal(int)

    def run(self):

        self.InterruptedComputation()
         
        self.NonInterruptedComputation()
        
        self.finished.emit()        

    def InterruptedComputation(self):
        """
        If some extra code can be injected in the computation,
        add some calls to time.sleep or processEvents to let the main
        GUI handle the events
        """
        for i in range(5):
            time.sleep(1)
            self.progress.emit(i + 1)
    
    def NonInterruptedComputation(self):
        """
        In most cases, computation cannot be interrupted with some extra code 
        The main GUI will have some refresh latency       
        """
        self.progress.emit(-1000000)
        x = 0
        for i in range(200000000) : 
            x=x+1        

    def InfiniteComputation(self):
        
        try:
            while (1) : pass
        except:
            print("Exception occured in Thread")

class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent
        self.clicksCount = 1
        
        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QVBoxLayout()
        self.setLayout(wdLayout)
        
        self.longRunningBtn = QtWidgets.QPushButton("Run Computation")
        wdLayout.addWidget(self.longRunningBtn)
        self.longRunningBtn.clicked.connect(self.runLongTask)

        self.wdProgressBar = QtWidgets.QProgressBar()  
        self.wdProgressBar.setTextVisible(False)
        wdLayout.addWidget(self.wdProgressBar)      
        
        self.stepLabel = QtWidgets.QLabel("step")
        wdLayout.addWidget(self.stepLabel)

        self.clicksLabel = QtWidgets.QLabel("click")
        wdLayout.addWidget(self.clicksLabel)
        
        self.countBtn = QtWidgets.QPushButton("Click me!", self)
        self.countBtn.clicked.connect(self.countClicks) 
        wdLayout.addWidget(self.countBtn)       
        
        
        
        
    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )  

        #######################################
        #Create a timer for QProgressBar update
        #######################################
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.UpdateProgressBar)
        
        #Stop and destroye the timer when the computation Thread is finished
        self.thread.finished.connect(self.timer.stop)
        self.thread.finished.connect(self.timer.deleteLater)

        #Reset the ProgressBar when timer is destroyed
        self.timer.destroyed.connect(lambda: self.wdProgressBar.setValue(0))
        
        self.timer.start(200)        
        
                         
    def countClicks(self):
        self.clicksCount += 1
        self.clicksLabel.setText(f"Counting: {self.clicksCount} clicks")

    def reportProgress(self, n):
        self.stepLabel.setText(f"Long-Running Step: {n}")
    

    def UpdateProgressBar(self):
        """
        Refresh the progress bar to display a "rolling" bar
        """
        
        if not self.wdProgressBar.invertedAppearance() : 
            
            if self.wdProgressBar.value() + 5 < self.wdProgressBar.maximum() : 
                self.wdProgressBar.setValue(self.wdProgressBar.value() + 5)
            else : 
                self.wdProgressBar.setInvertedAppearance(True)
        
        else : 
            
            if self.wdProgressBar.value() - 5 > 0 : 
                self.wdProgressBar.setValue(self.wdProgressBar.value() - 5)
            else : 
                self.wdProgressBar.setInvertedAppearance(False)  
                             
# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    wdFrm.show()

    sys.exit(app.exec_())  
    


   
