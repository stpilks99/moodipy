import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *

analysis = tk.Tk()
analysis.title("Analysis")
analysis.configure(bg = "black")
analysis.resizable(width = False, height = False)
analysis.geometry("900x680")

title = tk.Label(analysis, text ="Here's an analysis of your playlist:", 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 2,
                width = 28,
                font = "Helvetica 28 bold italic")
title.place(x = 95, y = 30)

stuff = tk.Label(analysis, text ="stuff : ", 
                fg = "black", 
                bg = "gray", 
                bd = 8, 
                relief = "sunken", 
                height = 10,
                width = 50,
                font = "Helvetica 16 bold italic")
stuff.place(x = 65, y = 250)

def closeWindow():
    analysis.destroy()

Done = Button(analysis, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = closeWindow)
Done.place(x = 685, y = 530)

analysis.mainloop()