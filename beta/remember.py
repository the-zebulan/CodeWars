from collections import defaultdict


def remember(string):
    d = defaultdict(int)
    result = []
    for a in string:
        d[a] += 1
        if d[a] == 2:
            result.append(a)
    return result
