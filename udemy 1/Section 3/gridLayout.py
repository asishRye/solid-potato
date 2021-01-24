from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        self.gridLayout = QGridLayout()

        for i in range(0, 4):
            for j in range(0, 4):
                self.btn = QPushButton("Button{}{}".format(i, j))
                self.gridLayout.addWidget(self.btn, i, j)
                self.btn.clicked.connect(self.buttonCallFunc)
        self.setLayout(self.gridLayout)

    def buttonCallFunc(self):
        print(self.btn.sender().text())


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
