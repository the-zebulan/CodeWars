def same(arr_a, arr_b):
    return sorted(sorted(a) for a in arr_a) == sorted(sorted(b) for b in arr_b)


assert same([], []) is True
assert same([[2, 5], [3, 6]], [[5, 2], [3, 6]]) is True
assert same([[2, 5], [3, 6]], [[6, 3], [5, 2]]) is True
assert same([[2, 5], [3, 6]], [[6, 3], [2, 5]]) is True
assert same([[2, 5], [3, 5], [6, 2]], [[2, 6], [5, 3], [2, 5]]) is True
assert same([[2, 5], [3, 5], [6, 2]], [[3, 5], [6, 2], [5, 2]]) is True
assert same([[2, 3], [3, 4]], [[4, 3], [2, 4]]) is False
assert same([[2, 3], [3, 2]], [[2, 3]]) is False
