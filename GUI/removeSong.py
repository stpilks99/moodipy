import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 

removeSong = tk.Tk()
removeSong.title("Time to remove a song from the playlist!")
removeSong.configure(bg = "black")
removeSong.resizable(width = False, height = False)
removeSong.geometry("900x680")

lt = tk.Label(removeSong, text ='Please enter the title and artist of\n the song title you would like to remove:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 3,
                width = 32,
                font = "Helvetica 30 bold italic")
lt.place(x = 56, y = 70)

#function that gets the title and artist to remove from playlist
#in this function need to add the function from functions group since command only accepts one function
def remove():
    titleRemove = et1.get()
    artistRemove = ea1.get()
    print(titleRemove)
    print(artistRemove)

    rm = messagebox.askquestion("confirm song removal", "Are you sure you want to remove this song?")

    if rm == 'yes':
        print("yes") #add remove function
        #if song is removed, get a return from function that indicates its removed
        messagebox.showinfo("song removed!", "Your song has been removed! Click cancel to go back to your playlist or remove another song.") 
        #else if not removed, display try again
        messagebox.showerror("Error", "A problem has occurred removing this song. Please check your playlist to ensure this song is in it by clicking cancel. If it is on your playlist, then please try again.") 
    elif rm == 'no':
        tk.messagebox.showinfo('Return','You will now return to the remove song window. Here you can either enter another song to remove or click cancel to go back to your playlist.')

#getting entry for title of song
et1 = Entry(removeSong, font = "Helvetica 40 italic", width = 21) 
et1.place(x = 230, y = 290) 

t1 = tk.Label(removeSong, text ='Title:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 1,
                width = 5,
                font = "Helvetica 32 bold italic")
t1.place(x = 65, y = 290)

#getting entry for artist of song
a1 = tk.Label(removeSong, text ='Artist:', 
                fg = "black", 
                bg = "green", 
                bd = 8, 
                relief = "sunken", 
                height = 1,
                width = 5,
                font = "Helvetica 32 bold italic")
a1.place(x = 65, y = 400)

ea1 = Entry(removeSong, font = "Helvetica 40 italic", width = 21) 
ea1.place(x = 230, y = 400) 

#creates Remove button that brings to playlist window
Remove = Button(removeSong, text = "Remove", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 9, 
                height = 2,
                command = remove)

Remove.place(x = 630, y = 520)

#creates cancel button that brings back to playlist window
Cancelr = Button(removeSong, text = "Cancel", 
                bg ="green", 
                bd = 6, 
                relief = "raised", 
                font = "Helvetica 30 bold italic", 
                width = 9, 
                height = 2)
Cancelr.place(x = 42 , y = 520)

removeSong.mainloop()