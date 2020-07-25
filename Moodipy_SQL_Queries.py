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

def addS(self,sURI,sNAME,userPlaylist,list):              #add song function
    #songInfo = (sURI,sNAME)
    for i in range(len(list)):
        songInfo = list[i]
        sURI  = songInfo[0]
        sNAME = songInfo[1]
        query1 = """INSERT INTO """ + userPlaylist + """           
             VALUES ('""" + sURI + """','""" + sNAME + """');"""
        cursor.execute(query1)
         
    query2 = """SELECT songname FROM """ + userPlaylist + """;"""
    
    cursor.execute(query2)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)
    database.commit()

def removeS(self,sURI,userPlaylist):
    query1 = """DELETE FROM """ + userPlaylist + """ WHERE songuri = '""" + sURI + """'"""
    cursor.execute(query1)
    database.commit()

def printS(self,sNAME,username,userPlaylist):           #print song function
    sNAME = """SELECT sNAME FROM """ + userPlaylist + """;"""
    username = """SELECT username FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(sNAME)
    cursor.execute(username)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def getNumbT(self,numTrack,userPlaylist):                         #get number of tracks in playlist
    numTrack = """SELECT COUNT(sURI) FROM """ + userPlaylist + """;"""
    cursor.execute(numTrack)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)

def createP(self,newPlaylist,userPlaylist):                       #create a playlist
    newPlaylist = """INSERT INTO playlistmaster (playlistname, playlistmood,playlistperiod, preferredartist, preferredgenre) VALUES ('""" + userPlaylist + """','jazz','2000','jackson5','swing'); 
    CREATE TABLE " """ + userPlaylist + """ (
	"sURI"	TEXT,
	"sNAME"	TEXT,
	"songrating"	NUMERIC,
	PRIMARY KEY("sURI")
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
    

    

    

    

    
    
    

    

	
    
    