# -*- coding: utf-8 -*-
"""
Created on 12/25, 2022 (Merry Christmas!!!)
@author: Willy Fang (WillyF)

"""

# https://www.geeksforgeeks.org/pyqt5-qlistwidget-getting-count-of-items/
# https://stackoverflow.com/questions/33919150/getting-selected-rows-in-qlistwidget
# https://www.geeksforgeeks.org/pyqt5-qlistwidget-setting-current-item/
# https://stackoverflow.com/questions/21566556/how-to-get-a-current-items-info-from-qtgui-qlistwidget
# https://www.geeksforgeeks.org/pyqt5-qlistwidget-current-selected-row-signal/
# https://pythongeeks.org/python-music-player/
# https://python.plainenglish.io/how-to-make-your-own-music-player-using-python-5f84c08be950
# https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2
# https://data-flair.training/blogs/python-mp3-player/
# https://techvidvan.com/tutorials/python-create-mp3-music-player/
# https://www.geeksforgeeks.org/pyqt5-how-to-add-image-in-window/
# https://www.geeksforgeeks.org/how-to-set-icon-to-a-window-in-pyqt5/
# https://stackoverflow.com/questions/11073972/pyqt-set-qlabel-image-from-url
# https://stackoverflow.com/questions/17504653/why-qpixmapscaled-does-not-work
# https://www.pygame.org/docs/ref/music.html
# https://www.adamsmith.haus/python/answers/how-to-format-a-number-as-a-percentage-in-python
# https://stackoverflow.com/questions/12876935/python-qt-qlistwidget-double-clicked

from UI_V01 import *
from pygame import mixer, time
from glob import glob
import urllib.request

mixer.init()
volume = 1


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Music_Player()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("christmas-carols.png"))
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.Xmas_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/Music_Player_Python/main/christmas-carols.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.Xmas_img.loadFromData(img_data)
        self.ui.Xmas_img = self.ui.Xmas_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.Xmas_img))
        self.ui.Xmas_Label.setPixmap(self.ui.Xmas_img)
        self.ui.Xmas_Label.setAlignment(Qt.AlignCenter)
        self.ui.Songs_ListWidget.clear()
        self.ui.Songs_ListWidget.addItems([i.replace("Music_Folder\\", "") for i in glob("Music_Folder/*.mp3")])
        if len(glob("Music_Folder/*.mp3")) > 0:
            self.ui.Songs_ListWidget.setCurrentRow(0)
        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)
        self.ui.Songs_ListWidget.itemDoubleClicked.connect(self.Play_Button_Clicked)
        self.ui.Play_Button.clicked.connect(self.Play_Button_Clicked)
        self.ui.Pause_Button.clicked.connect(self.Pause_Button_Clicked)
        self.ui.Resume_Button.clicked.connect(self.Resume_Button_Clicked)
        self.ui.Previous_Button.clicked.connect(self.Previous_Button_Clicked)
        self.ui.Next_Button.clicked.connect(self.Next_Button_Clicked)
        self.ui.Stop_Button.clicked.connect(self.Stop_Button_Clicked)
        self.ui.Turn_Up_Button.clicked.connect(self.Turn_Up_Button_Clicked)
        self.ui.Turn_Down_Button.clicked.connect(self.Turn_Down_Button_Clicked)

    def Turn_Up_Button_Clicked(self):
        global volume
        volume += 0.1
        if volume >= 1:
            volume = 1
        mixer.music.set_volume(volume)
        print("Current Volume:", "{:.0%}".format(round(mixer.music.get_volume(), 1)))

    def Turn_Down_Button_Clicked(self):
        global volume
        volume -= 0.1
        if volume <= 0.0:
            volume = 0.0
        mixer.music.set_volume(volume)
        print("Current Volume:", "{:.0%}".format(round(mixer.music.get_volume(), 1)))

    def Refresh_Button_Clicked(self):
        self.ui.Songs_ListWidget.clear()
        self.ui.Songs_ListWidget.addItems([i.replace("Music_Folder\\", "") for i in glob("Music_Folder/*.mp3")])
        if len(glob("Music_Folder/*.mp3")) > 0:
            self.ui.Songs_ListWidget.setCurrentRow(0)
        mixer.music.stop()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        self.ui.Current_Label.setText("Now Playing: ")

    def Play_Button_Clicked(self):
        # print("Music_Folder\\"+self.ui.Songs_ListWidget.currentItem().text())
        mixer.music.unpause()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        mixer.music.load("Music_Folder\\"+self.ui.Songs_ListWidget.currentItem().text())
        # n = self.ui.Songs_ListWidget.currentRow()
        # item_list = [self.ui.Songs_ListWidget.item(x).text() for x in range(self.ui.Songs_ListWidget.count())]
        # item_list = sorted(item_list)
        # item_list = item_list[n:] + item_list[:n]
        # item_list = item_list[:n][::-1] + item_list[n:][::-1]
        # item_list = item_list[n - 1::-1] + item_list[:n - 1:-1] + item_list[n - 1:n]
        # print(item_list)



        # for i, song in enumerate(item_list):
        #     print(song)
        #     if i == 0:
        #         mixer.music.load("Music_Folder\\"+song)
        #         mixer.music.play(0)
        #     else:
        #         mixer.music.queue("Music_Folder\\"+song)
        # print()


        mixer.music.play(loops=-1)
        # mixer.music.play()
        self.ui.Current_Label.setText("Now Playing: "+self.ui.Songs_ListWidget.currentItem().text())
        # while mixer.music.get_busy():
        #     time.Clock().tick(5)

# https://stackoverflow.com/questions/61202506/play-all-songs-in-pygame

    def Pause_Button_Clicked(self):
        mixer.music.pause()
        self.ui.Resume_Button.setEnabled(True)
        self.ui.Pause_Button.setEnabled(False)
        pass

    def Resume_Button_Clicked(self):
        mixer.music.unpause()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        pass

    def Previous_Button_Clicked(self):
        mixer.music.unpause()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        n = self.ui.Songs_ListWidget.currentRow()
        if n == 0:
            self.ui.Songs_ListWidget.setCurrentRow(self.ui.Songs_ListWidget.count() - 1)
        else:
            self.ui.Songs_ListWidget.setCurrentRow(n - 1)
        self.Play_Button_Clicked()
        # print("Music_Folder\\" + self.ui.Songs_ListWidget.currentItem().text())
        # mixer.music.load("Music_Folder\\" + self.ui.Songs_ListWidget.currentItem().text())
        # mixer.music.play(loops=-1)
        # self.ui.Current_Label.setText("Now Playing: " + self.ui.Songs_ListWidget.currentItem().text())

    def Next_Button_Clicked(self):
        mixer.music.unpause()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        n = self.ui.Songs_ListWidget.currentRow()
        if n == self.ui.Songs_ListWidget.count() - 1:
            self.ui.Songs_ListWidget.setCurrentRow(0)
        else:
            self.ui.Songs_ListWidget.setCurrentRow(n + 1)
        self.Play_Button_Clicked()
        # print("Music_Folder\\" + self.ui.Songs_ListWidget.currentItem().text())
        # mixer.music.load("Music_Folder\\" + self.ui.Songs_ListWidget.currentItem().text())
        # mixer.music.play(loops=-1)
        # self.ui.Current_Label.setText("Now Playing: " + self.ui.Songs_ListWidget.currentItem().text())

    def Stop_Button_Clicked(self):
        mixer.music.stop()
        self.ui.Pause_Button.setEnabled(True)
        self.ui.Resume_Button.setEnabled(False)
        self.ui.Current_Label.setText("Now Playing: ")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    IG_Photo_Downloader = AppWindow()
    IG_Photo_Downloader.show()
    sys.exit(app.exec_())


