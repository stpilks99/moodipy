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

# Function called when logout button pressed
def logout():
    sys.exit()

#def newPlaylistWindow():
    #("createPlaylist.py 1")

# Creating Main Menu window
mainMenu = Tk()
#container = ttk.Frame(mainMenu)
#canvas = tk.Canvas(container)
#scrollbar = ttk.Scrollbar(container, orient = "vertical", command = canvas.yview)
#scrollFrame = ttk.Frame(canvas)
mainMenu.title("Moodipy")
mainMenu.configure(bg = "black")
mainMenu.resizable(width = False, height = False)
mainMenu.geometry("900x680")

#Rectangle shape
p = Canvas(mainMenu, width = 800, height = 200, bg = "gray")
p.place(x = 46, y = 440)
#p.create_rectangle(50, 50, 0, 0, fill = 'red')

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
yp = tk.Label(mainMenu, text ='Your Playlists:', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
yp.place(x = 47, y = 375)

# Playlist labels
p1 = Button(p, text = '                                           Playlist 1                                           ', fg = "black", bg = "green", bd = 6, relief = "raised", font = "Helvetica 18 bold italic")
p1.place(x = 34, y = 100)



# Scrollbar
#sw = ScrolledWindow(mainMenu, width = 900, height = 600)
#sw.pack()
#win = sw.window


mainMenu.mainloop()