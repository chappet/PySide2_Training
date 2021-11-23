'''
Created on 15 nov. 2019

@author: cchappet

Display QPushButtons with a QVBoxLayout
Show the effect of QSizePolicy

Use QtDesigner to test the different QSizePolicy
Note that QSize is not enabled when the widget is in a layout
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wd = QtWidgets.QWidget()
    
    layout = QtWidgets.QVBoxLayout()
    wd.setLayout(layout)
    
    wdButton_1 = QtWidgets.QPushButton(text = "Open")
    layout.addWidget(wdButton_1)

    wdButton_2 = QtWidgets.QPushButton(text = "Close")
    layout.addWidget(wdButton_2)    
    
    #Uncomment to change Size Policy
    wdButton_2.setMinimumHeight(50)
    wdButton_2.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)

    wd.show()

    sys.exit(app.exec_())