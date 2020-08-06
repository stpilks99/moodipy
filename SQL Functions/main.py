# Moodipy SQL Team SQL Database creation, and functions

import os
# remove existing database file if it exists.
if os.path.exists("moodipy.db"):
    os.remove("moodipy.db")
    print("resetting db")
else:
    print("DB File does not exist")
# We can remove this if we want the database to persist between sessions
import sqlite3
database = sqlite3.connect("moodipy.db")
cursor = database.cursor()

def create_database():
    setup_master = """CREATE TABLE "playlistmaster" (
        "playlisturi"	CHAR(39) NOT NULL UNIQUE,
        "username"	TEXT,
        "playlistmood"	TEXT,
        "preferredartist"	TEXT,
        "preferredgenre"	TEXT,
        PRIMARY KEY("playlisturi")
    );"""
    # playlisturi is 39 characters long
    # songuri's are 36 characters long
    cursor.execute(setup_master)
    return 0

def create_playlist(uri,mood,artist,genre):
    # create entry in playlist master table
    sqlcommand = "INSERT INTO playlistmaster (playlisturi, playlistmood, preferredartist, preferredgenre) " + \
                 "VALUES('" + uri + "','" + mood + "','"  + artist + "','" + genre + "')"
    cursor.execute(sqlcommand)
    # print(sqlcommand) #debug to see SQL command

    #create table for playlist
    sqlcommand = "CREATE TABLE "+uri+""" ("songuri"	CHAR(36) NOT NULL UNIQUE,
           "songname"	TEXT,
           "songrating"	NUMERIC,
           PRIMARY KEY("songuri"));"""
    #print(sqlcommand) #debug to see SQL command
    cursor.execute(sqlcommand)
    database.commit()  # actually save the database
    return 0


create_database()
create_playlist("thisisanidentifier","happy","2000","Hamilton","rap","true")


database.close()