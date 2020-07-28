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
                                bd = 10, 
                                relief = "sunken", 
                                height = 2,
                                width = 32,
                                font = "Helvetica 28 bold italic")
title.place(x = 90, y = 30)


stuff = tk.Label(analysis, text ="Static    |               Description                   |   Happy    |   Sad   |   Motivated   |   Calm   |   Frantic   |   Party   |  Gaming  ", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff.place(x = 50, y = 190)
stuff1 = tk.Label(analysis, text ="Valence | 0-1 scale of how cheerful the track is  |   > 0.5   |   < 0.5   |   NA   |   NA   |   NA   |   > 0.5   |   NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff1.place(x = 50, y = 220)

stuff2 = tk.Label(analysis, text ="Energy   |   0-1 scale of how energetic the track is   |   NA   |   NA   |   >.7   |   <.7   |    >.7    |   >.7    |   NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff2.place(x = 50, y = 250)

stuff3 = tk.Label(analysis, text ="Acousticness |  0-1 scale of how acoustic the track is  |   NA   |   NA   |   NA   |   NA   |   NA   |   NA   |   NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff3.place(x = 50, y = 280)
stuff4 = tk.Label(analysis, text ="Danceability | 0-1 scale of tracks danceability    |    NA         |    NA       |    NA      |    NA    |    NA    |    >.65    |    NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff4.place(x = 50, y = 310)
stuff5 = tk.Label(analysis, text ="Speechiness |     0-1 how much speech dominates the track     |   NA   |  NA  |   NA   |   NA   |   NA   |   NA   |   <.085", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff5.place(x = 50, y = 340)
stuff6 = tk.Label(analysis, text ="Tempo |                 Bpm measure of track                      |    NA    |    NA    |    NA    |    <120    |    >120    |    NA    |    NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff6.place(x =50, y = 370)
stuff7 = tk.Label(analysis, text ="Popularity   |         0-100 scale of track’s popularity       |    NA    |    NA    |    NA    |    NA    |    NA    |    >65    |    NA", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 100,
                    font = "Helvetica 10 bold italic")
stuff7.place(x = 50, y = 400)
                    



def closeWindow():
    analysis.destroy()

Done = Button(analysis, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = closeWindow)
Done.place(x = 680, y = 515)

analysis.mainloop()