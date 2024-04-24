def verify_grammar(sentence):
    if not sentence:
        return False  # Return False for empty strings

    # Check if the sentence starts with a capital letter
    if not sentence[0].isupper():
        return False

    # Check if the sentence ends with a suitable punctuation mark
    if sentence[-1] not in [".", "!", "?", "..."]:
        return False

    return True

# return sentence[0].isupper() and sentence[-1] in [".", "!", "?", "..."]