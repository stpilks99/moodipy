from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from get_songs_with_criteria import get_songs_with_criteria
import spotipy

import collections


if __name__ == '__main__':
    # Get authorization
    authorize = auth()
    sp = authorize.authorize_util()

    #get_songs_with_criteria('sad',[],'','Juice WRLD', False, [], [], 0, 'spotify:user:buffalobulldoggy', sp)

    data1 = sp.recommendations(seed_genres=['alternative'], limit=50)
    data2 = sp.recommendations(seed_genres=['alternative'], limit=50)
    data3 = sp.recommendations(seed_genres=['alternative'], limit=50)
    data4 = sp.recommendations(seed_genres=['alternative'], limit=50)
    uri1 = []
    uri2 = []
    uri3 = []
    uri4 = []

    for song in data1['tracks']:
        uri1.append(song['uri'])
    for song in data2['tracks']:
        uri1.append(song['uri'])
    for song in data3['tracks']:
        uri1.append(song['uri'])
    for song in data3['tracks']:
        uri1.append(song['uri'])

    if collections.Counter(uri1) == collections.Counter(uri2):
        print("1 and 2.")
    if collections.Counter(uri1) == collections.Counter(uri3):
        print('1 and 3.')
    if collections.Counter(uri1) == collections.Counter(uri4):
        print('1 and 4')
    if collections.Counter(uri2) == collections.Counter(uri3):
        print('2 and 3')
    if collections.Counter(uri2) == collections.Counter(uri4):
        print('2 and 4')
    if collections.Counter(uri3) == collections.Counter(uri4):
        print('3 and 4')
    

    