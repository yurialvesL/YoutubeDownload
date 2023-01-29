import sys
import requests
import os
import random
from Ui.DownUi import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QComboBox
from PyQt6.QtGui import QPixmap
from pytube import YouTube
from Avisos import Avisos


def download_thumb(title, link):
    f = open('img/' + title + '.jpg', 'wb')
    response = requests.get(link)
    f.write(response.content)
    f.close()


class Downtube(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setavalue()
        self.pushButton.clicked.connect(self.search_video)

    def setavalue(self) -> None:
        self.comboBox.addItems(['360p', '480p', '720p', '1080p'])
        self.progressBar.setValue(0)

    def search_video(self) -> None:
        if len(self.lineEdit.text()) == 0:
            aviso = Avisos()
            aviso.avisos('vazio')
        else:
            yt = YouTube(self.lineEdit.text())
            self.title_video.setText(yt.title)
            download_thumb(yt.title, yt.thumbnail_url)
            self.label.setPixmap(QPixmap('img/' + yt.title + '.jpg'))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    down = Downtube()
    down.show()
    qt.exec()
