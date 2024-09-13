'''
Created on 15 nov. 2019

@author: cchappet

Display a simple QFrame and set some properties
'''
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QFrame
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdFrm = QtWidgets.QFrame() # Nommer la variable clairement :-)
    
    # Modification des propriétés de la widget (cf. https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFrame.html#PySide6.QtWidgets.QFrame)
    wdFrm.setFrameShadow(QtWidgets.QFrame.Raised)
    
    wdFrm.setFrameShape(QtWidgets.QFrame.Box)
    
    wdFrm.setLineWidth(15)
    print(wdFrm.lineWidth()) # Lire la valeur de la propriété
    
    wdFrm.setToolTip("Bonjour") # EXPLAIN : Pourquoi ne trouve t'on pas setToolTip sur la page QFrame ?
    
    wdFrm.show()

    sys.exit(app.exec())
