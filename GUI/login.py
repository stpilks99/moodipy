import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font

login = Tk()
login.title("Welcome to Moodipy!")
login.configure(bg = "black")
login.resizable(width = False, height = False)
login.geometry("1400x780")

B = Button(login,
    text = "Login with Spotify",
    bg ="green",
    bd = 6, relief = "raised",
    width = 100,
    height = 10)
B.place(x = 350,y = 550)

canvas = Canvas(login, width = 850, height = 460)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("./GUI/snake.png"))
canvas.create_image(20, 20, anchor=NW, image=img) 

login.mainloop()

