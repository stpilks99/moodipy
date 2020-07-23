import spotipy

class Track():
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
    __track_data = {}           # Raw data containing basic info about track

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
    __loudness = 0              # Average loudness of track in dB
    __track_audio_features = {} # Audio features of track
    

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
            track_values = track_audio_features
            self.__track_audio_features = track_audio_features

        # Assign private variables to stats from song
        self.__danceability = track_values['danceability']
        self.__energy = track_values['energy']
        self.__speechiness = track_values['speechiness']
        self.__acousticness = track_values['acousticness']
        self.__instrumentalness = track_values['instrumentalness']
        self.__valence = track_values['valence']
        self.__tempo = track_values['tempo']
        self.__loudness = track_values['loudness']

        # Check optional variable (basic song info)
        if len(track_data) == 0: # Initialized with general song data
            track_data = sp.track(self.__uri)
            self.__track_data = track_data['artists']
        else:
            self.__track_data = track_data  

        # Add data to class from track() 
        for artist in self.__track_data['artists']:
            self.__artists.append(artist['uri'])
        self.__explicit = bool(self.__track_data['explicit'])
        self.__popularity = self.__track_data['popularity']  
        

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


    def get_uri(self):
        '''Returns URI'''
        return self.__uri


    def get_release_year(self):
        '''Returns the decade that this song was released in.
        
            Format: last 2 digits of decade followed by an s (10s, 70s, etc). 
            Earlier dates will return 'older'
        '''
        track_album = self.__track_data['album']
        release_date = track_album['release_date']
        year = int(release_date[:4])
        # Choose decade
        if year >= 1970 and year < 1980:
            return '70s'
        elif year >= 1980 and year < 1990:
            return '80s'
        elif year >= 1990 and year < 2000:
            return '00s'
        elif year >= 2000:
            return '10s'
        else:
            return 'older'


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

        
    def get_mood(self):
        '''Determines the mood of the song. Criteria on OneNote.'''
        fitting_moods = [] # Holds the moods that this song fits into. 
        # Initialize variables for limits
        # Total range is 0-1 as a float value, if otherwise the variable unit of measurement is labeled
        acousticness_low_lim = 0.175 
        acousticness_high_lim = 0.25
        danceability_low_lim = 0.55
        danceability_high_lim = 0.7
        energy_low_lim = 0.675
        energy_high_lim = 0.825
        instrumentalness_cutoff = 0.05
        loudness_low_lim = -12 # dB
        loudness_high_lim = -8 # db
        speechiness_low_lim = 0.05
        speechiness_high_lim = 0.2
        valence_low_lim = 0.3
        valence_high_lim = 0/6
        tempo_low_lim = 110 # bpm
        tempo_high_lim = 135 # bpm
        popularity_low_lim = 50 # 0-100
        popularity_high_lim = 75 # 0-100

        # Check if happy
        if self.__valence >= valence_high_lim: 
            if self.__danceability >= danceability_high_lim:
                if self.__energy >= energy_high_lim:
                # High valence, danceability, energy
                    if tempo >= tempo_low_lim:
                        # Average to fast tempo
                        fitting_moods.append('happy')

        # Check if sad
        if self.__valence <= valence_low_lim:
            if self.__danceability <= danceability_low_lim:
                if self.__energy <= energy_low_lim:
                    # Low valence, danceability, energy
                    if self.__tempo <= tempo_high_lim:
                        # Average to slow tempo
                        fitting_moods.append('sad')

        # Check for motivated
        if self.__energy >= energy_high_lim:
            if self.__valence >= valence_high_lim:
                # High valence and energy
                if self.__tempo >= tempo_low_lim and self.__danceability >= danceability_low_lim:
                    # Average to high tempo and danceability
                    fitting_moods.append('motivated')

        # Check if calm
        if self.__acousticness >= acousticness_high_lim:
            # High acousticness
            if self.__loudness <= loudness_low_lim:
                if self.__energy <= energy_low_lim:
                    if self.__speechiness <= speechiness_low_lim:
                        # Low loudness, energy, speechiness
                        fitting_moods.append('calm')

        # Check if frantic
        if self.__tempo >= tempo_high_lim:
            if self.__loudness >= loudness_high_lim:
                if self.__energy >= energy_high_lim:
                    if self.__danceability >= danceability_high_lim:
                        # High tempo, loudness, danceability, energy
                        if self.__acousticness <= acousticness_low_lim:
                            # Low acousticness
                            fitting_moods.append('frantic')

        # Check if party
        if self.__danceability >= danceability_high_lim:
            if self.__energy >= energy_high_lim:
                if self.__valence >= valence_high_lim:
                    if self.__popularity >= popularity_high_lim:
                        # High danceability, energy, valence, loudness, popularity
                        if self.__acousticness <= acousticness_low_lim:
                            # Low acousticness
                            fitting_moods.append('party')

        # Check if gaming
        if self.__instrumentalness >= instrumentalness_cutoff:
            # High instrumentalness
            if self.__tempo >= tempo_low_lim:
                if self.__tempo <= tempo_high_lim:
                    if self.__valence >= valence_low_lim:
                        if self.__valence <= valence_high_lim:
                            if self.__energy >= energy_low_lim:
                                if self.__energy <= energy_high_lim:
                                    # Average tempo, valence, and energy
                                    if self.__speechiness <= speechiness_low_lim:
                                        # Low speechiness
                                        fitting_moods.append('gaming')

        # return list
        return fitting_moods
        