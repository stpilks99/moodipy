from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User
from get_songs_with_criteria import get_songs_with_criteria
import spotipy


if __name__ == '__main__':
    # Get authorization
    authorize = auth()
    sp = authorize.authorize_util()

    get_songs_with_criteria('',[],'','Juice WRLD', False, [], 0, 0, 'spotify:user:buffalobulldoggy', sp)
        