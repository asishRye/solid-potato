from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 400, 300)
        self.setWindowTitle("MessageBox")
        self.UI()
        self.show()

    def UI(self):
        self.bluePillRadio = QRadioButton("Blue Pill", self)
        self.bluePillRadio.move(30, 40)
        self.redPillRadio = QRadioButton("Red Pill", self)
        self.redPillRadio.move(100, 40)
        self.checkButton = QPushButton("Check..", self)
        self.checkButton.move(30, 60)
        self.checkButton.clicked.connect(self.check_Func)

    def check_Func(self):
        if self.redPillRadio.isChecked() or self.bluePillRadio.isChecked():
            messageBox = QMessageBox.question(
                self, "Message Box Name", "Description",
                QMessageBox.No | QMessageBox.Yes |
                QMessageBox.YesAll | QMessageBox.Cancel, QMessageBox.YesAll)
            if messageBox == QMessageBox.YesToAll:
                print("Selected yes to all")
            else:
                print("Something Else Selected")
        else:
            infoBox = QMessageBox.information(
                self, "Window Title - Information", "Please choose your destiny")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
