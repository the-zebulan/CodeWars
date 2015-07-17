def flatten(lst):
    result = []
    for a in lst:
        if isinstance(a, (list, tuple)):
            [result.append(b) for b in a]
        else:
            result.append(a)
    return result

assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([[1, 2, 3], ['a', 'b', 'c'], [1, 2, 3]]) == \
    [1, 2, 3, 'a', 'b', 'c', 1, 2, 3]
assert flatten([[[1, 2, 3]]]) == [[1, 2, 3]]
