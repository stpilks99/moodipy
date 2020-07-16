import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

removeSong = tk.Tk()
removeSong.title("Time to remove a song to the playlist!")
removeSong.configure(bg = "black")
removeSong.resizable(width = False, height = False)
removeSong.geometry("900x680")

lt = tk.Label(removeSong, text ='Please enter the title of the song\ntitle you would like to remove:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 3,
                width = 26,
                font = "Helvetica 36 bold italic")

e1 = Entry(removeSong, font = "Helvetica 40 italic", width = 27) 
lt.place(x = 56, y = 70)
e1.place(x = 65, y = 320) 

#creates Remove button that brings to playlist window
Remove = Button(removeSong, text = "Remove", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 10, 
                height = 3)

Remove.place(x = 600, y = 460)

removeSong.mainloop()