import os, sys
from moviepy.editor import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

unconverted = []


def media():
    global unconverted
    files = os.listdir(os.getcwd())
    videos = []
    audios = []
    for i in files:
        if '.mp4' in i:
            # print(i)
            videos.append(i)
        elif '.mp3' in i:
            audios.append(i)

    for i in videos:
        if i[:-1]+'3' in audios:
            print(f'{i} соответствует {i[:-1]+"3"}')
        else:
            print(f"{i} беспризорник")
            unconverted.append(i)


def convert(video_file: str):
    path = os.getcwd()
    if video_file[:-3]+'mp3' not in os.listdir(os.getcwd()):
        video = VideoFileClip(f'{path}\{video_file}')
        video.audio.write_audiofile(f'{path}\{video_file[:-4]}.mp3')
        video.close()
    else: print("Аудио от этого видео уже существует")


def convertation():
    if unconverted:
        for i in unconverted:
            convert(i)
    else: print("Нечего конвертировать")


if __name__ == '__main__':
    media()
    convert('videoplayback.mp4')
# print(os.chdir('C:/Users/Andreuff/VideoConverter'))
# video = VideoFileClip(r'C:\Users\Andreuff\VideoConverter\НОВЫЙ ГОДд.mp4')
# video.audio.write_audiofile(r'C:\Users\Andreuff\VideoConverter\taxi15.mp3')
# video.close()
