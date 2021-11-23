from Ui_Dialog import Ui_Dialog
from Ui_MainWindow import Ui_MainWindow

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import QFile

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.sFilename = ""
        
        self.dctInfoUser = {'name': '','phone' : ''}
        
        self.setupUi(self)

        #File Menu Management
        self.actionOpen.triggered.connect(self.OpenFile)
        self.actionSave.triggered.connect(self.SaveFile)
        self.actionSave.setEnabled(False)        
        
        self.actionSaveAs.triggered.connect(self.SaveFileAs)
        self.actionNew.triggered.connect(self.New)
        
        self.actionExit.triggered.connect(self.Exit)
        
        self.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.actionGet_User_Info.triggered.connect(self.GetUserInfo)

    def GetUserInfo(self):
        self.dctInfoUser = InfoDialog(self).GetResult(self.dctInfoUser)
    
    def closeEvent(self,event):
        """ 
        close application if the editor content is not empty
        """
        print ("CloseEvent called on MainWindow")  
        
        if self.textEdit.toPlainText() == "" :
            #Prevent window from closing
            print ("MainWindow will not close, textEdit content is empty !") 
            event.ignore()  

    def OpenFile(self):
        sFileName = QtWidgets.QFileDialog().getOpenFileName(filter = '*.txt;;*.*', dir= '.')
        #getOpenFileName return a QString in C++ but a tuple in Python
        #https://forum.qt.io/topic/757/pyside-qfiledialog-getopenfilename-returns-string-of-tuple-instead-of-just-string/5
        if sFileName[0] != "" : self.sFilename = sFileName[0]
        else: return
        
        with open(sFileName[0], 'r') as infile:
            sText = infile.read()
            self.textEdit.setPlainText(sText)
        
        self.actionSave.setEnabled(True) 

    def SaveFile(self):
        if self.sFilename != "":
            with open(self.sFilename, 'w') as outfile:
                outfile.write(self.textEdit.toPlainText())

    def SaveFileAs(self):
        sFileName = QtWidgets.QFileDialog().getSaveFileName(filter = '*.txt;;*.*', dir= '.')
        if sFileName[0] != "" : self.sFilename = sFileName[0]
        else: return
        
        with open(sFileName[0], 'w') as outfile:
            outfile.write(self.textEdit.toPlainText())
        
        self.actionSave.setEnabled(True)

    def New(self):
        self.sFilename = ""
        self.textEdit.setPlainText("")
        self.actionSave.setEnabled(False)
        
    def Exit(self):
        """
        Exiting an apllication with three differents ways
        """
#         self.close() #close the widget with call to closeEvent

        self.deleteLater() #kill the widget without call to closeEvent

#         sys.exit() #Quit the application without call to closeEvent
        
        
class InfoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(InfoDialog, self).__init__(parent)

        self.setupUi(self)
        
    def GetResult(self,dctInitInfoUser):
        self.dctInitInfoUser = dctInitInfoUser      
        self.wdInputName.setText(dctInitInfoUser['name'])
        self.wdInputPhone.setText(dctInitInfoUser['phone'])  

        ok = self.exec()
        print (ok)
        
        if ok : 
            return {'name': self.wdInputName.text(),'phone' : self.wdInputPhone.text()}  
        else:
            return self.dctInitInfoUser      

    def accept(self):
        if self.wdInputName.text() == "" or self.wdInputPhone.text() == "":
            return False
        else :
            super().accept()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    wd = MainWindow()
    wd.show()

    sys.exit(app.exec_())