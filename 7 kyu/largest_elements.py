def largest(n, xs):
    """Find the n highest elements in a list"""
    return sorted(xs)[-n:]

assert largest(2, [7, 6, 5, 4, 3, 2, 1]) == [6, 7]
