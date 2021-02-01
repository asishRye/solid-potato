# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'splashidNBbv.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropshadowFrame = QFrame(self.centralwidget)
        self.dropshadowFrame.setObjectName(u"dropshadowFrame")
        self.dropshadowFrame.setStyleSheet(u"QFrame{\n"
                                           "	\n"
                                           "	background-color: rgb(56, 58, 89);\n"
                                           "	color:rgb(220,220,220);\n"
                                           "	border-radius:20px;\n"
                                           "}")
        self.dropshadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropshadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropshadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropshadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setFrameShadow(QFrame.Plain)
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropshadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 240, 471, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "	background-color: rgb(98, 114, 164);\n"
                                       "	border-radius:10px;\n"
                                       "	color:rgb(200,200,200);\n"
                                       "	border-style:none;\n"
                                       "	text-align:center;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk{\n"
                                       "	border-radius:10px;\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.431818, x2:1, y2:0.563, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
                                       "}")
        self.progressBar.setValue(24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.label_loading = QLabel(self.dropshadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 270, 661, 20))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(10)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setFrameShadow(QFrame.Plain)
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropshadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">PROCESS BUD</span></p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate(
            "SplashScreen", u"<strong>RPA Tool</strong>", None))
        self.label_loading.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p>Loading...</p></body></html>", None))
    # retranslateUi
