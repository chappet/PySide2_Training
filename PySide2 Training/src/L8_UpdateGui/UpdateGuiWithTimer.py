'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates a way to update a widget created in the main thread from a Qt Timer
It actually works because Qt Timer are not threads !
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wdFrm = QtWidgets.QFrame()
    layout = QtWidgets.QVBoxLayout()
    wdFrm.setLayout(layout)
    
    #Create two labels that will display a counter
    wdCounter = QtWidgets.QLineEdit("0")
    layout.addWidget(wdCounter)

    #Create a function for widget updating
    def UpdateCounter():
        wdCounter.setText(str(int(wdCounter.text()) + 1))

    #Start a Qt Timer         
    timer = QtCore.QTimer()
    timer.start(10.)
    QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"),UpdateCounter)


    wdFrm.show()
    sys.exit(app.exec_())