'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

def ButtonWasClicked(button):
    print (button)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    window.wdPushButtonGenerate.setCheckable(True)
    window.wdPushButtonGenerate.clicked.connect(ButtonWasClicked)
    ui_file.close()
    window.show()

    sys.exit(app.exec_())
