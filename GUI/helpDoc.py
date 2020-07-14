import sys
#import spotipy
#import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

helpDoc = tk.Tk()
helpDoc.title("Moodipy Help/Documentation")
helpDoc.configure(bg = "black")
helpDoc.resizable(width = False, height = False)
helpDoc.geometry("900x680")

#creates done button that brings to playlist window
Home = Button(helpDoc, text = "Home", bg ="green", bd = 6, relief = "raised", width = 20, height = 6)
Home.place(x = 710,y = 550)

#creates label with message 
lm = tk.Label(helpDoc, 
    text="Frequently Asked Questions...", 
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "raised",
    font = "Helvetica 30 bold italic")

lm.place(x = 150, y = 35)

# Q1
q1 = tk.Label(helpDoc, 
    text = "How does this program work?",
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "sunken",
    font = "Helvetica 18 bold italic")
q1.place(x = 40, y = 120)

a1 = tk.Label(helpDoc,
    text = "Moodipy interfaces with the Spotify API to retrieve data on songs and playlists.\nIt organizes and sorts data to make playlist based on certain genres or moods.",
    fg = "black", 
    bg = "gray", 
    bd = 6, 
    relief = "sunken",
    font = "Helvetica 12 bold italic")
a1.place(x = 60, y = 170)

q2 = tk.Label(helpDoc,
    text = "How many songs can I add to a playlist?",
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "sunken",
    font = "Helvetica 18 bold italic")
q2.place(x = 40, y = 230)

a2 = tk.Label(helpDoc,
    text = "Using Moodipy, each playlist has a max of 30 songs. Moodipy only adds songs \nit thinks you'll really like (based on moods, ranking, time periods and more) so \nyou'll never find yourself skipping through a bunch of songs you hate.",
    fg = "black", 
    bg = "gray", 
    bd = 6, 
    relief = "sunken",
    font = "Helvetica 12 bold italic")
a2.place(x = 60, y = 280)

#another q: what does ranking a song do?

myScrollbar = Scrollbar(helpDoc)
myScrollbar.pack(side = RIGHT, fill = Y)


helpDoc.mainloop()