from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 180, 500, 350)
        self.setWindowTitle("List Widget")
        self.UI()
        self.show()

    def UI(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(30, 10)
        self.lineEdit.setPlaceholderText("Enter New Value")

        self.listWidget = QListWidget(self)
        self.listWidget.move(30, 50)
        itemList = ["Pen", "Book", "Pencil", "Eraser"]
        self.listWidget.addItems(itemList)

        self.addButton = QPushButton("Add", self)
        self.addButton.move(300, 50)
        self.addButton.clicked.connect(self.func_AddButton)

        self.deleteButton = QPushButton("Delete", self)
        self.deleteButton.move(300, 80)
        self.deleteButton.clicked.connect(self.func_DeleteButton)

        self.deleteAllButton = QPushButton("Delete All", self)
        self.deleteAllButton.move(300, 110)
        self.deleteAllButton.clicked.connect(self.func_DeleteAllButton)

        self.FetchButton = QPushButton("Fetch", self)
        self.FetchButton.move(300, 140)
        self.FetchButton.clicked.connect(self.func_fetchButton)

    def readInput(self):
        return self.lineEdit.text()

    def func_AddButton(self):
        if self.readInput().strip() == "":
            QMessageBox.information(self, "Warning", "Invalid Entry")
        else:
            self.listWidget.addItem(self.readInput())
            self.lineEdit.setText("")

    def func_DeleteAllButton(self):
        self.listWidget.clear()

    def func_DeleteButton(self):
        id = self.listWidget.currentRow()
        self.listWidget.takeItem(id)

    def func_fetchButton(self):
        try:
            print(self.listWidget.currentItem().text())
        except(Exception):
            QMessageBox.information(
                self, "Warning", "No items selected to fetch")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
