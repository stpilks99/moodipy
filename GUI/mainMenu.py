import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
#import createPlaylist
import os

from tkinter import *
from PIL import ImageTk,Image

# Function called when logout button pressed
def logout():
    sys.exit()

#def newPlaylistWindow():
    #("createPlaylist.py 1")

# Creating Main Menu window
mainMenu = Tk()
mainMenu.title("Moodipy")
mainMenu.configure(bg = "black")
mainMenu.resizable(width = False, height = False)
mainMenu.geometry("900x680")

# New playlist button
np = Button(mainMenu, text = "New Playlist", bg ="green", width = 20, height = 5)
np.place(x = 275, y = 250)

# Help button
hd = Button(mainMenu, text = "Help/Documentation", bg ="green", width = 20, height = 5)
hd.place(x = 500, y = 250)

# Logout button
lo = Button(mainMenu, command = logout, text = "Logout", bg ="green", width = 20, height = 5)
lo.place(x = 750, y = 000)

# Snake png
snake = Canvas(mainMenu, width = 232, height = 206)
snake.pack()
img = ImageTk.PhotoImage(Image.open("./GUI/mainSnake.png"))
snake.create_image(5, 5, anchor=NW, image=img)

# Description
yp = tk.Label(mainMenu, text ='Your Playlists:', fg = "black", bg = "green", font = "Helvetica 20 bold italic")
yp.place(x = 47, y = 375)

# Rectangle shape
#p = Canvas(mainMenu, width = 900, height = 400)
#p.pack()
#p.create_rectangle(50, 0, 50, 0, fill = 'red')

# Scrollbar
#sb = tk.Scrollbar(mainMenu, side = right)


mainMenu.mainloop()