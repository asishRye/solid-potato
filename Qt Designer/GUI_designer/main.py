from splash import Ui_SplashScreen
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
