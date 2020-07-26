#Moodipy SQL
import sqlite3
import os

#if os.path.exists("moodipy.db"): # remove existing database file if it exists.
#    os.remove("moodipy.db")
#    print("resetting db")
#else:
#    print("DB File does not exist")

# database = sqlite3.connect("moodipy.db")
# cursor = database.cursor()




def addS(self,sURI,sNAME,userPlaylist,list, databaseName):              #add song function
    #songInfo = (sURI,sNAME)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    for i in range(len(list)):
        songInfo = list[i]
        sURI  = songInfo[0]
        sNAME = songInfo[1]
        try:
            query1 = """INSERT INTO """ + userPlaylist + """           
                VALUES ('""" + sURI + """','""" + sNAME + """');"""
            cursor.execute(query1)
        except:
            return False 
    database.commit()
    database.close()
    return True

def removeS(self,sURI,userPlaylist, databaseName):
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    query1 = """DELETE FROM """ + userPlaylist + """ WHERE songuri = '""" + sURI + """'"""
    cursor.execute(query1)
    database.commit()
    database.close()

def printS(self,sNAME,username,userPlaylist, databaseName):           #print song function
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    sNAME = """SELECT sNAME FROM """ + userPlaylist + """;"""
    username = """SELECT username FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(sNAME)
    cursor.execute(username)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)
    database.close()

def getNumbT(self,numTrack,userPlaylist, databaseName):                         #get number of tracks in playlist
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    numTrack = """SELECT COUNT(sURI) FROM """ + userPlaylist + """;"""
    cursor.execute(numTrack)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)
    database.close()

def createP(self, userPlaylist, databaseName):                       #create a playlist
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    newPlaylist = """INSERT INTO playlistmaster (playlisturi, playlistmood,playlistperiod, preferredartist, preferredgenre) VALUES ('""" + userPlaylist + """','jazz','2000','jackson5','swing');""" 
    try:
        cursor.execute(newPlaylist)
    except:
        return -1
    cmd = """CREATE TABLE " """ + userPlaylist + """ (
            "sURI"	TEXT,
            "sNAME"	TEXT,
            "songrating"	NUMERIC,
            PRIMARY KEY("sURI")
            );"""
    try:
        cursor.execute(cmd)
        database.commit()
    except:
        return -1
    finally:
        database.close()
    return 0

def removeP(self, userPlaylist, databaseName):                       #remove a playlist
    #remove the table
    #remove the table row from the playlistmaster
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    remPlaylist = """DROP TABLE """  + userPlaylist + """; DELETE FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(remPlaylist)
    database.commit()
    database.close()
    return 0

