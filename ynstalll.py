from asyncore import loop
from cProfile import label
from email.mime import image
from logging import shutdown
from timeit import repeat
from tkinter import *
from tkinter import ttk
from turtle import delay
from typing_extensions import Never
import webbrowser
import PIL
from PIL import Image, ImageTk
import os
from tkinter import Frame
from tkinter import Tk
import tkinter
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
import time
#create root main loop
root = Tk()
pygame.init()
x = random.randint(1, 999)
y = random.randint(1, 999)
directory = os.getcwd()

def open_new_window():
    window2 = Toplevel()
    window2.title("pto el que lo lea")
    ttk.Label(window2, text="Tu pc se apagara en 5 segundos", font=('Helvetica', 15)).pack()
    window2.geometry(f"200x500+{x}+{y}")
    webbrowser.open("https://www.youtube.com/watch?v=o-YBDTqX_ZU")
    os.system("shutdown /s /t 5")

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
root.title("Ynstalladorm dem guindous tresse")
root.geometry("900x538")
root.mainloop()