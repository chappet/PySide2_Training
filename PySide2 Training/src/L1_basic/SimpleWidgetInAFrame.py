'''
Created on 15 nov. 2019

@author: cchappet

Display a QPushButton into a QFrame with static position and size (not recommended !)
Show the effect of parent attribut.

'''
import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    wdFrm = QtWidgets.QFrame()
    # wdFrm.resize(400,400) # Redimensionnement GUESS ! Commenter / décommenter

    #create a pushButton inside a QFrame by setting the parent
    wdPushButton = QtWidgets.QPushButton("Please Click !", parent = wdFrm)
    wdPushButton.move(10,10) # Positionnement absolu dans l'écran
    wdPushButton.resize(100,40) # Redimensionnement

    wdFrm.show() # GUESS ! Déplacer le show en ligne 19
 
    #TIPS ---------------------
    #Also try without a parent: 
    #--------------------------
    # wdPushButton = QtWidgets.QPushButton("Please Click !")
    # wdPushButton.show() # GUESS ! Commenter / décommenter

    
    sys.exit(app.exec())
