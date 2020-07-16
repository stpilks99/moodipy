import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

deletePlaylist = tk.Tk()
deletePlaylist.title("Time to delete a playlist!")
deletePlaylist.configure(bg = "black")
deletePlaylist.resizable(width = False, height = False)
deletePlaylist.geometry("900x680")

c = Canvas(deletePlaylist, width = 834, height = 330, bg = "gray")
c.place(x = 32, y = 310)

lt = tk.Label(deletePlaylist, text ='Are you sure you want to delete this playlist?\nclick yes to confirm\nclick no to return to your playlist', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 5,
                width = 36,
                font = "Helvetica 28 bold italic")

lt.place(x = 28, y = 50)

yes = Button(c, text = "yes", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 10, 
                height = 3)

yes.place(x = 480, y = 80)

no = Button(c, text = "no", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 10, 
                height = 3)

no.place(x = 100, y = 80)

deletePlaylist.mainloop()
