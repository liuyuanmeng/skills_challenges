import pytest
from lib.most_often import MostOften


def test_adds_item_to_list():
    basket = MostOften([])
    basket.add_new("apple")
    assert basket.starting_list == ["apple"]


def tests_highest_items():
    basket = MostOften(["apple", "bananna" "orange", "apple"])
    result = basket.get_most_often()
    assert result == "apple"


def tests_clear_winner():
    basket = MostOften(["apple", "bananna", "bananna",
                       "orange", "orange", "apple"])
    result = basket.get_most_often()
    assert result == "no clear winner"


def tests_with_no_string():
    basket = MostOften([])
    result = basket.get_most_often()
    assert result == "no clear winner"
