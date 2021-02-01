
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(20, 40, 600, 400)
        self.UI()
        self.show()

    def UI(self):

        self.layout = QVBoxLayout(self)
        self.layout.setset

        self.setWindowFlag(Qt.FramelessWindowHint)

        # self.setAttribute(Qt.TransluscentBackground)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
