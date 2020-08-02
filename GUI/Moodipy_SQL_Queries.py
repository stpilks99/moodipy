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

    # if uri already in database table, get rid of it.
    if len(uri_name_list[0]) == 0: # Check length
        return False
    try:
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
            try:
                cursor.execute(query1)
            except:
                database.commit()
                sNAME = sNAME + " (1)"
                query1 = """INSERT INTO '""" + userPlaylist + """'          
                VALUES('""" + sURI + """', '""" + sNAME + """', 0); """
                try:
                    cursor.execute(query1)
                except:
                    sNAME = sNAME + " (2)"
                    query1 = """INSERT INTO '""" + userPlaylist + """'          
                    VALUES('""" + sURI + """', '""" + sNAME + """', 0); """
                    cursor.execute(query1)
                    continue
                # Check all previous names in the database
                continue
    except:
        return False

    database.commit()
    database.close()
    return True

def get_track_uri(Puri,SongTitle, name_db):
    database = sqlite3.connect(name_db)
    cursor = database.cursor()
    SongTitle = SongTitle.replace("'", "") #remove '
    qurry = "select songuri from "+ Puri +" where songname like '%"+ SongTitle+"%'";
    print(qurry)
    cursor.execute(qurry)
    query_result = cursor.fetchall()
    try:
        adj_result = query_result[0][0] #get actual result
    except:
        print("No song:"+SongTitle+" Found in playlist table:"+Puri+" Please try again.")
        adj_result = "No Result"
    database.close()
    return adj_result

def removeS(song_title,playlist_uri, databaseName):
    playlist_name = uri_to_title(playlist_uri)
    sURI = get_track_uri(playlist_name, song_title, databaseName)
    if sURI == "No Result":
        return False # Song not found in database

    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    query1 = """DELETE FROM """ + playlist_name + """ WHERE songuri = '""" + sURI + """'"""
    try:
        cursor.execute(query1)
        database.commit()
        database.close()
    except:
        database.commit()
        database.close()
        return False
    return sURI

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


def createP(databaseName, uri, mood, artist, genre, p_title):  # create a playlist
    # create entry in playlist master table
    p_title_uri = uri_to_title(uri)
    database = sqlite3.connect(databaseName)
    cursor = database.cursor()
    first_genre = genre[0]
    if artist  == "":
        artist = "null"
    try:
        sqlcommand = "INSERT INTO playlistmaster (playlisturi, username, playlistmood, preferredartist, preferredgenre) " + \
                     "VALUES('" + p_title_uri + "','" + p_title + "','" + mood  + "','" + artist + "','" + first_genre + "')"
        cursor.execute(sqlcommand)
     #create table for playlist
        sqlcommand = "CREATE TABLE '"+p_title_uri+"""' ("songuri"	CHAR(36) NOT NULL UNIQUE,
               "songname"	TEXT UNIQUE,
               "songrating"	NUMERIC,
               PRIMARY KEY("songuri"));"""
        cursor.execute(sqlcommand)
    except:
        database.close()
        return False
    database.commit()  # actually save the database
    database.close()
    return True

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
    "Songuri"	TEXT);"""
    c.execute(setup_deleted_songs)

    database.commit()
    database.close()
    return 0

#Puri format:"playlist37i9dQZF1DWZAkrucRF6Gq"
#returns true if success, else returns false
def remove_lowrank_tracks(Puri, name_db):
    database = sqlite3.connect(name_db)
    cursor = database.cursor()
    try:
        qurry1 = """INSERT into deletedsongs select songuri from """+Puri+""" where songrating ==0;"""
        qurry2 = """delete from """+Puri+""" where songrating ==0;"""
        cursor.execute(qurry1)
        cursor.execute(qurry2)
    except:
        return False
        database.close()
    database.commit()
    database.close()
    return True

#Puri format:"playlist37i9dQZF1DWZAkrucRF6Gq"
#returns song list if success, else returns blank list
def get_slist_from_puri(Puri, name_db):
    database = sqlite3.connect(name_db)
    cursor = database.cursor()
    sNAME = """select songuri from """+Puri+""";"""
    try:
        cursor.execute(sNAME)
        query_result = cursor.fetchall()
        info  = list(query_result)
        songs = []
        for i in range(len(query_result)):
            name = info[i] #tuple drill to get to uri
            name = name[0] #tuple drill to get to uri
            songs.append(name)
    except:
        return []
        database.close()
    database.close()
    return songs

def update_track_rating(Puri,Suri,rank, name_db): #puri example: playlist37i9dQZF1DWZAkrucRF6Gq	
    database = sqlite3.connect(name_db)	    
    cursor = database.cursor()	    
    rank = str(rank)	    
    try:	    
        querry = "UPDATE "+Puri+" SET songrating = "+rank+" WHERE songuri IS '"+Suri+"';"	    
        print(querry)	        
        cursor.execute(querry)	        
        database.commit()	        
        database.close()	        
        return True	        
    except:
        print("Error updating song rank")
        database.close()
        return False	        
    return True  #we don't need this but it feels weird not to have it



def get_playlist_info(Puri, name_db):   #puri example: playlist37i9dQZF1DWZAkrucRF6Gq	
    #userPlaylist = uri_to_title(Puri)	  
    database = sqlite3.connect(name_db)	    
    cursor = database.cursor()
    sNAME = """select * from playlistmaster where playlisturi = '"""+Puri+"""'"""	 
    cursor.execute(sNAME)	  
    query_result = cursor.fetchall()	
    for i in query_result:	 
        print(i)
    database.close()
    #bs comment	   
    return query_result