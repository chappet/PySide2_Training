'''
Created on 9 janv. 2020

@author: cchappet
!!! NOT TO BE REPRODUCE !!!
This module demonstrates the use of a user defined custom signal
Use case : display information about the computation steps

Demonstrate the use of app.processEvents()
Using a thread is far better !
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot , QObject

import sys
import threading
import time

"""
Create the demo windows
"""        
class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent

        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QVBoxLayout()
        self.setLayout(wdLayout)
        
        self.longRunningBtn = QtWidgets.QPushButton("Run Computation")
        wdLayout.addWidget(self.longRunningBtn)
        self.longRunningBtn.clicked.connect(self.Compute)

        #A line edit to display computation step
        self.wdLineEdit = QtWidgets.QLineEdit("No computation running")
        wdLayout.addWidget(self.wdLineEdit)
        

    def Compute(self):
        print('init')
        
        #Try to display a message
        self.wdLineEdit.setText('init')        
        time.sleep(3)

        #Try to display a message
        print('step1')
        self.wdLineEdit.setText('step1')        
        time.sleep(3)
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #Texts are not updated in GUI unless processEvents is called 
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print('step2')
        self.wdLineEdit.setText('step2')
        for i in range(1000000):
            app.processEvents() #let the main loop process gui events.
        
        print('finish')
        self.wdLineEdit.setText('finish')
    
    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    
    wdFrm.show()
    
    sys.exit(app.exec_())