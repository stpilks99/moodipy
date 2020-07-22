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

def addS(self,option,addsong,songname):              #add song function
    cursor.execute(addsong)
    cursor.execute(songname)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def printS(self,option,songname,username):           #print song function
    cursor.execute(songname)
    cursor.execute(username)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def getNumbT(self,numTrack):                         #get number of tracks in playlist
    cursor.execute(numTrack)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def createP(self,newPlaylist):                       #create a playlist
    cursor.execute(newPlaylist)
    return 0

def removeP(self,remPlaylist):                       #remove a playlist
    cursor.execute(remPlaylist)
    return 0

def main():
    #menu

    userPlaylist = " "

    option = input("Select an option ")


    addsong = """INSERT INTO """ + userPlaylist + """ (songuri, songname, songrating) 
             VALUES ('spotify:track:3yrSvpt2l1xhsV9Em88Pul','Brown Eyed Girl','10');"""

    songname = """SELECT songname FROM """ + userPlaylist + """;"""

    username = """SELECT username FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""

    numTrack = """SELECT COUNT(songuri) FROM """ + userPlaylist + """;"""

    
    remPlaylist = """DROP TABLE """  + userPlaylist + """; DELETE FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    #remove the table
    #remove the table row from the playlistmaster

    newPlaylist = """INSERT INTO playlistmaster (playlistname, playlistmood,playlistperiod, preferredartist, preferredgenre) VALUES ('""" + userPlaylist + """','jazz','2000','jackson5','swing'); 
    CREATE TABLE " """ + userPlaylist + """ (
	"songuri"	TEXT,
	"songname"	TEXT,
	"songrating"	NUMERIC,
	PRIMARY KEY("songuri")
    );"""


	
    
    