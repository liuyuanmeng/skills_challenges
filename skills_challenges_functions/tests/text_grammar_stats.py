from lib.grammar_stats import GrammarStats
import pytest

@pytest.fixture
def grammar_stats():
    return GrammarStats()


def test_check_empty_string(grammar_stats):
    assert grammar_stats.check("") == False


def test_check_lowercase_start(grammar_stats):
    assert grammar_stats.check("this is a sentence.") == False


def test_check_uppercase_start_ends_with_period(grammar_stats):
    assert grammar_stats.check("This is a sentence.") == True


def test_check_uppercase_start_ends_with_exclamation(grammar_stats):
    assert grammar_stats.check("This is a sentence!") == True


def test_check_uppercase_start_ends_with_question(grammar_stats):
    assert grammar_stats.check("This is a sentence?") == True


def test_check_uppercase_start_ends_with_ellipsis(grammar_stats):
    assert grammar_stats.check("This is a sentence...") == True


def test_percentage_good_no_texts_checked(grammar_stats):
    assert grammar_stats.percentage_good() == 0


def test_percentage_good_no_passed_texts(grammar_stats):
    grammar_stats.total_texts_checked = 3
    assert grammar_stats.percentage_good() == 0


def test_percentage_good_some_passed_texts(grammar_stats):
    grammar_stats.total_texts_checked = 5
    grammar_stats.passed_text_count = 3
    assert grammar_stats.percentage_good() == 60


def test_percentage_good_all_passed_texts(grammar_stats):
    grammar_stats.total_texts_checked = 4
    grammar_stats.passed_text_count = 4
    assert grammar_stats.percentage_good() == 100
