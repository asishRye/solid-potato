from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


i = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        vBoxLayout = QVBoxLayout()
        hBoxLayout = QHBoxLayout()
        self.progressBar = QProgressBar()
        self.startButton = QPushButton("Start Timer")
        self.startButton.clicked.connect(self.startTimerFunc)
        self.stopButton = QPushButton("Stop Timer")
        self.stopButton.clicked.connect(self.stopTimerFunc)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.progressBarFunc)

        vBoxLayout.addLayout(hBoxLayout)
        vBoxLayout.addWidget(self.progressBar)
        hBoxLayout.addWidget(self.startButton)
        hBoxLayout.addWidget(self.stopButton)

        self.setLayout(vBoxLayout)

    def progressBarFunc(self):
        global i
        i = i + 1
        print(i)
        self.progressBar.setValue(i)
        if i == 100:
            self.stopTimerFunc()

    def stopTimerFunc(self):
        self.timer.stop()

    def startTimerFunc(self):
        global i
        i = 0
        self.timer.start()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
