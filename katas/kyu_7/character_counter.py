from collections import Counter


def validate_word(word):
    return len(set(Counter(word.lower()).itervalues())) == 1
