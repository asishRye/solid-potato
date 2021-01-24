from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpmenu = menubar.addMenu("Help")

        ###########################################################
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+0")
        filemenu.addAction(new)
        exitmenu = QAction("Exit", self)
        exitmenu.triggered.connect(self.exitFunc)
        filemenu.addAction(exitmenu)

    def exitFunc(self):
        if QMessageBox.question(self, "Information", "Are you sure you want to exit?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            sys.exit()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
