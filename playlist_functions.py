import spotipy
from user_functions import User
from spotify_authorize import auth


class Playlist:


    #This class holds functions meant to
    #manipulate and alter playlists.

    #Current rendition: Initial Phase

    #Variables
    __uri_tracks = []
    __uri_playlist = []
    __name = ''
    moved_to_spotify = False
    # Maybe we need more variables

    #User to access to playlists -- this may be improper


    def __init__(self, name, tracks, user):

        authorize = auth()
        sp = authorize.authorize_util()
        #Populate local trak list
        for track in tracks:
            self.__uri_tracks[track] = tracks[track]
        #Set track name, can be ''
        self.__name = name
        user = User()
        sp.user_playlist_create(user, self.__name)

    def choose_playlist(self, sp, ):

        authorize = auth()
        sp = authorize.authorize_util()
        user = User()
        options = []
        options = user.get_playlists()
        for i in options['items']:
            if self.__name == i['name']:
                return i['uri']

    def add_song_sp(self, uri, playlist_id):

        authorize = auth()
        sp = authorize.authorize_util()
        user = User()
        sp.user_playlist_add_tracks(sp, )

    def add_song(self, uri):
        #Add track to palylist locally
        self.__uri_tracks.append(uri)

    def remove_song(self, uri):
        #Remove song from local playlist
        self.__uri_tracks.remove((uri))

    '''def remove_playlist(self):

        authorize = auth()
        sp = authorize.authorize_util()

        sp.__del__()'''


    def move_to_spotify(self):
        #Commit playlist to spotify
        authorize = auth()
        sp = authorize.authorize_util()
        sp.user_playlist_create(sp, self.__name)
        for track in self.__uri_tracks:
            sp.user_playlist_add_tracks(sp,)
            #Function requires playlist id, so this incomplete
        #Need to incorporate the functionality of the Moved_to_Spotify flag