import spotipy
from spotify_authorize import auth

class Playlist:
    #This class holds functions meant to
    #manipulate and alter playlists.

    #Current rendition: Initial Phase

    #Variables
    __uri_tracks = []
    __uri_playlist = ''
    __name = ''
    moved_to_spotify = False
    # Maybe we need more variables

    def __init__(self, name, tracks):
        #Populate local trak list
        for track in tracks:
            self.__uri_tracks[track] = tracks[track]
        #Set track name, can be ''
        self.__name = name


    def add_song(self, uri):
        #Add track to URI list
        self.__uri_tracks.append(uri)


    def remove_song(self, uri):
        #Remove song from URI list
        self.__uri_tracks.remove((uri))

    '''def remove_playlist(self):

        authorize = auth()
        sp = authorize.authorize_util()

        sp.__del__()'''


    def set_playlist_name(self, new_name):
        #Alter the name of the playist
        self.__name = new_name


    def move_to_spotify(self):
        #Commit playlist to spotify
        authorize = auth()
        sp = authorize.authorize_util()
        sp.user_playlist_create(sp, self.__name)
        for track in self.__uri_tracks:
            sp.user_playlist_add_tracks(sp,)
            #Function requires playlist id, so this incomplete
        #Need to incorporate the functionality of the Moved_to_Spotify flag