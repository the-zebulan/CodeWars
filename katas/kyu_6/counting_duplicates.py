from collections import Counter


def duplicate_count(text):
    return sum(a >= 2 for a in Counter(text.lower()).values())
