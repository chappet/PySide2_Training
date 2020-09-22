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
if __name__ == "__main__":
    app = QApplication(sys.argv)

    def Compute():
        print('init')
        
        #emit a custom signal to send the name of the step
        app.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'init')        
        time.sleep(3)

        print('step1')
        app.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'step1')        
        time.sleep(3)
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #Texts are not updated in GUI unless processEvents is called 
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print('step2')
        app.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'step2')
        for i in range(1000000):
            app.processEvents() #let the main loop process gui events.
        
        print('finish')
        app.emit(QtCore.SIGNAL("SEND_MESSAGE(QString)"),'finish')
    
    
    #Create the demo container
    wdFrm = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(wdFrm)

    #A line edit to display computation step
    wdLineEdit = QtWidgets.QLineEdit("No computation running")
    layout.addWidget(wdLineEdit)
    
    #connect to the custom signal to print the step in the QLineEdit
    app.connect(QtCore.SIGNAL("SEND_MESSAGE(QString)"),wdLineEdit.setText)

    #Create a button to launch the computation
    wdButtonCompute = QtWidgets.QPushButton("Compute")
    layout.addWidget(wdButtonCompute)
    wdButtonCompute.clicked.connect(Compute)

    wdFrm.show()
    
    sys.exit(app.exec_())