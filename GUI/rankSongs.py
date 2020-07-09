import sys
#import spotipy
#import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

rankSongs = tk.Tk()
rankSongs.title("Time to rank songs!")
rankSongs.configure(bg = "black")
rankSongs.resizable(width = False, height = False)
rankSongs.geometry("900x680")

#creates done button that brings to playlist window
Done = Button(rankSongs, text = "Done", bg ="green", bd = 6, relief = "sunken", width = 20, height = 6)
Done.place(x = 710,y = 530)

#creates label with message 
lm = tk.Label(rankSongs, 
    text="  Here are your songs now rank them from 1-5  ", 
    fg = "black", 
    bg = "green", 
    bd = 6,
    relief = "sunken",
    font = "Helvetica 28 bold italic")

lm.place(x= 30, y = 50) 

#add query to find number of songs in playlist 

#do another query to pull song title

#creates a label with song 1 
s1 = tk.Label(rankSongs, text ='song 1', fg = "black", bg = "green", bd = 5, relief = "sunken", font = "Helvetica 20 bold italic")
s1.place(x = 47, y = 260)


sc1 = tk.Scale(rankSongs, from_= 1, to = 5) 
sc1.place(x = 75, y = 145)

s2 = tk.Label(rankSongs, text ='song 2', fg = "black", bg = "green", bd = 5, relief = "sunken", font = "Helvetica 20 bold italic")
s2.place(x = 197, y = 260) #added 150 to x

sc2 = tk.Scale(rankSongs, from_= 1, to = 5) 
sc2.place(x = 225, y = 145) #added 150 to x

s3 = tk.Label(rankSongs, text ='song 3', fg = "black", bg = "green", bd = 5, relief = "sunken", font = "Helvetica 20 bold italic")
s3.place(x = 347, y = 260) #added 150 to x

sc3 = tk.Scale(rankSongs, from_= 1, to = 5) 
sc3.place(x = 375, y = 145) #added 150 to x

rankSongs.mainloop()