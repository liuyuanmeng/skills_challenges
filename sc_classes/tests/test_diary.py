from lib.diary import Diary
from lib.diary_entry import DiaryEntry
import pytest


def test_diary_add_entry():
    diary = Diary()
    entry = DiaryEntry("Test Entry", "This is a test entry.")
    diary.add(entry)
    assert len(diary.all()) == 1


def test_diary_count_words():
    diary = Diary()
    diary.add(DiaryEntry("Test Entry", "This is a test entry."))
    assert diary.count_words() == 5


def test_diary_reading_time():
    diary = Diary()
    diary.add(DiaryEntry("Test Entry", "This is a test entry."))
    assert diary.reading_time(200) == 1


def test_diary_find_best_entry_for_reading_time_empty():
    diary = Diary()
    with pytest.raises(Exception):
        diary.find_best_entry_for_reading_time(200, 1)
