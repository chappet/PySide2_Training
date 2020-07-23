'''
Created on 7 juil. 2014

@author: cchappet
'''
import os, sys
import collections

from PySide2 import QtCore, QtWidgets, QtGui, QtPrintSupport
from PySide2.QtWidgets import QApplication


class GenericDataInputForm(QtWidgets.QDialog):
    def __init__(self, ordDctData, sTitle='', sTitleGroupBox='Infos', bShowButton = True):
        
        QtWidgets.QDialog.__init__(self) 
        
        self.ordDctData = ordDctData
                
        self.mainVLayout = QtWidgets.QVBoxLayout()

        #Create the button box
        if bShowButton : 
            buttonBox = QtWidgets.QDialogButtonBox(self)
            buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
            buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.accept)
            buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reject)
            
         
        if sTitle == '' : self.setWindowTitle('Data Input Form')
        else :    self.setWindowTitle(sTitle)
        
        GroupBox = QtWidgets.QGroupBox(sTitleGroupBox)
        self.layout = QtWidgets.QFormLayout()
        GroupBox.setLayout(self.layout)
        
        for item in ordDctData.items():
            wdLbl = QtWidgets.QLabel("%s : " % item[0])
            
            if item[1]['Type'] == "QLineEdit" : 
                if 'InitValue' in item[1].keys() : item[1]['widget'] = QtWidgets.QLineEdit(item[1]['InitValue'])
                else: item[1]['widget'] = QtWidgets.QLineEdit('')
                
                if 'Modified' in item[1].keys() and item[1]['Modified'] == False  : 
                    item[1]['widget'].setReadOnly(True)
                if 'State' in item[1].keys() :
                    if item[1]['State'] == "OFF"  : item[1]['widget'].setStyleSheet("QLineEdit { background-color : Red }")
                    else : item[1]['widget'].setStyleSheet("QLineEdit { background-color : Chartreuse }")
            
            elif item[1]['Type'] == "QComboBox" :
                item[1]['widget'] = QtWidgets.QComboBox()
                for sLabel in item[1]['LstLabel']:
                    item[1]['widget'].addItem(str(sLabel))
                
                if 'CurrentValue' in item[1].keys():
                    sValueToSet = str(item[1]['CurrentValue'])
                    if sValueToSet in item[1]['LstLabel']:
                        iIndex = item[1]['widget'].findText(sValueToSet)
                        item[1]['widget'].setCurrentIndex(iIndex)
                    
            elif item[1]['Type'] == "QSpinBox" :
                item[1]['widget'] = QtWidgets.QSpinBox()
                
                if "Max" in item[1].keys() :
                    item[1]['widget'].setMaximum(int(item[1]['Max']))
                if 'Min' in item[1].keys():
                    item[1]['widget'].setMaximum(int(item[1]['Min']))
                
                item[1]['widget'].setValue(int(item[1]['InitValue']))
            

            self.layout.addRow(wdLbl, item[1]['widget']) 

        self.mainVLayout.addWidget(GroupBox)
        if bShowButton : self.mainVLayout.addWidget(buttonBox)
        
        self.setLayout(self.mainVLayout)

    ###################################################################
    #Overwrite accept func to do some action before closing the window
#     def accept(self):
#         print ('Accepted')
#         super().accept()
    ###################################################################
     
                         
    def GetResultModal(self):
        ok = self.exec()  
        print ("Exec return : ",ok)
        
        if ok :
            dctValue = self.GetDictValues()
            return dctValue
        
        else : return None
    
    def GetDictValues(self):
        dctValue = collections.OrderedDict()
        for item in self.ordDctData.items():
        
            if item[1]['Type'] == "QLineEdit" : 
                dctValue[item[0]] = (item[1]['widget'].text())
            
            elif item[1]['Type'] == "QComboBox" :
                dctValue[item[0]] = (item[1]['widget'].currentText())     
            
            elif item[1]['Type'] == "QSpinBox" :      
                dctValue[item[0]] = (item[1]['widget'].value())  
            
        
        return dctValue


# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    ordDctData = collections.OrderedDict()
    ordDctData['Position (float)'] = {'Type' : "QLineEdit", 'InitValue' : "10.0"}
    ordDctData['Direction'] = {'Type' : "QComboBox", 'LstLabel' : ['Horizontal', 'Vertical'], 'CurrentValue' : 'Vertical'}
    ordDctData['Color'] = {'Type' : "QComboBox", 'LstLabel' : ['Red', 'Blue', 'Green'], 'CurrentValue':'Blue'}
    
    wd = GenericDataInputForm(ordDctData, 'Marker Definition')
    dctData = wd.GetResultModal() 
    print(dctData)
     
    
