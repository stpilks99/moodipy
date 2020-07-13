from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth


if __name__ == '__main__':
    # Get authorization
    authorize = auth()
    sp = authorize.authorize_util()

    # print(sp.artist('spotify:artist:4xRYI6VqpkE3UwrDrAZL8L'))
    artist1 = Artist('spotify:artist:4xRYI6VqpkE3UwrDrAZL8L', sp)
    related_artists = artist1.artist_top_tracks(sp)
    
    print(related_artists)