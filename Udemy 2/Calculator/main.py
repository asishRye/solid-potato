import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *

app = QGuiApplication(sys.argv)
app.setWindowIcon("Udemy 2\Calculator\resources\images\logo.png")

engine = QQmlApplicationEngine()
engine.load("Udemy 2\Calculator\resources\qml\main.qml")

sys.exit(app.exec())
