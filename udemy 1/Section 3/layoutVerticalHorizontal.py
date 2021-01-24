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
        mainVBoxLayout = QVBoxLayout()
        topHBoxLayout = QHBoxLayout()
        bottomHBoxLayout = QHBoxLayout()

        sendButton = QPushButton("Send Button")
        checkBox = QCheckBox("Check Box hurray!")
        comboBox = QComboBox()
        comboBox.addItems(["Alan", "Alpha"])
        topHBoxLayout.addWidget(sendButton)
        topHBoxLayout.addWidget(checkBox)
        topHBoxLayout.addWidget(comboBox)

        receiveButton = QPushButton("Receive Button")
        bottomHBoxLayout.addWidget(receiveButton)

        mainVBoxLayout.addLayout(topHBoxLayout)
        mainVBoxLayout.addLayout(bottomHBoxLayout)

        self.setLayout(mainVBoxLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
