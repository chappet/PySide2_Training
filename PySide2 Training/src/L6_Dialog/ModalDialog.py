'''
Created on 7 juil. 2014

@author: cchappet
'''
import os, sys
import collections

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from  GenericDataInputForm import GenericDataInputForm


class MyFrame(QtWidgets.QFrame):
    def __init__(self):
        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)
        
        self.wdInfoModalButton = QtWidgets.QPushButton("GET INFOS MODAL", parent = self)
        self.wdInfoModalButton.clicked.connect(self.GetResultModal)
        wdLayout.addWidget(self.wdInfoModalButton,0,0)

        self.wdShowInfosDialogButton = QtWidgets.QPushButton("Show Infos Dialog", parent = self)
        self.wdShowInfosDialogButton.clicked.connect(self.ShowInfosDiag)
        wdLayout.addWidget(self.wdShowInfosDialogButton,1,0)

        self.wdReadInfosButton = QtWidgets.QPushButton("Read Infos", parent = self)
        self.wdReadInfosButton.clicked.connect(self.ReadInfosDiag)
        wdLayout.addWidget(self.wdReadInfosButton,1,1)

        ###############################################################################################
        #NON MODAL INFOS DIALOG DEFINITION
        ordDctData = collections.OrderedDict()
        ordDctData['Position (float)'] = {'Type' : "QLineEdit", 'InitValue' : "10.0"}
        ordDctData['Direction'] = {'Type' : "QComboBox", 'LstLabel' : ['Horizontal', 'Vertical'], 'CurrentValue' : 'Vertical'}
        ordDctData['Color'] = {'Type' : "QComboBox", 'LstLabel' : ['Red', 'Blue', 'Green'], 'CurrentValue':'Blue'}
        
        self.wdDiagInfoNonModal = GenericDataInputForm(ordDctData, "User Info", bShowButton = False)

    def GetResultModal(self):
        ordDctData = collections.OrderedDict()
        ordDctData['Position (float)'] = {'Type' : "QLineEdit", 'InitValue' : "10.0"}
        ordDctData['Direction'] = {'Type' : "QComboBox", 'LstLabel' : ['Horizontal', 'Vertical'], 'CurrentValue' : 'Vertical'}
        ordDctData['Color'] = {'Type' : "QComboBox", 'LstLabel' : ['Red', 'Blue', 'Green'], 'CurrentValue':'Blue'}
        
        wdDiagInfo = GenericDataInputForm(ordDctData, "User Info")
        dctInfos = wdDiagInfo.GetResultModal()
        print (dctInfos)

    def ShowInfosDiag(self):
        self.wdDiagInfoNonModal.show()

    def ReadInfosDiag(self):
        print (self.wdDiagInfoNonModal.GetDictValues())

        
    
# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    wdFrm = MyFrame()
    wdFrm.show()

    sys.exit(app.exec_())   
