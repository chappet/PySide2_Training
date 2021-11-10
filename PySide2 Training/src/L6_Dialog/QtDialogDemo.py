'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui, QtPrintSupport
from PySide2.QtWidgets import QApplication

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

#   ############# MESSAGE BOX ###########################
#     #Critical information
    wd = QtWidgets.QMessageBox.critical(None,"Erreur Critique","Echec de l'installation de l'application StopCovid\nMerci de désactiver votre anti-virus")
 
    #Question
    reply = QtWidgets.QMessageBox.question(None,"Interruption","Voulez-vous continuer ?")
    print (reply == QtWidgets.QDialogButtonBox.Yes)
 
#     #Specify buttons
#     #https://doc.qt.io/qt-5/qmessagebox.html#StandardButton-enum
    wd = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Question,"Sauvegarde","Le fichier a été modifié, voulez-vous le sauvegarder ?",buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Discard)
    reply = wd.exec()
    print (reply)

#     #User Defined Button
#     #https://doc.qt.io/qt-5/qmessagebox.html#ButtonRole-enum
    wd = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Question,"Sauvegarde","Le fichier a été modifié, voulez-vous le sauvegarder ?")
    wd.addButton("Oui", QtWidgets.QMessageBox.YesRole) 
    wd.addButton("Non", QtWidgets.QMessageBox.NoRole)
    wd.addButton("Annuler", QtWidgets.QMessageBox.RejectRole)
    reply = wd.exec()
    print (reply)

    #Using a translator
    #Open qt_fr.qm with linguist
    translatorQt = QtCore.QTranslator()
    translatorQt.load('./qt_fr.qm')
    app.installTranslator(translatorQt)

    wd = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Question,"Sauvegarde","Le fichier a été modifié, voulez-vous le sauvegarder ?",buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Discard)
    wd.button(wd.Yes).setText(QApplication.translate("QDialogButtonBox",'&Yes'))
    wd.button(wd.No).setText(QApplication.translate("QDialogButtonBox",'&No'))
    wd.button(wd.Discard).setText(QApplication.translate("QDialogButtonBox",'Discard'))
    reply = wd.exec()
    print (reply)

#  
#     ############# COLOR EDITOR ###########################
    wd = QtWidgets.QColorDialog()
    wd.exec()
    print (wd.currentColor())
     
    #two ways to do the same thing ...
    color = QtWidgets.QColorDialog().getColor()
    print (color)
    
    ########### FILE SELECTOR ###########################################
    wd = QtWidgets.QFileDialog()
    wd.exec()
    print (wd.selectedFiles())

    ########### PRINTER SELECTOR ###########################################
    dialog = QtPrintSupport.QPrintDialog()
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        print (dialog.printer())

