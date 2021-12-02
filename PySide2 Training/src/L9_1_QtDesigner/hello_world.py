# File: main.py
import sys

from PySide2.QtUiTools import QUiLoader


from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile

"""
Demonstrate how to display a dialog widget created with QtDesigner
using QUiLoader().load

Warning : problem with closeEvent management
"""

class HelloWorldDiag(QDialog):
    def __init__(self, parent = None):
        super(HelloWorldDiag, self).__init__(parent)
        
        self.wdDiag = QUiLoader().load("ui/hello_world.ui")

        #Connect the button clicked signal
        self.wdDiag.wdButtonHello.clicked.connect(self.SayHello)

        #Connect the line returnPressed
        self.wdDiag.wdLine.returnPressed.connect(self.SayHello)

        #Connect the line textChanged
        self.wdDiag.wdLine.textChanged.connect(self.DisplayText)

        self.wdDiag.show()
        

            
    def SayHello(self):
        print ("Hello ", self.wdDiag.wdLine.text())

    def DisplayText(self,sText):
        print (sText)
    
    # WARNING
    # HelloWorldDiag will never receive closeEvent
    # The dialog is not shown, it just contains the hello_word wwidget
    def closeEvent(self,event):
        print("CloseEvent")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    diag = HelloWorldDiag()

    sys.exit(app.exec_())