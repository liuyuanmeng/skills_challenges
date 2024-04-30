from lib.diary import Diary
from lib.diary_entry import DiaryEntry
import pytest


@pytest.fixture
def diary_with_entries():
    diary = Diary()
    diary.add(DiaryEntry("Entry 1", "This is the first entry."))
    diary.add(DiaryEntry("Entry 2", "This is the second entry."))
    return diary


def test_diary_add_entry(diary_with_entries):
    assert len(diary_with_entries.all()) == 2


def test_diary_count_words(diary_with_entries):
    assert diary_with_entries.count_words() == 10


def test_diary_reading_time(diary_with_entries):
    assert diary_with_entries.reading_time(200) == 1


def test_diary_find_best_entry_for_reading_time(diary_with_entries):
    best_entry = diary_with_entries.find_best_entry_for_reading_time(200, 1)
    assert best_entry.title == "Entry 1"
