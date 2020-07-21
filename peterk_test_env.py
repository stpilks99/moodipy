from track_functions import Track
from artist_functions import Artist
from spotify_authorize import auth
from user_functions import User


if __name__ == '__main__':
    # Get authorization
    authorize = auth()
    sp = authorize.authorize_util()
    
   

    user1 = User(sp)
    print(user1.get_playlists(sp))
    

