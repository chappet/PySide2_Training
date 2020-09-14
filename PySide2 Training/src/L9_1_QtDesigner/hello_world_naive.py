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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "ui/hello_world.ui"
    ui_file = QFile(ui_file_name)
        
    loader = QUiLoader()
    wdDiag = loader.load(ui_file)
    ui_file.close()

    def SayHello(self):
        print ("Hello ", wdDiag.wdLine.text())

    wdDiag.wdButtonHello.clicked.connect(SayHello)

    wdDiag.show()

    sys.exit(app.exec_())