# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile

"""
Demonstrate how to display a dialog widget created with QtDesigner

Note : Some problems may arise in event management
"""

class HelloWorldDiag(QDialog):
    def __init__(self, parent = None):
        super(HelloWorldDiag, self).__init__(parent)
        
        ui_file_name = "ui/hello_world.ui"
        ui_file = QFile(ui_file_name)
            
        loader = QUiLoader()
        self.wdDiag = loader.load(ui_file,self)
        ui_file.close()

        self.wdDiag.wdButtonHello.clicked.connect(self.SayHello)
        self.wdDiag.show()
        
    def SayHello(self):
        print ("Hello ", self.wdDiag.wdLine.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    diag = HelloWorldDiag()

    sys.exit(app.exec_())