'''
Created on 15 nov. 2019

@author: cchappet

Display a QPushButton into a QFrame with static position and size (not recommended !)
Show the effect of parent attribut.

'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdFrm = QtWidgets.QFrame()
    
    #Set attributs
    wdFrm.setFrameShadow(QtWidgets.QFrame.Plain)
    wdFrm.setFrameShape(QtWidgets.QFrame.Box)
    wdFrm.setLineWidth(5)    
    
    wdPushButton = QtWidgets.QPushButton("Please Click !", parent = wdFrm)
    wdPushButton.move(10,10)
    wdPushButton.resize(100,40)
    
    #TIPS ---------------------
    #Also try without a parent: 
    #--------------------------
#     wdPushButton = QtWidgets.QPushButton("Please Click !")
        
    wdFrm.show()

    sys.exit(app.exec_())
