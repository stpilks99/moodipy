import spotipy

class User():

    __uri = '' #song URI's
    __songs = [] #using this to return an array of song URI's

    def __init__(self, uri, spotify_class, user_info={}):
        sp = spotify_class
        self.__uri = uri

        if len(user_info) == 0:
            user_info = sp.user(uri)
    
    def get_followed_artists(self, spotify_class): #error - TypeError: string indices must be integers
        sp = spotify_class
        result = sp.current_user_followed_artists(limit=5)
        uri_list = []
        print(result['artists'])        
        for i in result['artists']:
            uri_list.append(i['uri'])
        return uri_list
        #print(type(result))
        #print(result.keys())
        #print(result)

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

    def get_user_saved_tracks(self, spotify_class): #almost | error - KeyError: 'uri'
        sp = spotify_class
        result = sp.current_user_saved_tracks(limit=5)
        uri_list = []
        for i in result['items']:
            uri_list.append(i['uri'])
        return uri_list
        #print(type(result))
        #print(result.keys())
        #print(result['items'])
        #return result

    def get_playlists(self, spotify_class): #having trouble with the 3rd for loop | same error as get_user_saved_tracks
        sp = spotify_class
        result = sp.current_user_playlists(limit=1)
        uri_playlist = []
        for i in result['items']:
            uri_playlist.append(i['uri'])
        print(uri_playlist)
        hold = len(uri_playlist)
        print(hold)
        for i in range(hold):
            uri_hold = sp.playlist_tracks(uri_playlist[i])
        uri_list = []
        for i in uri_hold['items']:
            uri_list.append(i['uri'])
        #return uri_list
        #print(type(uri_hold))
        #print(uri_hold.keys())
        #print(uri_hold['items'])
        #return result