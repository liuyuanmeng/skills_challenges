from lib.track import Track
def test_construct_track_and_get_title_and_artist():
    track = Track("Title","Artist")
    assert track.title == "Title"
    assert track.artist == "Artist"


def test_track_format():
    # Create a Track instance
    track = Track("Song Title", "Artist Name")

    # Check if the format method returns the expected string
    assert track.format() == "Song Title by Artist Name"
