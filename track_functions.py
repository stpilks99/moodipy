import spotipy

class Track:
    # This class holds functions that are used to get data from 
    # Spotify for different tracks.

    # Current coverage:
    # Get audio analysis and track information (constructor) and set variables 
    # Get all audio analysis variables

    # Need to do: 

    # VARIABLES
    # General
    __uri = ''                  # Track URI
    __mood = ''                 # Track mood(s)
    __genre = ''                # Track genre(s)
    # from track analysis
    __artists = []              # List of contributors to track
    __album = ''                # Corresponding album
    __explicit = True           # Explicit flag, true if explicit, false if not explicit or unknown.
    __popularity = -1            # Popularity of song between 0-100, higher number is more popular

    # From audio analysis
    __year_released = ''        # Year track was released
    __explicit = False          # Marks track as explicit if true
    __acousticness = -0.1        # Acousticness of track between 0 and 1, with 1 representing high acousticness
    __danceability = -0.1        # Danceability of track, 1 is the most danceable
    __energy = -0.1              # Energy of track, 1 is most energetic
    __instrumentalness = -0.1    # Amount of vocals in track, 1 means there are no vocals (0 almost all vocals)
    __speechiness = -0.1         # Closer to 1 means the track is mostly words
    __valence = -0.1             # Cheerfulness/happiness to track, 1 is most happy
    __tempo = -1                # Estimated BPM of track
    

    def __init__(self, track_uri, spotify_class, track_data={}, track_audio_features={}):
        # Constructor
        # track_uri:                    Full URI of track
        # spotify_class:                Pre-authorized spotipy.Spotify() class
        # track_data:                   Optional, if the track() function has already been called the information can be passed here
        # track_audio_features:         Optional, if the audio_features() function has already been called for this track the information can be passed here

        self.__uri = track_uri
        sp = spotify_class          # authorized spotipy.Spotify() class passed in 
        
        # Get audio features of track if not already input
        if len(track_audio_features) == 0:
            audio_features_raw = sp.audio_features(track_uri)
            # Get information in dictionary
            track_values = {} # dictionaty
            track_values = audio_features_raw[0]
        else:
            track_values = track_audio_features[0]

        # Assign private variables to stats from song
        self.__danceability = track_values['danceability']
        self.__energy = track_values['energy']
        self.__speechiness = track_values['speechiness']
        self.__acousticness = track_values['acousticness']
        self.__instrumentalness = track_values['instrumentalness']
        self.__valence = track_values['valence']
        self.__tempo = track_values['tempo']

        # Check optional variable (basic song info)
        if len(track_data) == 0: # Initialized with general song data
            track_data = sp.track(self.__uri)

        # Add data to class from track() 
        for artist in track_data['artists']:
            self.__artists.append(artist['uri'])
        self.__explicit = bool(track_data['explicit'])
        self.__popularity = track_data['popularity']      
        

    def get_dance_val(self):
        '''Gets danceability of this song'''
        return self.__danceability


    def get_energy_val(self):
        '''Gets energy value of the song'''
        return self.__energy


    def get_speech_val(self):
        '''Gets speech value of the song 
        (0 to 0.33 is less speech and more music, 
        0.33 to 0.66 is a mix of speech and rap, 
        0.67 to 1 is probably all words/speech and no music'''
        return self.__speechiness


    def get_acoustic_val(self):
        '''Gets acoustic value of song'''
        return self.__acousticness


    def get_instrumental_val(self):
        '''Gets instrumental val of song (closer to 1 means more likely that there are no vocals)'''
        return self.__instrumentalness

    
    def get_valence_val(self):
        '''Gets valence (happiness/upbeat) value of a song'''
        return self.__valence


    def get_tempo_val(self):
        '''Gets tempo in BPM'''
        return self.__tempo

    
    def get_explicit_val(self):
        '''Returns True if explicit, False if not'''
        return self.__explicit


    def get_popularity(self):
        '''Gets popularity of a song from 0-100'''
        return self.__popularity

    
    def get_artists(self):
        '''Returns a list of artist(s) for this track'''
        return self.__artists


    def get_recommendations(self, authorized_class, query_limit=20):
        '''Get 5 songs similar to this one'''
        # limit: amount of URI's that are requested to be returned
        sp = authorized_class           # Type spotipy.Spotify()
        data = sp.recommendations(seed_tracks=[self.__uri], limit=query_limit)
        track_data = data['tracks']
        
        # Get the URI of each track 
        uri_lst = [] # Holds all URI's of the recommendation data
        for i in track_data:
            uri_lst.append(i['uri'])
        # Return list of URI's of recommended tracks
        return uri_lst

        