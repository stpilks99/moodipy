import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
import os

from tkinter import *
# for some reason, messagebox doesn't get imported automatically...
from tkinter import messagebox
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image

# global logout function to multiple windows can see it
def logout():
        log = messagebox.askquestion("logout", "Are you sure you want to logout?") 
        if log == 'yes':
                sys.exit()
        elif log == 'no':
                tk.messagebox.showinfo('Return','You will now return to your window.')


# main menu window class
class mainMenu:
        # constructor
        def __init__(self, master):
                self.master = master
                self.master.title("Moodipy")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

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
                self.yp = tk.Label(self.master, text ='Your Playlists:', fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.yp.place(x = 47, y = 375)

                #creating a frame in main window 
                self.myframe=Frame(self.master,relief=GROOVE,width=50,height=100,bd=1)
                self.myframe.place(x=80,y=450)

                self.canvas=Canvas(self.myframe)
                self.frame=Frame(self.canvas)

                #adding a scrollbar
                self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
                self.canvas.configure(yscrollcommand=self.myscrollbar.set)
                self.myscrollbar.pack(side="right",fill="y")

                #determines where canvas is 
                self.canvas.pack(side="left")

                #this allows for the frame with the widgets that are buttons
                self.canvas.create_window((0,0),window=self.frame,anchor='nw')

                #binding the myfunction to the frame to allow for scrolling 
                self.frame.bind("<Configure>",self.myfunction)
                self.playlists()

        def playlists(self):
                for i in range(10):
                        self.p1 = Button(self.frame, command = self.edit_playlist, text = '                                      Playlist 1                                           ', fg = "black", bg = "green", bd = 6, relief = "raised", font = "Helvetica 18 bold italic").grid(row=i,column=0)

        def myfunction(self, event):
                #used to limit scrolling operations 
                self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=700,height=200)
        
        # Function called when new playlist button clicked
        def new_playlist(self):
                # creating new Toplevel (on top of everything) window called newCreatePlaylist
                self.newCreatePlaylist = tk.Toplevel(self.master)
                # object is created through class definition
                self.moodipy = createPlaylist(self.newCreatePlaylist)

        # Function to open helpDoc window
        # new Toplevel window is created 
        def help_doc(self):
               self.newHelpDoc = tk.Toplevel(self.master)
               self.moodipy = helpDoc(self.newHelpDoc)
        
        # open editPlaylist window
        def edit_playlist(self):
                self.newEditPlaylist = tk.Toplevel(self.master)
                self.moodipy = editPlaylist(self.newEditPlaylist)

#create playlist window
class createPlaylist:
        def criteria(self):
                self.pName = self.playlistName.get()
                self.mSelected = self.moodsSelected.get()
                self.tSelected = self.timePeriod.get()
                self.artist = self.artistEntered.get()
                self.e = self.explicitOrNot.get()

                print(self.pName + "\n" + self.mSelected + "\n" + self.tSelected + "\n" + self.artist + "\n" + self.e)
                self.selection = self.listbox.curselection()
                for i in self.selection:
                        self.gselected = self.listbox.get(i)
                        print(self.gselected)
                        
        def __init__(self, master):
                self.master = master
                self.master.title("Time to create a new playlist!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #creates done button that brings to playlist window
                self.Done = Button(self.master, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = self.criteria)
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
                self.playlistName = Entry(self.master, font = "Helvetica 22 italic") 
                self.lt.place(x = 47, y = 150)
                self.playlistName.place(x = 230, y = 155) 

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

                self.moodsSelected = ttk.Combobox(self.master, values = self.moods, font = "Helvetica 22 italic")
                self.moodsSelected.place(x = 300, y = 215)

                #creates a drop down list where the user can select a time period
                self.Lp = tk.Label(self.master, text = "Select time period:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 270)

                self.times = ["2010's +",
                        "2000's", 
                        "90's", 
                        "80's", 
                        "70's",
                        "None"]

                self.timePeriod = ttk.Combobox(self.master, values = self.times, font = "Helvetica 22 italic")
                self.timePeriod.place(x = 317, y = 275)

                #creates a entry where user can enter prefered artist
                self.Lp = tk.Label(self.master, text = "Enter preferred artist:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 330)
                self.artistEntered = Entry(self.master, font = "Helvetica 22 italic") 
                self.artistEntered.place(x = 355, y = 335) 

                #creates a checkbox where the user can select preferred genres
                self.La = tk.Label(self.master, text = "Enter preferred genres:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.La.place(x = 47, y = 390)

                self.genres = ["Acoustic", "Alternative", "Classical", "Club", "Country", "Dubstep", "EDM", "Funk", "Rock", "Hard Rock", "Heavy Metal", "Hip Hop", "Indie", "Holidays", "Latin", "Pop", "RnB", "Reggae", "Soul", "Jazz", "Afrobeat"]

                self.listbox = tk.Listbox(self.master, bg = "white", height = 2, width = 42, bd = 6, relief = "sunken", font = "Helvetica 12 bold italic", selectmode = MULTIPLE) 
                self.listbox.pack(side = RIGHT, fill = BOTH) 
                self.listbox.place(x = 370, y = 388)
                self.scrollbar = tk.Scrollbar(self.master) 

                for self.values in self.genres: 
                        self.listbox.insert(END, self.values) 

                self.listbox.config(yscrollcommand = self.scrollbar.set) 
                self.scrollbar.config(command = self.listbox.yview)

                #creates a drop down list where the user can select yes for explict or no for non explicit
                self.La = tk.Label(self.master, text = "Would you like explicit songs:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.La.place(x = 47, y = 450)

                self.options = ["Yes", 
                        "No", ]

                self.explicitOrNot = ttk.Combobox(self.master, values = self.options, font = "Helvetica 22 italic")
                self.explicitOrNot.place(x = 450, y = 455)

                self.msg = tk.Label(self.master, text = " Please select the\ngenres you want last. \nIf not highlighted blue\n then they are not selected. ", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 12 bold italic" )
                self.msg.place(x =645, y = 115)

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
                text = "Using Moodipy, each playlist has a max of 60 songs. Moodipy only adds songs \nit thinks you'll really like (based on moods, ranking, time periods and more) so \nyou'll never find yourself skipping through a bunch of songs you hate.",
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
                text = "Ranking a song tells Moodipy which song attributes you like and dislike. After \nranking a song, you have the option to not hear it again in a playlist. ",
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
                self.t.place(x = 275, y = 50)

                # Sidebar buttons
                # Home
                self.h = Button(self.master,
                text = "Home",
                command = self.closeWindow,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 1)
                self.h.place(x = 0, y = 0)

                # Logout
                self.lo = Button(self.master,
                text = "Logout",
                # logout is a global function
                command = logout,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 1)
                self.lo.place(x = 0, y = 55)

                # Help/Doc
                self.hd = Button(self.master,
                text = "Help/Doc",
                command = self.help_doc,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 1)
                self.hd.place(x = 0, y = 110)

                # Edit/Options
                self.add = Button(self.master,
                text = "Add\nSong",
                command = self.add_song,
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2)
                self.add.place(x = 0, y = 165)

                self.rem = Button(self.master,
                text = "Remove\nSong",
                bg ="green", bd = 6,
                relief = "raised", 
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2,
                command = self.remove_song)
                self.rem.place(x = 0, y = 248)

                self.rank = Button(self.master,
                text = "Rank\nSong",
                command = self.rank_songs,
                bg ="green", bd = 6, 
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2)
                self.rank.place(x=0, y = 331)

                self.de = Button(self.master,
                text = "Delete\nPlaylist",
                bg ="green",
                bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2,
                command = self.deleteP)
                self.de.place(x = 0, y = 415)

                self.rec = Button(self.master,
                        text = "Add\nRecommendations",
                        bg ="green",
                        bd = 6,
                        relief = "raised",
                        font = "Helvetica 19 bold italic",
                        width = 14,
                        height = 2,
                        command = self.addRec)
                self.rec.place(x = 0, y = 498)

                self.analysis = Button(self.master,
                        text = "Analysis",
                        bg ="green",
                        bd = 6,
                        relief = "raised",
                        font = "Helvetica 19 bold italic",
                        width = 14,
                        height = 1,
                        command = self.analysis_window)
                self.analysis.place(x = 0, y =582)

                # Songs
                self.fields = Label(self.master, text = '                               Song Title                               ', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 18 bold italic")
                self.fields.place(x = 275, y = 150)

                self.listbox = Listbox(self.master, bg = "gray", height = 16, width = 50, bd = 6, relief = "sunken", font = "Helvetica 15 bold italic") 
                self.listbox.pack(side = RIGHT, fill = BOTH) 
                self.listbox.place(x = 275, y = 220)
                self.scrollbar = Scrollbar(self.master) 

                for self.values in range(100): 
                        self.listbox.insert(END, self.values) 

                self.listbox.config(yscrollcommand = self.scrollbar.set) 
                self.scrollbar.config(command = self.listbox.yview)

                # forces user to click on certain window
                self.master.grab_set()

        def addRec(self):
                #add recommendations function goes here
                #if successfully added
                tk.messagebox.showinfo('Recommendations added!','Recommendations have been added to your playlist reaching the max number of songs (60).')
                #if max songs reached
                tk.messagebox.showerror('Error!','The max amount of songs (60) has been reached.')

        def deleteP(self):
                self.dp = tk.messagebox.askquestion("confirm song removal", "Are you sure you want to delete this playlist?")

                if self.dp == 'yes':
                        print("yes") #add delete playlist query
                #ep.destroy() and bring back to homepage
                elif self.dp == 'no':
                        tk.messagebox.showinfo('Return','You will now return to your playlist.')       

        def closeWindow(self):
                self.master.destroy()
        
        def analysis_window(self):
                self.newAnalysisWindow = tk.Toplevel(self.master)
                self.moodipy = analysis(self.newAnalysisWindow)

        def help_doc(self):
                self.newHelpDoc = tk.Toplevel(self.master)
                self.moodipy = helpDoc(self.newHelpDoc)

        def rank_songs(self):
                self.newRankSongs = tk.Toplevel(self.master)
                self.moodipy = rankSongs(self.newRankSongs)

        def add_song(self):
                self.newAddSong = tk.Toplevel(self.master)
                self.moodipy = addSong(self.newAddSong)

        def remove_song(self):
                self.newRemoveSong = tk.Toplevel(self.master)
                self.moodipy = removeSong(self.newRemoveSong)

class rankSongs:
        def __init__(self, master):
                self.master = master
                self.master.title("Time to rank songs!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #creates done button that brings to playlist window
                self.Done = Button(self.master, command = self.closeWindow, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
                self.Done.place(x = 685,y = 525)

                #creates label with message 
                self.lm = tk.Label(self.master, 
                text="  Here are your songs now rank them from 1-5  ", 
                fg = "black", 
                bg = "green", 
                bd = 6,
                relief = "raised",
                font = "Helvetica 28 bold italic")

                self.lm.place(x= 30, y = 50) 

                #add query to find number of songs in playlist 

                #do another query to pull song title

                #creates a label with song 1 

                #creating a frame in main window that will hold a canvas 
                self.myframe=Frame(self.master,relief=GROOVE,width=50,height=100,bd=1)
                self.myframe.place(x=80,y=130)

                #canvas created on the myframe and then frame on the canvas where widgets will be placed
                self.canvas=Canvas(self.myframe)
                self.frame=Frame(self.canvas)

                #adding a scrollbar
                self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
                self.canvas.configure(yscrollcommand=self.myscrollbar.set)
                self.myscrollbar.pack(side="right",fill="y")

                #determines where canvas is 
                self.canvas.pack(side="left")

                #this allows for the frame with the widgets that are buttons
                self.canvas.create_window((0,0),window=self.frame,anchor='nw')

                #binding the myfunction to the frame to allow for scrolling 
                self.frame.bind("<Configure>",self.myfunction)
                self.songs()
                self.master.grab_set()

        #creating multiple scales and labels in a frame that is placed row after row using .grid
        def songs(self):
                self.j=0
                self.k=1
                for i in range(10):
                        
                        self.sc1 = tk.Scale(self.frame, from_= 1, to = 5).grid(row=self.j, column=0)

                        self.s1 = tk.Label(self.frame, text ='         song 1        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=self.k,column=0)

                        self.sc2 = tk.Scale(self.frame, from_= 1, to = 5).grid(row=self.j, column=1)

                        self.s2 = tk.Label(self.frame, text ='         song 2        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=self.k,column=1)

                        self.sc3 = tk.Scale(self.frame, from_= 1, to = 5).grid(row=self.j, column=2)

                        self.s3 = tk.Label(self.frame, text ='         song 3        ', fg = "black", bg = "green", bd = 5, relief = "raised", font = "Helvetica 20 bold italic").grid(row=self.k,column=2)

                        self.j+=2
                        self.k+=2

        def myfunction(self, event):
                #used to limit scrolling operations 
                self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=698,height=350)

        def closeWindow(self):
                self.master.destroy()

class addSong:
        def __init__(self, master):
                self.master = master
                self.master.title("Time to add a song to the playlist!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")
                self.lt = tk.Label(self.master, text ='Please enter the title and artist\n of the song you would like to add:', 
                        fg = "black", 
                        bg = "green", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 3,
                        width = 28,
                        font = "Helvetica 32 bold italic")
                self.lt.place(x = 65, y = 70)

        #Creating label and entry to get the title of song
                self.t = tk.Label(self.master, text ='Title:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 1,
                                width = 5,
                                font = "Helvetica 32 bold italic")
                self.t.place(x = 65, y = 300)

                self.et = Entry(self.master, font = "Helvetica 40 italic", width = 20) 
                self.et.place(x = 230, y = 300) 

                #Creating label and entry to get the artist of song
                self.a = tk.Label(self.master, text ='Artist:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 1,
                                width = 5,
                                font = "Helvetica 32 bold italic")
                self.a.place(x = 65, y = 400)

                self.ea = Entry(self.master, font = "Helvetica 40 italic", width = 20) 
                self.ea.place(x = 230, y = 400) 


                #creates Add button that brings to playlist window
                self.Add = Button(self.master, text = "Add", 
                                bg ="green", 
                                command = self.addSongToPlaylist,
                                bd = 6, 
                                relief = "raised", 
                                font = "Helvetica 30 bold italic", 
                                width = 9, 
                                height = 2)

                self.Add.place(x = 630, y = 520)

                #creates cancel button that brings back to homepage
                self.Cancela = Button(self.master, text = "Cancel", 
                                bg ="green", 
                                command = self.closeWindow,
                                bd = 6, 
                                relief = "raised", 
                                font = "Helvetica 30 bold italic", 
                                width = 9, 
                                height = 2)
                self.Cancela.place(x = 42 , y = 520)

                self.master.grab_set()
        
        #function that gets the title and artist to add to playlist
        #in this function need to add the function from functions group since command only accepts one function
        def addSongToPlaylist(self):
                self.titleAdd = self.et.get()
                self.artistAdd = self.ea.get()
                print(self.titleAdd)
                print(self.artistAdd)

                #if there are less than 60 songs then allow to add song
                self.confirmAdd = tk.messagebox.askquestion("confirm song to be added", "Are you sure you want to add this song?")

                if self.confirmAdd == 'yes':
                        print("yes")
                        #add query to see number of row, if 60 max reached then:
                        tk.messagebox.showerror('Error','The max amount of songs (60) has been reached. Please click cancel when returned to the add song window and delete a song to add more.')
                        #else:
                        #add add song function
                        #if song is added, get a return from function that indicates its added
                        tk.messagebox.showinfo("song added!", "Your song has been added! Click cancel to go back to your playlist or add another song.") 
                        #else if not added, display try again
                        tk.messagebox.showerror("Error", "A problem has occurred adding this song. Please try again.") 
                        
                elif self.confirmAdd == 'no':
                        tk.messagebox.showinfo('Return','You will now return to the add song window. Here you can either enter another song to add or click cancel to go back to your playlist.')

        def closeWindow(self):
                self.master.destroy()

class removeSong:
        def __init__(self, master):
                self.master = master
                self.master.title("Time to remove a song from the playlist!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                self.lt = tk.Label(self.master, text ='Please enter the title and artist of\n the song title you would like to remove:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 3,
                                width = 32,
                                font = "Helvetica 30 bold italic")
                self.lt.place(x = 56, y = 70)
                        #getting entry for title of song
                self.et1 = Entry(self.master, font = "Helvetica 40 italic", width = 21) 
                self.et1.place(x = 230, y = 290) 

                self.t1 = tk.Label(self.master, text ='Title:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 1,
                                width = 5,
                                font = "Helvetica 32 bold italic")
                self.t1.place(x = 65, y = 290)

                #getting entry for artist of song
                self.a1 = tk.Label(self.master, text ='Artist:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 1,
                                width = 5,
                                font = "Helvetica 32 bold italic")
                self.a1.place(x = 65, y = 400)

                self.ea1 = Entry(self.master, font = "Helvetica 40 italic", width = 21) 
                self.ea1.place(x = 230, y = 400) 

                #creates Remove button that brings to playlist window
                self.Remove = Button(self.master, text = "Remove", 
                                bg ="green", 
                                bd = 6, 
                                relief = "raised", 
                                font = "Helvetica 30 bold italic", 
                                width = 9, 
                                height = 2,
                                command = self.remove)

                self.Remove.place(x = 630, y = 520)

                #creates cancel button that brings back to playlist window
                self.Cancelr = Button(self.master, text = "Close", 
                                bg ="green", 
                                bd = 6, 
                                relief = "raised", 
                                font = "Helvetica 30 bold italic", 
                                width = 9, 
                                height = 2,
                                command = self.closeWindow)
                self.Cancelr.place(x = 42 , y = 520)

                self.master.grab_set()

        #function that gets the title and artist to remove from playlist
        #in this function need to add the function from functions group since command only accepts one function  
        def remove(self):
                self.titleRemove = self.et1.get()
                self.artistRemove = self.ea1.get()
                print(self.titleRemove)
                print(self.artistRemove)

                self.rm = tk.messagebox.askquestion("confirm song removal", "Are you sure you want to remove this song?")

                if self.rm == 'yes':
                        print("yes") #add remove function
                        #if song is removed, get a return from function that indicates its removed
                        tk.messagebox.showinfo("song removed!", "Your song has been removed! Click cancel to go back to your playlist or remove another song.") 
                        #else if not removed, display try again
                        tk.messagebox.showerror("Error", "A problem has occurred removing this song. Please check your playlist to ensure this song is in it by clicking cancel. If it is on your playlist, then please try again.") 
                elif self.rm == 'no':
                        tk.messagebox.showinfo('Return','You will now return to the remove song window. Here you can either enter another song to remove or click cancel to go back to your playlist.')

        def closeWindow(self):
                self.master.destroy()

class analysis:
        def __init__(self, master):
                self.master = master
                self.master.title("Analysis")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                self.title = tk.Label(self.master, text ="Here's an analysis of your playlist:", 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 2,
                                width = 28,
                                font = "Helvetica 28 bold italic")
                self.title.place(x = 95, y = 30)

                self.stuff = tk.Label(self.master, text ="stuff : ", 
                                fg = "black", 
                                bg = "gray", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 10,
                                width = 50,
                                font = "Helvetica 16 bold italic")
                self.stuff.place(x = 65, y = 250)

                self.Done = Button(self.master, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = self.closeWindow)
                self.Done.place(x = 685, y = 530)

        def closeWindow(self):
                self.master.destroy()

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