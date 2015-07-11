def count_by(x, n):
    """ Return a sequence of numbers counting by `x` `n` times. """
    return range(x, x * n + 1, x)

assert count_by(1, 5) == [1, 2, 3, 4, 5]
assert count_by(2, 5) == [2, 4, 6, 8, 10]
assert count_by(3, 5) == [3, 6, 9, 12, 15]
assert count_by(50, 5) == [50, 100, 150, 200, 250]
assert count_by(100, 5) == [100, 200, 300, 400, 500]
