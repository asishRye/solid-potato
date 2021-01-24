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
        formLayout = QFormLayout()

        name_Text = QLabel("Name:")
        name_Input = QLineEdit()
        pass_Text = QLabel("Password:")
        pass_Input = QLineEdit()
        pass_Input.setEchoMode(QLineEdit.Password)

        formLayout.addRow(name_Text, name_Input)
        formLayout.addRow(pass_Text, pass_Input)
        formLayout.addRow(QLabel("Country:"), QComboBox())

        self.setLayout(formLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
