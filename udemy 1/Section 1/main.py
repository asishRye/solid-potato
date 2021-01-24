
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        # Returns the display resolution of primary display
        windowSize = QDesktopWidget().screenGeometry(0)
        self.setGeometry(20, 40, 400, 250)
        self.UI()

    def UI(self):
        self.text1 = QLabel("Login Page", self)
        self.text1.move(50, 20)
        clickButton = QPushButton("Login", self)
        clickButton.move(50, 110)
        clickButton.clicked.connect(self.clickButtonFunc)
        exitButton = QPushButton("Reset", self)
        exitButton.move(150, 110)
        exitButton.clicked.connect(self.exitButtonFunc)

        self.uName = QLineEdit("a", self)
        self.uName.setGeometry(50, 40, 200, 18)
        self.uName.setPlaceholderText("Enter your username")
        self.password = QLineEdit("a", self)
        self.password.setGeometry(50, 65, 200, 18)
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(QLineEdit.Password)
        self.remember = QCheckBox("Remember me", self)
        self.remember.move(50, 90)
        self.image = QLabel(self)
        # Images is loaded only when I use absolute path
        self.image.setPixmap(
            QPixmap(r"udemy\Section 1\assets\profile.png"))
        self.image.close()

        self.comboBox = QComboBox(self)
        comboBoxItems = ["Admin", "HR", "Developer"]
        self.comboBox.addItems(comboBoxItems)
        self.comboBox.move(260, 40)
        self.show()
        # self.showMaximized()

    def clickButtonFunc(self):
        name = self.uName.text()
        password = self.password.text()
        if not name or not password:
            self.text1.setText("Please provide a valid username or password!!")
            self.text1.resize(300, 15)

        else:
            self.text1.setText("Logged in successfully")
            self.text1.resize(150, 15)
            self.image.show()
            self.image.move(260, 70)
            self.infoBox_Func([name, password, self.comboBox.currentText()])
            print("{} {} {} {}".format(
                name, password, self.remember.isChecked(), self.comboBox.currentText()))

    def exitButtonFunc(self):
        self.text1.setText("Login Page")
        self.text1.resize(150, 15)
        self.uName.setText("")
        self.password.setText("")
        self.image.close()
        self.remember.setChecked(False)
        self.comboBox.setCurrentText('Admin')
        # self.comboBox

    def infoBox_Func(self, lis):
        infoBox = QMessageBox.information(
            self, "Success", "Logged in as " + lis[0] + " to " + lis[2] + " page.")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
