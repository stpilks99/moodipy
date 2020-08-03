from playlist_functions import Playlist
from user_functions import User
from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth



def get_songs_with_criteria(mood, # User entered mood
                            genre_list, # list of genres from user
                            related_artist, # optional user related artist
                            disliked_songs, # list of songs that have been previously removed from the playlist
                            songs_on_list, # The current list of songs in the playlist
                            num_songs_needed, # How many songs should this return?
                            spotify_class):  # authorized class 

    ''' This will take a lot of inputs and return a list of songs that fit the user criteria'''                        
    # Instantiate user class
    sp = spotify_class
    current_user = User(sp)

    # Translate incoming genres
    for i in range(len(genre_list)):
        genre_list[i] = genre_list[i].lower()
        genre_list[i] = genre_list[i].replace(" ", "-")

    
    valid_tracks = []    # Return value, list of URI's of songs that match criteria

    # Add genres to broaden search
    added_genres = [] # Genres to be added to the genre list
    '''
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
            '''
        
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

        if len(genre_list) > 5:
            genre_list = genre_list[:5]

        print(len(genre_list))

        # Change artist to list
        artist_list = []
        artist_list.append(result_artist_uri)
        
        # Get info on all songs
        recommendations_raw = sp.recommendations(seed_genres=genre_list, limit=50)
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


    # Instantiate for use later in loop
    length_prev_loop = 0 
    fail_loop_count = 0
    last_5 = []
    total_loops = 0
    # Get song recommendations based on genre
    #while len(valid_tracks) <= num_songs_needed: # Loop until all songs found 
    while total_loops < 10:
        combined_track_list = songs_on_list + valid_tracks
        
        # Check entered mood, set target values
        if mood == 'Happy':
            # High valence
            target_valence = 0.99 # Higher valence means more cheerful
            recommendations_raw = sp.recommendations(seed_genres=genre_list,limit=50)
        elif mood == 'Sad':
            target_valence = 0.3 # Low valence
            recommendations_raw = sp.recommendations(seed_genres=genre_list,limit=50, target_valence=target_valence)
        elif mood == 'Motivated':
            target_energy = 0.9 # High energy
            recommendations_raw = sp.recommendations(seed_genres=genre_list,limit=50, target_energy=target_energy)
        elif mood == 'Calm':
            target_energy = 0.2 # Low energy
            recommendations_raw = sp.recommendations(seed_genres=genre_list, limit=50, target_energy=target_energy)
        elif mood == 'Frantic':
            target_tempo = 150  # Fast tempo and high energy
            target_energy = 0.9
            recommendations_raw = sp.recommendations(seed_genres=genre_list,limit=50, target_energy=target_energy, target_tempo=target_tempo)
        elif mood == 'Party':
            target_danceability = 0.8 # High danceability, energy, and popularity
            target_energy = 0.8
            target_popularity = 80
            recommendations_raw = sp.recommendations(seed_genres=genre_list, limit=50, target_energy=target_energy, target_danceability=target_danceability, target_popularity=target_popularity)
        elif mood == 'Gaming':
            target_speechiness = .05
            target_tempo = 120
            recommendations_raw = sp.recommendations(seed_genres=genre_list, limit=50, target_speechiness=target_speechiness)
        else:
            raise Exception('invalid mood input')

        # Check for returned results
        if len(recommendations_raw) == 0:
            print('No matches found for this criteria')
        
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
            
            if mood.lower() in track_moods: # Criteria matches
                valid_tracks.append(track[0]) # Add URI to valid tracks

        # Use last 5 songs added to the playlist as the recommendations for the next round
        if len(valid_tracks) > 5:
            last_5 = valid_tracks[-5:]
            #print(last_5)

        # Check to see if any of the songs are already on the playlist
        for track in songs_on_list:
            if track in valid_tracks:
                valid_tracks.remove(track)
                

        # Count number of loops that the tracks have not changed, if > 5 break the loop
        if len(valid_tracks) == length_prev_loop: # If the number of tracks retu
            fail_loop_count += 1
        if fail_loop_count > 4: # If the loop has failed 5 times
            break

        valid_tracks = list(dict.fromkeys(valid_tracks))

        length_prev_loop = len(valid_tracks)
        total_loops += 1 
        if total_loops > 10: # Should not take more than 10 loops to run
            return(valid_tracks)

    # Remove songs that the user has said they don't want
    for unwanted_track in disliked_songs:
        if unwanted_track in valid_tracks:
            valid_tracks.remove(unwanted_track)

    

    return(valid_tracks[:num_songs_needed]) # Only will return URI's of new tracks      