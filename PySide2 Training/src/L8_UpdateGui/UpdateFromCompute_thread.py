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

class ComputeThread(QtCore.QThread, QtCore.QObject):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print('init')
        
        #emit a custom signal to send the name of the step
        self.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'init') 
        QApplication.instance().emit(QtCore.SIGNAL("PROGRESS(int)"),10)       
        time.sleep(3)
        
        print('step1')
        self.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'step1')
        QApplication.instance().emit(QtCore.SIGNAL("PROGRESS(int)"),20)       

        self.sleep(3)

        print('step2')
        self.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'step2')
        QApplication.instance().emit(QtCore.SIGNAL("PROGRESS(int)"),60)       

        self.sleep(3)
        
        print('finish')
        self.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'finish')
        QApplication.instance().emit(QtCore.SIGNAL("PROGRESS(int)"),100)       


"""
Create the demo windows
"""        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    computeThread = ComputeThread()
    
    #Create the demo container
    wdFrm = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(wdFrm)

    #A line edit to display computation step
    wdLineEdit = QtWidgets.QLineEdit("No computation running")
    layout.addWidget(wdLineEdit)
    
    wdProgress = QtWidgets.QProgressBar()
    layout.addWidget(wdProgress)
    app.connect(QtCore.SIGNAL("PROGRESS(int)"),wdProgress.setValue)
    
    
    #connect to the custom signal to print the step in the QLineEdit
    computeThread.connect(QtCore.SIGNAL("SEND_MESSAGE(QString)"),wdLineEdit.setText)

    #Create a button to launch the computation
    wdButtonCompute = QtWidgets.QPushButton("Compute")
    layout.addWidget(wdButtonCompute)
    wdButtonCompute.clicked.connect(computeThread.start)

    wdFrm.show()
    
    sys.exit(app.exec_())