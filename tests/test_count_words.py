from lib.count_words import count_words

def test_count_words():
    text = "This is a sample sentence."
    assert count_words(text) == 5

#   # Test with an empty string
#     text2 = ""
#     assert count_words(text2) == 0

#     # Test with a string containing only whitespace
#     text3 = "   "
#     assert count_words(text3) == 0

#     # Test with a string containing special characters
#     text4 = "Hello, world! How are you today?"
#     assert count_words(text4) == 6
