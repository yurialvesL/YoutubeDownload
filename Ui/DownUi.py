# Form implementation generated from reading ui file 'DownUi.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 584)
        MainWindow.setMinimumSize(QtCore.QSize(466, 584))
        MainWindow.setMaximumSize(QtCore.QSize(466, 584))
        MainWindow.setStyleSheet("QMainWindow{\n"
"Background-color:black\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"Color:white\n"
"}\n"
"\n"
"QFrame{\n"
"Background-color:transparent;\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"Background-color:Transparent;\n"
"Border-Bottom: 2px solid white;\n"
"Border-Top: None;\n"
"Color:white;\n"
"\n"
"}\n"
"\n"
"QProgressBar{\n"
"Color:White;\n"
"border-radius:15px;\n"
"Text-align:center;\n"
"}\n"
"\n"
"QLabel{\n"
"text-align:center;\n"
"}\n"
"\n"
"QCheckBox{\n"
"Color:white;\n"
"Background-color: transparent;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_tittle_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tittle_url.setGeometry(QtCore.QRect(40, 400, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tittle_url.setFont(font)
        self.lbl_tittle_url.setObjectName("lbl_tittle_url")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 400, 231, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(340, 400, 75, 23))
        self.btn_search.setObjectName("btn_search")
        self.title_video = QtWidgets.QLabel(self.centralwidget)
        self.title_video.setGeometry(QtCore.QRect(90, 360, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_video.setFont(font)
        self.title_video.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title_video.setStyleSheet("")
        self.title_video.setObjectName("title_video")
        self.chk_audionly = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_audionly.setGeometry(QtCore.QRect(280, 450, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chk_audionly.setFont(font)
        self.chk_audionly.setObjectName("chk_audionly")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(190, 500, 75, 23))
        self.btn_download.setObjectName("btn_download")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(160, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 431, 271))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Download/no-internet (1).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lbl_video_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_video_status.setGeometry(QtCore.QRect(126, 540, 181, 20))
        self.lbl_video_status.setText("")
        self.lbl_video_status.setObjectName("lbl_video_status")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 430, 120, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.cb_res = QtWidgets.QComboBox(self.frame)
        self.cb_res.setGeometry(QtCore.QRect(10, 20, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cb_res.setFont(font)
        self.cb_res.setCurrentText("")
        self.cb_res.setObjectName("cb_res")
        self.frame.raise_()
        self.lbl_tittle_url.raise_()
        self.lineEdit.raise_()
        self.btn_search.raise_()
        self.title_video.raise_()
        self.chk_audionly.raise_()
        self.btn_download.raise_()
        self.lbl_title.raise_()
        self.label.raise_()
        self.lbl_video_status.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cb_res.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DownTube"))
        self.lbl_tittle_url.setText(_translate("MainWindow", "URL:"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.title_video.setText(_translate("MainWindow", "TITULO"))
        self.chk_audionly.setText(_translate("MainWindow", "Somente audio"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.lbl_title.setText(_translate("MainWindow", "DOWNTUBE"))
