# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Music_Player_UI_V01EhLIkW.ui'
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
        self.List_Label = QLabel(Music_Player)
        self.List_Label.setObjectName(u"List_Label")
        self.List_Label.setGeometry(QRect(30, 30, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.List_Label.setFont(font1)
        self.List_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.WillyF_Label = QLabel(Music_Player)
        self.WillyF_Label.setObjectName(u"WillyF_Label")
        self.WillyF_Label.setGeometry(QRect(10, 440, 411, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.WillyF_Label.setFont(font2)
        self.WillyF_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
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
        self.Resume_Button.setEnabled(False)
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
        self.Current_Label = QLabel(Music_Player)
        self.Current_Label.setObjectName(u"Current_Label")
        self.Current_Label.setGeometry(QRect(30, 380, 601, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.Current_Label.setFont(font4)
        self.Current_Label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.retranslateUi(Music_Player)

        QMetaObject.connectSlotsByName(Music_Player)
    # setupUi

    def retranslateUi(self, Music_Player):
        Music_Player.setWindowTitle(QCoreApplication.translate("Music_Player", u"Music_Player", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Music_Player", u"Refresh All", None))
        self.List_Label.setText(QCoreApplication.translate("Music_Player", u"Songs List:", None))
        self.WillyF_Label.setText(QCoreApplication.translate("Music_Player", u"Developed by WillyF", None))

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
        self.Current_Label.setText(QCoreApplication.translate("Music_Player", u"Now Playing: ", None))
    # retranslateUi

