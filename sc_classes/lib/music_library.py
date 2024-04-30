# File: lib/music_library.py

class MusicLibrary:

    def __init__(self):
        self._tracks = []

    def add(self, track):

        self._tracks.append(track)

    def all(self):
        return self._tracks

    def search_by_title(self, keyword):

        return [track for track in self._tracks if keyword.lower() == track.title.lower()]
