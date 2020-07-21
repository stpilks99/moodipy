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
Home = Button(helpDoc, text = "Home", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
Home.place(x = 680,y = 510)

#creates label with message 
lm = tk.Label(helpDoc, 
    text="Frequently Asked Questions...", 
    fg = "black", 
    bg = "green", 
    bd = 6, 
    relief = "raised",
    font = "Helvetica 30 bold italic")

lm.place(x = 150, y = 35)


#another q: what does ranking a song do

#creating multiple scales and labels in a frame that is placed row after row using .grid
def FQAs(): 
    q1 = tk.Label(frame, 
        text = "How does this program work?",
        fg = "black", 
        bg = "green", 
        bd = 6, 
        relief = "sunken",
        font = "Helvetica 20 bold italic").grid(row = 0, column =0)


    a1 = tk.Label(frame,
        text = "Moodipy interfaces with the Spotify API to retrieve data on songs and playlists.\nIt organizes and sorts data to make playlist based on certain genres or moods.",
        fg = "black", 
        bg = "gray", 
        bd = 6, 
        relief = "sunken",
        font = "Helvetica 14 bold italic").grid(row = 1, column =0)
        

    q2 = tk.Label(frame,
        text = "How many songs can I add to a playlist?",
        fg = "black", 
        bg = "green", 
        bd = 6, 
        relief = "sunken",
        font = "Helvetica 20 bold italic").grid(row = 2, column =0)
    

    a2 = tk.Label(frame,
        text = "Using Moodipy, each playlist has a max of 30 songs. Moodipy only adds songs \nit thinks you'll really like (based on moods, ranking, time periods and more) so \nyou'll never find yourself skipping through a bunch of songs you hate.",
        fg = "black", 
        bg = "gray", 
        bd = 6, 
        relief = "sunken",
        font = "Helvetica 14 bold italic").grid(row = 3, column =0) 

    q3 = tk.Label(frame,
                text = "What does ranking a song do?",
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 20 bold italic").grid(row = 4, column = 0)

    a3 = tk.Label(frame,
                text = "Ranking a song tells Moodipy which song attributes you like and dislike. After \nranking a song, you have the option to not hear it again in a playlist. ",
                fg = "black", 
                bg = "gray", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 14 bold italic").grid(row=5, column=0)

def myfunction(event):
    #used to limit scrolling operations 
    canvas.configure(scrollregion=canvas.bbox("all"),width=760,height=310)


#creating a frame in main window that will hold a canvas 
myframe=Frame(helpDoc,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=50,y=140)

#canvas created on the myframe and then frame on the canvas where widgets will be placed
canvas=Canvas(myframe)
frame=Frame(canvas, bg = "black")

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
FQAs()

helpDoc.mainloop()