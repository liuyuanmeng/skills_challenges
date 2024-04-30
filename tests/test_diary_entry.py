from  lib.diary_entry import DiaryEntry


def test_diary_entry_count_words():
    entry = DiaryEntry("Test Entry", "This is a test entry.")
    assert entry.count_words() == 5


def test_diary_entry_reading_time():
    entry = DiaryEntry("Test Entry", "This is a test entry.")
    assert entry.reading_time(200) == 1


def test_diary_entry_reading_chunk():
    entry = DiaryEntry("Test Entry", "This is a test entry.")
    chunk = entry.reading_chunk(200, 1)
    assert chunk == "This is a test entry."
