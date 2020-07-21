import spotipy

class User():

    __uri = '' #song URI's
    __songs = [] #using this to return an array of song URI's

    def __init__(self, spotify_class, user_info={}):
        sp = spotify_class
        #self.__uri = uri

        if len(user_info) == 0:
            self.__user_info = sp.me()
    
    def get_followed_artists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_followed_artists(limit=5)
        uri_list = []
        list = result['artists']
        for i in list['items']:
            uri_list.append(i['uri'])
        return uri_list

    def get_user_top_artists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_top_artists(limit=50)
        uri_list = []
        for i in result['items']:
            uri_list.append(i['uri'])
        return uri_list

    def get_user_top_tracks(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_top_tracks(limit=50)
        uri_list = []
        for i in result['items']:
            uri_list.append(i['uri'])
        return uri_list

    def get_user_saved_tracks(self, spotify_class): #Done, change limits
        sp = spotify_class
        result = sp.current_user_saved_tracks(limit=5)
        uri_list = []
        #print(result['items'])
        #print(result['items'][0]['track']['uri'])
        for i in result['items']: 
            uri_list.append(i['track']['uri'])
        return uri_list
        #print(type(result))
        #print(result.keys())
        #print(list)
        #print(result['items'])
        #return result

    def get_playlists(self, spotify_class): #having trouble with the 3rd for loop | same error as get_user_saved_tracks
        sp = spotify_class
        result = sp.current_user_playlists(limit=5)
        uri_playlist = []
        print(result.keys())
        print(type(result['items']))
        print(result['items'][0].keys())
        for playlist in result['items']:
            uri_playlist.append(playlist['uri'])

        return uri_playlist
       