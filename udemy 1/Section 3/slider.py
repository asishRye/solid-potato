from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        vBoxLayout = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(5)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.changeFunc)

        self.sliderValue = QLabel("0")
        self.sliderValue.setAlignment(Qt.AlignCenter)
        self.dispText = QLabel("Hello Python")

        vBoxLayout.addStretch()
        vBoxLayout.addWidget(self.sliderValue)
        vBoxLayout.addWidget(self.dispText)
        vBoxLayout.addWidget(self.slider)

        self.setLayout(vBoxLayout)

    def changeFunc(self):
        value = self.slider.value()
        self.sliderValue.setText(str(value))
        FONT = QFont("Times", value)
        self.dispText.setFont(FONT)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
