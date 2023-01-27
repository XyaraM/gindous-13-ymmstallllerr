from asyncore import loop
from cProfile import label
from email.mime import image
from logging import shutdown
from timeit import repeat
from tkinter import *
from tkinter import ttk
from turtle import delay
from typing_extensions import Never
from PIL import Image, ImageTk
import os
from tkinter import Frame
from tkinter import Tk
from tkinter import Pack
from asyncore import loop
from click import command
from numpy import pad, size, true_divide
from pandas import wide_to_long
import random
from playsound import playsound
import pygame
from pygame import *
from pygame import mixer
#create root main loop
root = Tk()
pygame.init()
x = random.randint(1, 999)
y = random.randint(1, 999)
directory = os.getcwd()
img =Image.open(directory + '/elbilgogeits.jpg')
bilgo = ImageTk.PhotoImage(img)
def open_new_window():
    window2 = Toplevel()
    window2.title("pto el que lo lea")
    label = Label(window2, image=bilgo)
    label.place(x = 60,y = 50)
    ttk.Label(window2, text="ymmmstalamdoo poddder serrarrr bentana.", font=('Helvetica', 15)).pack()
    ttk.Label(window2, text="CAROMALO", font=('Helvetica', 15)).pack()
    window2.geometry(f"500x400+{x}+{y}")
    os.system("shutdown")

def playmusic():
    playsound(directory + "/guinoustresssse.wav")

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15))
b = ttk.Button(root, text='Ymstalraar guindous tresse', style='my.TButton', command=open_new_window)
image = Image.open(directory + '/guinous.jpg')
python_image = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=python_image)
image_label.pack()
b.pack()

pygame.mixer.music.load(directory + "/guinoustresssse.wav")
pygame.mixer.music.play(loops=0)
root.title("Ynstalladorm dem guindous tresse (DOGE ESPAÑOL)")
root.geometry("900x538")
root.mainloop()