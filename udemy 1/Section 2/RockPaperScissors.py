from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import sys

imageLocList = ['Paper', 'Rock', 'Scissors']
scoreDict = {'ai': 0, 'player': 0}


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissor")
        self.setGeometry(700, 150, 600, 400)
        self.UI()
        self.show()

    def UI(self):
        self.scoreLabel = QLabel("Score AI:0 You:0", self)
        self.scoreLabel.setGeometry(205, 30, 300, 20)
        self.scoreLabel.setFont(QFont("Arial", 18))

        self.aiLabel = QLabel("AI", self)
        self.aiLabel.move(110, 60)
        self.aiLabel.setFont(QFont("Arial", 15))

        self.aiImage = QLabel(self)
        self.aiImage.setPixmap(QPixmap(r"udemy\Section 2\assets\paper.png"))
        self.aiImage.move(50, 100)
        self.aiImage.show()

        self.vsImage = QLabel(self)
        self.vsImage.setPixmap(QPixmap(r"udemy\Section 2\assets\vs.png"))
        self.vsImage.move(230, 100)

        self.userLabel = QLabel("You", self)
        self.userLabel.move(460, 60)
        self.userLabel.setFont(QFont("Arial", 15))

        self.userImage = QLabel(self)
        self.userImage.setPixmap(QPixmap(r"udemy\Section 2\assets\paper.png"))
        self.userImage.move(390, 100)
        self.userImage.show()

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(imageLocList)
        self.comboBox.move(210, 250)

        self.playButton = QPushButton("Play", self)
        self.playButton.move(280, 249)
        self.playButton.clicked.connect(self.decide_Func)

        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.start()
        self.timer.timeout.connect(self.changeaiImage)

    def changeaiImage(self):
        choice = random.randrange(1, 4)-1
        self.aiImage.setPixmap(
            QPixmap(r"udemy\Section 2\\assets\\" + imageLocList[choice] + ".png"))
        self.userImage.setPixmap(
            QPixmap(r"udemy\Section 2\\assets\\" + imageLocList[choice] + ".png"))

    def decide_Func(self):

        self.timer.stop()
        userChoice = self.comboBox.currentIndex()

        aiChoice = random.randrange(1, 4)-1
        self.aiImage.setPixmap(
            QPixmap(r"udemy\Section 2\\assets\\" + imageLocList[aiChoice] + ".png"))
        self.userImage.setPixmap(
            QPixmap(r"udemy\Section 2\\assets\\" + imageLocList[userChoice] + ".png"))

        if imageLocList[aiChoice] == imageLocList[userChoice]:
            QMessageBox.information(self, "Information", "Draw")
        elif imageLocList[aiChoice] == 'Rock' and imageLocList[userChoice] == 'Paper':
            QMessageBox.information(self, "Information", "You Win")
            scoreDict['player'] += 1
        elif imageLocList[aiChoice] == 'Rock' and imageLocList[userChoice] == 'Scissors':
            QMessageBox.information(self, "Information", "You Lose")
            scoreDict['ai'] += 1
        elif imageLocList[aiChoice] == 'Paper' and imageLocList[userChoice] == 'Rock':
            QMessageBox.information(self, "Information", "You Lose")
            scoreDict['ai'] += 1
        elif imageLocList[aiChoice] == 'Paper' and imageLocList[userChoice] == 'Scissors':
            QMessageBox.information(self, "Information", "You Win")
            scoreDict['player'] += 1
        elif imageLocList[aiChoice] == 'Scissors' and imageLocList[userChoice] == 'Paper':
            QMessageBox.information(self, "Information", "You Lose")
            scoreDict['ai'] += 1
        elif imageLocList[aiChoice] == 'Scissors' and imageLocList[userChoice] == 'Rock':
            QMessageBox.information(self, "Information", "You Win")
            scoreDict['player'] += 1

        else:
            QMessageBox.information(
                self, "Information", "This game is broke :(")
        self.scoreLabel.setText(
            "Score AI: " + str(scoreDict['ai']) + " You: " + str(scoreDict['player']))

        if scoreDict['ai'] == 5 or scoreDict['player'] == 5:
            QMessageBox.information(self, "Game Over", max(
                scoreDict, key=scoreDict.get) + " won with " + str(scoreDict[max(scoreDict, key=scoreDict.get)]) + " scores.")
            scoreDict['ai'] = 0
            scoreDict['player'] = 0
            self.scoreLabel.setText("Score AI:0 You:0")

        self.timer.start()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
