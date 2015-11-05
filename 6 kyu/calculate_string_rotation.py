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


assert shifted_diff("coffee", "eecoff") == 2
assert shifted_diff("eecoff", "coffee") == 4
assert shifted_diff("moose", "Moose") == -1
assert shifted_diff("isn't", "'tisn") == 2
assert shifted_diff("Esham", "Esham") == 0
assert shifted_diff("dog", "god") == -1
assert shifted_diff("yoyo", "oyoyoy") == -1
