'''
Created on 7 juil. 2014

@author: cchappet
'''
import sys

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication


class MyFrame(QtWidgets.QFrame):
    def __init__(self):
        super(MyFrame, self).__init__()
                
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)

        self.wdPushButton = QtWidgets.QPushButton(self.tr("Push"), parent = self)
        wdLayout.addWidget(self.wdPushButton,1,0)

        buttonBox = QtWidgets.QDialogButtonBox(self)
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        
        buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText(buttonBox.tr("Cancel"))
        wdLayout.addWidget(buttonBox)
        

      
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    translatorAppli = QtCore.QTranslator()
    translatorAppli.load('ModalDialog_fr.qm')

    translatorQt = QtCore.QTranslator()
    translatorQt.load('qt_fr.qm')
        
    app.installTranslator(translatorAppli)
    app.installTranslator(translatorQt)

    wdFrm = MyFrame()
    wdFrm.show()

    sys.exit(app.exec_())   
