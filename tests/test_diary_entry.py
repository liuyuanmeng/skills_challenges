from lib.diary_entry import DiaryEntry
import pytest 

def test_format():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    assert diary_entry.format() == "My Title: These are the contents"


def test_count_words():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    assert diary_entry.count_words() == 6

def test_errors_on_empty_title_or_contents():
     with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry("", "")
     assert str(e.value) == "Diary entries must have a title or contents."

def test_reading_time_two_words():
    diary_entry = DiaryEntry("My Title", "the contents")
    result = diary_entry.reading_time(2)
    assert result == 1

def test_reading_time_three_words():
    diary_entry = DiaryEntry("My Title", "contents is here")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_chunk():
    pass

