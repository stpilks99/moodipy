import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

rankSongs = tk.Tk()
rankSongs.title("Time to rank songs!")
rankSongs.configure(bg = "black")
rankSongs.resizable(width = False, height = False)
rankSongs.geometry("900x680")

#creates done button that brings to playlist window
Done = Button(rankSongs, text = "Done", bg ="green", width = 20, height = 6)
Done.place(x = 710,y = 530)

#creates label with message 
lm = tk.Label(rankSongs, 
    text="Here are your songs now rank them from 1-5", 
    fg = "black", 
    bg = "green", 
    font = "Helvetica 28 bold italic")

lm.place(x= 47, y = 50) 

#add query to find number of songs in playlist 

#do another query to pull song title

#creates a label with song 1 
s1 = tk.Label(rankSongs, text ='song 1', fg = "black", bg = "green", font = "Helvetica 20 bold italic")
s1.place(x = 47, y = 260)


rankSongs.mainloop()