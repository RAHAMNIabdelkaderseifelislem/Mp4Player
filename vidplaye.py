#import library to enter videos
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#import library to play videos
from moviepy.editor import *
import pygame
#choose video you want
Tk().withdraw()
video = askopenfilename()
#playing video
pygame.init()

pygame.display.set_caption('Show Video on screen')

video = VideoFileClip(video)
video.preview()

pygame.quit()