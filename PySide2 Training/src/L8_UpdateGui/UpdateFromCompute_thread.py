'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates the use of a user defined custom signal
Use case : display information about the computation steps

'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import threading
import time

class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent

        super(MyFrame, self).__init__()
        
        #Create a Thread for computing
        self.computeThread = ComputeThread()
        
        wdLayout = QtWidgets.QVBoxLayout()
        self.setLayout(wdLayout)

        #A line edit to display computation step
        self.wdLineEdit = QtWidgets.QLineEdit("No computation running")
        wdLayout.addWidget(self.wdLineEdit)
        #connect to the custom signal to print the step in the QLineEdit
        self.computeThread.stepSignal.connect(self.wdLineEdit.setText)
        
        self.longRunningBtn = QtWidgets.QPushButton("Run Computation")
        wdLayout.addWidget(self.longRunningBtn)
        self.longRunningBtn.clicked.connect(self.computeThread.start)
       


class ComputeThread(QtCore.QThread, QtCore.QObject):
    
    stepSignal = Signal(str)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        print('Start Running')
        
        #emit a custom signal to send the name of the step
        print('init')
        self.stepSignal.emit('init')    
        time.sleep(3)
        
        print('step1')
        self.stepSignal.emit('step1')
        self.sleep(3)

        print('step2')
        self.stepSignal.emit('step2')
        self.sleep(3)
        
        print('finish')
        self.stepSignal.emit('finish')

"""
Create the demo windows
"""        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    wdFrm.show()
    
    sys.exit(app.exec_())