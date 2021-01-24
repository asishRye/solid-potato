from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.tabs.addTab(self.tab1, "First Tab")
        self.tabs.addTab(self.tab2, "Second Tab")
        self.tabs.addTab(self.tab4, "Last Tab")

        vBoxLayout = QVBoxLayout()
        hBoxLayout = QHBoxLayout()

        self.textMain = QLabel("Some Text")
        buttonPush = QPushButton("Push Me")
        buttonPush.clicked.connect(self.buttonPushed)
        buttonPushAgain = QPushButton("Push Me AGain")
        buttonPushAgain.clicked.connect(self.changeFunc)

        vBoxLayout.addWidget(self.textMain)
        vBoxLayout.addWidget(buttonPush)
        vBoxLayout.addWidget(buttonPushAgain)
        self.tab1.setLayout(vBoxLayout)

        self.tab2TExt = QLabel("Change this")
        hBoxLayout.addWidget(self.tab2TExt)
        self.tab2.setLayout(hBoxLayout)

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

    def buttonPushed(self):
        self.textMain.setText("Pushed Button")

    def changeFunc(self):
        self.tab2TExt.setText("Pushed Button")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
