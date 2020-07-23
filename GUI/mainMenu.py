import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
#import createPlaylist
import os

from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox 

import sqlite3
database = sqlite3.connect('moodipy.db')
c = database.cursor()

# Function called when logout button pressed
def logout():
    log = messagebox.askquestion("logout", "Are you sure you want to logout?") 

    if log == 'yes':
        sys.exit()
    elif log == 'no':
        tk.messagebox.showinfo('Return','You will now return to the your playlist.')

#def newPlaylistWindow():
    #("createPlaylist.py 1")

# Creating Main Menu window
mainMenu = Tk()
mainMenu.title("Moodipy")
mainMenu.configure(bg = "black")
mainMenu.resizable(width = False, height = False)
mainMenu.geometry("900x680")


# New playlist button
np = Button(mainMenu, text = "New Playlist", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 2)
np.place(x = 200, y = 250)

# Help button
hd = Button(mainMenu, text = "Help/Documentation", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 16, height = 2)
hd.place(x = 425, y = 250)

# Logout button
lo = Button(mainMenu, command = logout, text = "Logout", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 2)
lo.place(x = 715, y = 000)

# Snake png
snake = Canvas(mainMenu, width = 232, height = 206)
snake.pack()
img = ImageTk.PhotoImage(Image.open("./GUI/mainSnake.png"))
snake.create_image(5, 5, anchor=NW, image=img)

# Description
yp = tk.Label(mainMenu, text ='Your Playlists:', fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
yp.place(x = 47, y = 375)

c = database.cursor()
c.execute("""SELECT COUNT(playlisturi) FROM playlistmaster;""")
numOfPlaylists = c.fetchall()

for i in numOfPlaylists:
    print(i[0])
    numOfP = i[0]

c.execute("""SELECT username FROM playlistmaster;""")
pName = c.fetchall()

for j in pName:
    print(j)

#creating multiple buttons in a frame that is placed row after row using .grid
def playlists():
    c = database.cursor()
    c.execute("""SELECT COUNT(playlisturi) FROM playlistmaster;""")
    numOfPlaylists = c.fetchall()

    for i in numOfPlaylists:
        print(i[0])
        numOfP = i[0]

    c.execute("""SELECT username FROM playlistmaster;""")
    pName = c.fetchall()
 

    for i in range(numOfP):
        n = str(pName[i])
        name = '                                    ' + n.strip('(),').replace('\'', '') + '                                          '
        p1 = Button(frame, text = name, fg = "black", bg = "green", bd = 6, relief = "raised", font = "Helvetica 18 bold italic").grid(row=i,column=0)


def myfunction(event):
    #used to limit scrolling operations 
    canvas.configure(scrollregion=canvas.bbox("all"),width=700,height=200)


#creating a frame in main window 
myframe=Frame(mainMenu,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=80,y=450)


canvas=Canvas(myframe, bg = "green")
frame=Frame(canvas, bg = "green")

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
playlists()

mainMenu.mainloop()