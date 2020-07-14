# Moodipy SQL Team SQL Database creation, and functions

import os
import sqlite3
if os.path.exists("moodipy.db"): # remove existing database file if it exists.
    os.remove("moodipy.db")
    print("resetting db")
else:
    print("DB File does not exist")

database = sqlite3.connect("moodipy.db")
cursor = database.cursor()

setup_master = """CREATE TABLE "playlistmaster" (
	"playlisturi"	CHAR(39) NOT NULL UNIQUE,
	"username"	TEXT,
	"playlistmood"	TEXT,
	"playlistperiod"	TEXT,
	"preferredartist"	TEXT,
	"preferredgenre"	TEXT,
	"explicit"	BOOL,
	PRIMARY KEY("playlisturi")
);"""
cursor.execute(setup_master)
#example data
playlisturi = "hello"
playlistmood = "Happy"
playlistperiod = "2000"
preferredartist = "hamilton"
preferredgenre = "rap"
explicit = "true"
#replace this data

#create entry in playlist master table
sqlcommand = "INSERT INTO playlistmaster (playlisturi, playlistmood,playlistperiod, preferredartist, preferredgenre, explicit) " +\
          "VALUES('"+playlisturi+"','"+playlistmood+"','"+playlistperiod+"','"+preferredartist+"','"+preferredgenre+"','"+explicit+"')"
cursor.execute(sqlcommand)
#print(sqlcommand) #debug to see SQL command

#create table for playlist
sqlcommand = "CREATE TABLE "+playlisturi+""" ("songuri"	CHAR(36) NOT NULL UNIQUE,
       "songname"	TEXT,
       "songrating"	NUMERIC,
       PRIMARY KEY("songuri"));"""
#print(sqlcommand) #debug to see SQL command
cursor.execute(sqlcommand)


database.commit() #actually save the database
database.close()
