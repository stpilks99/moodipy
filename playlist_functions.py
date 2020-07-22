import spotipy
from user_functions import User
from spotify_authorize import auth


class Playlist:
    # This class holds functions meant to
    # manipulate and alter playlists.

    # Current rendition: Initial Phase

    # Variables
    __uri_tracks = []
    __uri_playlist = ''
    __name = ''
    __moved = ''

    # Maybe we need more variables

    # User to access to playlists -- this may be improper

    def __init__(self, name, tracks, user):

        # This is redundant for every function...
        # Maybe pass it in as argument??
        authorize = auth()
        sp = authorize.authorize_util()

        # Populate local trak list
        for track in tracks:
            self.__uri_tracks[track] = tracks[track]
        # Set track name
        self.__name = name
        # instantaiting user for spotify purposes
        user = User(sp)

        # creating playlist in spotify (we talked about checking for playlist existence before adding new
        sp.user_playlist_create(user, self.__name)
        # assigning class attribute with playlist uri from spotify
        self.choose_playlist()

        # indicating playlist has not been transferred over yet
        self.moved_to_spotify = False

    # Function to find uri attribute from spotify
    def choose_playlist(self):

        # Gaining access to spotify (superfluous?)
        authorize = auth()
        sp = authorize.authorize_util()

        # User for accessing playlists
        user = User(sp)

        # dictionary to hold playlist values
        options = {}

        # pulling playlists for comparison
        options = user.get_playlists(sp)

        # Loop t check if playlist exists
        for i in options['items']:
            if self.__name == i['name']:
                # trying to define attribute when playlist found
                try:
                    self.__uri_playlist = i['uri']
                # finally throwing message if nothing is transferred
                finally:
                    print("ERROR: URI not transfered")

    '''Adding songs to spotify playlist
        This is the function that actually transfers songs over to spotify
        Happens in bulk, maybe tweak to do so for individual tracks'''
    def add_songs_sp(self):

        authorize = auth()
        sp = authorize.authorize_util()
        user = User(sp)

        # using attriute values to add song to spotify
        for track in self.__uri_tracks:
            # checking if this functioned has been previously called
            if self.moved_to_spotify:
                # remove all sane songs from playlist
                self.remove_song_sp(track)
            # Adding the track to spotify, (we can try passing tracks as an argument to add single tracks)
            sp.user_playlist_add_tracks(user, self.__uri_playlist, track, position=0)
        # signaling spotify has received the playlist
        self.move_to_spotify()

    # adding trach uri to the local list
    def add_song(self, uri):
        # Add track to palylisto locally
        self.__uri_tracks.append(uri)

    # dremoving all occurences of a song in the playlist
    def remove_song_sp(self, uri):

        authorize = auth()
        sp = authorize.authorize_util()
        user = User(sp)

        # function from API reference
        sp.user_playlist_remove_all_occurrences_of_tracks(user, self.__uri_playlist, uri)

    # remove uri from local list
    def remove_song(self, uri):
        # Remove song from local playlist
        self.__uri_tracks.remove((uri))


    # function to indicate playlist status in spotify
    def move_to_spotify(self):

        self.__moved = True
