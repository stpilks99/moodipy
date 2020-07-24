import spotipy
from spotify_authorize import auth
from track_functions import Track
from artist_functions import Artist
from user_functions import User


authorize = auth()
sp = authorize.authorize_util()
#print(sp)
spot = spotipy.Spotify()
#test = sp.current_user()
test2 = User.get_username('danielj1128', sp)
#print(test)
print(test2)
print('BREAK')
print('BREAK')
print('BREAK')
print('BREAK')
#artist1 = Artist('spotify:artist:4xRYI6VqpkE3UwrDrAZL8L', sp)
#related_artists = artist1.get_top_tracks(sp)
#print(related_artists)
