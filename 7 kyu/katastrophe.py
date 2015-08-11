def strong_enough(earthquake, age):
    magnitude = reduce(lambda a, b: a * b, (sum(c) for c in earthquake))
    strength = 1000 * 0.99 ** age
    return 'Needs Reinforcement!' if magnitude > strength else 'Safe!'

assert strong_enough([[2, 3, 1], [3, 1, 1], [1, 1, 2]], 2) == 'Safe!'
assert strong_enough([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 2) == 'Safe!'
assert strong_enough([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 3) == \
    'Needs Reinforcement!'
