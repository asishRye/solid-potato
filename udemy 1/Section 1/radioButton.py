from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox Window")
        self.setGeometry(30, 30, 500, 300)
        self.UI()

    def UI(self):
        self.welcome = QLabel("Hey!! Welcome", self)
        self.welcome.move(30, 20)
        self.radioBlue = QRadioButton("Blue Pill", self)
        self.radioBlue.move(30, 40)
        self.radioRed = QRadioButton("Red Pill", self)
        self.radioRed.move(100, 40)
        self.radioColorless = QRadioButton("Colorless Pill", self)
        self.radioColorless.move(170, 40)
        self.killButton = QPushButton("Show me", self)
        self.killButton.move(30, 60)
        self.killButton.clicked.connect(self.killButton_Func)

        self.show()

    def killButton_Func(self):
        if self.radioBlue.isChecked():
            print("You chose Blue Pill :) you are dead")
        elif self.radioRed.isChecked():
            print("You chose Red Pill :) you are dead")
        elif self.radioColorless.isChecked():
            print("You chose Colorless Pill :) you are dead")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
