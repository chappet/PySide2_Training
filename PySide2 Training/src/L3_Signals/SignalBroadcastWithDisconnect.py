'''
Created on 9 janv. 2020

@author: cchappet

This module demonstrates an application signal broadcast
a disconnection is needed to avoid signal re-entrance

Use case : set the same unit on several display in one clic
'''
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Signal, Slot 

import sys
import numpy

class MyDisplay(QtWidgets.QWidget):
    """
    A composite widget that display a number in seconds or milliseconds
    change the unit on one display will change the unit on the others existing displays.
    """
    def __init__(self,parent = None):
        super().__init__()
        
        self.parent = parent
        layout = QtWidgets.QVBoxLayout(self)
        
        self.wdCombo = QtWidgets.QComboBox()
        self.wdCombo.addItem("s")
        self.wdCombo.addItem("ms")
        layout.addWidget(self.wdCombo)

        self.wdLineEdit = QtWidgets.QLineEdit(str(1 + int(numpy.random.random() * 10)))
        layout.addWidget(self.wdLineEdit)
        self.show()
        
        """ Signals connection 
        Two signals needed :
        - The first signal changes the unit on the focused/activated widget
        - The second signal tells the other displays to change their unit 
        """
        self.wdCombo.currentTextChanged.connect(self.ChangeUnit)
        self.parent.connect(QtCore.SIGNAL("SEND_UNIT(QString)"),self.ChangeUnit)
 

    def ChangeUnit(self, sText):
        #who send the signal ?
        sender = self.sender()
        print ("Signal received from {}".format(type(sender)))

        #avoid signal re-entrance when text will change on the combo
        self.wdCombo.currentTextChanged.disconnect(self.ChangeUnit)
        
        if id(sender) == id(self.wdCombo) :
            
            #we are in the widget modified directly by the user
            print ("{} ---> emit Signal with {}".format(id(self), sText))
            
            #avoid signal re-entrance when signal will be emitted again
            self.parent.disconnect(QtCore.SIGNAL("SEND_UNIT(QString)"),self.ChangeUnit)
            self.parent.emit(QtCore.SIGNAL("SEND_UNIT(QString)"),sText)  
            #re-connect the signal for next emission          
            self.parent.connect(QtCore.SIGNAL("SEND_UNIT(QString)"),self.ChangeUnit)         
        else:
            #we are in a widget NOT changed by the user
            print ("{} ---> set text {}".format(id(self),sText))
            self.wdCombo.setCurrentText(sText)

        #change the value according to the unit               
        if sText == "ms" : self.wdLineEdit.setText(str(float(self.wdLineEdit.text()) / 1000.))
        else : self.wdLineEdit.setText(str(float(self.wdLineEdit.text()) * 1000.))

        #re-connect the signal for next user interaction 
        self.wdCombo.currentTextChanged.connect(self.ChangeUnit)                 
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    lstWd = []
    for i in range(2):
        lstWd.append(MyDisplay(app))
    
    sys.exit(app.exec_())