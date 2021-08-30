"""Extraction of data from a Spotify playlist
"""
import random

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
        self.get_playlist()

    def get_playlist(self):
        """Get full playlist (inspired by https://stackoverflow.com/a/39113522)
        """
        results = sp.playlist_items(self.id, additional_types=('track',))['tracks']
        self.playlist = results['items']
        while results['next']:  # need this trick to have full playlist
            results = sp.next(results)
            self.playlist.extend(results['items'])

        # NOT A PROBLEM
        if results['total'] != len(self.playlist):
            print('Warning : incomplete playlist !')

    def shuffle(self):
        if isinstance(self.playlist, list):
            random.shuffle(self.playlist)
        else:
            raise TypeError('self.playlist must be a list, did you launch .get_playlist()')

    def get_images_list(self, img_size=640):
        if img_size not in [640, 300, 64]:
            raise ValueError('Unavailable image size : try 64, 300 or 640')

        return [list(filter(lambda dico: dico['height'] == img_size,
                            item['track']['album']['images']))[0]['url']
                for item in self.playlist]

    def get_human_readable(self):
        # probably useless feature for our purpose
        pass


if __name__ == '__main__':
    playlist = Playlist('05kISTbCkMooGzBj5h28tp?si=ea26d808213c4a6a')
    liste = playlist.get_images_list(64)
    print(liste[0])