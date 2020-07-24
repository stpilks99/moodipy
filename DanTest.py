import spotipy
from spotify_authorize import auth
from track_functions import Track
from artist_functions import Artist
from user_functions import User


authorize = auth()
sp = authorize.authorize_util()
#print(sp)
spot = spotipy.Spotify()
#test = User.get_user_saved_tracks('danielj1128', sp)
tracks = ('artist:Halsey track:Castle')
test2 = User.testFunction('danielj1128', tracks, sp)
#print(test)
print('BREAK')
print('BREAK')
print('BREAK')
print('BREAK')
print(test2)
#artist1 = Artist('spotify:artist:4xRYI6VqpkE3UwrDrAZL8L', sp)
#related_artists = artist1.get_top_tracks(sp)
#print(related_artists)

#def testFunction(self, uri_list, spotify_class):
#    sp = spotify_class
#    result = sp.tracks(uri_list)
#    #print(result)
#    print(result.keys())
#    song_uri = []
#    song_name = []
#    #print(result['items'])
#    for i in result['tracks']:
#        song_uri.append(i['uri'])
#        song_name.append(i['name'])
#    song_list = (song_uri, song_name)
#    return song_list