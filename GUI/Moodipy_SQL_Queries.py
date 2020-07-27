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

def uri_to_title(uri):
    '''Takes full URI and takes only the last part'''
    uri_split = uri.split(':')
    playlist_title = 'playlist' + uri_split[2]
    return playlist_title


def addS(userPlaylist,uri_name_list, databaseName):              #add song function
    #songInfo = (sURI,sNAME)
    userPlaylist = uri_to_title(userPlaylist)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    for i in uri_name_list:
        songInfo = list(i)
        sURI = """"""
        sNAME = """"""
        sURI  = songInfo[0]
        sNAME = songInfo[1]
        sNAME = sNAME.replace("'", "") #remove the ' character
        print(sNAME)
        query1 = """INSERT INTO '""" + userPlaylist + """'          
                    VALUES ('""" + sURI + """','""" + sNAME + """', 0);"""
        cursor.execute(query1)


    database.commit()
    database.close()
    return True

def removeS(sURI,userPlaylist, databaseName):
    userPlaylist = uri_to_title(userPlaylist)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    query1 = """DELETE FROM """ + userPlaylist + """ WHERE songuri = '""" + sURI + """'"""
    try:
        cursor.execute(query1)
        return True
    except:
        return False
    database.commit()
    database.close()

def printS(sNAME,username,userPlaylist, databaseName):           #print song function
    userPlaylist = uri_to_title(userPlaylist)
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

def getNumbT(numTrack,userPlaylist, databaseName):                         #get number of tracks in playlist
    userPlaylist = uri_to_title(userPlaylist)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    numTrack = """SELECT COUNT(sURI) FROM """ + userPlaylist + """;"""
    cursor.execute(numTrack)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)
    database.close()


def createP(databaseName, uri, mood, period, artist, genre, explicit, p_title):  # create a playlist
    # create entry in playlist master table
    p_title_uri = uri_to_title(uri)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    first_genre = genre[0]
    if artist  == "":
        artist = "null"
    period = period.replace("'","")
    period = period.replace("+", "")
    sqlcommand = "INSERT INTO playlistmaster (playlisturi, username, playlistmood,playlistperiod, preferredartist, preferredgenre, explicit) " + \
                 "VALUES('" + p_title_uri + "','" + p_title + "','" + mood + "','" + period + "','" + artist + "','" + first_genre + "','" + str(explicit) + "')"
    print(sqlcommand)  # debug to see SQL command
    cursor.execute(sqlcommand)


    #create table for playlist
    sqlcommand = "CREATE TABLE '"+p_title_uri+"""' ("songuri"	CHAR(36) NOT NULL UNIQUE,
           "songname"	TEXT,
           "songrating"	NUMERIC,
           PRIMARY KEY("songuri"));"""
    # print(sqlcommand) #debug to see SQL command
    cursor.execute(sqlcommand)
    database.commit()  # actually save the database
    database.close()
    return 0

def removeP(userPlaylist, databaseName):                       #remove a playlist
    #remove the table
    #remove the table row from the playlistmaster
    userPlaylist = uri_to_title(userPlaylist)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    remPlaylist = """DROP TABLE """  + userPlaylist + """; DELETE FROM playlistmaster WHERE playlistname = '""" + userPlaylist + """';"""
    cursor.execute(remPlaylist)
    database.commit()
    database.close()
    return 0

def sql_delete_playlist(self,pURI, name_db):
    # sql delete playlist function
    database = sqlite3.connect(name_db)
    c = database.cursor()
    pURISPOT = "playlist" + pURI  # matching the pURI (Just the sudo string) to the table name
    querry1 = """DROP TABLE """ + pURISPOT + """; """
    querry2 = """DELETE FROM playlistmaster WHERE playlisturi = '""" + pURISPOT + """';"""
    c.execute(querry1)
    c.execute(querry2)
    database.commit()  # actually save the database
    database.close()


def sql_create_database(name_db):
    database = sqlite3.connect(name_db)
    c = database.cursor()
    setup_master = """CREATE TABLE IF NOT EXISTS "playlistmaster" (
        "playlisturi"	CHAR(39) NOT NULL UNIQUE,
        "username"	TEXT,
        "playlistmood"	TEXT,
        "playlistperiod"	TEXT,
        "preferredartist"	TEXT,
        "preferredgenre"	TEXT,
        "explicit"	BOOL,
        PRIMARY KEY("playlisturi")
    );"""
    c.execute(setup_master)
    setup_deleted_songs = """CREATE TABLE IF NOT EXISTS "deletedsongs" (
    "SongURI"	TEXT);"""
    c.execute(setup_deleted_songs)

    database.commit()
    database.close()
    return 0

