import spotipy

class User():

    __uri = '' #User URI
    __username = ''
    __songs = [] #using this to return an array of song URI's
    __user_info = {} # All data on user

    def __init__(self, spotify_class, user_info={}):
        sp = spotify_class

        if len(user_info) != 0: # All info already accessible
            self.__user_info = user_info
            self.__uri = user_info['uri']
            self.__username = user_info['id']
        else: # Info needed
            self.__user_info = sp.me()
            self.__uri = self.__user_info['uri']
            self.__username = self.__user_info['id']
    
    def get_followed_artists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_followed_artists(limit=50)
        #print('result.keys')
        #print(result.keys())
        #print('result artists')
        #print(result['artists'])
        uri_list = []
        list = result['artists']
        for i in list['items']:
            uri_list.append(i['uri'])
        #print('uri list ')
        return uri_list

    def get_user_top_artists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_top_artists(limit=50)
        #print('result.keys')
        #print(result.keys())
        #print('result items')
        #print(result['items'])
        uri_list = []
        for i in result['items']:
            uri_list.append(i['uri'])
        #print('uri list ')
        return uri_list

    def get_user_top_tracks(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_top_tracks(limit=50)
        #print('result.keys')
        #print(result.keys())
        #print('result items')
        #print(result['items'])
        uri_list = []
        for i in result['items']:
            uri_list.append(i['name'])
        #print('uri list')
        return uri_list

    def get_user_saved_tracks(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_saved_tracks(limit=50)
        #print('result.keys')
        #print(result.keys())
        #print('result items')
        #print(result['items'])
        uri_list = []
        for i in result['items']:
            uri_list.append(i['track']['uri'])
        #print('uri list')
        return uri_list

    def get_playlists(self, spotify_class): #done
        sp = spotify_class
        result = sp.current_user_playlists(limit=50)
        #print('result.keys')
        #print(result.keys())
        #print('result items')
        #print(result['items'])
        uri_playlist = []
        name_playlist = []
        #print(result['items'][0].keys())
        for playlist in result['items']:
            name_playlist.append(playlist['name'])
            uri_playlist.append(playlist['uri'])
        #print('uri list')

        tup = (uri_playlist, name_playlist)

        return tup

    def get_username(self):
        return self.__username


    def get_uri(self):
        return self.__uri

    def testFunction(self, artist, song, spotify_class):
        sp = spotify_class
        searchVal = ('artist:' + artist + ' track:' + song) #artist and song are pulled from user input in GUI
        #rint(searchVal)
        result = sp.search(searchVal)
        #print(result)
        print(result.keys())
        song_uri_val = []
        #print(testVal)
        #print(result['tracks'])
        #testVal = result[0]
        #print(testVal)
        for values in result['tracks']['items']:
            #print(values)
            song_uri_val.append(values['uri'])
        song_uri_hold = []
        song_uri_hold = song_uri_val[0]
        resultSong = sp.track(song_uri_hold)
        song_uri = []
        song_name = []
        song_name = resultSong['name']
        song_uri = resultSong['uri']
        addSongList = (song_uri, song_name)
        return addSongList