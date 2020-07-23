from playlist_functions import Playlist
from user_functions import User
from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth



def get_songs_with_criteria(mood, # User entered mood
                            genre_list, # list of genres from user
                            time_period, # User selected decade
                            related_artist, # optional user related artist
                            explicit, # true or false
                            disliked_songs, # list of songs that have been previously removed from the playlist
                            songs_on_list, # The current list of songs in the playlist
                            num_songs_needed, # How many songs should this return?
                            user_uri, # User's uri
                            spotify_class):  # authorized class 

    ''' This will take a lot of inputs and return a list of songs that fit the user criteria'''                        
    # Instantiate user class
    sp = spotify_class
    current_user = User(spotify_class)
    
    valid_tracks = []    # Return value, list of URI's of songs that match criteria

    # Add genres to broaden search
    added_genres = [] # Genres to be added to the genre list
    for genre in genre_list:
        if genre == 'acoustic':
            added_genres.append('folk')
        elif genre == 'alternative':
            added_genres.extend(['alt-rock', 'emo', 'synth-pop'])
        elif genre == 'ambient':
            added_genres.extend(['chill', 'dub', 'new-age'])
        elif genre == 'brazil':
            added_genres.extend(['bossanova', 'forro', 'mpb', 'pagode', 'sertanejo'])
        elif genre == 'classical':
            added_genres.append('piano')
        elif genre == 'club':
            added_genres.extend(['minimal-techno', 'progressive-rock', 'techno', 'chicago-house', 'deep-house', 'detroit-techno'])
        elif genre == 'country':
            added_genres.extend(['bluegrass', 'folk', 'honky-tonk'])
        elif genre == 'disco':
            added_genres.append('groove')
        elif genre == 'dubstep':
            added_genres.extend(['drum-and-bass', 'hardcore', 'idm', 'industrial', 'dubstep'])
        elif genre == 'edm':
            added_genres.extend(['breakbeat', 'drum-and-bass', 'electro', 'electronic', 'garage', 'hardstyle', 'techno', 'trance'])
        elif genre == 'funk':
            added_genres.append('groove')
        elif genre == 'hard-rock':
            added_genres.extend(['goth', 'grindcore'])
        elif genre == 'heavy-metal':
            added_genres.extend(['black-metal', 'death-metal', 'grindcore'])
        elif genre == 'indie':
            added_genres.extend(['emo', 'folk', 'indie-pop'])
        elif genre == 'jazz':
            added_genres.append('groove')
        elif genre == 'latin':
            added_genres.extend(['dancehall', 'latino', 'reggaeton', 'salsa', 'samba', 'tango'])
        elif genre == 'metal':
            added_genres.extend(['metal-misc', 'metalcore'])
        elif genre == 'pop':
            added_genres.extend(['indie-pop', 'pop-film', 'synth-pop'])
        elif genre == 'punk':
            added_genres.extend(['emo', 'punk-rock'])
        elif genre == 'reggae':
            added_genres.extend(['dub', 'dancehall', 'ska'])
        elif genre == 'r-n-b':
            added_genres.append('groove')
        elif genre == 'soul':
            added_genres.append('groove')
        
    # Add genres to the original genre list
    genre_list.extend(added_genres)

    # Check if user inputted an artist or not
    if len(related_artist) != 0: # Artist inputted
        # Get artist information
        results = sp.search(related_artist, limit=1, type='artist')
        result_artist_uri = results['artists']['items'][0]['uri']
        result_artist_info = results['artists']['items'][0]
        if len(results['artists']) == 0: # Check if results were found
            # No artist found
            raise Exception('Invalid artist entry')
        artist = Artist(result_artist_uri, spotify_class, artist_info=result_artist_info)
        
        # Get artist genres and add those to the list
        artist_genres = artist.get_artist_genres()
        for genre in artist_genres:
            if genre not in genre_list:
                genre_list.append(genre)

        # Get info on all songs
        recommendations_raw = sp.recommendations(seed_artists=[result_artist_uri], seed_genres=genre_list, limit=50)
        all_track_info = recommendations_raw['tracks']
        recommended_uris = [] # Holds URI's found from recommendations query
        for track in all_track_info:
            recommended_uris.append(track['uri'])
        
        # Get audio features of each recommended track
        tracks_features = sp.audio_features(recommended_uris)
        full_info = zip(recommended_uris, all_track_info, tracks_features)

        # Check criteria of each song
        for track in full_info:
            track_obj = Track(track[0], sp, track_data=track[1], track_audio_features=track[2])
            track_moods = track_obj.get_mood()
            
            if mood in track_moods: # Criteria matches
                valid_tracks.append(track[0]) # Add URI to valid tracks 


    # Get song recommendations based on genre
    while len(valid_tracks) <= num_songs_needed: # Loop until all songs found 
        combined_track_list = songs_on_list + valid_tracks
        recommendations_raw = sp.recommendations(seed_genres=genre_list, seed_tracks=combined_track_list,limit=50)
        all_track_info = recommendations_raw['tracks']
        recommended_uris = [] # Holds URI's found from recommendations query
        for track in all_track_info:
            recommended_uris.append(track['uri'])

        # Get audio features of each recommended track
        tracks_features = sp.audio_features(recommended_uris)
        full_info = zip(recommended_uris, all_track_info, tracks_features)

        # Check criteria of each song
        for track in full_info:
            track_obj = Track(track[0], sp, track_data=track[1], track_audio_features=track[2])
            track_moods = track_obj.get_mood()
            
            if mood in track_moods: # Criteria matches
                valid_tracks.append(track[0]) # Add URI to valid tracks

    # Remove songs that the user has said they don't want
    for unwanted_track in disliked_songs:
        if unwanted_track in valid_tracks:
            valid_tracks.remove(unwanted_track)


    return(valid_tracks) # Only will return URI's of new tracks      