# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Music_Player_UI_V01cJAppO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Music_Player(object):
    def setupUi(self, Music_Player):
        if not Music_Player.objectName():
            Music_Player.setObjectName(u"Music_Player")
        Music_Player.resize(680, 478)
        self.Refresh_Button = QPushButton(Music_Player)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(250, 30, 161, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Refresh_Button.setFont(font)
        self.label_2 = QLabel(Music_Player)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Label_WillyF = QLabel(Music_Player)
        self.Label_WillyF.setObjectName(u"Label_WillyF")
        self.Label_WillyF.setGeometry(QRect(10, 440, 411, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.Label_WillyF.setFont(font2)
        self.Label_WillyF.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Songs_ListWidget = QListWidget(Music_Player)
        QListWidgetItem(self.Songs_ListWidget)
        QListWidgetItem(self.Songs_ListWidget)
        QListWidgetItem(self.Songs_ListWidget)
        self.Songs_ListWidget.setObjectName(u"Songs_ListWidget")
        self.Songs_ListWidget.setGeometry(QRect(30, 80, 381, 291))
        font3 = QFont()
        font3.setPointSize(14)
        self.Songs_ListWidget.setFont(font3)
        self.Songs_ListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Play_Button = QPushButton(Music_Player)
        self.Play_Button.setObjectName(u"Play_Button")
        self.Play_Button.setEnabled(True)
        self.Play_Button.setGeometry(QRect(470, 80, 161, 41))
        self.Play_Button.setFont(font)
        self.Pause_Button = QPushButton(Music_Player)
        self.Pause_Button.setObjectName(u"Pause_Button")
        self.Pause_Button.setEnabled(True)
        self.Pause_Button.setGeometry(QRect(470, 130, 161, 41))
        self.Pause_Button.setFont(font)
        self.Resume_Button = QPushButton(Music_Player)
        self.Resume_Button.setObjectName(u"Resume_Button")
        self.Resume_Button.setEnabled(True)
        self.Resume_Button.setGeometry(QRect(470, 180, 161, 41))
        self.Resume_Button.setFont(font)
        self.Previous_Button = QPushButton(Music_Player)
        self.Previous_Button.setObjectName(u"Previous_Button")
        self.Previous_Button.setEnabled(True)
        self.Previous_Button.setGeometry(QRect(470, 230, 161, 41))
        self.Previous_Button.setFont(font)
        self.Next_Button = QPushButton(Music_Player)
        self.Next_Button.setObjectName(u"Next_Button")
        self.Next_Button.setEnabled(True)
        self.Next_Button.setGeometry(QRect(470, 280, 161, 41))
        self.Next_Button.setFont(font)
        self.Stop_Button = QPushButton(Music_Player)
        self.Stop_Button.setObjectName(u"Stop_Button")
        self.Stop_Button.setEnabled(True)
        self.Stop_Button.setGeometry(QRect(470, 330, 161, 41))
        self.Stop_Button.setFont(font)

        self.retranslateUi(Music_Player)

        QMetaObject.connectSlotsByName(Music_Player)
    # setupUi

    def retranslateUi(self, Music_Player):
        Music_Player.setWindowTitle(QCoreApplication.translate("Music_Player", u"Music_Player", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Music_Player", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("Music_Player", u"Songs List:", None))
        self.Label_WillyF.setText(QCoreApplication.translate("Music_Player", u"Developed by Willy Fang", None))

        __sortingEnabled = self.Songs_ListWidget.isSortingEnabled()
        self.Songs_ListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.Songs_ListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Music_Player", u"1", None));
        ___qlistwidgetitem1 = self.Songs_ListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Music_Player", u"2", None));
        ___qlistwidgetitem2 = self.Songs_ListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Music_Player", u"3", None));
        self.Songs_ListWidget.setSortingEnabled(__sortingEnabled)

        self.Play_Button.setText(QCoreApplication.translate("Music_Player", u"Play", None))
        self.Pause_Button.setText(QCoreApplication.translate("Music_Player", u"Pause", None))
        self.Resume_Button.setText(QCoreApplication.translate("Music_Player", u"Resume", None))
        self.Previous_Button.setText(QCoreApplication.translate("Music_Player", u"Previous", None))
        self.Next_Button.setText(QCoreApplication.translate("Music_Player", u"Next", None))
        self.Stop_Button.setText(QCoreApplication.translate("Music_Player", u"Stop", None))
    # retranslateUi

