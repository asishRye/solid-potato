from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

FONT = QFont("Times", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 50, 500, 300)
        self.setWindowTitle("SpinBox")
        self.UI()
        self.show()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.setFont(FONT)
        self.spinBox.move(30, 30)
        self.spinBox.setMaximum(10000)
        self.spinBox.setMinimum(-10)
        self.spinBox.setSuffix(" (US Dollars)")
        self.spinBox.setPrefix("$ ")
        self.spinBox.valueChanged.connect(self.spinBox_Func)

        self.submitButton = QPushButton("Submit", self)
        self.submitButton.move(30, 80)
        self.submitButton.clicked.connect(self.submit_Func)

    def submit_Func(self):
        print("From Submit Button", self.spinBox.value())

    def spinBox_Func(self):
        print("From Spin Box Function", self.spinBox.value())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
