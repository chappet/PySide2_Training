'''
Created on 13 mars 2020

@author: cchappet

This module demonstrate the use of stylesheet to change widget appearance
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit,QFileDialog,QMessageBox,QAction
from PySide2.QtCore import Signal, Slot,QFile,QTextStream,QFileInfo,QSettings,QSize,QPoint
from PySide2.QtGui import QIcon,QKeySequence
import PySide2.QtMultimedia as QtMultimedia

import sys

from Ressources import ressources


class MyTextEditor(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.textEdit =  QPlainTextEdit()
        self.setCentralWidget(self.textEdit)
    
        self.createActions()

        self.readSettings()
    
        self.setCurrentFile("")

    def createActions(self):
        
        self.toolBar = self.addToolBar("main tool bar")
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')
        self.helpMenu = self.menuBar.addMenu('Help')

        
        Act = QAction(QIcon(":/icons/new.png"), self.tr("&New"), self)
        Act.setShortcuts(QKeySequence.New)
        Act.setStatusTip(self.tr("Create a new file"))
        Act.triggered.connect(self.newFile)
     
        self.fileMenu.addAction(Act)
        self.toolBar.addAction(Act)
        
        openAct =  QAction(QIcon(":/icons/openconf.png"), self.tr("&Open..."), self)
        openAct.setShortcuts(QKeySequence.Open)
        openAct.setStatusTip(self.tr("Open an existing file"))
        self.fileMenu.addAction(openAct)
        self.toolBar.addAction(openAct)
        openAct.triggered.connect(self.open)

        saveAct =  QAction(QIcon(":/icons/save.png"), self.tr("&Save..."), self)
        saveAct.setShortcuts(QKeySequence.Save)
        saveAct.setStatusTip(self.tr("Save a file"))
        self.fileMenu.addAction(saveAct)
        self.toolBar.addAction(saveAct)
        saveAct.triggered.connect(self.save)


        self.fileMenu.addSeparator()

        quitAct =  QAction(QIcon(":/icons/exit.png"), self.tr("&Exit..."), self)
        quitAct.setShortcuts(QKeySequence.Close)
        quitAct.setStatusTip(self.tr("Exit"))
        self.fileMenu.addAction(quitAct)
        self.toolBar.addAction(quitAct)
        quitAct.triggered.connect(self.exit)


        aboutQtAct =  QAction(self.tr("About &Qt"), self)
        aboutQtAct.setStatusTip(self.tr("Show the Qt library's About box"))
        aboutQtAct.triggered.connect(self.about)
        self.helpMenu.addAction(aboutQtAct)
        
    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, self.tr("Application"), self.tr("Cannot read file "
                "{}:\n{}.".format(fileName, file.errorString())))
            return
    
        inStream = QTextStream(file)
        QApplication.setOverrideCursor(QtGui.Qt.WaitCursor)
        self.textEdit.setPlainText(inStream.readAll())
        print(inStream.readAll())
        QApplication.restoreOverrideCursor()
    
        self.setCurrentFile(fileName)
        self.statusBar().showMessage(self.tr("File loaded"), 2000)
        
    def newFile(self):
        if self.maybeSave():
            self.fileName = QFileDialog.getOpenFileName(self)
            if not self.fileName == "":
                self.loadFile(self.fileName[0])
    
    def open(self):
        if self.maybeSave():
            fileName = QFileDialog.getOpenFileName(self)
            if not fileName == "" :
                self.loadFile(fileName[0])
    
    def save(self):
        if self.curFile == "":
            return self.saveAs()
        else:
            return self.saveFile(self.curFile)

    def saveAs(self):
        fileName = QFileDialog.getSaveFileName(self)
        if fileName == "" :
            return False
        return self.saveFile(fileName[0])      

    def saveFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, self.tr("Application"),
                                 self.tr("Cannot write file %1:\n%2.")
                                 .arg(fileName)
                                 .arg(file.errorString()))
            return False
    
        out = QTextStream(file)
        QApplication.setOverrideCursor(QtGui.Qt.WaitCursor)
        print (self.textEdit.toPlainText())
        out << self.textEdit.toPlainText()
        QApplication.restoreOverrideCursor()
    
        self.setCurrentFile(fileName)
        self.statusBar().showMessage(self.tr("File saved"), 2000)
        return True

    def documentWasModified(self):
        self.setWindowModified(self.textEdit.document().isModified())
        
    def about(self):
       QMessageBox.about(self, self.tr("About Application"),
                self.tr("The <b>Application</b> example demonstrates how to "
                   "write modern GUI applications using Qt, with a menu bar, "
                   "toolbars, and a status bar."))                          
    def File(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile("")

    def setCurrentFile(self,fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        self.setWindowModified(False)
    
        if self.curFile == "":
            shownName = "untitled.txt"
        else:
            shownName = self.strippedName(self.curFile)
    
        self.setWindowTitle(self.tr("{}[*] - {}").format(shownName,self.tr("Application")))    

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()


    def readSettings(self):
        settings = QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QSettings("Trolltech", "Application Example")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())
                    
    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()   

    def exit(self):
        self.close() #with call to closeEvent
        #self.deleteLater() #Do not call closeEvent
        
    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QMessageBox.warning(self, self.tr("Application"),
                                      self.tr("The document has been modified.\n"
                                         "Do you want to save your changes?"),
                                     QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                return self.save()
            elif ret == QMessageBox.Cancel:
                return False
        return True                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
        
    wdEditor = MyTextEditor()

    wdEditor.show()
    
    sys.exit(app.exec_())                 