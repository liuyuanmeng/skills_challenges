import pytest
from lib.management import BirthdayReminder
from datetime import datetime, timedelta



@pytest.fixture
def birthday_reminder():
    reminder = BirthdayReminder()
    reminder.add_friend("Alice", datetime.now().date() - timedelta(days=365))
    reminder.add_friend("Bob", datetime.now().date() + timedelta(days=30))
    reminder.add_friend("Carol", datetime.now().date() + timedelta(days=60))
    reminder.add_friend("David", datetime.now().date() + timedelta(days=90))
    return reminder


def test_add_friend(birthday_reminder):
    assert len(birthday_reminder.friends) == 4


def test_update_birthdate(birthday_reminder):
    birthday_reminder.update_birthdate(
        "Alice", datetime.now().date() - timedelta(days=400))
    assert birthday_reminder.friends["Alice"] == datetime.now(
    ).date() - timedelta(days=400)


def test_update_name(birthday_reminder):
    birthday_reminder.update_name("Alice", "Alicia")
    assert "Alice" not in birthday_reminder.friends
    assert "Alicia" in birthday_reminder.friends


def test_upcoming_birthdays(birthday_reminder):
    upcoming = birthday_reminder.upcoming_birthdays(days=45)
    assert len(upcoming) == 3


def test_upcoming_ages(birthday_reminder):
    upcoming_ages = birthday_reminder.upcoming_ages()
    assert len(upcoming_ages) == 4


def test_mark_card_done(birthday_reminder):
    birthday_reminder.mark_card_done("Alice", datetime.now().year)
    assert birthday_reminder.friends["Alice"][datetime.now().year] == "done"
