import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel("Hello, World!")
    label.show()
    sys.exit(app.exec())
