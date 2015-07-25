from collections import Counter


def duplicate_count(text):
    return sum(a >= 2 for a in Counter(text.lower()).values())

assert duplicate_count("abcde") == 0
assert duplicate_count("abcdea") == 1
assert duplicate_count("aabbcde") == 2
assert duplicate_count("aabbcdeB") == 2
assert duplicate_count("indivisibility") == 1
assert duplicate_count('indivisibilities') == 2
