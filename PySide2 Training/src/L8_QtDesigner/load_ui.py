# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QMainWindow,QDialog
from PySide2.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        ui_file_name = "ui/Ui_editor.ui"
        ui_file = QFile(ui_file_name)

        loader = QUiLoader()
        self.window = loader.load(ui_file,parent)
        ui_file.close()
            
        self.window.actionOpen.triggered.connect(self.open)
        self.window.actionGet_User_Info.triggered.connect(self.GetUserInfo)

        
        self.setCentralWidget(self.window)
        self.show()
                
    def open(self):
        print ("Open")

    def GetUserInfo(self):
        wd = InfoDialog(self).GetResult()
        if wd : print (wd)
    
    def closeEvent(self,event):
        print ("CloseEvent")
                

class InfoDialog(QDialog):
    def __init__(self, parent = None):
        super(InfoDialog, self).__init__(parent)
        
        ui_file_name = "ui/Ui_Dialog_Info.ui"
        ui_file = QFile(ui_file_name)
            
        loader = QUiLoader()
        self.wdDiag = loader.load(ui_file,parent)
        ui_file.close()

    def GetResult(self):        
        ok = self.wdDiag.exec()
        print (ok)
        
        if ok : 
            return {'name': self.wdDiag.wdInputName.text(),'phone' : self.wdDiag.wdInputPhone.text()}
             
            
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
#     diag = InfoDialog()
#     diag.GetResult()

    sys.exit(app.exec_())