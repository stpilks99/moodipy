from track_functions import Track
from spotify_authorize import auth


if __name__ == '__main__':
    # Get authorization
    authorize = auth()
    sp = authorize.authorize_util()

    # # Testing out track 
    # track = Track('spotify:track:7fPuWrlpwDcHm5aHCH5D9t', sp)
    # rec_dict = track.get_recommendations(sp, artists=[''], tracks=['spotify:track:3nPpCn5nYTMg0ajmzv57Jq'])
    # for i in rec_dict:
    #     print(i)

    # print(type(rec_dict['tracks']))
    # print(len(rec_dict['tracks']))
    # for i in rec_dict['tracks'][0]:
    #     print(i)
    #print(rec_dict['tracks'][1])

    # Testing out current user top artists function
    #================================================================
    # user_info = sp.current_user_top_artists()
    # print(type(user_info))
    # for entry in user_info:
    #     print(entry)
    
    # user_artists = user_info['items']
    # print(type(items))
    # for i in items:
    #     print(i)
    #     print('\n\n\n')
    #================================================================

    # Testing out different functions for tracks

    track_info = sp.track('spotify:track:2Yer0p7uB2lVBUAtANuuQp') # Magic in the hamptons
    print(type(track_info))
    print(len(track_info['album']))
    
    

