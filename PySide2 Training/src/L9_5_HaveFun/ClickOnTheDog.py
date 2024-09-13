'''
Created on 12 mars 2020

@author: cchappet
'''
import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication
import PySide6.QtMultimedia as QtMultimedia

import sys

class MySoundPlayer(QtMultimedia.QMediaPlayer):
    """
    A custom sound player
    """
    def __init__(self):
        super().__init__()
        # self.setVolume(100)
    
    def SetAndPlay(self, url):
        self.setMedia(QtCore.QUrl.fromLocalFile(url))
        self.play()
    
class SoundBoard(QtWidgets.QFrame):
    """
    A custom QFrame that play sounds...
    """
    def __init__(self):
        super().__init__()

        self.player = MySoundPlayer()
        
        dctButton = {
            'cow' : {'pos' : (0,0),'icon':'../ressources/cow.jpg','sound' : "../ressources/crazycow.mp3"},
            'dog' : {'pos' : (1,0),'icon':'../ressources/dog.jpg','sound' : "../ressources/You know what.mp3"},
            'bipbip' : {'pos' : (0,1),'icon':'../ressources/bipbip.jpg','sound' : "../ressources/bipbip.mp3"},
            'coq' : {'pos' : (1,1),'icon':'../ressources/coq.jpg','sound' : "../ressources/kikiriki.mp3"}
        }
        
        #the mapper simplifies the association between buttons and sound files
        self.mapper = QtCore.QSignalMapper()
        
        layout = QtWidgets.QGridLayout(self)
        
        for item in dctButton.values():
            #Create the button and set an icon
            wd = QtWidgets.QPushButton()
            wd.setIcon(QtGui.QIcon(item['icon']))
            wd.setIconSize(QtCore.QSize(65, 65)) 
            layout.addWidget(wd,item['pos'][0],item['pos'][1])     
            
            #map the sound file and the button in the mapper
            self.mapper.setMapping(wd, item['sound'])
            wd.clicked.connect(self.mapper.map)

        QtCore.QObject.connect(self.mapper,QtCore.SIGNAL('mapped(QString)'),self.PlaySound)

    def PlaySound(self, url):
        self.player.SetAndPlay(url)
        
            
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
 
    wd = SoundBoard()
    wd.show()
      
    sys.exit(app.exec_())