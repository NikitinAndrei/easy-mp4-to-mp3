# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoToAudio(object):
    def setupUi(self, VideoToAudio):
        VideoToAudio.setObjectName("VideoToAudio")
        VideoToAudio.resize(442, 215)
        self.centralwidget = QtWidgets.QWidget(VideoToAudio)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        VideoToAudio.setCentralWidget(self.centralwidget)

        self.retranslateUi(VideoToAudio)
        QtCore.QMetaObject.connectSlotsByName(VideoToAudio)

    def retranslateUi(self, VideoToAudio):
        _translate = QtCore.QCoreApplication.translate
        VideoToAudio.setWindowTitle(_translate("VideoToAudio", "Видео в аудио"))
        self.label.setText(_translate("VideoToAudio", "Видео в папке и их аудио"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoToAudio = QtWidgets.QMainWindow()
    ui = Ui_VideoToAudio()
    ui.setupUi(VideoToAudio)
    VideoToAudio.show()
    sys.exit(app.exec_())
