from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 50, 500, 300)
        self.setWindowTitle("SpinBox")
        self.UI()
        self.show()

    def UI(self):
        self.textEditor = QTextEdit(self)
        self.textEditor.move(30, 30)
        self.textEditor.setAcceptRichText(False)
        self.textEditor.setAcceptDrops(True)
        self.sendButton = QPushButton("Send", self)
        self.sendButton.clicked.connect(self.getValue_Func)
        self.sendButton.move(30, 230)
        self.show()

    def getValue_Func(self):
        print(self.textEditor.toPlainText())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
