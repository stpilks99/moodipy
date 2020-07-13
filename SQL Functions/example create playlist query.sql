--create row in master list of playlists with information from user
INSERT INTO playlistmaster (playlistname, playlistmood,playlistperiod, preferredartist, preferredgenre) VALUES ('playlist5','jazz','2000','jackson5','swing');
--create table to store songs that are part of playlist
CREATE TABLE "playlist5" (
	"songuri"	TEXT,
	"songname"	TEXT,
	"songrating"	NUMERIC,
	PRIMARY KEY("songuri")
);

--add songs to playlist
