'''
Created on 13 mars 2020

@author: cchappet

This module demonstrate the use of stylesheet to change widget appearance
'''
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Signal, Slot 
import PySide2.QtMultimedia as QtMultimedia

import sys

class MyApplication(QtWidgets.QMainWindow):
    """
    A central widget with some dock widgets
    """       
    def __init__(self):
        super(MyApplication,self).__init__()
        
        #get the application handle to connect signal
        qApp = QtCore.QCoreApplication.instance()
        
        #change the QMainWindow StyleSheet with signal StyleSheet_0
        qApp.connect(QtCore.SIGNAL("StyleSheet_0(QString)"),self.setStyleSheet)
        
        #########################################
        # Define a TextEdit as a central widget
        #########################################
        sText = """
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum."        
        """
        self.textEdit = QtWidgets.QTextEdit(sText,parent = self)
        self.setCentralWidget(self.textEdit)

        #####################################
        # Define a Calendar in a DockWidget
        #####################################
        wdDockCalendar  = QtWidgets.QDockWidget("Calendar",self)
        calendar = QtWidgets.QCalendarWidget()
        wdDockCalendar.setWidget(calendar)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, wdDockCalendar)
        
        #change the DockWidget StyleSheet with signal StyleSheet_1
        qApp.connect(QtCore.SIGNAL("StyleSheet_1(QString)"),wdDockCalendar.setStyleSheet)

        #####################################
        # Define a TextEdit in a DockWidget
        #####################################
        sText = """
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque 
        ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia 
        voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
        Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi 
        tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem 
        ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea 
        voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"        
        """
        wdDockTextEdit  = QtWidgets.QDockWidget("Editor",self)
        wdTextEdit = QtWidgets.QTextEdit(sText)
        wdDockTextEdit.setWidget(wdTextEdit)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, wdDockTextEdit)
        
        #change the DockWidget StyleSheet with signal StyleSheet_2
        qApp.connect(QtCore.SIGNAL("StyleSheet_2(QString)"),wdDockTextEdit.setStyleSheet)
        
class StyleSheetEditors(QtWidgets.QFrame): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StyleSheet Editors")
        layout = QtWidgets.QVBoxLayout(self)
        
        ####################################################################
        # Create three different TextEdit widgets for StyleSheet definition
        ####################################################################
        for i,sLabel in enumerate(["Mainwindow", "Dock Calendar", "Dock TextEdit"]):
            layout.addWidget(QtWidgets.QLabel(sLabel))
            
            sInitText = "color:blue;background-color: white; font: normal 12px" if i == 0 else ''
            
            editor = QtWidgets.QTextEdit(sInitText)
            editor.setWindowTitle("Editor_{}".format(i))
            layout.addWidget(editor)
            
            wdButton = QtWidgets.QPushButton("APPLY")
            
            #### A function generator ########################################
            def CreateFctEmit(wdEditor, i):
                #The function emits the content of the current editor in a StyleSheet_X signal
                def EmitStyleSheet():
                    print ("Emit StyleSheet_{}(QString)".format(i))
                    qApp = QtCore.QCoreApplication.instance()
                    qApp.emit(QtCore.SIGNAL("StyleSheet_{}(QString)".format(i)),wdEditor.toPlainText())
                    
                return EmitStyleSheet
            #### End of Function Generator ####################################              
            
            #connect the dynamic created function to the button 
            fctSignal = CreateFctEmit(editor, i)
            wdButton.clicked.connect(fctSignal)
            
            if sInitText != "": wdButton.click()
            
            layout.addWidget(wdButton)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    wdMain = MyApplication()
    wdMain.show()
    
    wdStyle = StyleSheetEditors()
    wdStyle.show()
    
    sys.exit(app.exec_())


