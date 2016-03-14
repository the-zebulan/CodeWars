from collections import Counter


def shifted_diff(first, second):
    # pivek303 - one line solution from CodeWars
    # return (second + second).find(first) if len(first) == len(second) else - 1
    if not Counter(first) == Counter(second):
        return -1
    for i, a in enumerate(xrange(len(first), -1, -1)):
        if second == '{}{}'.format(first[a:], first[:a]):
            return i
    return -1
