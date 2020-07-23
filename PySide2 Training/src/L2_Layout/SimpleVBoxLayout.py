'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wd = QtWidgets.QWidget()
    
    layout = QtWidgets.QVBoxLayout()
    wd.setLayout(layout)
    
    wdButton = QtWidgets.QPushButton(text = "Open")
    layout.addWidget(wdButton)

    wdButton = QtWidgets.QPushButton(text = "Close")
    layout.addWidget(wdButton)    
    
    wd.show()

    sys.exit(app.exec_())