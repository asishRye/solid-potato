from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

DURATION = 1000


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 50, 500, 300)
        self.setWindowTitle("SpinBox")
        self.UI()
        self.show()

    def UI(self):
        self.timerLabel = QLabel("Timer has not started", self)
        self.timerLabel.move(30, 30)

        self.timer = QTimer()
        self.timer.setInterval(DURATION)
        self.timer.timeout.connect(self.makeChanges_Func)
        self.startTimerButton = QPushButton("Start", self)
        self.startTimerButton.move(30, 50)
        self.startTimerButton.clicked.connect(self.startTimer_Func)
        self.show()

    def startTimer_Func(self):
        self.timer.start()
        print("Timer has started")
        self.timerLabel.setText("Timer has started")

    def makeChanges_Func(self):
        print(
            "Changes are made and timer has stopped, the timer ran for {} milliseconds".format(DURATION))
        self.timer.stop()
        self.timerLabel.setText("Timer has stopped")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
