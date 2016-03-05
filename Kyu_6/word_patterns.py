from collections import OrderedDict


def get_pattern(iterable):
    unique_ordered = list(OrderedDict.fromkeys(iterable))
    return tuple(unique_ordered.index(a) for a in iterable)


def word_pattern(pattern, string):
    return get_pattern(pattern) == get_pattern(string.split())
