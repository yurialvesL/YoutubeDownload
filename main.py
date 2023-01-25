import sys
import requests
import os
from Ui.DownUi import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QLabel,QComboBox,QMessageBox
from pytube import YouTube
from Avisos import Avisos





class Downtube(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setavalue()
        self.pushButton.clicked.connect(self.search_video)


    def setavalue(self) -> None:
        self.comboBox.addItems(['360p','480p','720p','1080p'])

    def search_video(self) -> None:
        if len(self.lineEdit.text()) == 0:
            aviso = Avisos()
            aviso.avisos('vazio')
        else:
            yt = YouTube(self.lineEdit.text())
            self.title_video.setText(yt.title)













if __name__ == '__main__':
    qt= QApplication(sys.argv)
    down = Downtube()
    down.show()
    qt.exec()
