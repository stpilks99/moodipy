import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 

addSong = tk.Tk()
addSong.title("Time to add a song to the playlist!")
addSong.configure(bg = "black")
addSong.resizable(width = False, height = False)
addSong.geometry("900x680")

lt = tk.Label(addSong, text ='Please enter the title and artist\n of the song you would like to add:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 3,
                width = 28,
                font = "Helvetica 32 bold italic")
lt.place(x = 65, y = 70)

#function that gets the title and artist to add to playlist
#in this function need to add the function from functions group since command only accepts one function
def addSongs():
    titleAdd = et.get()
    artistAdd = ea.get()
    print(titleAdd)
    print(artistAdd)

    #if there are less than 60 songs then allow to add song
    confirmAdd = messagebox.askquestion("confirm song to be added", "Are you sure you want to add this song?")

    if confirmAdd == 'yes':
        print("yes") #add remove function
        #if song is added, get a return from function that indicates its added
        messagebox.showinfo("song added!", "Your song has been added! Click cancel to go back to your playlist or add another song.") 
        #else if not added, display try again
        messagebox.showerror("Error", "A problem has occurred adding this song. Please try again.") 
        #else if song max is reached display error
        tk.messagebox.showerror('Return','The max amount of songs (60) has been reached. Please click cancel when returned to the add song window.')
        
    elif confirmAdd == 'no':
        tk.messagebox.showinfo('Return','You will now return to the add song window. Here you can either enter another song to add or click cancel to go back to your playlist.')

    


#Creating label and entry to get the title of song
t = tk.Label(addSong, text ='Title:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 1,
                width = 5,
                font = "Helvetica 32 bold italic")
t.place(x = 65, y = 300)

et = Entry(addSong, font = "Helvetica 40 italic", width = 20) 
et.place(x = 230, y = 300) 


#Creating label and entry to get the artist of song
a = tk.Label(addSong, text ='Artist:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 1,
                width = 5,
                font = "Helvetica 32 bold italic")
a.place(x = 65, y = 400)

ea = Entry(addSong, font = "Helvetica 40 italic", width = 20) 
ea.place(x = 230, y = 400) 


#creates Add button that brings to playlist window
Add = Button(addSong, text = "Add", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 9, 
                height = 2,
                command = addSongs)

Add.place(x = 630, y = 520)

#creates cancel button that brings back to homepage
Cancela = Button(addSong, text = "Cancel", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 9, 
                height = 2)
Cancela.place(x = 42 , y = 520)

addSong.mainloop()