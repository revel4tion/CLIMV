import cv2
import numpy as np
import os
import time
from colorama import init, Fore, Style
from moviepy.editor import VideoFileClip
import playsound
import threading


class VideoToASCII:
    def __init__(self, filename):
        self.filename = filename
        self.clip = VideoFileClip(filename)
        self.chars = np.asarray(list(' .,:irs@9B#&@'))
        self.width = 80
        self.height = 60
        self.fps = self.clip.fps

    def convert_frame_to_ascii(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (self.width, self.height), interpolation=cv2.INTER_AREA)
        ascii_frame = self.chars[(resized // 25)]
        return '\n'.join([''.join(row) for row in ascii_frame])

    def play(self):
        init(autoreset=True)
        for frame in self.clip.iter_frames():
            ascii_frame = self.convert_frame_to_ascii(frame)
            os.system('cls' if os.name == 'nt' else 'clear')
            for row in ascii_frame.split('\n'):
                line = ''
                for char in row:
                    line += f"{Fore.GREEN}{char}{Style.RESET_ALL}"
                print(line)
            time.sleep(1 / self.fps)

def sound():
    playsound.playsound("audio921837129837.mp3")

if __name__ == '__main__':
    path = input("Enter path to video: ")
    vid = VideoToASCII(path)
    aud = VideoFileClip(path).audio
    os.chdir(f"C:/Users/{str(os.getlogin())}/Downloads")
    with open(f"C:/Users/{str(os.getlogin())}/Downloads/audio921837129837.mp3", 'a') as f:
        aud.write_audiofile("audio921837129837.mp3")
    
    t1 = threading.Thread(target=vid.play)
    t2 = threading.Thread(target=sound)
    t1.start()
    t2.start()
