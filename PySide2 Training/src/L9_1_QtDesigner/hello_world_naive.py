# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile

"""
Demonstrate how to display a dialog widget created with QtDesigner
BAD solution ! 
Better create a QDialog and load the ui into it.
"""
def Test():
    print ("TEST")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wdDiag = QUiLoader().load("ui/hello_world.ui")

    def SayHello(self):
        print ("Hello ", wdDiag.wdLine.text())

    wdDiag.wdButtonHello.clicked.connect(SayHello)

    wdDiag.show()

    sys.exit(app.exec_())