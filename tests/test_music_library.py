from lib.music_library import MusicLibrary

def test_initially_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []


def test_add_track():
    music_library = MusicLibrary()
    track = "Song Title: Artist Name"
    music_library.add(track)

def show_all_tracks():
     music_library = MusicLibrary()
