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

def addS(self,songuri,songname,userPlaylist):              #add song function
    query1 = """INSERT INTO """ + userPlaylist + """ (songuri, songname, songrating) 
             VALUES ('spotify:track:3yrSvpt2l1xhsV9Em88Pul','Brown Eyed Girl','10');"""
    query2 = """SELECT songname FROM """ + userPlaylist + """;"""
    cursor.execute(query1)
    cursor.execute(query2)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def printS(self,songname,username,userPlaylist):           #print song function
    songname = """SELECT songname FROM """ + userPlaylist + """;"""
    username = """SELECT username FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(songname)
    cursor.execute(username)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def getNumbT(self,numTrack,userPlaylist):                         #get number of tracks in playlist
    numTrack = """SELECT COUNT(songuri) FROM """ + userPlaylist + """;"""
    cursor.execute(numTrack)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def createP(self,newPlaylist,userPlaylist):                       #create a playlist
    newPlaylist = """INSERT INTO playlistmaster (playlistname, playlistmood,playlistperiod, preferredartist, preferredgenre) VALUES ('""" + userPlaylist + """','jazz','2000','jackson5','swing'); 
    CREATE TABLE " """ + userPlaylist + """ (
	"songuri"	TEXT,
	"songname"	TEXT,
	"songrating"	NUMERIC,
	PRIMARY KEY("songuri")
    );"""
    cursor.execute(newPlaylist)
    cursor.execute()
    return 0

def removeP(self,userPlaylist):                       #remove a playlist
    #remove the table
    #remove the table row from the playlistmaster
    remPlaylist = """DROP TABLE """  + userPlaylist + """; DELETE FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(remPlaylist)
    return 0

def main():
    #menu

    userPlaylist = " "

    option = input("Select an option ")


    

    

    

    
    
    

    

	
    
    