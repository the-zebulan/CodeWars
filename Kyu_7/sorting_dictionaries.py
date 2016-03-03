from operator import itemgetter


def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1), reverse=True)

assert sort_dict({3: 1, 2: 2, 1: 3}) == [(1, 3), (2, 2), (3, 1)]
assert sort_dict({1: 2, 2: 4, 3: 6}) == [(3, 6), (2, 4), (1, 2)]
assert sort_dict({1: 2, 2: 4, 3: 6}) == [(3, 6), (2, 4), (1, 2)]
assert sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8}) == \
    [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)]
