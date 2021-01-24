from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        vBoxLayout = QVBoxLayout()

        self.tableWiget = QTableWidget()
        self.tableWiget.setRowCount(5)
        self.tableWiget.setColumnCount(5)
        self.tableWiget.setVerticalHeaderItem(0, QTableWidgetItem("Name"))
        self.tableWiget.setVerticalHeaderItem(1, QTableWidgetItem("Place"))
        self.tableWiget.setVerticalHeaderItem(2, QTableWidgetItem("Area"))
        self.tableWiget.setVerticalHeaderItem(3, QTableWidgetItem("Model"))
        self.tableWiget.setVerticalHeaderItem(4, QTableWidgetItem("Section"))
        self.tableWiget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWiget.doubleClicked.connect(self.doubleClick)

        for i in range(0, 5):
            for j in range(0, 5):
                self.tableWiget.setItem(i, j, QTableWidgetItem(
                    "( " + str(i) + ", " + str(j) + " )"))
        button = QPushButton("GET")
        button.clicked.connect(self.getValueFunc)

        vBoxLayout.addWidget(self.tableWiget)
        vBoxLayout.addWidget(button)
        self.setLayout(vBoxLayout)

    def getValueFunc(self):
        for _ in self.tableWiget.selectedItems():
            print(_.text(), _.row(), _.column())

    def doubleClick(self):
        for _ in self.tableWiget.selectedItems():
            print(_.text(), _.row(), _.column())


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
