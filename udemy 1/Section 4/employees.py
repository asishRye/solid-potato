from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3
from PIL import Image
import sys
import os

con = sqlite3.connect('employees.db')
cur = con.cursor()
global defaultImage
defaultImage = "user.png"
global idValue


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 500, 400)
        self.setWindowTitle("Employee App")
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployeesFunc()
        self.displayFirstRecord()

    def mainDesign(self):
        ############### Button Widgets ####################
        self.buttonNew = QPushButton("New")
        self.buttonUpdate = QPushButton("Update")
        self.buttonDelete = QPushButton("Delete")

        self.buttonNew.clicked.connect(self.addEmployeeFunc)
        self.buttonUpdate.clicked.connect(self.updateEmployeeFunc)
        self.buttonDelete.clicked.connect(self.deleteEmployeeFunc)

        ############### Left Form Widgets ################
        self.nameLabel = QLabel("")
        self.positionLabel = QLabel("")
        self.emailLabel = QLabel("")

        ############### Left Window Widgets ################
        self.listWidget = QListWidget()
        self.listWidget.itemClicked.connect(self.singleClickFunc)

    def layouts(self):
        self.mainLayout = QHBoxLayout()
        self.leftMainLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()

        ###################################################
        self.leftMainLayout.addRow(self.nameLabel)
        self.leftMainLayout.addRow(self.positionLabel)
        self.leftMainLayout.addRow(self.emailLabel)

        ####################################################
        self.rightTopLayout.addWidget(self.listWidget)

        #####################################################
        self.rightBottomLayout.addWidget(self.buttonNew)
        self.rightBottomLayout.addWidget(self.buttonUpdate)
        self.rightBottomLayout.addWidget(self.buttonDelete)

        #####################################################
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)

        #####################################################
        self.mainLayout.addLayout(self.leftMainLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)

        self.setLayout(self.mainLayout)

    def updateEmployeeFunc(self):
        self.updateEmployee = updateEmployee()
        self.close()

    def deleteEmployeeFunc(self):
        global idValue
        idValue = self.listWidget.currentItem().text().split('.')[0]
        if QMessageBox.warning(self, "Warning", "Are you sure?", QMessageBox.Yes | QMessageBox.No):
            try:
                query = "DELETE FROM employees WHERE id=?"
                cur.execute(query, (idValue,))
                con.commit()
                QMessageBox.information(self, "Deleted",
                                        "Record is removed from DB")
                self.close()
                self.window = Window()
            except:
                QMessageBox.information(self, "Unable to delete",
                                        "Unable to delete from database contact admin")

    def displayFirstRecord(self):
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cur.execute(query).fetchone()
        if employee:
            img = QLabel()
            img.setPixmap(
                QPixmap("udemy\\Section 4\\assets\\" + employee[5]))
            name = QLabel(employee[1])
            surname = QLabel(employee[2])
            phone = QLabel(employee[3])
            email = QLabel(employee[4])
            address = QLabel(employee[6])

            self.leftMainLayout.addRow("", img)
            self.leftMainLayout.addRow("Name:", name)
            self.leftMainLayout.addRow("Surname:", surname)
            self.leftMainLayout.addRow("Phone:", phone)
            self.leftMainLayout.addRow("Email:", email)
            self.leftMainLayout.addRow("Adress:", address)

    def singleClickFunc(self):
        idValue = self.listWidget.currentItem().text().split('.')[0]
        query = "SELECT * FROM employees WHERE id=?"
        employee = cur.execute(query, (idValue,)).fetchone()
        if employee:
            print("udemy\\Section 4\\assets\\" + employee[5])
            img = QLabel()
            img.setPixmap(
                QPixmap("udemy\\Section 4\\assets\\" + employee[5]))
            name = QLabel(employee[1])
            surname = QLabel(employee[2])
            phone = QLabel(employee[3])
            email = QLabel(employee[4])
            address = QLabel(employee[6])

            for i in reversed(range(self.leftMainLayout.count())):
                widget = self.leftMainLayout.takeAt(i).widget()

                if widget is not None:
                    widget.deleteLater()

            self.leftMainLayout.addRow("", img)
            self.leftMainLayout.addRow("Name:", name)
            self.leftMainLayout.addRow("Surname:", surname)
            self.leftMainLayout.addRow("Phone:", phone)
            self.leftMainLayout.addRow("Email:", email)
            self.leftMainLayout.addRow("Adress:", address)

    def addEmployeeFunc(self):
        self.newEmployee = AddEmployee()
        self.close()

    def getEmployeesFunc(self):
        query = "SELECT id, name, surname FROM employees"
        employees = cur.execute(query).fetchall()
        for emp in employees:
            self.listWidget.addItem(
                "{}. {} {}".format(emp[0], emp[1], emp[2]))


class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450, 150, 400, 400)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):

        ########### Top Layout Widgets ############
        self.title = QLabel("Add Person")
        self.setStyleSheet("background-color:white; font-size:12pt")
        self.title.setStyleSheet(
            'font-size:24pt;font-family:Arial Bold;')
        self.img = QLabel()
        self.img.setPixmap(QPixmap("udemy\\Section 4\\assets\\user.png"))

        ########### Bottom Layout Widgets ############
        self.name = QLabel("Name:")
        self.nameEntry = QLineEdit("User1")
        self.nameEntry.setPlaceholderText("Enter your name")
        self.surname = QLabel("Surname:")
        self.surnameEntry = QLineEdit("Surname1")
        self.surnameEntry.setPlaceholderText("Enter your surname")
        self.phone = QLabel("Phone:")
        self.phoneEntry = QLineEdit("+91 1234567890")
        self.phoneEntry.setPlaceholderText("Enter your phone number")
        self.email = QLabel("Email:")
        self.emailEntry = QLineEdit("someone@somewhere.com")
        self.emailEntry.setPlaceholderText("Enter your email address")
        self.picture = QLabel("Picture:")
        self.pictureEntry = QPushButton("Browse")
        self.pictureEntry.setStyleSheet("background-color:orange")
        self.pictureEntry.clicked.connect(self.openImageFunc)
        self.address = QLabel("Address:")
        self.addressEntry = QTextEdit("Nowhere P.O, 00000")
        self.submitButton = QPushButton("Submit")
        self.submitButton.setStyleSheet("background-color:orange")
        self.submitButton.clicked.connect(self.submitButtonFunc)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.img)
        self.topLayout.setContentsMargins(20, 20, 10, 10)

        self.bottomLayout.addRow(self.name, self.nameEntry)
        self.bottomLayout.addRow(self.surname, self.surnameEntry)
        self.bottomLayout.addRow(self.phone, self.phoneEntry)
        self.bottomLayout.addRow(self.email, self.emailEntry)
        self.bottomLayout.addRow(self.picture, self.pictureEntry)
        self.bottomLayout.addRow(self.address, self.addressEntry)
        self.bottomLayout.addRow("", self.submitButton)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

    def submitButtonFunc(self):
        global defaultImage
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImage
        address = self.addressEntry.toPlainText()

        if name.strip() and surname.strip() and phone.strip() != "":
            try:
                query = "INSERT INTO employees (name, surname, phone, email, image, address) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(
                    self, "Success", "Person has been added")
            except:
                QMessageBox.information(
                    self, "Warning", "Person has not been added")

        else:
            QMessageBox.information(
                self, "Information", "Fields cannot be empty")

    def closeEvent(self, event):
        self.window = Window()

    def openImageFunc(self):
        global defaultImage
        self.fileName, ok = QFileDialog.getOpenFileName(
            self, 'Upload Image', '', 'Image Files (*jpg *.png)')
        if ok:
            size = (128, 128)
            defaultImage = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("udemy\\Section 4\\assets\{}".format(
                os.path.basename(self.fileName)))


class updateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employees")
        self.setGeometry(450, 150, 400, 400)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):

        ########### Top Layout Widgets ############
        self.title = QLabel("Update Details")
        self.setStyleSheet("background-color:white; font-size:12pt")
        self.title.setStyleSheet(
            'font-size:24pt;font-family:Arial Bold;')
        self.img = QLabel()
        self.img.setPixmap(QPixmap("udemy\\Section 4\\assets\\user.png"))

        ########### Bottom Layout Widgets ############
        self.name = QLabel("Name:")
        self.nameEntry = QLineEdit("User1")
        self.nameEntry.setPlaceholderText("Enter your name")
        self.surname = QLabel("Surname:")
        self.surnameEntry = QLineEdit("Surname1")
        self.surnameEntry.setPlaceholderText("Enter your surname")
        self.phone = QLabel("Phone:")
        self.phoneEntry = QLineEdit("+91 1234567890")
        self.phoneEntry.setPlaceholderText("Enter your phone number")
        self.email = QLabel("Email:")
        self.emailEntry = QLineEdit("someone@somewhere.com")
        self.emailEntry.setPlaceholderText("Enter your email address")
        self.picture = QLabel("Picture:")
        self.pictureEntry = QPushButton("Browse")
        self.pictureEntry.setStyleSheet("background-color:orange")
        self.address = QLabel("Address:")
        self.addressEntry = QTextEdit("Nowhere P.O, 00000")
        self.submitButton = QPushButton("Update")
        self.submitButton.setStyleSheet("background-color:orange")

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.img)
        self.topLayout.setContentsMargins(20, 20, 10, 10)

        self.bottomLayout.addRow(self.name, self.nameEntry)
        self.bottomLayout.addRow(self.surname, self.surnameEntry)
        self.bottomLayout.addRow(self.phone, self.phoneEntry)
        self.bottomLayout.addRow(self.email, self.emailEntry)
        self.bottomLayout.addRow(self.picture, self.pictureEntry)
        self.bottomLayout.addRow(self.address, self.addressEntry)
        self.bottomLayout.addRow("", self.submitButton)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
