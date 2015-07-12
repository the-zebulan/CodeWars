def last(*args):
    end = args[-1]
    return end[-1] if isinstance(end, (str, list, tuple)) else end

assert last([1, 2, 3, 4, 5]) == 5
assert last('abcde') == 'e'
assert last(1, 'b', 3, 'd', 5) == 5
assert last((['a', 'b', 'c', 'k', 'x', 'y', 'z'],),
            ['a', 'b', 'c', 'k', 'x', 'y', 'z']) == 'z'
