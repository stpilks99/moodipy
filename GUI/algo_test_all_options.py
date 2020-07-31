from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from playlist_functions import Playlist
from get_songs_with_criteria import get_songs_with_criteria
import spotipy

if __name__ == '__main__':

    # This is to test out all combinations to see which ones do not generate a list of songs

    genres1 = ['Acoustic', 'Afrobeat', 'Alternative', 'Ambient', 'Brazil', 'Classical']
    genres2 = ['Club', 'Country', 'Disco', 'Dubstep', 'EDM', 'Funk']
    genres3 = ['Gospel', 'Hard-rock', 'Heavy-metal', 'Hip-hop', 'Holidays', 'Indie']
    genres4 = ['Jazz', 'K-pop', 'Latin', 'Metal', 'Pop', 'Punk']
    genres5 = ['Reggae', 'R-n-b', 'Rock', 'Soul']

    all_genres = genres1 + genres2 + genres3 + genres4 + genres5
    print(all_genres)

    moods = ['Happy', 'Sad', ]