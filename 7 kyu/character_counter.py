from collections import Counter


def validate_word(word):
    return len(set(Counter(word.lower()).itervalues())) == 1


assert validate_word("abcabc") is True
assert validate_word("Abcabc") is True
assert validate_word("AbcabcC") is False
assert validate_word("AbcCBa") is True
assert validate_word("pippi") is False
assert validate_word("?!?!?!") is True
assert validate_word("abc123") is True
assert validate_word("abcabcd") is False
assert validate_word("abc!abc!") is True
assert validate_word("abc:abc") is False
