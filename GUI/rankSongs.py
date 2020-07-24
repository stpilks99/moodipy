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

#creates label with message 
lm = tk.Label(rankSongs, 
    text="  Here are your songs now rank them from 1-3  \n1 = bad, 2 = average, 3 = above average", 
    fg = "black", 
    bg = "green", 
    bd = 6,
    relief = "raised",
    font = "Helvetica 28 bold italic")

lm.place(x= 30, y = 20) 

def rank(x, y, z):
    songranks = []

    songranks.append(x)
    songranks.append(y)
    songranks.append(z)

    print(songranks)


#creating multiple scales and labels in a frame that is placed row after row using .grid
def songs():
    j=0
    k=1
    for i in range(10):
        sc1 = tk.Scale(frame, from_= 1, to = 3).grid(row=j, column=0)

        s1 = tk.Label(frame, text ='         song 1        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=k,column=0)

        sc2 = tk.Scale(frame, from_= 1, to = 3).grid(row=j, column=1)

        s2 = tk.Label(frame, text ='         song 2        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=k,column=1)

        sc3 = tk.Scale(frame, from_= 1, to = 3).grid(row=j, column=2)

        s3 = tk.Label(frame, text ='         song 3        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=k,column=2)

        j+=2
        k+=2

        a = sc1.get()
        b = sc2.get()
        c = sc3.get()

        rank(a, b, c)


def myfunction(event):
    #used to limit scrolling operations 
    canvas.configure(scrollregion=canvas.bbox("all"),width=698,height=350)


#creating a frame in main window that will hold a canvas 
myframe=Frame(rankSongs,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=80,y=130)

#canvas created on the myframe and then frame on the canvas where widgets will be placed
canvas=Canvas(myframe)
frame=Frame(canvas)

#adding a scrollbar
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")

#determines where canvas is 
canvas.pack(side="left")

#this allows for the frame with the widgets that are buttons
canvas.create_window((0,0),window=frame,anchor='nw')

#binding the myfunction to the frame to allow for scrolling 
frame.bind("<Configure>",myfunction)
songs()

#creates done button that brings to playlist window
Done = Button(rankSongs, 
            text = "Done", 
            bg ="green", 
            bd = 6, 
            relief = "raised", 
            font = "Helvetica 20 bold italic", 
            width = 10, 
            height = 3,
            command = rank)
Done.place(x = 685,y = 525)

#creates cancel button that brings back to homepage
Cancelr = Button(rankSongs, text = "Cancel", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 20 bold italic", 
                width = 10, 
                height = 3)
Cancelr.place(x = 42 , y = 525)

rankSongs.mainloop()
