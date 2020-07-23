'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui, QtPrintSupport
from PySide2.QtWidgets import QApplication

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wd = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical,"Erreur Critique","Echec de l'installation de l'application StopCovid\nMerci de désactiver votre anti-virus",buttons = QtWidgets.QMessageBox.StandardButtons(QtWidgets.QDialogButtonBox.Ok))
    reply = wd.exec()
    print (reply == QtWidgets.QDialogButtonBox.Yes)
 
    ############# COLOR EDITOR ###########################
    wd = QtWidgets.QColorDialog()
    wd.exec()
    print (wd.currentColor())
    
    #two ways to do the same thing ...
    color = QtWidgets.QColorDialog().getColor()
    print (color)
    ######################################################
     
    wd = QtWidgets.QFileDialog()
    wd.exec()
    print (wd.selectedFiles())

    dialog = QtPrintSupport.QPrintDialog()
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        print (dialog.printer())

