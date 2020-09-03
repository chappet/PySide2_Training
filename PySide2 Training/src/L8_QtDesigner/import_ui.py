from Ui_Dialog_Info import Ui_Dialog
from Ui_editor import Ui_MainWindow

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionGet_User_Info.triggered.connect(self.GetUserInfo)

    def open(self):
        print ("Open")

    def GetUserInfo(self):
        wd = InfoDialog(self).GetResult()
        if wd : print (wd)
    
    def closeEvent(self,event):
        print ("CloseEvent")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    wd = MainWindow()
    wd.show()

    sys.exit(app.exec_())