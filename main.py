import sys
import requests
import os
import random
from Ui.DownUi import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap
from pytube import YouTube
from Avisos import Avisos


def download_thumb(title, link):
    symbols = ['[',']','(',')','"','!','|']
    for i in symbols:
        if i in title:
            title = title.replace(i,'')
    f = open('img/' + title + '.jpg', 'wb')
    response = requests.get(link)
    f.write(response.content)
    f.close()
    return title


class Downtube(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setavalue()
        self.btn_search.clicked.connect(self.search_video)
        self.btn_download.clicked.connect(self.down_video)

    def setavalue(self) -> None:
        self.cb_res.addItems(['360p', '480p', '720p', '1080p'])


    def search_video(self) -> None:
        if len(self.lineEdit.text()) == 0:
            aviso = Avisos()
            aviso.avisos('vazio')
        else:
            yt = YouTube(self.lineEdit.text())
            self.title_video.setText(yt.title)
            title = download_thumb(yt.title, yt.thumbnail_url)

            self.label.setPixmap(QPixmap('img/' + title + '.jpg'))

    def down_video(self) -> None:
        match self.cb_res.currentText():
            case '360p':
                self.lbl_video_status.setText('Baixando aguarde...')
                file = QFileDialog.getExistingDirectory(caption='Selecione a pasta')
                youtube = YouTube(self.lineEdit.text())
                youtube.streams.filter(file_extension='mp4').get_by_resolution(self.cb_res.currentText()).download(output_path=file)
                self.lbl_video_status('Sucesso!')
            case '480p':
                self.lbl_video_status.setText('Baixando aguarde...')
                file = QFileDialog.getExistingDirectory(caption='Selecione a pasta')
                youtube = YouTube(self.lineEdit.text())
                youtube.streams.filter(file_extension='mp4').get_by_resolution(self.cb_res.currentText()).download(
                    output_path=file)
                self.lbl_video_status('Sucesso!')
            case '720p':
                self.lbl_video_status.setText('Baixando aguarde...')
                file = QFileDialog.getExistingDirectory(caption='Selecione a pasta')
                youtube = YouTube(self.lineEdit.text())
                youtube.streams.filter(file_extension='mp4').get_by_resolution(self.cb_res.currentText()).download(
                    output_path=file)
                self.lbl_video_status('Sucesso!')
            case '1080p':
                self.lbl_video_status.setText('Baixando aguarde...')
                file = QFileDialog.getExistingDirectory(caption='Selecione a pasta')
                youtube = YouTube(self.lineEdit.text())
                youtube.streams.filter(file_extension='mp4').get_by_resolution(self.cb_res.currentText()).download(
                    output_path=file)
                self.lbl_video_status('Sucesso!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    down = Downtube()
    down.show()
    qt.exec()
