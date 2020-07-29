from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from playlist_functions import Playlist
from get_songs_with_criteria import get_songs_with_criteria
import spotipy
import sqlite3

if __name__ == '__main__':

    authorize = auth('buffalobulldoggy')
    sp = authorize.authorize_util()
    userClass = User(sp)

    user_uri = userClass.get_uri()
    mood = ['Happy', 'Sad', 'Motivated', 'Calm', 'Frantic', 'Party', 'Gaming'] # Pick from one
    genres = ['Acoustic']
    disliked_song_uris = [] # Songs that the user does not want to hear anymore
    songs_on_list = []
    num_songs_needed = 25


    uris = get_songs_with_criteria(mood[1], genres, '', '', True, disliked_song_uris, [], num_songs_needed, sp)
    for uri in uris:
        track1 = Track(uri, sp)
        print('URI: ', track1.get_uri(), ', Valence level: ', track1.get_valence_val())

