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
        self.showMaximized()

    def UI(self):
        mainVBoxLayout = QVBoxLayout()
        topHBoxLayout = QHBoxLayout()
        bottomHBoxLayout = QHBoxLayout()

        image1 = QLabel(self)
        image1.setPixmap(
            QPixmap(r"D:\accubits\pyqt5\udemy\Section 3\assets\img.jpg"))
        topHBoxLayout.addWidget(image1)

        image2 = QLabel(self)
        image2.setPixmap(
            QPixmap(r"D:\accubits\pyqt5\udemy\Section 3\assets\img.jpg"))
        image3 = QLabel(self)
        image3.setPixmap(
            QPixmap(r"D:\accubits\pyqt5\udemy\Section 3\assets\img.jpg"))
        image4 = QLabel(self)
        image4.setPixmap(
            QPixmap(r"D:\accubits\pyqt5\udemy\Section 3\assets\img.jpg"))

        bottomHBoxLayout.addWidget(image2)
        bottomHBoxLayout.addWidget(image3)
        bottomHBoxLayout.addWidget(image4)

        mainVBoxLayout.addLayout(topHBoxLayout)
        mainVBoxLayout.addLayout(bottomHBoxLayout)

        self.setLayout(mainVBoxLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
