from itertools import chain, izip
from string import ascii_lowercase as low, ascii_uppercase as up, digits

KEYS = {a: i for i, a in enumerate(chain(
    up, low, chain.from_iterable(izip(xrange(10), digits))))}


def unusual_sort(array):
    return sorted(array, key=lambda a: KEYS[a])


assert unusual_sort(['a', 'z', 'b']) == ['a', 'b', 'z']
assert unusual_sort(['a', 'Z', 'B']) == ['B', 'Z', 'a']
assert unusual_sort(['1', 'z', 'a']) == ['a', 'z', '1']
assert unusual_sort(['1', 'Z', 'a']) == ['Z', 'a', '1']
assert unusual_sort([3, 2, 1, 'a', 'z', 'b']) == ['a', 'b', 'z', 1, 2, 3]
assert unusual_sort([3, '2', 1, 'a', 'c', 'b']) == ['a', 'b', 'c', 1, '2', 3]
assert unusual_sort([3, '2', 1, '1', '3', 2]) == [1, '1', 2, '2', 3, '3']
