from lib.make_snippet import make_snippet

def test_empty_string():
    result = make_snippet("")
    assert result == ""


def test_same_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"


def test_string_more_than_5():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five" + "..."
