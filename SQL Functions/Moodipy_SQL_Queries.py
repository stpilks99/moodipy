#Moodipy SQL
import sqlite3
import os

#if os.path.exists("moodipy.db"): # remove existing database file if it exists.
#    os.remove("moodipy.db")
#    print("resetting db")
#else:
#    print("DB File does not exist")

database = sqlite3.connect("moodipy.db")
cursor = database.cursor()

def addS(option,addsong,songname):
    if option == '1':
        cursor.execute(addsong)
        cursor.execute(songname)
        query_result = cursor.fetchall()
        for i in query_result:
          print(i)
    return i

def printS(option,songname,username):
    if option == '2':
        cursor.execute(songname)
        cursor.execute(username)
        query_result = cursor.fetchall()
        for i in query_result:
          print(i)
    return i

def main():
    #menu

    option = input("Select an option ")


    addsong = """INSERT INTO playlist5 (songuri, songname, songrating) 
             VALUES ('spotify:track:3yrSvpt2l1xhsV9Em88Pul','Brown Eyed Girl','10');"""

    songname = """SELECT songname FROM playlist5;"""

    username = """SELECT username FROM playlistmaster WHERE playlistname = 'playlist5';"""