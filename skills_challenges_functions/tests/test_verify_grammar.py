from lib.verify_grammar import verify_grammar


def test_valid_sentence():
    assert verify_grammar("This is a valid sentence.") == True


def test_sentence_not_starting_with_capital_letter():
    assert verify_grammar("this is not a valid sentence.") == False


def test_sentence_not_ending_with_punctuation():
    assert verify_grammar(
        "This is a valid sentence but without proper punctuation") == False


def test_empty_string():
    assert verify_grammar("") == False


def test_single_word_starting_with_capital_letter():
    assert verify_grammar("Hello") == False


def test_single_word_starting_with_lowercase_letter():
    assert verify_grammar("hello") == False


def test_sentence_ending_with_ellipsis():
    assert verify_grammar("This is a valid sentence...") == True


def test_sentence_ending_with_question_mark():
    assert verify_grammar("Is this a valid sentence?") == True
