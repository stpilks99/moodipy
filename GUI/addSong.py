import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

addSong = tk.Tk()
addSong.title("Time to add a song to the playlist!")
addSong.configure(bg = "black")
addSong.resizable(width = False, height = False)
addSong.geometry("900x680")

lt = tk.Label(addSong, text ='Please enter the song title\nyou would like to add:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 3,
                width = 25,
                font = "Helvetica 37 bold italic")

e1 = Entry(addSong, font = "Helvetica 40 italic", width = 26) 
lt.place(x = 65, y = 70)
e1.place(x = 65, y = 320) 

#creates Add button that brings to playlist window
Add = Button(addSong, text = "Add", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 10, 
                height = 3)

Add.place(x = 600, y = 460)

addSong.mainloop()