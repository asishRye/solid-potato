from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()
        self.show()

    def UI(self):
        vBoxLayout = QVBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        button4 = QPushButton("Button4")
        vBoxLayout.addStretch()
        vBoxLayout.addWidget(button1)
        vBoxLayout.addWidget(button2)
        vBoxLayout.addWidget(button3)
        vBoxLayout.addWidget(button4)
        vBoxLayout.addStretch()

        self.setLayout(vBoxLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
