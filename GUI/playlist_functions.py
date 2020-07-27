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
    __user_name = '' # Spotify username of current user
    __user_uri = '' # URI of current user
    __moved_to_spotify = False

    # Maybe we need more variables

    # User to access to playlists -- this may be improper

    def __init__(self, user_uri, spotify_class, name='', tracks=[], uri=''):
        '''
        user_playlist_uris: tuple with 2 lists, first one contains playlist URI's and second one 
                            contains playlist names. 
        '''
        sp = spotify_class
        self.__user_uri = user_uri
        user_data = sp.me()
        self.__user_name = user_data['id']
        if len(uri) == 0:
            # This playlist doesn't exist yet
            self.__moved_to_spotify = False
            # Check for duplicate playlist name
            user_playlists_raw = sp.user_playlists(self.__user_name)
            playlist_names = []
            for playlist in user_playlists_raw['items']:
                if playlist['name'] == name:
                    raise Exception("The user has a playlist with this name.")
                    
            #If name is not found in duplicates
            if len(name) > 0:
                self.__name = name

            if len(tracks) != 0: # If instantiated with tracks
                self.__temp_add = tracks

        else: # The playlist already exists
            self.__uri_playlist = uri
            user_playlists_raw = sp.user_playlists(self.__user_name)
            for playlist in user_playlists_raw['items']:
                if playlist['uri'] == self.__uri_playlist:
                    self.__name = playlist['name']
                    break
                else:
                    self.__name = name
            self.__moved_to_spotify = True


    def add_songs_local(self, uri_list, spotify_class):
        sp = spotify_class
        resultSong = sp.tracks(uri_list)
        song_uri = '' # Holds temp song uri
        song_name = '' # Holds temp song name
        addSongList = [] # Holds tuples
        print(type(resultSong['tracks'][0]))
        print(resultSong['tracks'][0]['uri'])
        print(resultSong['tracks'][0]['name'])    
        for i in resultSong['tracks']:
            tup = (i['uri'], i['name'])
            addSongList.append(tup)
        print(addSongList)
        return addSongList


    def get_playlist_uri(self):
        # if self.__moved_to_spotify == False:
        #     raise Exception("Playlist not created in Spotify yet.")
        # else:
        return self.__uri_playlist


    def remove_songs_local(self, uri_playlist, song_list, spotify_class):
        sp = spotify_class
        song_uri = []
        song_name = []
        resultSong = sp.track(song_list)
        song_name = resultSong['name']
        song_uri = resultSong['uri']
        removeSongList = (song_uri, song_name)
        return removeSongList


    def add_search_songs_sp(self, artist, song, spotify_class):
        '''Adds a song or list of songs to the playlist'''
        sp = spotify_class
        searchVal = ('artist:' + artist + ' track:' + song) #artist and song are pulled from user input in GUI
        result = sp.search(searchVal)
        song_uri_val = []
        for values in result['tracks']['items']:
            song_uri_val.append(values['uri'])
        song_uri_hold = []
        self.__temp_add = song_uri_val[0]
        song_uri_hold = song_uri_val[0]
        try:
            sp.user_playlist_add_tracks(self.__user_name, self.__uri_playlist, self.__temp_add) # Add to playlist
        except:
            return []
        self.__temp_add = [] 
        return self.add_songs_local(self.__user_name, song_uri_hold, sp)
        

    def add_songs_sp(self, tracks, sp):
        '''takes a list of URI's and adds them to a playlist'''
        # for track 
        if not isinstance(tracks, list):
            raise Exception("Tracks are not in a list")
        # Add songs
        try:
            sp.user_playlist_add_tracks(self.__user_name, self.__uri_playlist, tracks)
        except:
            return False
            
        return True
        

    def remove_songs_sp(self, song_uri, spotify_class):
        '''Removes selected songs from playlist''' 
        sp = spotify_class
        sp.user_playlist_remove_all_occurrences_of_tracks(self.__user_name, self.__uri_playlist, self.__temp_remove) # Remove from Spotify
        songs = self.__temp_remove[0]
        self.__temp_remove = [] # Reset list
        Playlist.remove_songs_local(self.__user_name, self.__uri_playlist, songs, sp)


    def create_spotify_playlist(self, spotify_class):
        #Commit playlist to spotify
        if self.__moved_to_spotify == True:
            raise Exception("This playlist has already been created.")
        sp = spotify_class
        try:
            sp.user_playlist_create(self.__user_name, self.__name)
        except:
            raise Exception('Playlist not able to be created')
        self.__moved_to_spotify = True
        user_playlists_raw = sp.user_playlists(self.__user_name)
        playlist_names = []
        for playlist in user_playlists_raw['items']:
            if playlist['name'] == self.__name:
                self.__uri_playlist = playlist['uri']
                return playlist['uri']
        # return URI, if it did not work return ''
        return ''


    def get_playlist_tracks(self, spotify_class, playlist_uri):
        '''Get all track URI's in a playlist'''
        if self.__moved_to_spotify == False:
            raise Exception("The playlist has not been created in Spotify.")

        sp = spotify_class
        raw_data = sp.playlist(playlist_uri)
        #print(raw_data['tracks']['items'][0]['track'])
        uri_list = []
        for i in raw_data['tracks']['items']:
            uri_list.append(i['track']['uri'])

        return uri_list



