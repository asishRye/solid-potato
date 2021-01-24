from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Open")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        vBoxLayout = QVBoxLayout()
        hBoxLayout = QHBoxLayout()

        self.textEditor = QTextEdit()
        openButton = QPushButton("Open File")

        openButton.clicked.connect(self.openFileFunc)

        vBoxLayout.addWidget(self.textEditor)
        hBoxLayout.addWidget(openButton)
        vBoxLayout.addLayout(hBoxLayout)
        self.setLayout(vBoxLayout)

    def openFileFunc(self):
        url = QFileDialog.getOpenFileName(self, "Open file", filter="*.txt")
        fileread = open(url[0], 'r')
        self.textEditor.setText(fileread.read())


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
