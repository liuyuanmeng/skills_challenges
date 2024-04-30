from lib.reading_time import estimate_reading_time
import pytest

def test_estimate_reading_time():
    # Test with a simple text
    words = " ".join(["word" + str(i) for i in range(200)])
    assert estimate_reading_time(words) == 1

def test_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for an empty text."

def test_300_words():
    text = " ".join(["word" for i in range(0, 300)])
    result = estimate_reading_time(text)
    assert result == 2
