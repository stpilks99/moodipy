import spotipy
from user_functions import User
from spotify_authorize import auth


class Playlist:
    # This class holds functions meant to
    # manipulate and alter playlists.

    # Current rendition: Initial Phase

    #This class holds functions meant to
    #manipulate and alter playlists.

    #Current rendition: Initial Phase

    #Variables
    __uri_tracks = [] # Current tracks on the user's playlist
    __uri_playlist = '' # Playlist URI
    __temp_add = [] # If playlist has been created, list of queued songs to add
    __temp_remove = [] # If playlist has been created, list of queued songs to remove
    __name = '' # Playlist name
    __user = '' # Spotify username of current user
    __moved_to_spotify = False

    # Maybe we need more variables

    # User to access to playlists -- this may be improper

    def __init__(self, name, user, spotify_class, user_playlist_info, tracks=[], uri=''):
        '''
        user_playlist_uris: tuple with 2 lists, first one contains playlist URI's and second one 
                            contains playlist names. 
        '''
        sp = spotify_class
        self.__user = user
        if len(uri) == 0:
            # This playlist doesn't exist yet
            self.__moved_to_spotify = False
            # Check for duplicate playlist name
            playlist_uris = user_playlist_info[0]
            playlist_names = user_playlist_into[1]
            for i in range(len(playlist_uris)):
                if playlist_names[i] == name:
                    raise Exception("The user has a playlist with this name.")
            #If name is not found in duplicates
            self.__name = name

            if len(tracks) != 0: # If instantiated with tracks
                self.__uri_tracks = tracks

        else: # The playlist already exists
            self.__uri_playlist = uri
            self.__name = name
            self.__moved_to_spotify = True


    def add_songs_local(self, uri_list):
        #Add track to palylist locally
        for song in uri_list:
            self.__temp_add.append(song)

        # Get name from Spotify
        # data = sp.tracks()

        # Will have to return [(uri0, name0), (uri1, name1)...]


    def remove_songs_local(self, uri_list):
        #Remove song from local playlist
        for song in uri_list:
            self.__temp_remove.append(song)


    def add_songs_sp(self, spotify_class):
        '''Adds a song or list of songs to the playlist'''
        if self.__moved_to_spotify == False: # Check if playlist has been created in Spotify yet
            raise Exception("The playlist has not been exported to Spotify yet.")
        sp = spotify_class
        try:
            sp.user_playlist_add_tracks(self.__user, self.__uri_playlist, self.__temp_add) # Add to playlist
        except:
            return False
        self.__temp_add = []
        return True
        


    def remove_songs_sp(self, spotify_class):
        '''Removes selected songs from playlist''' 
        if self.__moved_to_spotify == False: # Check if playlist exists in Spotify
            raise Exception('This playlist has not been exported to Spotify yet.')
        sp = spotify_class
        sp.user_playlist_remove_all_occurrences_of_tracks(self.__user, self.__uri_playlist, self.__temp_remove) # Remove from Spotify
        self.__temp_remove = [] # Reset list


    def create_spotify_playlist(self, spotify_class):
        #Commit playlist to spotify
        if self.__moved_to_spotify == True:
            raise Exception("This playlist has already been created.")
        sp = spotify_class
        sp.user_playlist_create(self.__user, self.__name)
        # return URI, if it did not work return falase


    def get_playlist_tracks(self, spotify_class):
        '''Get all track URI's in a playlist'''
        if self.__moved_to_spotify == False:
            raise Exception("The playlist has not been created in Spotify.")

        sp = spotify_class
        
