# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
import PySide2.QtWidgets
from PySide2.QtWidgets import QApplication,QMainWindow,QDialog,QWidget,QFrame
from PySide2.QtCore import QFile,QObject

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        ui_file_name = "ui/Ui_MainWindow.ui"
        ui_file = QFile(ui_file_name)

        loader = QUiLoader()
        self.window = loader.load(ui_file,parent)
        ui_file.close()
            
        self.window.actionOpen.triggered.connect(self.open)
        self.window.actionExit.triggered.connect(self.exit)

        self.window.actionGet_User_Info.triggered.connect(self.GetUserInfo)

        self.setCentralWidget(self.window)
        self.show()
                
    def open(self):
        print ("Open")

    def exit(self):
        #kill the application without a call to close
#         sys.exit(0)
        
        #try to close the window and trig closeEvent
        self.close()
        
    def GetUserInfo(self):
        wd = InfoDialog(self).GetResult()
        if wd : print (wd)

    def closeEvent(self,event):
        """ 
        close application if the editor content is not empty
        """
        print ("CloseEvent called on MainWindow")  
        
        if self.window.textEdit.toPlainText() == "" :
            #Prevent window from closing
            print ("MainWindow will not close, textEdit content is empty !") 
            event.ignore()  

class Dialog(PySide2.QtWidgets.QDialog):
    def accept(self):
        print ("Call to Dialog.accept")
        return False          
               
class InfoDialog(QObject):
    def __init__(self, parent = None):
        super(InfoDialog, self).__init__(parent)
        
        ui_file_name = "ui/Ui_Dialog.ui"
        ui_file = QFile(ui_file_name)
            
        loader = QUiLoader()
        loader.registerCustomWidget(Dialog)
        
        self.ui = loader.load(ui_file)
        print(self.ui.__class__)
        ui_file.close()
        
        #QDialog accept method should be overrided ... BUT IT IS NOT !!!
        # see https://srinikom.github.io/pyside-bz-archive/533.html
        # see https://github.com/mottosso/Qt.py/issues/192
#         self.ui.accept = self.accept

    def GetResult(self):        
        ok = self.ui.exec()
        print ("exec returns : {}".format(ok))
        
        if ok : 
            return {'name': self.ui.wdInputName.text(),'phone' : self.ui.wdInputPhone.text()}

    def closeEvent(self,event):
        print ("CloseEvent called on Dialog")

    #!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!! Wont be called on exit
    #!!!!!!!!!!!!!!!!!!!!!!!!!!
#     def accept(self):
#         return False          
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    
    sys.exit(app.exec_())