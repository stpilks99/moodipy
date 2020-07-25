from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from playlist_functions import Playlist
from get_songs_with_criteria import get_songs_with_criteria
import spotipy

import collections


if __name__ == '__main__':
    # Get authorization
    authorize = auth('buffalobulldoggy')
    sp = authorize.authorize_util()
    authorize.logout()

    #get_songs_with_criteria('sad',[],'','Juice WRLD', False, [], [], 0, 'spotify:user:buffalobulldoggy', sp)

    return_uris = get_songs_with_criteria('calm', ['acoustic', 'indie'], '', '', True, [], [], 50, sp)
    print(len(return_uris))
    # user1 = User(sp)
    # user_uri = user1.get_uri()
    # playlist1 = Playlist('Calming acoustic', user_uri, sp, tracks=return_uris)
    # playlist_uri = playlist1.create_spotify_playlist(sp)
    # playlist1.add_songs_sp(sp)
    
    
        
    #sp.recommendations(seed_genres=['club', 'progressive-rock', 'techno', 'chicago-house', 'deep-house', 'detroit-techno'])

    