import cv2
import numpy as np
import os
import time
from moviepy.editor import VideoFileClip
import threading
from tqdm import tqdm
import playsound
from shutil import get_terminal_size

class VideoToASCII:
    def __init__(self, filename):
        self.filename = filename
        self.clip = VideoFileClip(filename)
        self.chars = np.asarray(list(' .,:irs@9B#&@'))
        self.width, self.height = get_terminal_size()
        self.fps = self.clip.fps
        self.ascii_frames = self.render_video()

    def convert_frame_to_ascii(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (self.width, self.height), interpolation=cv2.INTER_AREA)
        ascii_frame = self.chars[(resized // 25)]
        return '\n'.join([''.join(row) for row in ascii_frame])

    def render_video(self):
        ascii_frames = []
        for frame in tqdm(self.clip.iter_frames(), desc="Rendering video", unit=" frames "):
            ascii_frame = self.convert_frame_to_ascii(frame)
            ascii_frames.append(ascii_frame)
        return ascii_frames

    def display_video(self):
        for ascii_frame in self.ascii_frames:
            os.system('cls')
            for row in ascii_frame.split('\n'):
                line = ''
                for char in row:
                    line += char
                print(line)
            time.sleep(0.65 / self.fps)

    def play(self):
        self.display_video()

def sound():
    playsound.playsound("CLIMVTEMPAUDIO.mp3")

if __name__ == '__main__':
    os.system("color 2")
    path = input("Enter path to video: ")
    vid = VideoToASCII(path)
    aud = VideoFileClip(path).audio
    with open(f"C:/Users/{str(os.getlogin())}/Downloads/CLIMVTEMPAUDIO.mp3", 'a') as f:
        aud.write_audiofile("CLIMVTEMPAUDIO.mp3")
    
    t1 = threading.Thread(target=vid.play)
    t2 = threading.Thread(target=sound)
    t1.start()
    t2.start()
