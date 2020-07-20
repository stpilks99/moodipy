import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
import os

from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox 

ep = Tk()
ep.title("View Playlist")
ep.configure(bg = "black")
ep.resizable(width = False, height = False)
ep.geometry("900x680")

# Function called when logout button pressed
def logout():
    log = messagebox.askquestion("logout", "Are you sure you want to logout?") 

    if log == 'yes':
        sys.exit()
    elif log == 'no':
        tk.messagebox.showinfo('Return','You will now return to the your playlist.')

# Playlist title label
t = Label(ep, text = '        Playlist Title        ',  fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 40 bold italic")
t.place(x = 275, y = 50)

# Sidebar buttons
# Home
h = Button(ep,
    text = "Home",
    bg ="green", bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 1)
h.place(x = 0, y = 0)

# Logout
lo = Button(ep,
    text = "Logout",
    command = logout,
    bg ="green", bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 1)
lo.place(x = 0, y = 55)

# Help/Doc
hd = Button(ep,
    text = "Help/Doc",
    bg ="green", bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 1)
hd.place(x = 0, y = 110)

# Edit/Options
add = Button(ep,
    text = "Add\nSong",
    bg ="green", bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 2)
add.place(x = 0, y = 165)

rem = Button(ep,
    text = "Remove\nSong",
    bg ="green", bd = 6,
    relief = "raised", 
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 2)
rem.place(x = 0, y = 248)

rank = Button(ep,
    text = "Rank\nSong",
    bg ="green", bd = 6, 
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 2)
rank.place(x=0, y = 331)

def deleteP():
    dp = messagebox.askquestion("confirm song removal", "Are you sure you want to delete this playlist?")

    if dp == 'yes':
        print("yes") #add delete playlist query
        #ep.destroy() and bring back to homepage
    elif dp == 'no':
        tk.messagebox.showinfo('Return','You will now return to your playlist.')

de = Button(ep,
    text = "Delete\nPlaylist",
    bg ="green",
    bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 2,
    command = deleteP)
de.place(x = 0, y =415)

def addRec():
    #add recommendations function goes here
    #if successfully added
    tk.messagebox.showinfo('Recommendations added!','Recommendations have been added to your playlist reaching the max number of songs (60).')
    #if max songs reached
    tk.messagebox.showerror('Error!','The max amount of songs (60) has been reached.')

rec = Button(ep,
    text = "Add\nRecommendations",
    bg ="green",
    bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 2,
    command = addRec)
rec.place(x = 0, y =498)

analysis = Button(ep,
    text = "analysis",
    bg ="green",
    bd = 6,
    relief = "raised",
    font = "Helvetica 19 bold italic",
    width = 14,
    height = 1)
analysis.place(x = 0, y =582)

# Songs
fields = Label(ep, text = '                               Song Title                               ', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 18 bold italic")
fields.place(x = 275, y = 150)

listbox = Listbox(ep, bg = "gray", height = 16, width = 50, bd = 6, relief = "sunken", font = "Helvetica 15 bold italic") 
listbox.pack(side = RIGHT, fill = BOTH) 
listbox.place(x = 275, y = 220)
scrollbar = Scrollbar(ep) 

for values in range(100): 
    listbox.insert(END, values) 

listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview) 

ep.mainloop()