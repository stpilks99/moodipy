import spotipy

class Track:
    # This class holds functions that are used to get data from 
    # Spotify for different tracks.

    # Current coverage:
    #

    # Need to do: 

    # VARIABLES
    __mood = ''             # Track mood(s)
    __uri = ''              # Track URI
    __genre = ''            # Track genre(s)
    __year_released = ''    # Year track was released
    __explicit = False      # Marks track as explicit if true
    __user_listens = 0      # Total times logged in user listened to song
    __overall_listens = 0   # Total listens between all Spotify users
    __acousticness = 0.0    # Acousticness of track between 0 and 1, with 1 representing high acousticness
    __danceability = 0.0    # Danceability of track, 1 is the most danceable
    __energy = 0.0          # Energy of track, 1 is most energetic
    __instrumalness = 0.0   # Amount of vocals in track, 1 means there are no vocals (0 almost all vocals)
    __speechiness = 0.0     # Closer to 1 means the track is mostly words
    __valence = 0.0         # Cheerfulness/happiness to track, 1 is most happy
    __tempo = 0.0           # Estimated BPM of track

    def __init__(track_uri, token):
        # Constructor
        # When Track called, audio analysis will be performed
        # and the data will be saved to private variables shown above
        try:
            sp = spotipy.Spotify(auth=token)
            audio_features_raw = sp.audio_features()
            print(audio_features_raw)
            



