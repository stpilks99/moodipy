import spotipy

class User():

    __uri = '' #song URI's
    __songs = [] #using this to return an array of song URI's

    def __init__(self, uri, spotify_class, user_info={}):
        sp = spotify_class
        self.__uri = uri

        if len(user_info) == 0:
            user_info = sp.user(uri)
    
    def get_followed_artists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_followed_artists(limit=50)
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

    def get_user_saved_tracks(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_saved_tracks(limit=5)
        uri_list = []
        print(result['items'])
        for i in result['items']:
            uri_list.append(i['track']['uri'])
        return uri_list

    def get_playlists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_playlists(limit=50)
        uri_playlist = []
        name_playlist = []
        print(result.keys())
        print(type(result['items']))
        #print(result['items'])
        print(result['items'][0].keys())
        for playlist in result['items']:
            name_playlist.append(playlist['name'])
            uri_playlist.append(playlist['uri'])

        tup = (uri_playlist, name_playlist)

        return tup
