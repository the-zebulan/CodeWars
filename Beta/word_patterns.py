from collections import OrderedDict


def get_pattern(iterable):
    unique_ordered = list(OrderedDict.fromkeys(iterable))
    return tuple(unique_ordered.index(a) for a in iterable)


def word_pattern(pattern, string):
    return get_pattern(pattern) == get_pattern(string.split())


assert word_pattern('abab', 'apple banana apple banana') is True
assert word_pattern('abba', 'car truck truck car') is True
assert word_pattern('abab', 'apple banana banana apple') is False
assert word_pattern('aaaa', 'cat cat cat cat') is True
assert word_pattern('aaaa', 'cat cat dog cat') is False
