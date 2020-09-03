'''
Created on 15 nov. 2019

@author: cchappet

Display various widget in a QGridLayout
Show the effect of stretch and pan
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wd = QtWidgets.QWidget()
    
    layout = QtWidgets.QGridLayout()
    wd.setLayout(layout)
    layout.setColumnStretch(0,1)
    layout.setColumnStretch(1,2)

    
    #Create Push buttons
    wdButton_1 = QtWidgets.QPushButton(text = "Button 1")
    wdButton_2 = QtWidgets.QPushButton(text = "Button 2")
    wdButton_3 = QtWidgets.QPushButton(text = "Button 3")
    
    #Create Line Edit
    wdLineEdit_1 = QtWidgets.QLineEdit()
    wdLineEdit_1.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)

    wdLineEdit_2 = QtWidgets.QLineEdit()
    wdLineEdit_3 = QtWidgets.QLineEdit()
    
    #Create action buttons
    wdAction_1 = QtWidgets.QRadioButton("Action 1")
    wdAction_2 = QtWidgets.QRadioButton("Action 2")
    
    #Add widgets to layout
    # widget,row, col, rowspan, colspan
    layout.addWidget(wdLineEdit_1,0,0,1,2)
    layout.addWidget(wdButton_1,0,2,1,1)
    
    layout.addWidget(wdLineEdit_2,1,0,1,1)
    layout.addWidget(wdLineEdit_3,1,1,1,1)
    layout.addWidget(wdButton_2,1,2,2,1)

    layout.addWidget(wdAction_1,2,0,1,1)
    layout.addWidget(wdAction_2,2,1,1,1)
        
    layout.addWidget(wdButton_3,3,0,1,3)
    


    

  
    
    wd.show()

    sys.exit(app.exec_())
    
