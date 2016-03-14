from collections import Counter


def has_unique_chars(s):
    return Counter(s).most_common(1)[0][1] == 1


# def has_unique_chars(s):
#     return len(s) == len(set(s))
