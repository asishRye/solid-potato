import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon("Udemy 2\Calculator\\resources\images\logo.png"))

engine = QQmlApplicationEngine()
engine.load("Udemy 2\Calculator\\resources\qml\main.qml")
engine.quit.connect(app.quit)
sys.exit(app.exec())
