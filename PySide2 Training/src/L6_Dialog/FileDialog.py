'''
Created on 15 nov. 2019

@author: cchappet
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

import sys

def GetOpenFiles():
    lstFiles = QtWidgets.QFileDialog().getOpenFileNames(filter = '*.doc')
    print (lstFiles)

def GetSaveFiles():
    lstFiles = QtWidgets.QFileDialog().getSaveFileName()
    print (lstFiles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    layout = QtWidgets.QVBoxLayout()
    
    window = QtWidgets.QMainWindow()

    
    wdCentralFrame = QtWidgets.QFrame()
    
    wdCmdOpenFile = QtWidgets.QPushButton("Get Multiple File to Open")
    wdCmdOpenFile.clicked.connect(GetOpenFiles)
    
    wdCentralFrame.setLayout(layout)
    layout.addWidget(wdCmdOpenFile)
    
    window.setCentralWidget(wdCentralFrame)

    menubar = QtWidgets.QMenuBar(window)
#     menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
    menubar.setObjectName("menubar")
    menuFile = QtWidgets.QMenu(menubar)
    menuFile.setObjectName("menuFile")
    window.setMenuBar(menubar)
    actionOpen = QtWidgets.QAction(window)
    actionOpen.setObjectName("actionOpen")
    actionSave = QtWidgets.QAction(window)
    actionSave.setObjectName("actionSave")
    menuFile.addAction(actionOpen)
    menuFile.addAction(actionSave)
    menubar.addAction(menuFile.menuAction())    
    
    menuFile.setTitle('File')
    actionOpen.setText("Open")
    actionOpen.triggered.connect(GetOpenFiles)
    
    actionSave.setText("Save")
    actionSave.triggered.connect(GetSaveFiles)
    
    
    window.show()

    sys.exit(app.exec_())
