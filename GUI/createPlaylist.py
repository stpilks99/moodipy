import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

createPlaylist = tk.Tk()
createPlaylist.title("Time to create a new playlist!")
createPlaylist.configure(bg = "black")
createPlaylist.resizable(width = False, height = False)
createPlaylist.geometry("900x680")

#creates label with message 
lm = tk.Label(createPlaylist, 
    text="Just enter what you want and we will do the rest!", 
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "raised",
    font = "Helvetica 26 bold italic")

lm.place(x= 47, y = 50) 

def criteria():
    pName = playlistName.get()
    mSelected = moodsSelected.get()
    tSelected = timePeriod.get()
    artist = artistEntered.get()
    e = explicitOrNot.get()

    print(pName + "\n" + mSelected + "\n" + tSelected + "\n" + artist + "\n" + e )
    selection = listbox.curselection()
    for i in selection:
        gselected = listbox.get(i)
        print(gselected)


#creates label for entry and entry so user can enter playlist title
lt = tk.Label(createPlaylist, text ='Playlist title:', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
lt.place(x = 47, y = 150)

playlistName = Entry(createPlaylist, font = "Helvetica 22 italic") 
playlistName.place(x = 230, y = 155) 

#creates a drop down list where the user can select a mood with a label next to it
Lmd = tk.Label(createPlaylist, text = "Select one mood:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lmd.place(x = 47, y = 210)

moods = ["Happy", 
        "Sad", 
        "Motivated", 
        "Calm",
        "Frantic",
        "Party",
        "Gaming"]

moodsSelected = ttk.Combobox(createPlaylist, values = moods, font = "Helvetica 22 italic")
moodsSelected.place(x = 300, y = 215)

#creates a drop down list where the user can select a time period
Lp = tk.Label(createPlaylist, text = "Select time period:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lp.place(x = 47, y = 270)

times = ["2010's +",
        "2000's", 
        "90's", 
        "80's", 
        "70's",
        "None"]

timePeriod = ttk.Combobox(createPlaylist, values = times, font = "Helvetica 22 italic")
timePeriod.place(x = 317, y = 275)

#creates a entry where user can enter prefered artist
Lpa = tk.Label(createPlaylist, text = "Enter preferred artist:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lpa.place(x = 47, y = 330)
artistEntered = Entry(createPlaylist, font = "Helvetica 22 italic") 
artistEntered.place(x = 355, y = 335) 

#creates a checkbox where the user can select preferred genres
Lg = tk.Label(createPlaylist, text = "Enter preferred genres:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Lg.place(x = 47, y = 390)

msg = tk.Label(createPlaylist, text = " Please select the\ngenres you want last. \nIf not highlighted blue\n then they are not selected. ", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 12 bold italic" )
msg.place(x =645, y = 115)

genres = ["Acoustic", "Alternative", "Classical", "Club", "Country", "Dubstep", "EDM", "Funk", "Rock", "Hard Rock", "Heavy Metal", "Hip Hop", "Indie", "Holidays", "Latin", "Pop", "RnB", "Reggae", "Soul", "Jazz", "Afrobeat"]

listbox = Listbox(createPlaylist, bg = "white", height = 2, width = 42, bd = 6, relief = "sunken", font = "Helvetica 12 bold italic", selectmode = MULTIPLE) 
listbox.pack(side = RIGHT, fill = BOTH) 
listbox.place(x = 370, y = 388)
scrollbar = Scrollbar(createPlaylist) 

for values in genres: 
    listbox.insert(END, values) 

listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview) 

#creates a drop down list where the user can select yes for explict or no for non explicit
Le = tk.Label(createPlaylist, text = "Would you like explict songs:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
Le.place(x = 47, y = 450)

options = ["Yes", 
        "No", ]

explicitOrNot = ttk.Combobox(createPlaylist, values = options, font = "Helvetica 22 italic")
explicitOrNot.place(x = 450, y = 455)

#creates done button that brings to playlist window
Done = Button(createPlaylist, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = criteria)
Done.place(x = 685, y = 530)

#creates cancel button that brings back to homepage
Cancel = Button(createPlaylist, text = "Cancel", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
Cancel.place(x = 42, y = 530)

createPlaylist.mainloop()