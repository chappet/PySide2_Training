'''
Created on 12 mars 2020

@author: cchappet

This module demonstrates an input dialog with controlled inputs (mask & validator)
'''

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot 
import PySide2.QtMultimedia as QtMultimedia

import sys

class QDoubleValidator(QtWidgets.QLineEdit):
    """
    Subclass of QLineEdit with QDoubleValidator
    """
    def __init__(self, fMin, fMax, iDec=6):
        super().__init__()
        self.wdLineValidator = QtGui.QDoubleValidator(fMin, fMax, iDec)
        self.setValidator(self.wdLineValidator)

                            
class QIntValidator(QtWidgets.QLineEdit):
    """
    Subclass of QLineEdit with QIntValidator
    """
    def __init__(self, iMin, iMax):
        super().__init__()
        self.wdLineValidator = QtGui.QIntValidator(iMin, iMax)
        self.setValidator(self.wdLineValidator)     
       

class MyInputFrame(QtWidgets.QDialog):  
    """
    This dialog enable the input of different kinds of data with controle
    """  
    def __init__(self):
        super().__init__()
        self.lstFctCheck = []
        
        # Color informations to show the inputs validities
        self.redPalette = QtGui.QPalette()
        self.redPalette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)   
         
        self.blackPalette = QtGui.QPalette()
        self.blackPalette.setColor(QtGui.QPalette.Text, QtCore.Qt.black) 
            
        # form declaration
        layout = QtWidgets.QFormLayout(self)
    
    
        # Declare three widget for inputs
        wd = QDoubleValidator(-10., 20., 6)
        layout.addRow("Double between -10 and +20", wd)
        self.AddLineEditWidget(wd)
    
        wd = QIntValidator(-4, 2)
        layout.addRow("int between -4 and 2", wd)
        self.AddLineEditWidget(wd)
    
        wd = QtWidgets.QLineEdit()
        wd.setInputMask("999.999.999.999;_")
        layout.addRow("Ip Adress", wd)
        self.AddLineEditWidget(wd)

        # The OK button will be disabled until all input are valid   
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout.addWidget(self.buttonBox)

    def GetData(self):
        """
        return valid inputs
        """
        lstData = []
        for wd, fctCheck in self.lstFctCheck:
            lstData.append(wd.text())
        
        return lstData

    def AddLineEditWidget(self, wd):
        """
        PRIVATE
        add widget to check process
        """
        self.lstFctCheck.append((wd, wd.hasAcceptableInput))
        wd.textChanged.connect(self.CheckInputs)            
 
    def CheckInputs(self):
        """
        PRIVATE
        Check that all inputs are valid
        Called whenever an input changes
        """
        bOk = True
        for wd, fctCheck in self.lstFctCheck:
            print (fctCheck())
            if fctCheck() == False : 
                self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
                wd.setPalette(self.redPalette)
                bOk = False
            else:
                wd.setPalette(self.blackPalette)
        
        if bOk : self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
        

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    wdFrm = MyInputFrame()
    ok = wdFrm.exec()
    if ok : print (wdFrm.GetData())

