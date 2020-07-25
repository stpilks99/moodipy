import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os


class auth:

    def __init__(self, username):
        self.__auth_info = {} # Instantiate
        self.__auth_info['username'] = username 
        self.__auth_info['scopes'] = 'user-read-private playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private user-library-read user-top-read user-read-recently-played user-follow-read'
        self.__auth_info['client_id'] = '780d705b61304bd8a72ffc3c18885e1a'
        self.__auth_info['client_secret'] = 'b370d65c6ac641af92b4958c11d7586e'
        self.__auth_info['redirect_uri'] = "http://localhost:8080/login"

    def authorize_util(self):
        '''Provides authorization with Spotify'''
        try:
            token = util.prompt_for_user_token(self.__auth_info['username'], self.__auth_info['scopes'] , self.__auth_info['client_id'], self.__auth_info['client_secret'], self.__auth_info['redirect_uri'])
        except:
            # Handle failure
            return None
        # pass back authorized Spotify class
        return spotipy.Spotify(auth=token)


    def authorize_oauth(self):
        '''Provides authorization with Spotify'''
       
        client_credentials_manager = SpotifyClientCredentials(client_id = self.__auth_info['client_id'], client_secret = self.__auth_info['client_secret'])
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    def logout(self):
        '''Logs a user out of their session. Returns true if successful.'''
        filename = './.cache-' + self.__auth_info['username']
        if os.path.isfile(filename):
            # Check if the file exists, delete if so
            try:    
                os.remove(filename)
            except FileNotFoundError: # File not found
                print("The file does not exist")
                return False
            return True


    

