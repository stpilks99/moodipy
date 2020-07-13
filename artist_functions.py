import spotipy
import moodipy

class Artist(Moodipy):
    '''Holds functions to get and set data on a particular artist'''

    # Variables
    __uri = ''              # Artist URI
    __genres = []           # All artist genres
    __popularity = -1      # 0-100 scale of how popular the artist is on Spotify

    def __init__(self, uri, spotify_class, artist_info={}):
        # Constructor
        # Instantiate class by drawing data on the artist
        # spotify_class:            Pre-authorized spotipy.Spotify() class
        # artist_info:              Optional dict for inputting previously found artist information from artist() spotipy function
        
        sp = spotify_class      # Set object name
        self.__uri = uri

        # Check artist info optional variable
        if len(artist_info) == 0:
            artist_info = sp.artist(uri)

        self.__genres = artist_info['genres']
        self.__popularity = artist_info['popularity']
    
       
    def get_uri(self):
        '''Gets URI of artist'''
        return self.__uri()


    def get_related_artists(self, spotify_class):
        '''Gets a list of URI's of related artists'''
        sp = spotify_class

        # Check spotify class type
        if isinstance(sp, spotipy.client.Spotify):
            # Call related artist function
            data = sp.artist_related_artists(self.__uri)

            # Sort data to list of URI's
            artist_list = data['artists']
            uri_list = []
            for artist in artist_list:
                uri_list.append(artist['uri'])
            return uri_list
            

    def get_artist_genres(self):
        '''Returns a list of genres pertaining to the artist'''
        return self.__genres

    
    def get_artist_popularity(self):
        '''Gets the artist's popularity on Spotify between 0 and 100'''
        return self.__popularity


    def get_top_tracks(self, spotify_class):
        '''Returns a list of track URI's of the artist's most popular songs'''

        sp = spotify_class
        data = sp.artist_top_tracks(self.__uri)
        uri_lst = []
        for i in data['tracks']:
            uri_lst.append(i['uri'])
        return uri_lst
