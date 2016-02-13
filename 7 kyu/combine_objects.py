from collections import Counter


def combine(*args):
    return sum((Counter(a) for a in args), Counter())


a = {'a': 10, 'b': 20, 'c': 30}
b = {'a': 3, 'c': 6, 'd': 3}
c = {'a': 5, 'd': 11, 'e': 8}
d = {'c': 3}

assert combine(a, b) == {'a': 13, 'b': 20, 'c': 36, 'd': 3}
assert combine(a, c) == {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8}

assert combine(a, b, c) == {'a': 18, 'b': 20, 'c': 36, 'd': 14, 'e': 8}
assert combine(a, c, d) == {'a': 15, 'b': 20, 'c': 33, 'd': 11, 'e': 8}

assert combine({}, {}, {}) == {}
assert combine(a, c, {}) == {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8}

assert combine({}) == {}
assert combine(a, a, a) == {'a': 30, 'b': 60, 'c': 90}
assert combine(d, d, d, d, d, d) == {'c': 18}
assert combine(a, {}, a) == {'a': 20, 'b': 40, 'c': 60}
