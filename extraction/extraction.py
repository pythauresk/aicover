"""Extraction of data from a Spotify playlist
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# FIXME : add a way to get api keys without showing it
from config.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET  # noqa


credentials = SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)


class Playlist:
    def __init__(self, playlist_id):
        """
        :param playlist_id: playlist id (end of a playlist url), str
        """
        # TODO : verify playlist_id, correct it if necessary and del Playlist if there is a problem
        self.id = playlist_id
        self.playlist = None
        self.get_raw()

    def get_raw(self):
        self.playlist = sp.playlist(self.id)['tracks']['items']

    def shuffle(self):
        pass

    def get_human_readable(self):
        # probably useless feature for our purpose
        pass

    def get_images_list(self):
        # TODO
        # add size as parameters
        # create a json with an option, is it useful ?
        pass


if __name__ == '__main__':
    pass
