'''
Created on 7 juil. 2014

@author: cchappet

Animate a progress bar
BAD EXEMPLE : never create a Widget in a Thread, it is NOT SAFE

'''
import os, sys,time
import collections

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication


class AnimeProgressBar(QtCore.QThread, QtCore.QObject):
    """
    A QThread that creates and update a QProgressBar
    """
    
    def __init__(self,iDelay):
        super(AnimeProgressBar, self).__init__()
        self.iDelay = iDelay
        
        self.wdProgress = QtWidgets.QProgressBar()
        self.wdProgress.show()

    def run(self):
        time0 = time.time()
        
        while time.time() - time0 < self.iDelay : 
            timeElapse = time.time() - time0
            self.wdProgress.setValue(timeElapse * 100 / self.iDelay)
        
        self.wdProgress.deleteLater()
    
class MyFrame(QtWidgets.QFrame):
    """
    The test dashboard
    """
    def __init__(self, parent):
        self.parent = parent
        
        super(MyFrame, self).__init__()
        wdLayout = QtWidgets.QGridLayout()
        self.setLayout(wdLayout)
        
        self.wdShowProgessBar = QtWidgets.QPushButton("Show Progress Bar", parent = self)
        self.wdShowProgessBar.clicked.connect(self.ShowProgressBar)
        wdLayout.addWidget(self.wdShowProgessBar,2,0,1,2)

    def ShowProgressBar(self):
        self.tProgressBar = AnimeProgressBar(iDelay = 10)

        self.tProgressBar.start()

    
# --------------------------------------------------------------------
# Programme de test
# --------------------------------------------------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    wdFrm = MyFrame(app)
    wdFrm.show()

    sys.exit(app.exec_())   
