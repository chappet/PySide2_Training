# -*- coding: cp1252 -*-

'''
Created on 26 nov. 2009

@author: christophe
'''
import sys
import string
import logging
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QWidget

class QtMenu(QtWidgets.QMenu):
    '''
    Generateur de menu contextuel Qt
    '''

    def __init__(self,parent=None,szTitle = None,bAutoConnectFct = True):
        '''
        Constructor

        IN : 
            szTitle : Titre du Menu (imperatif si le menu doit etre ajoute dans une MenuBar !)
            bAutoConnectFct(True) : la fonction associée à une entree de menu est appelée automatiquement lorsque l'item est choisi
                                    Si False, l'affichage du menu n'est pas geré par la fonction ShowMenu (cas de l'utilisation avec QtGMTTreeWidget pour récupérer les noeuds sélectionnés).
                                    
                                
        
        '''
        
        self.dictLabel = {}
        self.bAutoConnectFct = bAutoConnectFct
        QtWidgets.QMenu.__init__(self,parent)
        if szTitle != None : self.setTitle(szTitle)
        self.setAttribute(QtCore.Qt.WA_AlwaysShowToolTips,True)
        self.bMenuTriggered = False

    def AddEntryFromPath(self,szMenuPath,fct=None,data=None,bAutoConnectFct = True,bEnable = True,bCheckable = False,bNeedSelectedItems = True, sToolTip = None):
        """ 
        Creation d'une entrée du menu spécifiée par une 
        chaine de caractère de type : 'Menu1.Menu2.Menu3'
        
        IN : 
            szMenuPath : chaine de caractère de type : 'Menu1.Menu2.Menu3'
        
            fct(None) : fonction associée a l'item de menu
            data(None) : variable passee en argument à la fct associée
            bAutoConnectFct(True) : si data == None, la fonction associée est appelée automatiquement si True lorsque l'item est choisi
                                    mettre à False si l'affichage du menu n'est pas geré par la fonction ShowMenu
            bNeedSelectedItem : si le flag est True et que le menu est associé à un TreeWidget 
            
        Dans tous les cas, le dictionnaire {'fct' : fct , 'data: data} est affectee 
        à l'item par la fonction setData pour traitements particuliers
        
        """
        szMenuPath = szMenuPath.replace("\.","\,")

        lstLabel = szMenuPath.split(".")
        currentMenu = self
        actionMenu = None
        dictSubMenu = self.dictLabel
        for iIndLabel in range(len(lstLabel)):
            
            szLabel = lstLabel[iIndLabel].replace("\,", ".")
            if iIndLabel < (len(lstLabel)-1) :
                # Creation de l'arborescence des menus
                if not szLabel in dictSubMenu : 
                    currentMenu = currentMenu.addMenu(szLabel)
                    dictSubMenu[szLabel] = {"menu" : currentMenu, "dictSubMenu" : {}}
                else:
                    currentMenu = dictSubMenu[szLabel]["menu"]

                #Si le sous-menu existe deja et est une action, on sort    
                if type(currentMenu) == QtWidgets.QAction : return currentMenu
                     
                dictSubMenu = dictSubMenu[szLabel]["dictSubMenu"]
            else:
                # Creation de l'action associée au menu
                if not szLabel in dictSubMenu : 
                    actionMenu = currentMenu.addAction(szLabel)
                    actionMenu.setEnabled(bEnable)
                    actionMenu.setCheckable(bCheckable)
                    dictSubMenu[szLabel] = {"menu" : actionMenu}
                    
                    actionMenu.setData({"fct" : fct,"data" : data,"bNeedSelectedItems" : bNeedSelectedItems})
                    if fct != None and data == None and bAutoConnectFct == True and self.bAutoConnectFct == True : 
                        actionMenu.triggered.connect(fct)
                        actionMenu.setData(None)
                    elif fct != None and data != None and bAutoConnectFct == True and self.bAutoConnectFct == True :
                        if self.bMenuTriggered == False :  
                            QtCore.QObject.connect(self,QtCore.SIGNAL("triggered(QAction *)"),self.ExecMenu)
                            self.bMenuTriggered = True

                    if sToolTip != None : actionMenu.setToolTip(sToolTip)
                else : 
                    currentMenu = dictSubMenu[szLabel]["menu"]
                    currentMenu.setData({"fct" : fct,"data" : data,"bNeedSelectedItems" : bNeedSelectedItems})
                    if fct != None and data == None and bAutoConnectFct == True and self.bAutoConnectFct == True : 
                        currentMenu.triggered.connect(fct)
                        currentMenu.setData(None)
           
        return actionMenu

    def RemoveEntryFromPath(self,sMenuPath):
        sMenuPath = sMenuPath.replace("\.","\,")
        lstLabel = sMenuPath.split(".")

        currentMenu = self
        actionMenu = None
        dictSubMenu = self.dictLabel
        
        for iIndLabel in range(len(lstLabel)):
            
            szLabel = lstLabel[iIndLabel].replace("\,", ".")
            if iIndLabel < (len(lstLabel)-1) :
                # Creation de l'arborescence des menus
                if not dictSubMenu.has_key(szLabel) : 
                    logging.error("QtMenu::RemoveEntryFromPath Menu %s doesn't exist"%sMenuPath)
                    return
                else:
                    parentMenu = dictSubMenu[szLabel]['menu']
                    dictSubMenu = dictSubMenu[szLabel]["dictSubMenu"]

        #Si le sous-menu existe et est une action, on le supprime    
        currentMenu = dictSubMenu[szLabel]["menu"]                
        if type(currentMenu) == QtWidgets.QAction :  parentMenu.removeAction(currentMenu)
        
    def Clear(self):
        self.dictLabel = {}
        self.clear()
 
    def AddSeparator(self):
        self.addSeparator()

    def ShowMenu(self):
        """ Activation du menu
        """
        actionMenu = self.exec_(QtGui.QCursor.pos())
    
    def ExecMenu(self,actionMenu):
        if actionMenu != None : 
            mnuDictData = actionMenu.data()
            if mnuDictData == None : return
            
            fct = mnuDictData['fct']
            if fct == None : return
            
            data = mnuDictData['data']
            if data == None : 
                fct()
                return     
            elif type(data).__name__ == "QString" : data = str(data)
            
            fct(data)                
# --------------------------------------------------------------------
# Module Test
# --------------------------------------------------------------------
if __name__ == "__main__": # pragma: no cover

    def Test(data):
        print(data)

    def ExecMenuFile(data):
        print(data)        
            
    app = QApplication(sys.argv)
    frmMain = QtWidgets.QMainWindow()
    wdCentral = QWidget()
    frmMain.setCentralWidget(wdCentral)
    
    layout = QtWidgets.QVBoxLayout()
    wdCentral.setLayout(layout)
    
    wdPushButton = QtWidgets.QPushButton("Right Click On Me !")
    layout.addWidget(wdPushButton)

    #-----------------------------------------
    #Creation du menu contextuel de la fenêtre
    #-----------------------------------------          
    menu = QtMenu() 
    menu.AddEntryFromPath("m1.m11.m12",fct = Test,data = ['toto','titi']) 
    menu.AddEntryFromPath("m2.m21",fct = Test,data ='m2.m21',bEnable = True)
    menu.AddEntryFromPath("m2.m22.m221",fct = Test,data ='m2.m22.m221',bEnable = True)
    menu.AddEntryFromPath("m2.m22.m222",fct = Test,data ='m2.m22.m222',bEnable = True)
    menu.AddEntryFromPath("m2.m22.m223",fct = Test,data ='m2.m22.m223',bEnable = True)
      
    frmMain.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    QtCore.QObject.connect(frmMain,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),menu.ShowMenu)

    #-----------------------------------------
    #Creation du menu contextuel du PushButton
    #-----------------------------------------          
    menuPush = QtMenu() 
    menuPush.AddEntryFromPath("Push1",fct = Test,data = "Push1") 
    menuPush.AddEntryFromPath("Push2",fct = Test,data = "Push2") 
    wdPushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    QtCore.QObject.connect(wdPushButton,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),menuPush.ShowMenu)
 
    #----------------------------
    #Creation d'une barre de menu
    #----------------------------
    mainMenu = frmMain.menuBar()
     
    mnuFile = QtMenu(frmMain,szTitle = "File")
    mnu = mnuFile.AddEntryFromPath("Open",fct = ExecMenuFile,data = "open")
    mnuFile.AddSeparator()
    mnuFile.AddEntryFromPath("Exit",fct = ExecMenuFile, data = "quit")
    mainMenu.addMenu(mnuFile)
 
    mnuEdit = QtMenu(frmMain,szTitle = "Edit")
    mnu = mnuEdit.AddEntryFromPath("Curve",fct = ExecMenuFile)
    mnuEdit.AddEntryFromPath("Graph",fct = ExecMenuFile)
    mainMenu.addMenu(mnuEdit)
    

    frmMain.show()
    
    sys.exit(app.exec_())        