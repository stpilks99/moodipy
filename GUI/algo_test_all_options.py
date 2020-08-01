# This is to test out all combinations to see which ones do not generate a list of songs

from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from playlist_functions import Playlist
from get_songs_with_criteria import get_songs_with_criteria
import spotipy
import datetime

if __name__ == '__main__':

    
    # Authorize Spotify connection
    authorize = auth('buffalobulldoggy')
    sp = authorize.authorize_util()
    
    # All genres in project so far
    genres1 = ['Acoustic', 'Afrobeat', 'Alternative', 'Ambient', 'Brazil', 'Classical']
    genres2 = ['Club', 'Country', 'Disco', 'Dubstep', 'EDM', 'Funk']
    genres3 = ['Gospel', 'Hard-rock', 'Heavy-metal', 'Hip-hop', 'Holidays', 'Indie']
    genres4 = ['Jazz', 'K-pop', 'Latin', 'Metal', 'Pop', 'Punk']
    genres5 = ['Reggae', 'R-n-b', 'Rock', 'Soul']

    genres = genres1 + genres2 + genres3 + genres4 + genres5 
    #print(genres)


    moods = ['Happy', 'Sad', 'Calm', 'Motivated', 'Frantic', 'Party', 'Gaming']

    song_lim = 30 # Number of songs returned from Spotify

    successes = [] 
    fails = []
    # Loop through each combination and try
    with open('algo_test_log.txt', 'w') as f: # log file setup
        date = datetime.datetime.now()
        time_now = date.strftime('%X')
        f.writestr(, '\n')
        for i in range(len(moods)):
            for j in range(len(genres)):
                # The genres must be in the format of a list
                f.write(date.strftime('%X'))
                genre_as_list = []
                genre_as_list.append(genres[j])
                # try:
                uris = get_songs_with_criteria(moods[i], genre_as_list, '', [], [], song_lim, sp)
                # except:
                #     fails.append((moods[i], genres[j]))
                #     continue

                if len(uris) != song_lim: # Number of desired songs has not been reached
                    fails.append((moods[i], genres[j]))
                else:
                    successes.append((moods[i], genres[j]))
            break

    print('Failed combinations:')       
    for combo in fails:
        print('Mood: ', combo[0], ', genre: ', combo[1])
            