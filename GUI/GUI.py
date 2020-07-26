import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
import os
import fnmatch

from tkinter import *
from tkinter import messagebox
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
from functools import partial

#import spotify_authorize
import spotipy
from track_functions import *
from artist_functions import *
from spotify_authorize import *
from user_functions import *
from playlist_functions import *
from get_songs_with_criteria import *

from Moodipy_SQL_Queries import *

# global logout function to multiple windows can see it
def logout():
        log = messagebox.askquestion("logout", "Are you sure you want to logout?") 
        if log == 'yes':
                logout_flag = auth.logout()
                if logout_flag == False:
                    tk.messagebox.showerror('Logout failed', 'Logout unsuccessful.')
                else:
                    tk.messagebox.showinfo('Logout successful', 'User successfully signed out')
                #add logout function
                sys.exit()
        elif log == 'no':
                tk.messagebox.showinfo('Return','You will now return to your window.')


# main menu window class
class mainMenu:
        # constructor
        def __init__(self, master, name_db, sp, userClass):
                self.name_db = name_db
                self.sp = sp
                self.userClass = userClass
                print(type(userClass))
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

                self.canvas=Canvas(self.myframe, bg = "green")
                self.frame=Frame(self.canvas, bg = "green")

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
                self.master.grab_set()

        def playlists(self):
                database = sqlite3.connect(self.name_db)
                c = database.cursor()
                c.execute("""SELECT COUNT(playlisturi) FROM playlistmaster;""")
                self.numOfPlaylists = c.fetchall()
                # printing total number of playlists user has in library
                for i in self.numOfPlaylists:
                        #print(i[0])
                        self.numOfP = i[0]

                c.execute("""SELECT username FROM playlistmaster;""")
                self.pName = c.fetchall()

                c.execute("""SELECT playlisturi FROM playlistmaster;""")
                self.qr = c.fetchall()

                self.pURIList = []
                # array kept printing backwards so we had
                # to iterate through the query of playlist uris
                for self.val in self.qr:
                        j = 0
                        self.pURIList.insert(j, self.val)
                        j += 1
                        print(self.pURIList)
                
                # printing all of the URIs as a list in playlist master
                #print(self.pURI)
                for i in range(self.numOfP):
                        playlistURI = str(self.pURIList[i]).strip('(,)')
                        print(playlistURI)
                        self.n = str(self.pName[i])
                        self.name = '                                    ' + self.n.strip('(),').replace('\'', '') + '                                          '
                        # each button needs a different name to distinguish them
                        #print(i)
                        # Using a lambda function here (a small anonymous function) 
                        # because each button calls the same edit_playlist open window function but with different arguments.
                        # Otherwise, clicking each button would just give editPlaylist the same playlistURI over and over.
                        # Variables x and y have to be declared inside the lambda because i and uri are global to the outer scope and can be 
                        # changed immediately by the next loop (which is why only the last playlistURI in the query kept showing). 
                        self.playlistButton = tk.Button(self.frame, command = lambda x = i, y = playlistURI: self.onButtonClick(x, y), text = self.name, fg = "black", bg = "green", bd = 6, relief = "raised", font = "Helvetica 18 bold italic").grid(row=i,column=0)
                #print(i)
                database.close()

        def onButtonClick(self, buttonID, playlistURI):
                database = sqlite3.connect(self.name_db)
                c = database.cursor()
                c.execute("""SELECT COUNT(playlisturi) FROM playlistmaster;""")
                self.numOfPlaylists = c.fetchall()
                for i in self.numOfPlaylists:
                        # printing total number of playlists user has in library
                        #print(i[0])
                        self.numOfP = i[0]
                for j in range(self.numOfP):
                        #print(j)
                        #print(buttonID)
                        # if the buttonID you clicked matches the 'nth' playlist we want to edit
                        if (buttonID == j):
                                print(playlistURI)
                                self.edit_playlist(playlistURI)
                                break
                database.close()
                        


        def myfunction(self, event):
                #used to limit scrolling operations 
                self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=700,height=200)
        
        # Function called when new playlist button clicked
        def new_playlist(self):
                # creating new Toplevel (on top of everything) window called newCreatePlaylist
                self.newCreatePlaylist = tk.Toplevel(self.master)
                # object is created through class definition
                self.moodipy = createPlaylist(self.newCreatePlaylist, self.name_db, self.sp,self.userClass)

        # Function to open helpDoc window
        # new Toplevel window is created 
        def help_doc(self):
               self.newHelpDoc = tk.Toplevel(self.master)
               self.moodipy = helpDoc(self.newHelpDoc, self.name_db, self.sp, self.userClass)
        
        # open editPlaylist window
        def edit_playlist(self, playlistURI):
                #print(str(self.playlistURI))
                self.newEditPlaylist = tk.Toplevel(self.master)
                self.moodipy = editPlaylist(self.newEditPlaylist, playlistURI, self.name_db, self.sp, self.userClass)

#create playlist window
class createPlaylist:
        # SQL Create playlist function
        def __init__(self, master,  name_db, sp, userClass):
                self.name_db = name_db
                self.userClass = userClass
                self.sp = sp
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
                self.lt.place(x = 47, y = 120)
                self.playlistName.place(x = 230, y = 125) 

                #creates a drop down list where the user can select a mood with a label next to it
                self.Lmd = tk.Label(self.master, text = "Select one mood:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lmd.place(x = 47, y = 180)

                #array of moods to be placed inside drop down menu
                self.moods = ["Happy", 
                        "Sad", 
                        "Motivated", 
                        "Calm",
                        "Frantic",
                        "Party",
                        "Gaming"]

                self.moodsSelected = ttk.Combobox(self.master, values = self.moods, font = "Helvetica 22 italic")
                self.moodsSelected.place(x = 295, y = 185)

                #creates a drop down list where the user can select a time period
                self.Lp = tk.Label(self.master, text = "Select time period:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 240)

                self.times = ["2010's +",
                        "2000's", 
                        "90's", 
                        "80's", 
                        "70's",
                        "None"]

                self.timePeriod = ttk.Combobox(self.master, values = self.times, font = "Helvetica 22 italic")
                self.timePeriod.place(x = 317, y = 244)

                #creates a entry where user can enter prefered artist
                self.Lp = tk.Label(self.master, text = "Enter preferred artist:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lp.place(x = 47, y = 300)
                self.artistEntered = Entry(self.master, font = "Helvetica 22 italic") 
                self.artistEntered.place(x = 355, y = 305) 

                #creates a checkbox where the user can select preferred genres
                self.Lg = tk.Label(self.master, text = "Enter preferred genres:", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Lg.place(x = 47, y = 420)

                self.msg = tk.Label(self.master, text = " Please select up to 5 \ngenres you want last. \nIf not highlighted blue\n then they are not selected. ", fg = "black", bg = "gray", bd = 6, relief = "sunken", font = "Helvetica 12 bold italic" )
                self.msg.place(x = 645, y = 115)

                #28 genres
                self.genres = ["Acoustic", "Afrobeat", "Alternative", "Ambient", "Brazil", "Classical", "Club", "Country", "Disco", "Dubstep", "EDM", "Funk", "Gospel", "Hard Rock", "Heavy Metal", "Hip Hop", "Holidays", "Indie", "Jazz", "Kpop", "Latin", "Metal", "Pop", "Punk", "Reggae", "RnB", "Rock", "Soul"]

                self.listbox = tk.Listbox(self.master, bg = "white", height = 4, width = 45, bd = 6, relief = "sunken", font = "Helvetica 12 bold italic", selectmode = MULTIPLE) 
                self.listbox.pack(side = RIGHT, fill = BOTH) 
                self.listbox.place(x = 370, y = 420)
                self.scrollbar = tk.Scrollbar(self.master) 

                for self.values in self.genres: 
                        self.listbox.insert(END, self.values) 

                self.listbox.config(yscrollcommand = self.scrollbar.set) 
                self.scrollbar.config(command = self.listbox.yview) 

                #creates a drop down list where the user can select yes for explict or no for non explicit
                self.Le = tk.Label(self.master, text = "Would you like explict songs:", fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 20 bold italic")
                self.Le.place(x = 47, y = 360)

                self.options = ["Yes", 
                        "No", ]

                self.explicitOrNot = ttk.Combobox(self.master, values = self.options, font = "Helvetica 22 italic")
                self.explicitOrNot.place(x = 450, y = 365)
                

                # forces user to click on new playlist window so they can't use 2 windows at once
                self.master.grab_set()


        
        def criteria(self):
                self.pName = self.playlistName.get()
                self.mSelected = self.moodsSelected.get()
                self.tSelected = self.timePeriod.get()
                self.artist = self.artistEntered.get()
                self.e = self.explicitOrNot.get()

                print(self.pName + "\n" + self.mSelected + "\n" + self.tSelected + "\n" + self.artist + "\n" + self.e)
                self.selection = self.listbox.curselection()
                genre_list = []
                for i in self.selection:
                        genre_list.append(self.listbox.get(i))
                print(genre_list)
                #Note: the variables on lines above are the user input
                # need to add create playlist functions here
                # functions team will generate the playlist uri from spotify
                # Match up variables
                playlist_title = self.pName
                playlist_genres = genre_list
                playlist_mood = self.mSelected
                pref_artist = self.artist
                time_period = self.tSelected
                playlist_explicit = self.e
                num_songs_needed = 30
                #name_db = self.name_db

                # Code for creating playlist and adding recommendations
                user_uri = self.userClass.get_uri()
                playlistClass = Playlist(user_uri, self.sp, playlist_title)
                uri_playlist = playlistClass.create_spotify_playlist(self.sp)
                flag = createP(self.name_db, uri_playlist, playlist_mood, time_period, pref_artist, playlist_genres, playlist_explicit) # Not working right now
                if flag != 0:
                    print('ERROR with creating database table')
                    # Popup error
                print(flag)
                # Find recommendations based on user input
                returned_list = get_songs_with_criteria(playlist_mood, playlist_genres, time_period, pref_artist, False, [], [], num_songs_needed, self.sp)        
                flag = playlistClass.add_songs_sp(returned_list, self.sp)
                if flag == False:
                    print('ERROR moving songs to Spotify')
                
                '''Add songs to playlist in SQL'''
                song_uris_names = playlistClass.add_songs_local(returned_list, self.sp)
                flag = addS(uri_playlist, song_uris_names, name_db)
                if flag == False:
                    print('ERROR pushing songs to database')


        def closeWindow(self):
                self.master.destroy()

class helpDoc:
        def myfunction(self, event):
                #used to limit scrolling operations 
                self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=760,height=310)
        def FQAs(self):
                self.q1 = tk.Label(self.frame, 
                        text = "How does this program work?",
                        fg = "black", 
                        bg = "green", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 20 bold italic").grid(row = 0, column =0)


                self.a1 = tk.Label(self.frame,
                        text = "Moodipy interfaces with the Spotify API to retrieve data on songs and playlists.\nIt organizes and sorts data to make playlist based on certain genres or moods.",
                        fg = "black", 
                        bg = "gray", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 14 bold italic").grid(row = 1, column =0)
                        

                self.q2 = tk.Label(self.frame,
                        text = "How many songs can I add to a playlist?",
                        fg = "black", 
                        bg = "green", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 20 bold italic").grid(row = 2, column =0)
                

                self.a2 = tk.Label(self.frame,
                        text = "Using Moodipy, each playlist has a max of 60 songs. Moodipy only adds songs \nit thinks you'll really like (based on moods, ranking, time periods and more) so \nyou'll never find yourself skipping through a bunch of songs you hate.",
                        fg = "black", 
                        bg = "gray", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 14 bold italic").grid(row = 3, column =0) 

                self.q3 = tk.Label(self.frame,
                                text = "What does ranking a song do?",
                                fg = "black", 
                                bg = "green", 
                                bd = 6, 
                                relief = "sunken",
                                font = "Helvetica 20 bold italic").grid(row = 4, column = 0)

                self.a3 = tk.Label(self.frame,
                                text = "Ranking a song tells Moodipy which song attributes you like and dislike. After \nranking a song, you have the option to not hear it again in a playlist. ",
                                fg = "black", 
                                bg = "gray", 
                                bd = 6, 
                                relief = "sunken",
                                font = "Helvetica 14 bold italic").grid(row=5, column=0)

                self.q4 = tk.Label(self.frame,
                        text = "How does adding recommendations work?",
                        fg = "black", 
                        bg = "green", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 20 bold italic").grid(row = 6, column = 0)
                
                self.a4 = tk.Label(self.frame,
                        text = "The program takes in all criteria that the user enters,\nand queries Spotify for songs that have the desired attributes.",
                        fg = "black", 
                        bg = "gray", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 14 bold italic").grid(row=7, column=0)

                self.q5 = tk.Label(self.frame,
                        text = "Is there a link with the code that creates Moodipy?",
                        fg = "black", 
                        bg = "green", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 20 bold italic").grid(row = 8, column = 0)

                self.a5 = tk.Label(self.frame,
                        text = "To see how Moodipy was created you can go to: \n https://github.com/stpilks99/Moodipy",
                        fg = "black", 
                        bg = "gray", 
                        bd = 6, 
                        relief = "sunken",
                        font = "Helvetica 14 bold italic").grid(row=9, column=0)

        def __init__(self, master, name_db, sp):
                self.sp = sp
                self.name_db = name_db
                self.master = master
                self.master.title("Moodipy Help/Documentation")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                self.lm = tk.Label(self.master, 
                        text="Frequently Asked Questions...", 
                        fg = "black", 
                        bg = "green", 
                        bd = 6, 
                        relief = "raised",
                        font = "Helvetica 30 bold italic")

                self.lm.place(x = 150, y = 35)

                #creates done button that brings to playlist window
                self.Home = tk.Button(self.master, text = "Done", command = self.closeWindow, bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3)
                self.Home.place(x = 700,y = 540)

                 #creating a frame in main window that will hold a canvas 
                self.myframe=tk.Frame(self.master,relief=GROOVE,width=50,height=100,bd=1)
                self.myframe.place(x=50,y=140)

                #canvas created on the myframe and then frame on the canvas where widgets will be placed
                self.canvas=tk.Canvas(self.myframe)
                self.frame=tk.Frame(self.canvas, bg = "black")

                #adding a scrollbar
                self.myscrollbar=tk.Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
                self.canvas.configure(yscrollcommand=self.myscrollbar.set)
                self.myscrollbar.pack(side="right",fill="y")

                #determines where canvas is 
                self.canvas.pack(side="left")

                #this allows for the frame with the widgets that are buttons
                self.canvas.create_window((0,0),window=self.frame,anchor='nw')

                #binding the myfunction to the frame to allow for scrolling 
                self.frame.bind("<Configure>", self.myfunction)
                self.FQAs()
                self.master.grab_set() 

        def closeWindow(self):
                self.master.destroy()

class editPlaylist:
        def __init__(self, master, playlistURI,  name_db, sp, userClass):
                self.name_db = name_db
                self.sp = sp
                self.userClass = userClass
                self.master = master
                #select username from playlistmaster where playlisturi = uri
                self.master.title("View Playlist")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")
                
                print("this is the uri " + playlistURI)
                
                # c.execute("""SELECT username FROM playlistmaster WHERE playlisturi = '""" + u  + """';""")
                # self.pURI = c.fetchall()
                # for i in self.pURI:
                #         print(i)
                database = sqlite3.connect(self.name_db)
                c = database.cursor()
                fetchPlaylistTitle = """SELECT username FROM playlistmaster WHERE playlisturi = """ + playlistURI + """;"""
                
                c.execute(fetchPlaylistTitle)
                playlistTitle = str(c.fetchone()).strip('(,)\'')
                
                # Playlist title label
                self.t = Label(self.master, text =  str(playlistTitle) ,  fg = "black", bg = "green", bd = 6, width = 20, relief = "sunken", font = "Helvetica 35 bold italic")
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

                #Edit/Options
                self.add = Button(self.master,
                text = "Add\nSong",
                bg ="green", bd = 6,
                relief = "raised",
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2,
                command = lambda x = playlistURI: self.add_song(x)) ###
                self.add.place(x = 0, y = 165)

                self.rem = Button(self.master,
                text = "Remove\nSong",
                bg ="green", bd = 6,
                relief = "raised", 
                font = "Helvetica 19 bold italic",
                width = 14,
                height = 2,
                command = lambda x = playlistURI: self.remove_song(x)) ###
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
                command = lambda x = playlistURI: self.deleteP(x)) ###
                self.de.place(x = 0, y = 415)

                self.rec = Button(self.master,
                        text = "Add\nRecommendations",
                        bg ="green",
                        bd = 6,
                        relief = "raised",
                        font = "Helvetica 19 bold italic",
                        width = 14,
                        height = 2,
                        command = lambda x = playlistURI: self.addRec(x))
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
                pURI = playlistURI.replace('spotify:playlist:', '').strip('\'')
                print(pURI)
                c.execute("""SELECT songname FROM """ + pURI + """;""")
                songs = c.fetchall()

                self.fields = Label(self.master, text = 'Song Title', fg = "black", bg = "green", bd = 6, width = 39, relief = "sunken", font = "Helvetica 18 bold italic")
                self.fields.place(x = 275, y = 150)

                self.listbox = Listbox(self.master, bg = "gray", height = 16, width = 53, bd = 6, relief = "sunken", font = "Helvetica 15 bold italic") 
                self.listbox.pack(side = RIGHT, fill = BOTH) 
                self.listbox.place(x = 275, y = 220)
                self.scrollbar = Scrollbar(self.master) 

                for self.values in songs: 
                        sngs =str(self.values).strip(',()').replace('\'', '')
                        self.listbox.insert(END, sngs) 

                self.listbox.config(yscrollcommand = self.scrollbar.set) 
                self.scrollbar.config(command = self.listbox.yview)

                # forces user to click on certain window
                self.master.grab_set()
                database.close()
        def addRec(self, playlistURI,name_db):
                pURI = playlistURI.replace('spotify:playlist:', '').strip('\'')
                print(pURI)
                database = sqlite3.connect(name_db)
                c = database.cursor()
                c.execute("""SELECT COUNT(songname) FROM playlist""" + pURI + """;""")
                s = c.fetchall()

                numOfSongs = str(s[0]).strip(',()')

                print(numOfSongs)

                if int(numOfSongs) >= 60:
                        tk.messagebox.showerror('Error!','The max amount of songs (60) has been reached.')
                else:
                        #add recommendations function goes here
                        #add recommendations function goes here
                        #if successfully added:
                        tk.messagebox.showinfo('Recommendations added!','Recommendations have been added to your playlist reaching the max number of songs (60).')    
                database.close()
        def closeWindow(self):
                self.master.destroy()
        
        def analysis_window(self):
                self.newAnalysisWindow = tk.Toplevel(self.master)
                self.moodipy = analysis(self.newAnalysisWindow, self.name_db, self.sp, self.userClass)

        def help_doc(self):
                self.newHelpDoc = tk.Toplevel(self.master)
                self.moodipy = helpDoc(self.newHelpDoc, self.name_db, self.sp, self.userClass)

        def rank_songs(self):
                self.newRankSongs = tk.Toplevel(self.master)
                self.moodipy = rankSongs(self.newRankSongs, self.name_db, self.sp, self.userClass)

        def add_song(self, playlistURI):
                self.newAddSong = tk.Toplevel(self.master)
                self.moodipy = addSong(self.newAddSong, playlistURI, self.name_db, self.sp, self.userClass)

        def remove_song(self, playlistURI):
                self.newRemoveSong = tk.Toplevel(self.master)
                self.moodipy = removeSong(self.newRemoveSong, playlistURI, self.name_db, self.sp, self.userClass)


class rankSongs:
        def __init__(self, master, name_db, sp, userClass):
                self.name_db = name_db
                self.sp = sp
                self.userClass = userClass
                self.master = master
                self.master.title("Time to rank songs!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                #need to add function to add to command so it can bring back to playlist and give back the ratings chosen
                #add recommendations function would go here inside function when created
                #add recommendations function would go here inside function when created

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
        def __init__(self, master, playlistURI, name_db, sp, userClass):
                self.name_db = name_db
                self.userClass = userClass
                self.sp = sp
                self.playlistURI
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
                                bd = 6, 
                                relief = "raised", 
                                font = "Helvetica 30 bold italic", 
                                width = 9, 
                                height = 2,
                                command = lambda x = playlistURI: self.addSongToPlaylist(x))

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
        def addSongToPlaylist(self, playlistURI, name_db):
                database = sqlite3.connect(name_db)
                c = database.cursor()
                self.titleAdd = self.et.get()
                self.artistAdd = self.ea.get()
                print(self.titleAdd)
                print(self.artistAdd)

                pURI = playlistURI.replace('spotify:playlist:', '').strip('\'')
                print(pURI)
                c.execute("""SELECT COUNT(songname) FROM playlist""" + pURI + """;""")
                s = c.fetchall()

                numOfSongs = str(s[0]).strip(',()')

                print(numOfSongs)

                if int(numOfSongs) < 60:
                        self.confirmAdd = tk.messagebox.askquestion("confirm song to be added", "Are you sure you want to add this song?")

                        if self.confirmAdd == 'yes':
                                print("yes")
                                #add add song function here
                                # inputs: list of uri's and names
                                # output: 
                                #add add song function here
                                #if song is added, get a return from function that indicates its added:
                                tk.messagebox.showinfo("song added!", "Your song has been added! Click cancel to go back to your playlist or add another song.") 
                                #else if not added (get something from function that indicates its has not been added), display try again:
                                tk.messagebox.showerror("Error", "A problem has occurred adding this song. Please try again.")               
                        elif self.confirmAdd == 'no':
                                tk.messagebox.showinfo('Return','You will now return to the add song window. Here you can either enter another song to add or click cancel to go back to your playlist.')
                else:
                        tk.messagebox.showerror('Error','The max amount of songs (60) has been reached. Please click cancel when returned to the add song window and delete a song to add more.')

        def closeWindow(self):
                database.close()
                self.master.destroy()


class removeSong:

        def __init__(self, master, playlistURI, name_db, sp, userClass):
                self.sp = sp
                self.name_db = name_db
                self.userClass = userClass
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
                                command = lambda x = playlistURI: self.remove(x))

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
        def remove(self, playlistURI):
                self.titleRemove = self.et1.get()
                self.artistRemove = self.ea1.get()
                print(self.titleRemove)
                print(self.artistRemove)

                #name of table for playlist that its on
                pURI = playlistURI.replace('spotify:playlist:', '').strip('\'')
                print("URI where song will be removed: " + pURI)

                self.rm = tk.messagebox.askquestion("confirm song removal", "Are you sure you want to remove this song?")

                if self.rm == 'yes':
                        print("yes")
                        #add remove function here
                        #if song is removed, get a return from function that indicates its removed:
                        tk.messagebox.showinfo("song removed!", "Your song has been removed! Click cancel to go back to your playlist or remove another song.") 
                        #else if not removed, display try again:
                        tk.messagebox.showerror("Error", "A problem has occurred removing this song. Please check your playlist to ensure this song is in it by clicking cancel. If it is on your playlist, then please try again.") 
                elif self.rm == 'no':
                        tk.messagebox.showinfo('Return','You will now return to the remove song window. Here you can either enter another song to remove or click cancel to go back to your playlist.')

        def closeWindow(self):
                self.master.destroy()

class analysis:
        def __init__(self, master,name_db, sp, userClass):
                self.sp = sp
                self.name_db = name_db
                self.userClass = userClass
                self.master = master
                self.master.title("Analysis")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x680")

                self.title = tk.Label(self.master, text ="Here's an analysis of your playlist:", 
                                fg = "black", 
                                bg = "green", 
                                bd = 10, 
                                relief = "sunken", 
                                height = 2,
                                width = 32,
                                font = "Helvetica 28 bold italic")
                self.title.place(x = 90, y = 30)

                self.stuff = tk.Label(self.master, text ="Static |  Description |  Happy  |  Sad  | Motivated  |  Calm | Frantic  | Party  |  Gaming", 
                        fg = "black", 
                        bg = "gray", 
                        bd = 8, 
                        relief = "sunken", 
                        height = 1,
                    width = 80,
                    font = "Helvetica 10 bold italic")
                self.stuff.place(x = 0, y = 150)
                self.stuff1 = tk.Label(self.master, text ="Valence | 0-1 scale of how cheerful the track is  | > 0.5 | < 0.5 | NA | NA | NA | > 0.5 | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff1.place(x = 0, y = 180)

                self.stuff2 = tk.Label(self.master, text ="Energy   | 0-1 scale of how energetic the track is | NA | NA | >.7 |  <.7 |  >.7  | >.7  | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff2.place(x = 0, y = 210)

                self.stuff3 = tk.Label(self.master, text ="Acousticness | 0-1 scale of how acoustic the track is | NA | NA | NA | NA | NA | NA | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff3.place(x = 0, y = 240)
                self.stuff4 = tk.Label(self.master, text ="Danceability | 0-1 scale of how much you can dance to the track | NA | NA | NA | NA | NA | >.65 | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff4.place(x = 0, y = 270)
                self.stuff5 = tk.Label(self.master, text ="Speechiness | 0-1 how much speech dominates the track | NA | NA | NA | NA | NA | NA | <.085", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff5.place(x = 0, y = 300)
                self.stuff6 = tk.Label(self.master, text ="Tempo | Bpm measure of track | NA | NA | NA | <120 | >120 | NA | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff6.place(x = 0, y = 330)
                self.stuff7 = tk.Label(self.maste, text ="Popularity | 0-100 scale of track’s popularity | NA | NA | NA | NA | NA | >65 | NA", 
                                        fg = "black", 
                                        bg = "gray", 
                                        bd = 8, 
                                        relief = "sunken", 
                                        height = 1,
                                width = 80,
                                font = "Helvetica 10 bold italic")
                self.stuff7.place(x = 0, y = 360)

                self.Done = Button(self.master, text = "Done", bg ="green", bd = 6, relief = "raised", font = "Helvetica 20 bold italic", width = 10, height = 3, command = self.closeWindow)
                self.Done.place(x = 685, y = 530)
                self.master.grab_set()

        def closeWindow(self):
                self.master.destroy()

class login:

        def __init__(self, master):
                self.master = master
                self.master.title("Welcome to Moodipy!")
                self.master.configure(bg = "black")
                self.master.resizable(width = False, height = False)
                self.master.geometry("900x600")
                self.usernameEntry = Entry(self.master, font = "Helvetica 20 italic", width = 21) 
                self.usernameEntry.place(x = 440, y = 400) 
 
                self.uTitle = tk.Label(self.master, text ='username:', 
                                fg = "black", 
                                bg = "green", 
                                bd = 8, 
                                relief = "sunken", 
                                height = 1,
                                width = 10,
                                font = "Helvetica 20 bold italic")
                self.uTitle.place(x = 225, y = 400)

                self.B = Button(self.master,
                text = "Login with Spotify",
                bg ="green",
                font = "Helvetica 18 bold italic",
                bd = 6, relief = "raised",
                width = 25,
                height = 2,
                ##### call spotify login function here
                # for now it will just close the window
                command = self.log)
                self.B.place(x = 225,y = 480)
                self.canvas = Canvas(self.master, width = 400, height = 350)
                self.canvas.pack()
                self.img = ImageTk.PhotoImage(Image.open("./GUI/mainSnake.png"))
                self.canvas.create_image(75, 75, anchor=NW, image=self.img)


        def log(self):

                self.username = self.usernameEntry.get()
                print(self.username)
                def find(pattern, path):
                        result = []
                        for root, dirs, files in os.walk(path):
                            for name in files:
                                if fnmatch.fnmatch(name, pattern):
                                    result.append(os.path.join(root, name))
                        return result

                cList = find('.cache-*', '../')
                print(cList)
                for entry in cList:
                    os.remove(entry)

                cList = find('.cache-*', '../')
                print(cList)
                self.name_db = self.username + '.db'                
                sql_create_database(self.name_db)
                
                #username = 'b3qviosg0fm0mqq9k0uh6uit1' # Must be changed for final version
                authorize = auth(self.username)
                self.sp = authorize.authorize_util() # Spotify authorized class
                self.userClass = User(self.sp)

                cList = find('.cache-*', '../')
                name = '' # Spotify username of user
                if len(cList) > 1:
                    print("Error, to many cache files")
                    tk.messagebox.showerror('Login failed', 'Multiple cache files found. Please try again')
                elif len(cList) == 0:
                    print("Error, no cache file found")
                    tk.messagebox.showerror('Login failed', 'No cache file found, login unsuccessful')
                    sys.exit()
                else:
                    name = cList[0][cList[0].find('-')+1:] #stripped down username from spotify
                    print("Found Spotify username:"+ name+"\nUsing it to create a database file.")
                database = sqlite3.connect(name+".db")
                #c = database.cursor()
                self.main_menu()


        def closeWindow(self):
                # add login function here
                self.master.destroy()

        def main_menu(self):
                self.newMainMenu = tk.Toplevel(self.master)
                self.moodipy = mainMenu(self.newMainMenu, self.name_db, self.sp, self.userClass)

        #def main_menu(self)

def main():
        #add function to check login credentials
        root = tk.Tk()
        moodipy = login(root)
        
        # if creds match:
                
                # close login window with closeWindow()
                # open mainmenu
        # else
                #show error
        
        root.mainloop()

if __name__ == '__main__':
        main()