from get_information import Ui_Dialog

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wd = MainWindow()
    wd.show()

    sys.exit(app.exec_())