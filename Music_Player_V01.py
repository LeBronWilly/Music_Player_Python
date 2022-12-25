# -*- coding: utf-8 -*-
"""
Created on 12/25, 2022
@author: Willy Fang

"""

from UI_V01 import *
import os
import glob
from PySide2.QtWidgets import QMessageBox
import shutil


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Music_Player()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        pass





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    IG_Photo_Downloader = AppWindow()
    IG_Photo_Downloader.show()
    sys.exit(app.exec_())