import sys
#import spotipy
#import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

createPlaylist = tk.Tk()
createPlaylist.title("Time to create a new playlist!")
createPlaylist.configure(bg = "black")
createPlaylist.resizable(width = False, height = False)
createPlaylist.geometry("900x680")

#creates done button that brings to playlist window
Done = Button(createPlaylist, text = "Done", bg ="green", bd = 6, relief = "raised", width = 20, height = 6)
Done.place(x = 710,y = 530)

#creates cancel button that brings back to homepage
Cancel = Button(createPlaylist, text = "Cancel", bg ="green", bd = 6, relief = "raised", width = 20, height = 6)
Cancel.place(x = 42, y = 530)

#creates label with message 
lm = tk.Label(createPlaylist, 
    text="Just enter what you want and we will do the rest!", 
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "raised",
    font = "Helvetica 26 bold italic")

lm.place(x= 47, y = 50) 

#creates entry so user can enter playlist title
lt = tk.Label(createPlaylist, text ='Playlist title:', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
e1 = Entry(createPlaylist, font = "Helvetica 22 italic") 
lt.place(x = 150, y = 150)
e1.place(x = 330, y = 150) 

#creates a drop down list where the user can select a mood with a label next to it
Lmd = tk.Label(createPlaylist, text = "Select one mood:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lmd.place(x = 150, y = 210)

moods = ["Happy", 
        "Sad", 
        "Motivated", 
        "Calm",
        "Frantic",
        "Party",
        "Gaming"]

dropl = ttk.Combobox(createPlaylist, values = moods, font = "Helvetica 22 italic")
dropl.place(x = 400, y = 210)

#creates a drop down list where the user can select a time period
Lp = tk.Label(createPlaylist, text = "Select time period:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lp.place(x = 150, y = 270)

times = ["2010's +",
        "2000's", 
        "90's", 
        "80's", 
        "70's",
        "None"]

dropl = ttk.Combobox(createPlaylist, values = times, font = "Helvetica 22 italic")
dropl.place(x = 425, y = 270)

#creates a entry where user can enter prefered artist
Lp = tk.Label(createPlaylist, text = "Enter preferred artist:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lp.place(x = 150, y = 330)
e2 = Entry(createPlaylist, font = "Helvetica 22 italic") 
e2.place(x = 452, y = 330) 

#creates a checkbox where the user can select preferred genres
La = tk.Label(createPlaylist, text = "Enter preferred genres:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
La.place(x = 150, y = 390)

menubutton = tk.Menubutton(createPlaylist, text="Check all preferred genres", indicatoron=True, borderwidth=1, relief="raised", font = "Helvetica 22 italic")

menu = tk.Menu(menubutton, tearoff=False)
menubutton.configure(menu=menu) 
menubutton.place(x = 475, y = 390)

genres = {}
for genre in ("Acoustic", "Alternative", "Classical", "Club", "Country", "Dubstep", "EDM", "Funk", "Rock", "Hard Rock", "Heavy Metal", "Hip Hop", "Indie", "Holidays", "Latin", "Pop", "RnB", "Reggae", "Soul", "Jazz", "Afrobeat"):
        genres[genre] = tk.IntVar(value=0)
        menu.add_checkbutton(label=genre, variable=genres[genre], onvalue=1)

#creates a drop down list where the user can select yes for explict or no for non explicit
La = tk.Label(createPlaylist, text = "Would you like explict songs:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
La.place(x = 150, y = 450)

options = ["Yes", 
        "No", ]

dropl = ttk.Combobox(createPlaylist, values = options, font = "Helvetica 22 italic")
dropl.place(x = 540, y = 450)

createPlaylist.mainloop()