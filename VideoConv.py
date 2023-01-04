import os, sys
from moviepy.editor import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Видео в аудио")
    window.setGeometry(300, 250, 300, 200)

    text = 

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    print(os.getcwd())
    application()
# print(os.chdir('C:/Users/Andreuff/VideoConverter'))
# video = VideoFileClip(r'C:\Users\Andreuff\VideoConverter\НОВЫЙ ГОДд.mp4')
# video.audio.write_audiofile(r'C:\Users\Andreuff\VideoConverter\taxi15.mp3')
# video.close()
