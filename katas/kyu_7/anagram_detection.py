from collections import Counter


def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())
