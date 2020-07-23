'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdFrm = QtWidgets.QFrame()
    wdFrm.setFrameShadow(QtWidgets.QFrame.Raised)
    wdFrm.setFrameShape(QtWidgets.QFrame.Box)
    wdFrm.setLineWidth(5)
    
    wdFrm.show()

    sys.exit(app.exec_())
