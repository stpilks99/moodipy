import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

helpDoc = tk.Tk()
helpDoc.title("Moodipy Help/Documentation")
helpDoc.configure(bg = "black")
helpDoc.resizable(width = False, height = False)
helpDoc.geometry("900x680")

#creates done button that brings to playlist window
Home = Button(helpDoc, text = "Home", bg ="green", width = 20, height = 6)
Home.place(x = 710,y = 530)

#creates label with message 
lm = tk.Label(helpDoc, 
    text="Frequently Asked Questions...", 
    fg = "black", 
    bg = "green", 
    font = "Helvetica 30 bold italic")

lm.place(x = 150, y = 50)

helpDoc.mainloop()