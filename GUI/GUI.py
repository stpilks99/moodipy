import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
import os

from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image

# global logout function to multiple windows can see it
def logout():
        sys.exit()

# main menu window class
class mainMenu:
        # constructor
        def __init__(self, master):
                self.master = master
                self.master.title("Moodipy")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #Rectangle shape
                self.p = Canvas(self.master, width = 800, height = 200, bg = "gray")
                self.p.place(x = 46, y = 440)

                # New playlist button
                self.np = Button(self.master, text = "New Playlist", command = self.new_playlist, bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 2)
                self.np.place(x = 200, y = 250)

                # Help button
                self.hd = Button(self.master, text = "Help/Documentation", command = self.help_doc, bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 16, height = 2)
                self.hd.place(x = 425, y = 250)

                # Logout button
                self.lo = Button(self.master, command = logout, text = "Logout", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 2)
                self.lo.place(x = 715, y = 000)

                # Snake png
                self.snake = Canvas(self.master, width = 232, height = 206)
                self.snake.pack()
                self.img = ImageTk.PhotoImage(Image.open("./GUI/mainSnake.png"))
                self.snake.create_image(5, 5, anchor=NW, image=self.img)

                # Description
                self.yp = tk.Label(self.master, text ='Your Playlists:', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.yp.place(x = 47, y = 375)

                # Playlist labels
                self.p1 = Button(self.p, text = '                                           Playlist 1                                           ', command = self.edit_playlist, fg = "black", bg = "green", bd = 6, relief = "raised", font = "Helvetica 18 bold italic")
                self.p1.place(x = 34, y = 100)
        
        # Function called when new playlist button clicked
        def new_playlist(self):
                # creating new Toplevel (on top of everything) window called newCreatePlaylist
                self.newCreatePlaylist = tk.Toplevel(self.master)
                # object is created through class definition
                self.moodipy = createPlaylist(self.newCreatePlaylist)

        # Function to open helpDoc window
        def help_doc(self):
               self.newHelpDoc = tk.Toplevel(self.master)
               self.moodipy = helpDoc(self.newHelpDoc)
        
        # open editPlaylist window
        def edit_playlist(self):
                self.newEditPlaylist = tk.Toplevel(self.master)
                self.moodipy = editPlaylist(self.newEditPlaylist)

#create playlist window
class createPlaylist:
        def __init__(self, master):
                self.master = master
                self.master.title("Time to create a new playlist!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #creates done button that brings to playlist window
                self.Done = Button(self.master, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
                self.Done.place(x = 685, y = 530)

                #creates cancel button that brings back to homepage
                self.Cancel = Button(self.master, command = self.closeWindow, text = "Cancel", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
                self.Cancel.place(x = 42, y = 530)

                #creates label with message 
                self.lm = tk.Label(self.master, 
                text="Just enter what you want and we will do the rest!", 
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "raised",
                font = "Helvetica 26 bold italic")

                self.lm.place(x= 47, y = 50) 

                #creates entry so user can enter playlist title
                self.lt = tk.Label(self.master, text ='Playlist title:', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.e1 = Entry(self.master, font = "Helvetica 22 italic") 
                self.lt.place(x = 47, y = 150)
                self.e1.place(x = 230, y = 155) 

                #creates a drop down list where the user can select a mood with a label next to it
                self.Lmd = tk.Label(self.master, text = "Select one mood:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lmd.place(x = 47, y = 210)

                #array of moods to be placed inside drop down menu
                self.moods = ["Happy", 
                        "Sad", 
                        "Motivated", 
                        "Calm",
                        "Frantic",
                        "Party",
                        "Gaming"]

                self.dropl = ttk.Combobox(self.master, values = self.moods, font = "Helvetica 22 italic")
                self.dropl.place(x = 300, y = 215)

                #creates a drop down list where the user can select a time period
                self.Lp = tk.Label(self.master, text = "Select time period:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 270)

                self.times = ["2010's +",
                        "2000's", 
                        "90's", 
                        "80's", 
                        "70's",
                        "None"]

                self.dropl = ttk.Combobox(self.master, values = self.times, font = "Helvetica 22 italic")
                self.dropl.place(x = 317, y = 275)

                #creates a entry where user can enter prefered artist
                self.Lp = tk.Label(self.master, text = "Enter preferred artist:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 330)
                self.e2 = Entry(self.master, font = "Helvetica 22 italic") 
                self.e2.place(x = 355, y = 335) 

                #creates a checkbox where the user can select preferred genres
                self.La = tk.Label(self.master, text = "Enter preferred genres:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.La.place(x = 47, y = 390)

                self.menubutton = tk.Menubutton(self.master, text="Check all preferred genres", indicatoron=True, borderwidth=1, relief="raised", font = "Helvetica 22 italic")

                self.menu = tk.Menu(self.menubutton, tearoff=False)
                self.menubutton.configure(menu=self.menu) 
                self.menubutton.place(x = 370, y = 395)

                self.genres = {}
                for genre in ("Acoustic", "Alternative", "Classical", "Club", "Country", "Dubstep", "EDM", "Funk", "Rock", "Hard Rock", "Heavy Metal", "Hip Hop", "Indie", "Holidays", "Latin", "Pop", "RnB", "Reggae", "Soul", "Jazz", "Afrobeat"):
                        self.genres[genre] = tk.IntVar(value=0)
                        self.menu.add_checkbutton(label=genre, variable=self.genres[genre], onvalue=1)

                #creates a drop down list where the user can select yes for explict or no for non explicit
                self.La = tk.Label(self.master, text = "Would you like explict songs:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.La.place(x = 47, y = 450)

                self.options = ["Yes", 
                        "No", ]

                self.dropl = ttk.Combobox(self.master, values = self.options, font = "Helvetica 22 italic")
                self.dropl.place(x = 450, y = 455)

                # forces user to click on new playlist window so they can't use 2 windows at once
                self.master.grab_set()

        def closeWindow(self):
                self.master.destroy()

class helpDoc:
        def __init__(self, master):
                self.master = master
                self.master.title("Moodipy Help/Documentation")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #creates done button that brings to playlist window
                self.Home = Button(self.master, text = "Done", command = self.closeWindow, bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
                self.Home.place(x = 700,y = 540)

                #creates label with message 
                self.lm = tk.Label(self.master, 
                text="Frequently Asked Questions...", 
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "raised",
                font = "Helvetica 30 bold italic")

                self.lm.place(x = 150, y = 35)

                # Q1 labels
                self.q1 = tk.Label(self.master, 
                text = "How does this program work?",
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 18 bold italic")
                self.q1.place(x = 40, y = 120)

                self.a1 = tk.Label(self.master,
                text = "Moodipy interfaces with the Spotify API to retrieve data on songs and playlists.\nIt organizes and sorts data to make playlist based on certain genres or moods.",
                fg = "black", 
                bg = "gray", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 12 bold italic")
                self.a1.place(x = 60, y = 170)

                self.q2 = tk.Label(self.master,
                text = "How many songs can I add to a playlist?",
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 18 bold italic")
                self.q2.place(x = 40, y = 230)

                self.a2 = tk.Label(self.master,
                text = "Using Moodipy, each playlist has a max of 30 songs. Moodipy only adds songs \nit thinks you'll really like (based on moods, ranking, time periods and more) so \nyou'll never find yourself skipping through a bunch of songs you hate.",
                fg = "black", 
                bg = "gray", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 12 bold italic")
                self.a2.place(x = 60, y = 280)

                self.q3 = tk.Label(self.master,
                text = "What does ranking a song do?",
                fg = "black", 
                bg = "green", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 18 bold italic")
                self.q3.place(x = 40, y = 360)

                self.a3 = tk.Label(self.master,
                text = "stuff",
                fg = "black", 
                bg = "gray", 
                bd = 6, 
                relief = "sunken",
                font = "Helvetica 12 bold italic")
                self.a3.place(x = 60, y = 410)

                #another q: what does ranking a song do 
                # forces user to click on certain window
                self.master.grab_set()       

        def closeWindow(self):
                self.master.destroy()

class editPlaylist:
        def __init__(self, master):
                self.master = master
                self.master.title("View Playlist")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                # Function called when logout button pressed

                # Playlist title label
                self.t = Label(self.master, text = '        Playlist Title        ',  fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 40 bold italic")
                self.t.place(x = 250, y = 50)

                # Sidebar buttons
                # Home
                self.h = Button(self.master,
                text = "Home",
                command = self.closeWindow,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.h.place(x = 0, y = 0)

                # Logout
                self.lo = Button(self.master,
                text = "Logout",
                command = logout,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.lo.place(x = 0, y = 95)

                # Help/Doc
                self.hd = Button(self.master,
                text = "Help/Doc",
                command = self.help_doc,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.hd.place(x = 0, y = 190)

                # Edit/Options
                self.add = Button(self.master,
                text = "Add\nSong",
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.add.place(x = 0, y = 285)

                self.rem = Button(self.master,
                text = "Remove\nSong",
                bg ="green", bd = 6,
                relief = "raised", 
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.rem.place(x = 0, y = 380)

                self.rank = Button(self.master,
                text = "Rank\nSong",
                bg ="green", bd = 6, 
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.rank.place(x=0, y = 475)

                self.de = Button(self.master,
                text = "Delete\nPlaylist",
                bg ="green",
                bd = 6,
                relief = "raised",
                font = "Helvetica 20 bold italic",
                width = 10,
                height = 2)
                self.de.place(x = 0, y =570)

                # Songs
                self.fields = Label(self.master, text = '       Song               Artist           Album                 ', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 18 bold italic")
                self.fields.place(x = 250, y = 150)

                self.listbox = Listbox(self.master, bg = "gray", height = 16, width = 49, bd = 6, relief = "sunken", font = "Helvetica 15 bold italic") 
                self.listbox.pack(side = RIGHT, fill = BOTH) 
                self.listbox.place(x = 250, y = 220)
                self.scrollbar = Scrollbar(self.master) 

                for values in range(100): 
                        self.listbox.insert(END, values) 

                self.listbox.config(yscrollcommand = self.scrollbar.set) 
                self.scrollbar.config(command = self.listbox.yview)

                # forces user to click on certain window
                self.master.grab_set()       

        def closeWindow(self):
                self.master.destroy()
        
        def help_doc(self):
               self.newHelpDoc = tk.Toplevel(self.master)
               self.moodipy = helpDoc(self.newHelpDoc)


class login:
        def __init__(self, master):
                self.master = master
                self.master.title("Welcome to Moodipy!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x600")

                self.B = Button(login,
                text = "Login with Spotify",
                bg ="green",
                font = "Helvetica 20 bold italic",
                bd = 6, relief = "raised",
                width = 25,
                height = 2)
                self.B.place(x = 225,y = 480)
                self.canvas = Canvas(login, width = 850, height = 460)
                self.canvas.pack()
                self.img = ImageTk.PhotoImage(Image.open("./GUI/snake.png"))
                self.canvas.create_image(20, 20, anchor=NW, image=self.img) 

def main():
        #add function to check login credentials
        root = tk.Tk()
        moodipy = mainMenu(root)
        root.mainloop()

if __name__ == '__main__':
        main()
