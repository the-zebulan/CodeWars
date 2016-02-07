def list_depth(lst):
    result = [list_depth(a) for a in lst if isinstance(a, list)]
    return 1 + max(result) if result else 1


assert list_depth([True]) == 1
assert list_depth([]) == 1
assert list_depth([2, 'yes', [True, False]]) == 2
assert list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]) == 6
assert list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]) == 2
