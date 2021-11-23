'''
Created on 7 juil. 2014

@author: cchappet

Show the differences between modal and non modal Dialogs / Widgets
'''
import os, sys,time
import collections

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from  GenericDataInputForm import GenericDataInputForm

DELAY = 15

class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent
        
        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)
        

        self.wdInfoModalButton = QtWidgets.QPushButton("GET INFOS MODAL", parent = self)
        self.wdInfoModalButton.clicked.connect(self.GetResultModal)
        wdLayout.addWidget(self.wdInfoModalButton,0,0,1,2)
        
        self.wdShowInfosDialogButton = QtWidgets.QPushButton("Show Infos Dialog", parent = self)
        self.wdShowInfosDialogButton.clicked.connect(self.ShowInfosDiag)
        wdLayout.addWidget(self.wdShowInfosDialogButton,1,0)

        self.wdReadInfosButton = QtWidgets.QPushButton("Read Infos", parent = self)
        self.wdReadInfosButton.clicked.connect(self.ReadInfosDiag)
        wdLayout.addWidget(self.wdReadInfosButton,1,1)

        self.wdShowProgessBar = QtWidgets.QPushButton("Show Progress Bar", parent = self)
        self.wdShowProgessBar.clicked.connect(self.ShowProgressBar)
        wdLayout.addWidget(self.wdShowProgessBar,2,0,1,2)

        self.wdShowProgessIndic = QtWidgets.QPushButton("Show Progress Indicator", parent = self)
        self.wdShowProgessIndic.clicked.connect(self.ShowProgressIndic)
        wdLayout.addWidget(self.wdShowProgessIndic,3,0,1,2)
        
        

        ###############################################################################################
        #NON MODAL INFOS DIALOG DEFINITION
        ordDctData = collections.OrderedDict()
        ordDctData['Pressure (bar'] = {'Type' : "QLineEdit", 'InitValue' : "1.0"}
        ordDctData['unit'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        
        self.wdDiagInfoNonModal = GenericDataInputForm(ordDctData, "User Info", bShowButton = False)

    def GetResultModal(self):
        ordDctData = collections.OrderedDict()
        ordDctData['Pressure (bar'] = {'Type' : "QLineEdit", 'InitValue' : "1.0"}
        ordDctData['unit'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit1'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit2'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit3'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit4'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit5'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit6'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit7'] = {'Type' : "QComboBox", 'LstLabel' : ['atm', 'psi'], 'CurrentValue':'Blue'}
        ordDctData['unit8'] = {'Type' : "QSpinBox", 'InitValue': 5, 'Min' : 0., 'Max' : 10}
        
        wdDiagInfo = GenericDataInputForm(ordDctData, "User Info")
        dctInfos = wdDiagInfo.GetResultModal()
        print (dctInfos)

    def ShowInfosDiag(self):
        self.wdDiagInfoNonModal.show()

    def ReadInfosDiag(self):
        print (self.wdDiagInfoNonModal.GetDictValues())

    def ShowProgressBar(self):
        time0 = time.time()
        
        #Three types of modality
        wdProgress = QtWidgets.QProgressBar()
        wdProgress.setWindowModality(QtCore.Qt.NonModal)
#         wdProgress.setWindowModality(QtCore.Qt.WindowModal)
#         wdProgress.setWindowModality(QtCore.Qt.ApplicationModal)

        wdProgress.show()

        while time.time() - time0 < DELAY : 
            timeElapse = time.time() - time0
            self.parent.processEvents() #comment line to show GUI freeze
            wdProgress.setValue(timeElapse * 100 / DELAY)

    def ShowProgressIndic(self):
        time0 = time.time()
        
        wdMyProgress = MyProgressIndic()
        wdMyProgress.setModal(True)
        wdMyProgress.show()
        
        while time.time() - time0 < DELAY : 
            timeElapse = time.time() - time0
            self.parent.processEvents()
            wdMyProgress.setText(str(round(timeElapse,2)))
            
        
class MyProgressIndic(QtWidgets.QDialog):
    """
    A QDialog that displays a string in a QLabel
    """
    def __init__(self):
        
        super(MyProgressIndic, self).__init__()
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)
        
        self.wdLabel = QtWidgets.QLabel()
        
        wdLayout.addWidget(self.wdLabel)

    def setText(self,sValue):
        self.wdLabel.setText(sValue)        
    
# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    wdFrm.show()

    sys.exit(app.exec_())   
